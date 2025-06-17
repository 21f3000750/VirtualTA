import requests
import os
import json

import openai
import base64

import re
from PIL import Image
import time
from io import BytesIO
from datetime import datetime, timezone # Ensure timezone is imported
from urllib.parse import urljoin, urlencode
from bs4 import BeautifulSoup

from dotenv import load_dotenv
from google import genai

load_dotenv()

openai.api_key=os.getenv("OPENAI_API_KEY")
openai.base_url="https://aiproxy.sanand.workers.dev/openai/v1/"
retreived_topic_ids=[]

# ========== CONFIGURATION ==========

DISCOURSE_BASE_URL = "https://discourse.onlinedegree.iitm.ac.in/"
CATEGORY_SLUG = "courses/tds-kb"
CATEGORY_ID = 34
START_DATE = "2025-01-01" # Inclusive
END_DATE = "2025-04-15"   # Inclusive

RAW_COOKIE_STRING = "_ga_QHXRKWW9HH=GS1.3.1724508127.1.1.1724508130.0.0.0; _ga=GA1.1.1963192533.1724508127; _fbp=fb.2.1724508135614.156612395551918289; _gcl_au=1.1.35594112.1745647838; _ga_5HTJMW67XK=GS2.1.s1749740201$o26$g0$t1749740218$j43$l0$h0; _ga_08NPRH5L4M=GS2.1.s1749740194$o99$g1$t1749740412$j60$l0$h0; _t=xAYFrw11VzK%2FMA1wY6Zf4ww5NkmB9wv4XeHt%2B6%2FzHTObqM%2FkoEGlCa98qnmO4lv8BLawrFEWs83pnLsIz2mSYCf%2BSUBIIShRu25j%2FDYfwlF8skj27Y2jRy%2FZNiYnjwNmiONjXM31D3g2hWvH0xqd0DE2ZUb5bDchLU2HZ0jmcHtjODM9z768CBjEvecT7d39xUbtfd9L8ML%2FjtGx2t50FLp0vwfNdyKViZJHp6fbmOgdBxn26UWLjDL5tqdIppNsx2YN6TElKfdvnGt74lYqUDNo5gbBgAxL9iu7cNYJrKdZhfy6QM78aD4JOlc%3D--LB3zsEo0ULJcSi7o--adw0exkQPwR%2FQpAFb%2BMrqQ%3D%3D; _bypass_cache=true; _forum_session=ri2W%2F6AHP2R%2B5DHJ%2FLP2a8bn9w2obYnzrjDVUo41RFrF9udbTgyAlDbCFx2t7FwWvDAv4%2FvoGG4ZLLYAIEPNlOrecl7TaDpJqFNwoyYt2sWZwtKsgy6BmgcDQ7PafcDS19pHzHhqRKPl%2BfRJhRh1sjEC17G5NjXH4eXtfRG8AD7%2Fvw1RCjhzhadSCq98OCF%2FKSlCtrzC3K1qNdTk7BRAxP85rL%2BS7lO4EoCkn3SuylhTEqj09OacN4qBAmc6KsIraVlgmjLI21awlgnP6%2BKe5WRx0FuibUk0LAVLL4enCdkBllHJk3QdIzbcq9txjb45eYKkfbnI%2F7iR4smH%2FvkV883DppBCKKcb8qnMRMzMyNEe53fq8I%2BVqapQ5CgReo5W4Qak4Apq%2FMFPHjs4ZORDFLGmREjxS8DeDjPPePftc%2BD7RZWcVL18b8RcGPMj%2BqdPwcIkqA19WkCu5X%2FUPHNJ0YuEzTolCq8rLqdQ78YS916pw99HyO%2B%2F%2F1JEyKwZ9k2kbn6b7Ug%2FKidRKqV1bc132Be6jpXfWjoFgMmnqB2EmtTk1P5x4gEW%2FCJ7hA%2BlpHdbIG2jOqEK9f2eRVALD9%2FqkdKXb4MqlWxIJVYkpn%2F17PHN1ahHwSVveJLl5goKOy5czs6%2BgVP6l1qjPw%3D%3D--bPNrmN9MTJqaVB%2Bi--X3rxyCSFbJTD7p24ynOsLA%3D%3D"
 # Replace with your actual cookie string

OUTPUT_DIR = "discourse_md"
POST_ID_BATCH_SIZE = 50
MAX_CONSECUTIVE_PAGES_WITHOUT_NEW_TOPICS = 5 # New configuration for breaking loop

# === SETUP ===
os.makedirs(OUTPUT_DIR, exist_ok=True)

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


