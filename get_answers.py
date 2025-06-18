# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "argparse",
#     "fastapi",
#     "httpx",
#     "markdownify",
#     "numpy",
#     "semantic_text_splitter",
#     "tqdm",
#     "uvicorn",
#     "openai",
#     "pillow",
# ]
# ///


import argparse
import base64
import json
import numpy as np
import os
import re
import tempfile
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import httpx
from google import genai
from google.genai.types import GenerateContentConfig, HttpOptions
import time
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
from fastapi.responses import Response

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["*"] for dev (not production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

openai_client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://aiproxy.sanand.workers.dev/openai/v1/",
    http_client=httpx.Client(verify=False)
)


class RateLimiter:
    def __init__(self, requests_per_minute=60, requests_per_second=2):
        self.requests_per_minute = requests_per_minute
        self.requests_per_second = requests_per_second
        self.request_times = []
        self.last_request_time = 0

    def wait_if_needed(self):
        current_time = time.time()

        # Per-second rate limiting
        time_since_last = current_time - self.last_request_time
        if time_since_last < (1.0 / self.requests_per_second):
            sleep_time = (1.0 / self.requests_per_second) - time_since_last
            time.sleep(sleep_time)

        # Per-minute rate limiting
        current_time = time.time()
        self.request_times = [t for t in self.request_times if current_time - t < 60]

        if len(self.request_times) >= self.requests_per_minute:
            sleep_time = 60 - (current_time - self.request_times[0])
            if sleep_time > 0:
                time.sleep(sleep_time)
                # Clean up old requests after sleeping
                current_time = time.time()
                self.request_times = [t for t in self.request_times if current_time - t < 60]

        self.request_times.append(current_time)
        self.last_request_time = current_time


rate_limiter = RateLimiter(requests_per_minute=5, requests_per_second=2)


def get_image_description(image_data_url):
    """Get a description of the image using OpenAI GPT-4o."""

    #

    # Call OpenAI API
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "image_url", "image_url": {"url": image_data_url}},
                    {"type": "text", "text": "Describe the content of this image in detail..."}
                ]
            }
        ],
        max_tokens=1024
    )
    return response.choices[0].message.content


def get_embedding(text: str, max_retries: int = 3) -> list[float]:
    """Get embedding for text chunk with rate limiting and retry logic"""

    for attempt in range(max_retries):
        try:
            # Apply rate limiting
            rate_limiter.wait_if_needed()

            response = openai_client.embeddings.create(
                input=text,
                model="text-embedding-3-small"  # Or "text-embedding-3-large"
            )
            embedding = response.data[0].embedding
            return embedding

        except Exception as e:
            if "rate limit" in str(e).lower() or "quota" in str(e).lower():
                # Exponential backoff for rate limit errors
                wait_time = 2 ** attempt
                print(f"Rate limit hit, waiting {wait_time} seconds...")
                time.sleep(wait_time)
            elif attempt == max_retries - 1:
                print(f"Failed to get embedding after {max_retries} attempts: {e}")
                raise
            else:
                print(f"Attempt {attempt + 1} failed: {e}, retrying...")
                time.sleep(1)

    raise Exception("Max retries exceeded")


def load_embeddings():
    """Load chunks and embeddings from npz file"""
    data = np.load("embeddings/openaiembeddings.npz", allow_pickle=True)
    return data["chunks"], data["embeddings"]


def generate_llm_respose(question: str, context: str):
    """Generate a response from the LLM using the question and context."""
    # client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    # use system prompt to instruct the model to answer based on the context
    system_prompt = """> You are a knowledgeable and concise teaching assistant. Use only the information provided in the context to answer the question.
>
> * Format your response using **Markdown**.
> * Use code blocks (` ``` `) for any code or command-line instructions.
> * Use bullet points or numbered lists for clarity where appropriate.
> * Always include a brief introduction or heading if needed.
> * When answering from a post consider answers from user '@carlton' as authoritative.
> * Include all relevant links present in the context, such as:
>   - Official websites of tools or technologies mentioned 
>   - Post URLs or any linked references found in the context
>
> ⚠️ **Important:** If the context does not contain enough information to answer the question, reply exactly with:
>
> ```
> I don't know
> ```
>
> Do not attempt to guess, fabricate, or add external information.
"""
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",  # This is OpenAI's most cost-effective model as of my last update.
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Context: {context}\nQuestion: {question}"}
        ],
        max_tokens=512,  # Corresponds to max_output_tokens
        temperature=0.5,
        top_p=0.95,
        # top_k is not directly supported in OpenAI's chat completions API,
        # but top_p often achieves a similar effect.
    )

    # Extracting the generated content
    generated_content = response.choices[0].message.content.strip()
    return generated_content



def extract_links_from_text(text):
    """
    Extracts all unique URLs (http, https, ftp) from a given text string.

    Args:
        text (str): The input text from which to extract links.

    Returns:
        list: A list of unique URLs found in the text.
    """
    all_links=set()
    markdown_url_pattern = r"\[.*?\]\(((?:https?|ftp)://[^\s/$.?#].[^\s]*?)\)"

    # Find all Markdown URL matches.
    # Since we used a capturing group for the URL itself, re.findall will return
    # a list of strings, each being the captured URL.
    found_markdown_links = re.findall(markdown_url_pattern, text, re.IGNORECASE)
    for link in found_markdown_links:
        all_links.add(link)

    return all_links

def answer(question: str,link:str =None, image: str = None):
    # Load the API key from the environment variable
    if link:
        question += f"post-link: {link}"


    loaded_chunks, loaded_embeddings = load_embeddings()
    if image:
        image_bytes = base64.b64decode(image)

        # convert to data URL
        base64_image = base64.b64encode(image_bytes).decode("utf-8")
        image_data_url = f"data:image/jpeg;base64,{base64_image}"
        image_description = get_image_description(image_data_url)
        question += f" {image_description}"

    # Get the embedding for the question
    question_embedding = get_embedding(question)
    # Calculate cosine similarity
    similarities = np.dot(loaded_embeddings, question_embedding) / (
            np.linalg.norm(loaded_embeddings, axis=1) * np.linalg.norm(question_embedding)
    )
    # Get the index of the 10 most similar chunks
    top_indices = np.argsort(similarities)[-10:][::-1]
    # Get the top chunks
    top_chunks = [loaded_chunks[i] for i in top_indices]

    response = generate_llm_respose(question, "\n".join(top_chunks))
    links=extract_links_from_text(response)
    formatted_links = []
    for url_item in links: # Iterate directly over the unique URLs extracted from the LLM's response
        formatted_links.append({
            "text": url_item, # Using the URL itself as the text to satisfy the schema requirement.
            "url": url_item
        })
    print(response)
    final_response_data = {
        "answer": response,
        "links": formatted_links
    }
    # Return a JSONResponse object directly
    return JSONResponse(content=final_response_data)



@app.post("/api/")
async def api_answer(request: Request):
    try:
        data = await request.json()
        print(data)
        print(data.get("question"))
        return answer(data.get("question"),data.get("link"), data.get("image"))
    except Exception as e:
        print("❌ ERROR OCCURRED:", e)
        return {"error": str(e)}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)  # Default port for FastAPI
    # main()