rate_limiter = RateLimiter(requests_per_minute=7, requests_per_second=2)

# === HELPERS ===
def sanitize_filename(name):
    return re.sub(r'[^a-zA-Z0-9_-]', '_', name)


def html_to_text(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text(separator="\n").strip()

def extract_from_image_url(image_url: str):
    """
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"),
                           base_url="https://aiproxy.sanand.workers.dev/openai/v1/")

    # Download the image
    response = requests.get(image_url)
    response.raise_for_status()
    image_bytes = BytesIO(response.content)

    prompt = "Describe the content of this image in detail, focusing on any text, objects, or relevant features that could help answer questions about it."

    # Send image + prompt to GPT-4o
    result = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": image_url}}
                ]
            }
        ]
    )
    # return result.choices[0].message.content.strip()
    """
    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    prompt = "Describe the content of this image in detail, focusing on any text, objects, or relevant features that could help answer questions about it."
    response = requests.get(image_url)
    response.raise_for_status()

    image = Image.open(BytesIO(response.content))

    result = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=[prompt, image],
    )
    # Return the description
    return result.text.strip()




def extract_image_descriptions(cooked_html):
    soup = BeautifulSoup(cooked_html, "html.parser")
    image_descriptions = []

    for img_tag in soup.find_all("img"):
        src = img_tag.get("src")
        if (
                src
                and src.startswith("https://europe1.discourse-cdn.com")
                and ( src.endswith(".png") or src.endswith(".jpeg") or src.endswith(".jpg") or ".png?" in src)
        ):
            print(src)
            extracted_data = extract_from_image_url(src)
            if extracted_data:
                # image_desc = describe_image_with_gemini(extracted_data.strip())
                image_md = f"![Image]({src})\n\n**Image Description:** {extracted_data}"
                image_descriptions.append(image_md)

    return "\n\n".join(image_descriptions)

def parse_cookie_string(raw_cookie_string):
    """Parses a raw cookie string into a dictionary."""
    cookies = {}
    if not raw_cookie_string.strip():
        print("Warning: RAW_COOKIE_STRING is empty. Requests might fail if authentication is needed.")
        return cookies
    for cookie_part in raw_cookie_string.strip().split(";"):
        if "=" in cookie_part:
            key, value = cookie_part.strip().split("=", 1)
            cookies[key] = value
    return cookies


def get_topic_ids(base_url, category_slug, category_id, start_date_str, end_date_str, cookies):
    """Fetches topic IDs from a specific category within a date range."""
    url = urljoin(base_url, f"c/{category_slug}/{category_id}.json")
    topic_ids = []
    page = 0

    start_dt_naive = datetime.fromisoformat(start_date_str + "T00:00:00")
    start_dt = start_dt_naive.replace(tzinfo=timezone.utc)
    end_dt_naive = datetime.fromisoformat(end_date_str + "T23:59:59.999999")
    end_dt = end_dt_naive.replace(tzinfo=timezone.utc)

    print(f"Fetching topic IDs from category between {start_dt} and {end_dt}...")

    # Variables for the new loop break condition
    consecutive_pages_with_no_new_unique_topics = 0
    last_known_unique_topic_count = 0

    while True:
        paginated_url = f"{url}?page={page}"
        try:
            response = requests.get(paginated_url, cookies=cookies, timeout=30)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch page {page}: {e}")
            break

        try:
            data = response.json()
        except json.JSONDecodeError:
            print(f"Failed to decode JSON from page {page}. Content: {response.text[:200]}...")
            break

        topics_on_page = data.get("topic_list", {}).get("topics", [])

        if not topics_on_page:
            print(f"No more topics found on page {page} (API returned empty list).")
            break # Primary stop condition: API says no more topics on this page

        # Store current number of unique topics before processing this page
        # This helps check if *this specific page fetch* added anything new
        count_before_processing_page = len(set(topic_ids))

        for topic in topics_on_page:
            created_at_str = topic.get("created_at")
            if created_at_str:
                try:
                    created_date = datetime.fromisoformat(created_at_str.replace("Z", "+00:00"))
                except ValueError:
                    print(f"Warning: Could not parse date '{created_at_str}' for topic ID {topic.get('id')}")
                    continue

                if start_dt <= created_date <= end_dt:
                    topic_ids.append(topic["id"]) # Add ID, will be deduped later for count

        current_unique_topic_count = len(set(topic_ids))

        if topics_on_page and current_unique_topic_count == count_before_processing_page :
            # This means the current page had topics, but none of them were new *and* within the date range,
            # or all topics fetched from this page were duplicates of ones already in topic_ids from *previous pages*.
            # For the staleness check, we care if the overall unique set isn't growing.
             pass # Handled by the check below using last_known_unique_topic_count

        # Staleness check: Has the *total* number of unique topics found stopped growing?
        if current_unique_topic_count == last_known_unique_topic_count and topics_on_page:
            # topics_on_page is checked to ensure we don't increment if an empty page was returned (which is a valid end)
            consecutive_pages_with_no_new_unique_topics += 1
            print(f"Page {page} did not yield any new unique topics. Consecutive stale pages: {consecutive_pages_with_no_new_unique_topics}.")
        else:
            consecutive_pages_with_no_new_unique_topics = 0 # Reset if new unique topics were found

        last_known_unique_topic_count = current_unique_topic_count

        if consecutive_pages_with_no_new_unique_topics >= MAX_CONSECUTIVE_PAGES_WITHOUT_NEW_TOPICS:
            print(f"No new unique topics found for {MAX_CONSECUTIVE_PAGES_WITHOUT_NEW_TOPICS} consecutive pages. Assuming end of relevant category listing.")
            break

        # Original secondary stop condition (heuristic)
        more_topics_url = data.get("topic_list", {}).get("more_topics_url")
        if not more_topics_url:
            # This typically means it's the last page.
            # The condition `len(topics_on_page) < 30` was a heuristic for when more_topics_url might be missing
            # but the page wasn't full. If more_topics_url is definitively gone, it's a strong signal.
            print(f"No 'more_topics_url' indicated on page {page}. Assuming this is the last page of topics.")
            break

        print(f"Fetched page {page}, {len(topics_on_page)} topics on page. Total unique topics found so far: {current_unique_topic_count}. Continuing...")
        page += 1


    final_unique_topic_ids = list(set(topic_ids)) # Deduplicate
    print(f"Total unique topics found in timeframe: {len(final_unique_topic_ids)}")
    return final_unique_topic_ids


def get_full_topic_json(base_url, topic_id, cookies):
    """Fetches the full topic JSON, including all posts by handling pagination."""
    initial_topic_url = urljoin(base_url, f"t/{topic_id}.json")
    print(f"Fetching initial data for topic {topic_id} from {initial_topic_url}")

    try:
        response = requests.get(initial_topic_url, cookies=cookies, timeout=30)
        response.raise_for_status()
        topic_data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch initial topic data for {topic_id}: {e}")
        return None
    except json.JSONDecodeError:
        print(f"Failed to decode initial JSON for topic {topic_id}. Content: {response.text[:200]}...")
        return None

    post_stream = topic_data.get("post_stream")
    if not post_stream or "stream" not in post_stream or "posts" not in post_stream:
        print(f"Error: 'post_stream' not found or incomplete in topic {topic_id}. Skipping post fetching.")
        return topic_data

    all_post_ids_in_stream = post_stream.get("stream", [])
    loaded_post_ids = {post["id"] for post in post_stream.get("posts", [])}

    all_post_ids_in_stream = [pid for pid in all_post_ids_in_stream if pid is not None]

    missing_post_ids = [pid for pid in all_post_ids_in_stream if pid not in loaded_post_ids]

    print(f"Topic {topic_id}: Total posts in stream: {len(all_post_ids_in_stream)}, Initially loaded: {len(loaded_post_ids)}, Missing: {len(missing_post_ids)}")

    if not missing_post_ids:
        print(f"All posts for topic {topic_id} already loaded in initial fetch.")
        return topic_data

    fetched_additional_posts = []
    for i in range(0, len(missing_post_ids), POST_ID_BATCH_SIZE):
        batch_ids = missing_post_ids[i:i + POST_ID_BATCH_SIZE]

        query_params = [("post_ids[]", pid) for pid in batch_ids]
        posts_url = urljoin(base_url, f"t/{topic_id}/posts.json")

        print(f"Fetching batch of {len(batch_ids)} posts for topic {topic_id} (IDs: {batch_ids[0]}...{batch_ids[-1]})")

        try:
            batch_response = requests.get(posts_url, params=query_params, cookies=cookies, timeout=60)
            batch_response.raise_for_status()
            batch_data = batch_response.json()

            if isinstance(batch_data, list):
                 fetched_additional_posts.extend(batch_data)
            elif "post_stream" in batch_data and "posts" in batch_data["post_stream"]:
                fetched_additional_posts.extend(batch_data["post_stream"]["posts"])
            elif "posts" in batch_data and isinstance(batch_data["posts"], list):
                 fetched_additional_posts.extend(batch_data["posts"])
            else:
                print(f"Warning: Unexpected JSON structure for post batch in topic {topic_id}. Data: {str(batch_data)[:200]}...")

        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch post batch for topic {topic_id} (IDs: {batch_ids}): {e}")
        except json.JSONDecodeError:
            print(f"Failed to decode JSON for post batch in topic {topic_id}. Response: {batch_response.text[:200]}...")

    if fetched_additional_posts:
        print(f"Successfully fetched {len(fetched_additional_posts)} additional posts for topic {topic_id}.")
        existing_posts_in_topic_data = {post['id']: post for post in topic_data["post_stream"]["posts"]}
        for post in fetched_additional_posts:
            if post['id'] not in existing_posts_in_topic_data:
                topic_data["post_stream"]["posts"].append(post)
                existing_posts_in_topic_data[post['id']] = post

        post_id_to_post_map = {post['id']: post for post in topic_data["post_stream"]["posts"]}

        sorted_posts = []
        for post_id_val in all_post_ids_in_stream: # Renamed post_id to post_id_val to avoid conflict
            if post_id_val in post_id_to_post_map:
                sorted_posts.append(post_id_to_post_map[post_id_val])

        topic_data["post_stream"]["posts"] = sorted_posts
        print(f"Topic {topic_id}: Final post count in JSON: {len(topic_data['post_stream']['posts'])}")

    return topic_data


def process_discourse_json(data):

    topic_title = data.get("title", "Untitled Topic")
    topic_id = data.get("id", "unknown_topic")
    posts = data.get("post_stream", {}).get("posts", [])

    md_lines = [
        f"# Topic: {topic_title}",
        f"**Topic ID**: {topic_id}",
        f"**Total Posts**: {len(posts)}",
        "\n---\n"
    ]

    for post in posts:
        post_id = post.get("id")
        post_number = post.get("post_number")
        author = post.get("username", "anonymous")
        cooked_html = post.get("cooked", "")
        text = html_to_text(cooked_html)
        # image_insights = extract_image_descriptions(cooked_html)

        md_lines.append(f"## Post #{post_number} by {author} (Post ID: {post_id})")
        md_lines.append(text)
        # if image_insights:
        #     md_lines.append("\n### Image Insight:\n" + image_insights)
        md_lines.append("\n---\n")

    filename = sanitize_filename(f"{topic_id}_{topic_title}")+'.md'
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    print(f"[✓] Markdown saved to: {filepath}")


def main():
    """Main function to orchestrate the downloading process."""
    print("Script started.")
    cookies = parse_cookie_string(RAW_COOKIE_STRING)
    if not cookies and DISCOURSE_BASE_URL != "https://meta.discourse.org/":
        print("Warning: Running without cookies. This may fail for private forums or specific content.")

    for filename in os.listdir(OUTPUT_DIR):
        topic_id = filename.split("_")[0]
        retreived_topic_ids.append(topic_id)

    topic_ids = get_topic_ids(
        DISCOURSE_BASE_URL,
        CATEGORY_SLUG,
        CATEGORY_ID,
        START_DATE,
        END_DATE,
        cookies
    )

    if not topic_ids:
        print("No topic IDs found for the given criteria. Exiting.")
        return

    total_topics = len(topic_ids)
    success_downloads = 0
    failed_topic_ids = []

    print(f"\nStarting download of {total_topics} topics...\n")

    for i, topic_id in enumerate(topic_ids, 1):
        print(f"--- [{i}/{total_topics}] Processing topic ID: {topic_id} ---")
        print(f"retreived_topic_ids", retreived_topic_ids)
        print(type(topic_id))
        print(topic_id not in retreived_topic_ids)
        if str(topic_id) not in retreived_topic_ids:
            topic_json_data = get_full_topic_json(DISCOURSE_BASE_URL, topic_id, cookies)
            if topic_json_data:
                process_discourse_json(topic_json_data)
                success_downloads += 1
            else:
                print(f"Failed to get complete data for topic {topic_id}.")
                failed_topic_ids.append(topic_id)
            # print(f"--- Finished processing topic ID: {topic_id} ---\n") # Reduced verbosity

    print("\n========= SUMMARY =========")
    print(f"Total topics identified: {total_topics}")
    print(f"Successfully downloaded full data for: {success_downloads} topics")
    print(f"Failed to download/process: {len(failed_topic_ids)} topics")
    if failed_topic_ids:
        print("Failed topic IDs:", failed_topic_ids)
    print(f"Downloaded files are in: {os.path.abspath(OUTPUT_DIR)}")
    print("Script finished.")

if __name__ == "__main__":
    main()