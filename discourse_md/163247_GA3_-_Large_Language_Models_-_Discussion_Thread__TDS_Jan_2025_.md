# Topic: GA3 - Large Language Models - Discussion Thread [TDS Jan 2025]
**Topic ID**: 163247
**Total Posts**: 149

---

## Post #1 by s.anand (Post ID: 579668)
Please post any questions related to 
Graded Assignment 3 - Large Language Models
.




Important Instruction


Please use markdown code formatting (fenced code blocks) when sharing code in Discourse posts. This makes the code much easier to read and differentiate from non-code text. It also makes it easier for people to copy code snippets and run it themselves. See below code for example


ping exam.sanand.workers.dev

Pinging exam.sanand.workers.dev [104.21.31.149] with 32 bytes of data:
Reply from 104.21.31.149: bytes=32 time=9ms TTL=58
Reply from 104.21.31.149: bytes=32 time=8ms TTL=58
Reply from 104.21.31.149: bytes=32 time=8ms TTL=58
Reply from 104.21.31.149: bytes=32 time=9ms TTL=58

Ping statistics for 104.21.31.149:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 8ms, Maximum = 9ms, Average = 8ms



Visit this link for more details: 
Extended Syntax | Markdown Guide
.


A friendly suggestion: kindly go through 
Discourse Docs
! 




Deadline: 
Sunday, February 2, 2025 6:29 PM


@carlton
 
@Jivraj
 
@Saransh_Saini

---

## Post #2 by s.anand (Post ID: 579673)


---

## Post #3 by nilaychugh (Post ID: 580013)
how to get the dummy API key?

---

## Post #4 by Jivraj (Post ID: 580073)
Hi Nilay,


In order to make a api call to openai chat completions you are required to send authentication information(openai key) in headers. For first question of GA3 you don’t have to send actual(working) api key, any dummy api key would work(you can put your name, or tds anything works)


kind regards

---

## Post #6 by nilaychugh (Post ID: 581443)
which API should i use in 7th question

---

## Post #7 by 22f3001315 (Post ID: 581855)
need help in question 4th. how can i correct this json body? sir  
@Jivraj


{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": "Extract text from this image."
    },
    {
      "role": "user",
      "content": {
        "image_url": "data:image/png;base64,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"
      }
    }
  ]
}




error:The JSON body must have 1 message


{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": {
        "text": "Extract text from this image.",
        "image_url": "data:image/png;base64,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"
      }
    }
  ]
}




Error: The message must have a 2 content parts

---

## Post #8 by 22f3001315 (Post ID: 582119)
@Jivraj
 
@carlton
  sir plz see it once.

---

## Post #9 by Jivraj (Post ID: 582598)
Hi 
@22f3001315
 ,


You are almost correct, there are very minor changes that needs to be made.


Take help from Chat GPT or use this documentation which have correct json body 
Vision - OpenAI API
.


Kind regards

Jivraj

---

## Post #10 by 22f3001315 (Post ID: 582639)
it worked thanks sir

---

## Post #12 by 22f3002034 (Post ID: 582722)
Are we supposed to buy open ai api key ?

---

## Post #13 by 23f2000237 (Post ID: 582744)
No, if you scroll down to the last question, we can get our Ai Proxy key

---

## Post #14 by carlton (Post ID: 582749)
@nilaychugh
 
@22f3002034


The API key is available at 
https://aiproxy.sanand.workers.dev/


The instructions on how to use the token is given at 
GitHub - sanand0/aiproxy: Authorizing proxy for LLMs


You cannot use this token directly with Open AI or any other gpt. These are only valid via the API exposed by the above instructions.


You get a limit of $1. Use with care.


Kind regards

---

## Post #15 by nilaychugh (Post ID: 582810)
but the embedding model that is said to be used is text embedding 3 small, which is the model of OpenAI

---

## Post #16 by Jivraj (Post ID: 583185)
Hi Nilay,


Yes you would need to use 
text-embedding-3-small
 model of openai for embedding questions.


Kind regards

Jivraj

---

## Post #17 by nilaychugh (Post ID: 583854)
i have a doubt, while submitting the GA3, both 7th and 8th questions require the API url to be active and connected right, but its not possible as both the URLs use same port, so if we check my 7th question URL is running right now, it’ll show as correct, but then if i  run 8th question URL, the 7th question will automatically show the error, 
is there any solution to this problem?

---

## Post #18 by 21f3002277 (Post ID: 583913)
Q5.  How to handle the error ? sir 
@Jivraj


Error: The first input does not match the first text exactly

---

## Post #19 by 21f3002277 (Post ID: 583919)
Q4. How to handle this error? 
@Jivraj


{
  "id": "chatcmpl-AshDCPwSiXNao1QXmCxCmi63GifFx",
  "object": "chat.completion",
  "created": 1737599182,
  "model": "gpt-4o-mini-2024-07-18",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "The image contains an email address and a number. The email address appears to be associated with an educational institution, and the number seems to be a numerical sequence.",
        "refusal": null
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 592,
    "completion_tokens": 33,
    "total_tokens": 625,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "audio_tokens": 0
    },
    "completion_tokens_details": {
      "reasoning_tokens": 0,
      "audio_tokens": 0,
      "accepted_prediction_tokens": 0,
      "rejected_prediction_tokens": 0
    }
  },
  "service_tier": "default",
  "system_fingerprint": "fp_bd83329f63",
  "monthlyCost": 0.05490624000000001,
  "cost": 0.001974,
  "monthlyRequests": 14,
  "costError": "crypto.createHash is not a function"
}



Error: Model must be gpt-4o-mini

---

## Post #20 by Jivraj (Post ID: 584032)
Hi Nilay,








 nilaychugh:




both the URLs use same port,






You can run two servers on different port numbers.

---

## Post #21 by Jivraj (Post ID: 584038)
Hi Vikash,


I looked at your answers in backend. In answer you submitted response from openai, but you need to submit json object which is required for sending a request to LLM.


Kind regards

---

## Post #22 by Jivraj (Post ID: 584042)
You made same mistake here, instead of response use json body that’s required for sending request to LLM.


Kind regards

---

## Post #23 by 21f3002277 (Post ID: 584257)
Q4. how to handle this error ? 
@Jivraj


{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Extract text from this image"},
        {
          "type": "image_url",
          "image_url": { "url": "data:image/png;base64,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DOYQc83d7la67bar84q8XbP//qXbYYfS9YuJSdsaR+6nbLvsUsfWGWeU7n3vK93225du881L96Uvla4X6JP3+8X35P173KPeW77mwd12K92mm5bujW+sfVQ5+kX/ZNzvumvp+kXOanZa6KVeyqz8/cJ1UrfpuSOvvPLKK691+1rWM/UiPyLDokEPe1gp1752jYaJdvVOr/QOYhKV6x3UJDLXcGSlF9mld7aTiJBt38XSO9FJtEz02fa3yNdVrlLKXe5Sj9/YdhYNl6fImoi6yOed7lSjaragHaF46ENrNPl736vpeyFQeqc62SoXLRX9Ug/b7I78qIfomyi9yJ4ovnv2AmGSv8iX4yreEzkUlWcX+ftpK7t3ymdxm9vU4wei3yKM8h2D3dRZBE19+4VAudKV5j6cws6E6NxrXlMjbHe9a42GDukFwCTiLwpnO/+Rj6z2m4a9eqFUHve4GiV0nTqHsNIwLh05GY4P85D5qBfNk503O12i24udr0S8Rfnt8Pnc+DVOhuPctXZS+gXAJK37iNr3Yn0SDfe5a8whyvTyl9fovflDeey63fe+9ViOeUC+5gjjWEReOaVXN0d6+oXI5IiifO3APeQh9SiiHZ42j4q2mx/tNngtFrsadvfa/BlCCGHlsayintPYaqtSXvjCKlL9bbvYNjBnw7FxVqedVtOffnp1UEccUR3btttWB0hoNzgmDorod/SmHV0hwglbju/JTy7lEY+o29TuxcnJ2zEZIrhfzUxenKb3CFvHcjhc5eNELQo4T+WwnW3r3Ra1ow62vpVb3u5BuMuLo1W+612vlMMPr2W3pS5PL+J+ww3rVj+RrlzS7r9/KQ96UCkbbDBXyR5pLDIc/yEglHcM2/e22ZV1111XCYsx1IN9iZeddqr3bmdnm+0//ekqMHbeuQp/9T7wwCqGHvCAUp71rGpzP9lfWmW3SCF2iBcor8WLYwy77VbbcvvtSzn44LpAmsYC69BDa7r2evSj63GZ1j/mQ7scdVQVQO1aYu3446sAme4vjj886lHVbur8speVcthhdRFKgEE9LG4II/3KZyCKCCj97V73qvfae+9a91ZONhu7FmxicaiPKt+pp859MIdjF45GPP7xtW21i2MXjlYcdFA9EmI8WZgph7zYyZERotHRiPZyf+Vj95afoxePfeyq9w85ZLw9xrC4bNe213xt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u8WDcehevqFFP4N89S12sTg3P8h/DAsSbUzAa2NtpY+ab/R3/VAZlGVN5ivzhbpb7LKxvsuW7qeNzFe+KrKNafmbGyyEzQ36pHmEgCfS1U2ZlE1gwNgzBo1X+Rqn6ihw0fLV/7S7er3ylXWh6z35e1lUSMtGymtctP5rblAffYE9jTMP5hvr2mwabehBdu2hb3n+pbVHCCGEdc/6z+iZ+30R9J5zDeCEOCNb2y1SxBkMX8QTAeQnZzQNB+w6IpjAGDobwsJ1RI17EJTSi4o5KiE/ESwvQqaJT++7VnpOlMDg8OSvTMQgIShti5qrByEqL2mJGPcWfSNIiC9pOUjOVDpnpznT6Tq7H8HgGk6YEyUy50ur/mzkvsrN6fudIFUvkVR1mQ/p2cc95Dmd1t/qR0BZCBElykRsEBTqomzawAKC4PK58hNpIoUELQFMzItEawf3IrIJEW3CXkSUa7xEdC0MfO4lrfZodVdeUVR2bEK/CSeiSX6u0dZ+tnt6sZdrLQq0G7vJm4iRnl3dX1rl1fby8H4rp2vZTb2l0b6u97l+qAxso/8RWu5pgae9Wr8BMW4hpg677FLzcr2+wl7Ekn5EQOqbriWOjRll1j5NZLqXeiqrdmA35VGXVh79Vzptp96Qj/5i4el3+EwaaV2jTyuLhZI6EI3SKo/f3bONEfck+tlI2V3vxdbqp0+61qulN548N6HfqNOwLdm9oX3YktD2ub6u3Pog+zfkIW/9hG2kHYPd2YltXKMu+p1+RZy7lh3WdL5qc4Z2YBt1dQ/XmT/YZ1gvNvFSFnaSn3rpO+zo+jYvaW92kM41ymzMeVhXmZugl177yMtPZVEm5dMeFpDq4zN9zk+fqa+08tHX9Nv2z6XGBH1D2ZSTzZV92B4hhBDWLcsaqQ+zA4EpSuzbLU45pQovAp6wJ0LGFlzO4Ypc2zEQ+SMUnGUf23X5X8UCzy6Qc9QEn3+IRQgRRyGEEEIIS0VEfVgN0VPHPrxEAX0LjSiwiOE0jhE4AuIIgsikozSivqFGvD0E6Qy1o1L+dszDgieEEEIIYamJqA+r0b41gxh1BthZZed7HROaxvEIItU/9RGlF50fi+j/L+IM9xFH1HPRjo3sums9389OIYQQQghLTUR9GIW4d7beA4B+OkYyTTtfTtyH1fEQoqNJvlnEmWjnrJ0dDyGEEEJYDiLqQwghhBBCmHHyuF4IIYQQQggzTkR9CCGEEEIIM84aHr8JIYQQQgghrDQSqQ8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYcaJqA8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYcaJqA8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYcaJqA8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYcaJqA8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYcaJqA8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYcaJqA8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYaYp5f8A91ro9coVvFcAAAAASUVORK5CYII=" }
        }
      ]
    }
  ]
}



Error: The image_url.url must be the base64 data URL of the image

---

## Post #24 by 21f3002277 (Post ID: 584261)
Q8. how to handle the error ? 
@Jivraj


http://127.0.0.1:8000/execute?q=Expense+balance+for+emp+52094


{“name”: “expense_balance”, “arguments”: “{“employee_id”: 52094}”}


TypeError: Failed to fetch

---

## Post #25 by 22f3000445 (Post ID: 584413)
image
1366×622 27.1 KB


Why is my score is out of 8.5? It should be 9.5 right?

It was 9.5 before a reload.

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/d/1d37c6ff7591a3175f7be06068d9025f2627e65b_2_690x314.png)

**Image Description:** Here's a detailed description of the image:

**Overall Layout:**

The image appears to be a screenshot of a web application or platform, possibly for a coding or assessment task. It has a dark, sleek interface with green accents.

**Top Bar:**

*   A green bar at the very top displays the following:
    *   "Due Sun, 2 Feb, 2025, 11:59 pm IST" indicating a deadline.
    *   "Score: 2.75 / 8.5" showing the user's current score out of the total possible score.
    *   "Check" and "Save" buttons, suggesting actions related to an assessment or task.
    *   An icon on the right likely a display control.

**Content Sections:**

1.  **Recent Saves:**
    *   A green section with a title "Recent saves".
    *   Three "Reload" buttons, each linked to a save timestamp "from 24/1/2025, 12:25:51 pm" and a "Score: 2.75".

2.  **Questions:**
    *   A section titled "Questions".
    *   A numbered list of questions, each related to the topic of LLM (likely "Large Language Models"):
        *   LLM Sentiment Analysis (1 mark)
        *   LLM Token Cost (0.75 marks)
        *   Generate addresses with LLMs (1 mark)
        *   LLM Vision (1 mark)
        *   LLM Embeddings (0.75 marks)
        *   Embedding Similarity (1 mark)
        *   Vector Databases (1.5 marks)
        *   Function Calling (1.5 marks)
        *   Get an LLM to say Yes (1 mark)

**Color Scheme:**

The dominant colors are dark gray (background), green (highlighting, buttons, and sections), and white or light gray (text).

**Overall Impression:**

The screenshot presents a user interface for an assessment, quiz, or coding assignment related to LLMs. It allows the user to view their score, submit their work, and potentially reload previous saves. The clear structure and concise question titles suggest a well-organized and focused learning or evaluation environment.

---

## Post #26 by 23f2000237 (Post ID: 584421)
You should answer the third question every time the site reloads

---

## Post #27 by 22f3000445 (Post ID: 584453)
image
1122×471 13.9 KB


For question no.6, there was some pre-written code there, right?

I am not able to see it now.

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/c/ac8e969c93aa57f9b61d8e5a90ddf2a6174220e5.png)

**Image Description:** The image is a coding environment, likely a Python environment, as indicated by the instructions, code snippets, and error message.

**Here's a breakdown of the image's content:**

1.  **Instructions/Task:** The main instruction asks the user to write a Python function called `most_similar(embeddings)`. This function should calculate the cosine similarity between each pair of word embeddings provided in the `embeddings` argument. It should then return a tuple containing the two phrases from the `embeddings` dictionary that have the highest cosine similarity.

2.  **Initial Data:** The code begins by defining a dictionary called `embeddings`. This dictionary contains a single key-value pair, with the key being the string "Packaging was excellent." and the value being a list of floating-point numbers, likely representing the word embedding for the phrase.

3.  **Coding Area:** There's a large, empty code box where the user is expected to write the Python code for the `most_similar` function.

4.  **Error Message:** At the bottom, a `PythonError` traceback appears. The traceback indicates a `NameError` in the code. Specifically, it says "name 'most\_similar' is not defined". This means the user attempted to use the function `most_similar` but hadn't yet defined it in their code.

**In essence, the image presents a coding exercise where the user needs to implement a function to find the most similar phrases based on their word embeddings. The error message suggests that the user has yet to write the correct code.**

---

## Post #28 by 22f3000445 (Post ID: 584459)
image
1017×146 6.62 KB


I am getting insufficient_quota message for the 2nd question

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/0/4014d114b8ab5a993183871727062efe6a839400.png)

**Image Description:** The image is a screenshot of a command-line interface, likely a terminal or PowerShell window. It shows the execution of a Python script and the resulting error message.

Here's a breakdown:

1.  **Prompt:** At the beginning and end of the output, there is a prompt: "PS C:\\Users\\Varad\\OneDrive\\Documents\\Desktop\\Temp\\TDS>". This indicates the user is in a PowerShell environment and the current directory is "TDS" within the specified file path.
2.  **Command:** The command executed is `python -u "c:\Users\Varad\OneDrive\Documents\Desktop\Temp\TDS\request.py"`. This runs a Python script named "request.py". The `-u` flag forces Python to operate in unbuffered mode, meaning output is flushed immediately.
3.  **Error Message:** The script generates an error output in the format of a JSON object:
    *   `{'error': {...}}`: Encapsulates the error details.
    *   `'message': 'You exceeded your current quota, please check your plan and billing details.'`:  The core error message, indicating the user has exceeded their usage quota.
    *   `'type': 'insufficient_quota'`: Specifies the type of error.
    *   `'param': None`: Indicates no specific parameter is associated with the error.
    *   `'code': 'insufficient_quota'`: Gives a code associated with the error.
    *   `he docs: https://platform.openai.com/docs/guides/error-codes/api-errors.'`:Provides a URL to OpenAI documentation on error codes, specifically API errors.

In essence, the image reveals that a Python script, probably interacting with an OpenAI API (given the URL), failed due to quota exhaustion.

---

## Post #29 by Jivraj (Post ID: 586911)
21f3002277:




The image_url.url must be the base64 data URL of the image






I tried downloading image for your dataset it is 2.36 KB in size.

Using base64 encoded string from 
image_url.url
 in your code when decoded comes out to be 8.18 KB, when I encoded image from your dataset and decoded it was 2.36 KB.


image
1518×765 95.5 KB


Hints : check if encoding is correct.

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/a/aa81c404ee3eb793693a5bc6406886bd079e1635_2_690x347.png)

**Image Description:** Here's a detailed description of the image content:

**Overall Structure:**

The image appears to be a screenshot of a web page or application interface. It is displaying the results of base64 encoding or decoding.

**Key Sections & Elements:**

*   **"Base64\*" Section:**
    *   This is the primary section of the image, showcasing the base64 encoded data.
    *   There is a large text area containing a very long string that is likely the encoded data itself. It starts with "data:image/png;base64," indicating it is an encoded PNG image.
    *   The top right of the section has links to "copy", "clear", and "download".
*   **"Decode Base64 to Image" Button:**
    *   A blue button which will decode the base64 string in the previous section.
*   **"Preview Image" Section:**
    *   It displays the decoded image with a yellow bar on the bottom that says "21f3002277@ds.study.iitm.ac.in 92893354".
    *   Also contains a button that says "Toggle Background Color".
*   **"File Info" Section:**
    *   Provides metadata about the image that's been decoded:
        *   Resolution: 757x66 pixels
        *   MIME type: image/png
        *   Extension: png
        *   Size: 8.18 KB
        *   A link to download the "image.png".
        *   Bit depth: 8

**Content and Context:**

Based on the elements present, this image is a tool designed for base64 encoding or decoding. It allows a user to:

1.  Input a base64 string (or decode one).
2.  Preview the decoded image.
3.  See information about the image file (resolution, size, etc.).
4.  Download the decoded image.

---

## Post #30 by sharma_abhay (Post ID: 586942)
Is it required to give SCT for the ROE of this course?


Thank you.

---

## Post #31 by carlton (Post ID: 587025)
SCT is not required for ROE. ROE is not proctored.


Kind regards

---

## Post #32 by 23f2003853 (Post ID: 587062)
This is regarding Question 2 I tried to find number of tokens for the message. Using chatgpt identified the followings are valid English words for the given text in the question 
D
 
m
 
Ay
 
E r u y Vy
 
V Ky
 
P
 
c
. then, checked with 
https://platform.openai.com/tokenizer
. whatever number given by it seems to wrong.


@Jivraj
 could you inform me where I did mistake

---

## Post #33 by carlton (Post ID: 587070)
@23f2003853
 You have to find the input tokens from the json response you receive from the proxy.

---

## Post #34 by Jivraj (Post ID: 587175)
Hi VIKASH,


This problem must be because CORS not enabled or you are running your application inside wsl, if you using WSL then you would need to identify ipaddress of WSL and use it in place of 
127.0.0.1


kind regards

---

## Post #35 by 23f2003853 (Post ID: 587180)
Sir, from where can I  learn to locate the json response

---

## Post #36 by Jivraj (Post ID: 587188)
Hi 
@23f2003853
 ,


You can learn from 
Python’s Requests Library (Guide) – Real Python
 tutorial about how to use requests module and see responses.


kind regards

---

## Post #37 by Jivraj (Post ID: 587193)
22f3000445:




I am getting insufficient_quota message for the 2nd question






Which url are you using to send request to openai.

---

## Post #38 by Jivraj (Post ID: 587196)
22f3000445:




For question no.6, there was some pre-written code there, right?






pre-written code is not required for question 6.

---

## Post #39 by Divya1 (Post ID: 587325)
In the 6th question ,as I open the graded assignment all the time the new question is generated (NUMERICAL DATA) and the previous answer shows as incorrect answer


My doubt is that should I again and again answer the same quetion(6) all the time until the due passes?

Is there any alternative ways to look after this problem?

---

## Post #40 by 23f2002592 (Post ID: 587371)
Screenshot 2025-01-29 094832
1770×659 35.1 KB


how to solve???

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/b/ebc5f88e712a270b0763135c5a220d2fcd690c71_2_690x256.png)

**Image Description:** The image is a screenshot of code, likely a Python script, interacting with an API (likely OpenAI's), with a focus on error handling.  Here's a breakdown:

**1. Code Snippet:**

*   **JSON structure:**  At the top, there is a JSON structure representing a "messages" array. Within this array, there's a single object with the keys "role" (set to "user") and "content".  The content is a prompt to the API, asking it to "List only the valid English words from these:" and providing a list of seemingly random strings of characters.
*   **API Request:** The line `response = requests.post(url, headers=headers, json=json_data)` suggests the script is making a POST request to a specified URL. It's likely sending the JSON data (the prompt) to an API endpoint. The `headers` variable contains the headers, and the `json_data` variable contains the JSON payload.
*   **Error Handling:** The script includes error handling:
    *   It checks the `response.status_code` to see if the request was successful (status code 200).
    *   If successful, it prints the JSON response with an indent for readability.
    *   If the status code is not 200, it prints an error message indicating the request failed and prints the error text for debugging.

**2. Error Response:**

*   **Status Code 429:** The output at the bottom displays "Request failed with status code: 429".  Status code 429 indicates "Too Many Requests" (or rate limiting).
*   **Error Details (JSON):**  Below that, there is a JSON response detailing the error:
    *   `"message": "You exceeded your current quota, please check your plan and billing details..."`  This message confirms the reason for the error: the user's API usage has hit a quota limit.
    *   `"type": "insufficient_quota"`: Indicates the type of error.
    *   `"param": null`:  Provides no specific parameter related to the error.
    *   `"code": "insufficient_quota"`: A code also indicating the issue.
    *   **Docs link:** A link to the documentation on how to resolve the issue - suggests user to check billing details

**3. Overall:**

The image shows an attempt to use an API, likely OpenAI's API for text generation, with a Python script. The script formats a request to the API, and then the response indicates the user has reached their usage limit, triggering a 429 error. The script then displays an error message and some debugging info.

---

## Post #41 by 23f2002592 (Post ID: 587379)
getting quota full message for 7th question. How to get the answers then?

---

## Post #42 by Jivraj (Post ID: 587575)
Hi 
@Divya1
 ,


Question 6 requires to write a generic code for finding most similar pair. If your code is doing so, pls mention exact steps that you have used to arrive at answer.

---

## Post #43 by Jivraj (Post ID: 587577)
sanand0/aiproxy: Authorizing proxy for LLMs


Are you using this document?

---

## Post #44 by 23f2003853 (Post ID: 587882)
each time when I run the following code it gives me different number. None of the answer is correct. can help to fix the issue


image
584×246 46 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/e/1ec36689ada1168f9ad8b8d208eea27a96d39df5.png)

**Image Description:** Here's a detailed description of the image:

**Overall:**

The image appears to be a screenshot of a code editor window, likely displaying Python code related to interacting with an OpenAI API, specifically for chat completions using GPT-4. The code is well-structured with comments and hints, suggesting this is for educational or development purposes. The layout is typical of a coding environment, with syntax highlighting.

**Key Elements and Text:**

1.  **URL:**
    *   `url = "https://api.openai.com/v1/chat/completions"`
    *   This line establishes the endpoint for interacting with the OpenAI chat completion API.

2.  **Headers:**
    *   `headers = {`
    *   `    "Authorization": "Bearer {key}",`
    *   `    "Content-Type": "application/json"`
    *   This section sets the necessary headers for the API request, including the authorization (presumably using a bearer token) and the content type.

3.  **Input Strings:**
    *   `# List of input strings`
    *   `user_message = ...`
    *   `# List only the valid English words from these:`followed by gibberish words, perhaps used for testing.

4.  **Data Preparation:**
    *   `# Prepare the payload for Chat API (gpt-4 model)`
    *   `data = {`
    *   `    "model": "gpt-4-mini", # Use the gpt-4 model`
    *   `    "messages": [{"role": "user", "content": user_message}], # Messages format`
    *   This section creates the payload (data) that will be sent to the API. It specifies the model to be used ("gpt-4-mini"), and forms the message structure (role and content).

5.  **API Request:**
    *   `# Send the POST request to OpenAI API`
    *   `response = requests.post(url, headers=headers, json=data)`
    *   This line performs the POST request to the OpenAI API using the prepared `url`, `headers`, and `data`. The `requests` library is used.

6.  **Response Processing:**
    *   `# Parse the JSON response`
    *   `response_json = response.json()`
    *   This part parses the JSON response received from the API.

7.  **Status Check:**
    *   `# Check if the request was successful`
    *   `if response.status_code == 200:`
    *   `    input_tokens = response_json.get("usage", {}).get("total_tokens", "N/A")`
    *   `    print(f"Input tokens used: {input_tokens}")`
    *   `else:`
    *   `    print(f"Request failed with status code: {response.status_code}: {response_json}")`
    *   This is a standard check to see if the API request was successful (status code 200). If successful, the code extracts and prints the "total\_tokens" value from the response.  If unsuccessful, an error message including the status code and the response JSON is printed.

8.  **Additional Information:**

    *   "Input tokens used: 644"
    *   This is at the bottom, outside of the code, showing a final metric or result (likely after executing this program).

9. **Environment:**

    *   The code is written in Python, based on the syntax and the import of the "requests" library.
    *   The window also shows the "Activate Windows" prompt, so the OS is most likely Windows

**Possible Questions Answered by the Image:**

*   How to set up a basic API request to the OpenAI chat completion API.
*   The format of the request (headers, data, etc.).
*   How to handle the API response (parsing, checking status).
*   How to retrieve the number of tokens used.
*   The programming language being used.

**In summary,** the image shows example Python code that sends requests to the OpenAI API to generate text completions for use in a chat bot. The comments guide the user through the different steps that are necessary.

---

## Post #46 by Jivraj (Post ID: 588058)
Hi 
@23f2003853
 ,


Please join tomorrow’s session, we can take it there, I am not sure why you facing this problem.

---

## Post #47 by 23f2003853 (Post ID: 588067)
Sure Sir. I am providing you the code below


import json
import os

api_key = key

# Set up the endpoint and headers
url = "https://api.openai.com/v1/chat/completions"  # Use chat completions endpoint for GPT-4
headers = {
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json"
}

# List of input strings
user_message = """
List only the valid English words from these: Q5YpaFZ0S, qZXgs13f, zyCiAjPh, JfcKU, G51N4, D, 9GbmmI27, jbdnhCd, 2dTr75, m, kS, lhO3Uc8e, SjpEmLl, u1cnuqk50, W54, 9, 7YWtUR, reoWxE2, Ay, ANRl2pFjL, E, 4hcE4cB, TZ2t, vck6a, Sb6vQ5K, CzQ, T5lYjxy1m, 2D, yG7PLW, mvgHmixMqn, YOPzsuhQ3, nSF7e6zFF, J60xA5WVp3, oz, vJM, vp2Zrsr, 59wiruyNzq, r, 8N, wv, z, MAKFrf5, 2L, 1IwLjzNpma, 5N20N7Zuq, 9dVp, tmUao0x, u, QRxy67, y, jrIvOZ, t3i, rptivNJF, Vy, 5WWaC1u, WC, xfoGYp, 350c94lf, Pc9oNu, 1bOnLseHUm, aguOp0jxE, Tbz, qX, 9amaVxKFh, bnBkkNN5jc, o7N4y6, V, Ky, ewWw0qcLnw, bbD7MBGM7x, c0l, P, TMFOMvW, c, THRovqGNKb, BV, XIZcX, J0rDx3c, DxEvjEh, j9, Db5Hij, vpSJyCeyh, Z, D, yWpxiOwRXx, 7NeZN1GVE, Y, Lq6Pk, BCJT
"""

# Prepare the payload for Chat API (gpt-4o-mini model)
data = {
    "model": "gpt-4o-mini",  
    "messages": [{"role": "user", "content": user_message}],  

}

# Send the POST request to OpenAI API
response = requests.post(url, headers=headers, json=data)

# Parse the JSON response
response_json = response.json()

# Check if the request was successful
if response.status_code == 200:
    input_tokens = response_json.get("usage", {}).get("total_tokens", "N/A")
    print(f"Input tokens used: {input_tokens}")
else:
    print(f"Request failed with status code {response.status_code}: {response_json}")```

---

## Post #48 by 24f2006531 (Post ID: 588214)
Hello Sir,


I am unable to recieve a proper output for q1 of ga3.

This is my test message. Its been given in two lines.




The below is my code for the question.


import httpx

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Authorization": "Bearer api_key",
    "Content-Type": "application/json"
}

system_message = "Analyze the input message if it's  GOOD , BAD or NEUTRAL."
user_message = "2 b7 rkS94mn4  AM dNG4j EVevK24Ev VEpI G LeeHS"

payload = {
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "system", "content": system_message},  # System message
        {"role": "user", "content": user_message}       # One user message
    ],
    "temperature": 0.7
}

response = httpx.post(url, headers=headers, json=payload)

response.raise_for_status()

result = response.json()

for choice in result["choices"]:
    print("AI Response:", choice["message"]["content"])



I tried to put the two test lines as two user messages but received an error stating that the json body must contain only 2 messages with one mandatorily being a system message. With that in mind, i also tried the alternative


user_message = "2 b7 rkS94mn4 \n AM dNG4j EVevK24Ev VEpI G LeeHS"


The error message i keep receiving is as below.




Kindly advice on how to proceed.


Thanks and Regards

Shalini

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/0/60deb1fe7cda3d6876df481d07803e66d1974e45.png)

**Image Description:** Here's a detailed description of the image content:

**Overall:**

The image appears to be a text snippet or a data entry displayed on a dark background. It contains a series of short alphanumeric strings, likely representing codes, identifiers, or possibly names.

**Text and Characters:**

*   The text is displayed in a sans-serif font, likely white or light gray against the dark background.
*   The text is arranged in two rows.
*   **Row 1:**
    *   "2" (in a slightly lighter shade of blue)
    *   "b7"
    *   "rkS94mn4"
*   **Row 2:**
    *   "AM"
    *   "dNG4j"
    *   "EVevK24Ev"
    *   "VEpI"
    *   "G" (colored in green)
    *   "LeeHS"

**Additional Notes**

*   The presence of the green "G" suggests it could potentially be a status indicator.

![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/4/740853eca092fd94814c5c4cb8cc4ddb5f10eba3.png)

**Image Description:** Here's a detailed description of the image:

**Overall Structure:**

The image appears to be a screenshot of a code or log output. It has a dark background and uses a monospaced font, suggesting it's related to programming or system administration.

**Textual Elements:**

*   **Title/Heading Area:** The top portion begins with "payload = {".  This likely indicates the start of a data structure or message.
*   **Error Message:** The primary content of the image is an error message: "Error: The user message must be 2 b7 rkS94mn4 AM dNG4j EVevK24Ev VEpI G LeeHS, not 2 b7 rkS94mn4 AM dNG4j EVevK24Ev VEpI G LeeHS"
    *   The error message states that the user message is invalid. It specifies an invalid user message and an expected user message. The invalid and expected user messages are identical, highlighting a potential issue with the system's validation logic.

**Visual Cues:**

*   **Error Indicator:** The presence of the word "Error:" and the reddish-pink highlighting around the text indicate that the information is an error. This is a typical way to convey error messages in coding environments.
*   **Code Formatting:** The use of a monospaced font and indentation patterns aligns with the styling of a code output or log.

**In Summary:**

The image shows an error message related to the validation of a "user message" within a code or system environment. The error message's content is contradictory, where the rejected and the expected message are identical. The image suggests a problem in data handling and likely related to a software application.

---

## Post #49 by carlton (Post ID: 588213)
Hi Shalini,


Your 
user_message
 is incorrect. I looked at your exact GA and it works if you make sure your 
user_message
 is precisely what is given to you.


Hint: How do you store a multi-line variable in python?


Kind regards

---

## Post #50 by 21f2000588 (Post ID: 588228)
Hello, could anyone please confirm that GA 3 is worth 9.5 points? Since our GAs are typically 10 marks apiece, I wanted to inquire about and obtain clarification on this.

Thank you in advance.

---

## Post #51 by Yogesh1 (Post ID: 588278)
I was unable to make the answer box in Question 3 visible. I was only able to make white space appear there, but couldn’t make it so that answer can be input to the box.

---

## Post #52 by carlton (Post ID: 588283)
In addition to CSS classes there is also a tag attribute acting on it. Check carefully.


Kind regards

---

## Post #53 by 22f2000113 (Post ID: 588333)
I am getting below error for Q6 if i am importing sklearn libarary


image
1731×180 13.1 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/9/69111b8923cdb9542a042b96ae4fcb2501f758b1.png)

**Image Description:** The image displays a Python traceback, which is an error message that indicates a problem occurred during the execution of a Python program. 

Here's a breakdown:

*   **Error Type:** `ModuleNotFoundError`, meaning that the Python interpreter couldn't find a module called `scipy`.
*   **Context:** The traceback shows that the error occurred within the Pyodide environment, which is a Python distribution designed to run in the browser. The traceback points to files within the `_pyodide` directory within the Python installation.
*   **Problem:** The error message explicitly states that the `scipy` module is part of the Pyodide distribution but is not installed.
*   **Solution:** The message provides instructions on how to install the missing module using `await micropip.install("scipy")` in Python or `await pyodide.loadPackage("scipy")` in Javascript. It also includes a link to the Pyodide documentation for more information.

---

## Post #54 by 23ds2000092 (Post ID: 588423)
Hi team, I am using OpenAI API key for solving Q7 and getting the error like below


{'error': {'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.', 'type': 'insufficient_quota', 'param': None, 'code': 'insufficient_quota'}}



Is it necessary to pay for the OpenAI API key? Is there any other way?

---

## Post #57 by carlton (Post ID: 588469)
@21f2000588


Sure does add up to 9.5 , unless you want another question 


Kind regards

---

## Post #58 by s.anand (Post ID: 588481)
Yeah, after all these years of learning and teaching computing, I realize I can’t even count to 10 correctly anymore.


600×187 16.6 KB

---

## Post #59 by 23ds2000092 (Post ID: 588484)
@Jivraj
 Please let me know if the code is needed for this. I can share the code generated by chatgpt

---

## Post #60 by 24ds3000090 (Post ID: 588749)
@Jivraj
 , 
@carlton
  Dear Sirs, I need help in solving this question. I have the same issue. I have tried tokenizer tool, tried writing request code but still couldn’t get the correct answer. I have tried numerous time and ended up consuming lot of tokens . What should be the optimal approach in this question?


  "id": "chatcmpl-Aw7eXQ8hciiQ0ZedatQEifFGxnLhQ",
  "object": "chat.completion",
  "created": 1738415805,
  "model": "gpt-4o-mini-2024-07-18",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "The valid English words from the given list are:\n\n- a\n- I\n- o\n- t\n- U\n- w\n- y\n- z",
        "refusal": null
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 532,
    "completion_tokens": 34,
    "total_tokens": 566,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "audio_tokens": 0
    }
  },
  "service_tier": "default",
  "system_fingerprint": "fp_bd83329f63",
  "monthlyCost": 0.01662212,
  "cost": 0.001863,
  "monthlyRequests": 41,
  "costError": "crypto.createHash is not a function"
}

---

## Post #62 by 23f1000403 (Post ID: 589234)
Tried hundreds of different prompts, different situations but in Q9 AI is not responding “Yes”. Is there anything i am missing?

---

## Post #64 by 23f2003853 (Post ID: 589391)
Dear Sir, I got the answer in json but none out put is correct. Please help me to correct the code

curl 
https://api.openai.com/v1/chat/completions
 \                                             >   -H “Content-Type: application/json” \                                                                               >   -H “Authorization: Bearer $TOKEN” \                                                                                 '{                                                                                                                          >   -d ‘{                                                                                                           >     “model”: “gpt-4o-mini”,                                                                                            "messa>     “messages”: [{                                                                                             >       “role”: “user”,                                                                                                      "c>       “content”: “List only the valid English words from these: zqndWw3FB, kM, K, njuHs9A, r, lkXJ1lG, Z, yLHDClp, G1Db, 7, m, MYieYF3B, pFTQ1JU8Fj, RL9n6kE, EVpChB, V6iCpP, 9YwiwAnBc5, R, UM, mrnyc, 4ej9x, 8X, CQA9, jHC, uL4G6, f, zzaozWC9, 0qsOenEndF, qaZ2WoX, nXGZ”                                                                                   >     }]                                                                                                                >   }’                                                                                                                  {                                                                                                                         “id”: “chatcmpl-AwTPGH241yjyg9EkO1t1tbeGU7KCu”,                                                                         “object”: “chat.completion”,                                                                                            “created”: 1738499426,                                                                                                  “model”: “gpt-4o-mini-2024-07-18”,                                                                                      “choices”: [                                                                                                              {                                                                                                                         “index”: 0,                                                                                                             “message”: {                                                                                                              “role”: “assistant”,                                                                                                    “content”: “The valid English words from your list are:\n\n- my\n- is\n- an\n- or\n- in\n\n(Note: This assumes a focus on short English words. Longer words or specific proper nouns may also exist but were not included in this selection.)”,                                                                                                                         “refusal”: null                                                                                                       },                                                                                                                      “logprobs”: null,                                                                                                       “finish_reason”: “stop”                                                                                               }                                                                                                                     ],                                                                                                                      “usage”: {                                                                                                                “prompt_tokens”: 160,                                                                                                   “completion_tokens”: 53,                                                                                                “total_tokens”: 213,                                                                                                    “prompt_tokens_details”: {                                                                                                “cached_tokens”: 0,                                                                                                     “audio_tokens”: 0                                                                                                     },                                                                                                                      “completion_tokens_details”: {                                                                                            “reasoning_tokens”: 0,                                                                                                  “audio_tokens”: 0,                                                                                                      “accepted_prediction_tokens”: 0,                                                                                        “rejected_prediction_tokens”: 0                                                                                       }                                                                                                                     },                                                                                                                      “service_tier”: “default”,                                                                                              “system_fingerprint”: “fp_72ed7ab54c”                                                                                 }

---

## Post #65 by 22f3002557 (Post ID: 589614)
Pls give some kind of clue. It seems like a waste of so much time!

---

## Post #67 by 23f1000403 (Post ID: 589632)
i agree, i have wasted around 300 requests (prompts) and got nothing.

---

## Post #69 by 21f3002277 (Post ID: 590138)
Sir I am stuck in Q4. how to handle the error please help me 
@Jivraj
 
@carlton


Error: The image_url.url must be the base64 data URL of the image

---

## Post #70 by 21f2000588 (Post ID: 590143)
Okay thank you sir, for the clarification.

---

## Post #71 by Yogesh1 (Post ID: 590322)
You have to download that image, and find the base_url of that image.

---

## Post #72 by 21f3002277 (Post ID: 590325)
from where to download

---

## Post #73 by Yogesh1 (Post ID: 590342)
The image is part of the question.

---

## Post #74 by s.anand (Post ID: 590350)
For those who want to experiment with GPT-4o Mini (or other models), 
Github Models
 is free. You can explore and compare models, including GPT-4o Mini, DeepSeek R1, and others.


It has rate limits, so you can’t use it in production, but is a good place to prototype applications and experiment with prompts.


Please let me know if you face any problems accessing it.

---

## Post #75 by 23f2001915 (Post ID: 590386)
how to answer the question in first place ?

---

## Post #76 by Jivraj (Post ID: 590397)
Check if you are requesting through anand sir’s proxy 
AI Proxy
.

---

## Post #77 by Jivraj (Post ID: 590398)
sklearn might be using scipy for some purpose, just install it, it should work.


Btw what are you trying to do with Sklearn?

---

## Post #78 by 22f2000113 (Post ID: 590422)
thanks for the reply i was using cosine function but got another solution.

---

## Post #80 by 23f3004114 (Post ID: 590530)
Q2 LLM Token Cost ,


We have 
https://platform.openai.com/tokenizer
 , which helps us count tokens in a string, shouldn’t this be a better way than calling the API? However the returned value does not show as correct answer!

---

## Post #81 by 22f2001630 (Post ID: 590614)
Hi guys, just wanted to share that I found it hysterical when I saw this question:


image
1920×1080 305 KB

Like I literally showed this question to my mother and younger bro, stating the fact we ourselves had enable the answer box, they laughed there pants off…

More courses could be like this.

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/8/186f9bdca2765063fc8a6cfadc3e7b489543bfd4_2_690x388.png)

**Image Description:** Here's a breakdown of the image content:

**Overall Structure:**

*   The image appears to be a screenshot of a web page, likely related to a coding or programming assignment.
*   The top section of the page displays header information.
*   The main body contains text describing a task/problem to be solved, along with instructions and constraints.
*   There is a "Check" button at the bottom left, suggesting a code evaluation or submission mechanism.

**Header Information:**

*   The top bar indicates the website name, "exam.sanand.workers.dev/tds-2025-01-ga3".
*   There are titles, which might include "My Dashboard - IIT Madras On," "Graded Assignment 3: ITM," and other tabs.
*   The time and date are displayed: "Due Wed, 5 Feb, 2025, 11:59 pm IST".
*   The current score is 1/9.5, with "Check all" and "Save" buttons next to it.

**Main Content (Task Description):**

*   **Problem Context:** The text describes a logistics and delivery company, RapidRoute Solutions, facing issues with address data. They need to automate address generation using OpenAI's GPT-4o-Mini.
*   **Task:**  The user is tasked with creating the JSON body that should be sent to OpenAI's chat completion API.
*   **Specific Requirements:** The JSON must adhere to specific rules:
    *   Use model: gpt-4o-mini
    *   System message: Respond in JSON
    *   User message: Generate 10 random addresses in the US
    *   Use structured outputs to respond with an array of objects containing `apartment` (string), `zip` (number), and `latitude` (number) fields.
    *   Set `additionalProperties` to `false`.
*   **Instructions/Constraints:** The assignment clarifies that an API key is not needed, and the user should just write the correct JSON body.
*   **Other Details:** Includes a URL for the API call: https://api.openai.com/v1/chat/completions.

**Other Features:**

*   **Code snippets:** There appear to be some example code snippets showing the expected format for certain data fields.
*   **Check Button:** At the bottom left, there's a "Check" button for potentially submitting/testing the code.

In summary, the image showcases a programming assignment that involves using OpenAI's GPT model to generate address data in JSON format, focusing on specific requirements for data structure and API interaction.

---

## Post #82 by 23f1002382 (Post ID: 590620)
Q4

s3 string was given by


image_b64 = ""
import base64
with open('/content/TDS_wk3_q4.png', 'rb') as f:
    binary_data = f.read()
    image_b64 = base64.b64encode(binary_data).decode()
data_uri = f"data:image/png;base64,{image_b64}"




s4 string given by : 


used this 
link 
  to generate image url


 Then checked them both, they were the same


for x,y in zip(s3,s4):
  if (x != y):
    print(x,y)



i verified that both were equal but still one gave the wrong answer(python code), while the online converter gave the right one?

I know i’m missing something, but why?

---

## Post #83 by 23f1002382 (Post ID: 590626)
Screenshot 2025-02-04 193342
1670×487 54.1 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/3/930cebd4faf92d9bf89cf1f4939525e563be75fd_2_690x201.png)

**Image Description:** The image presents a coding environment with a Python code snippet. Here's a detailed breakdown:

**Overall Structure:**

*   **Header:** Contains instructions: The user is tasked with writing a Python function called `most_similar(embeddings)` that calculates the cosine similarity between embeddings and returns the most similar pair.
*   **Code Editor:** A rectangular box where the user can write Python code. It includes:
    *   `import numpy`:  This line imports the NumPy library, likely for numerical operations (e.g., calculating cosine similarity).
    *   `def most_similar(embeddings):`: This is the function definition as requested in the problem description.
    *   `# Your code here`: A comment indicating where the user should insert their code.
    *   `return (phrase1, phrase2)`: A placeholder return statement. This is where the most similar phrases should be returned.
*   **Error Message:** Below the code editor, a red-colored error message is displayed. This suggests that the code written inside the code editor is not correct, and it encountered errors. Specifically, the error is a `NameError: name 'phrase1' is not defined`.
*   **"Incorrect answer"**: A button that probably triggers evaluation and shows that the user has failed the assessment.

**Specific Elements and Their Significance:**

*   **`most_similar(embeddings)` Function:** The core task involves creating a function named `most_similar` that takes `embeddings` as an argument.  This implies that the code will need to iterate through the `embeddings`, calculate similarities, and return the pair of phrases that have the highest similarity.
*   **`import numpy`**: This line imports the NumPy library, and it implies the need for using linear algebra for the cosine similarity calculation.
*   **Error Analysis**: The `NameError` message tells us the error happened because the code attempted to use the variables `phrase1` or `phrase2` without them being defined or assigned to a value.  This indicates that the current placeholder `return` statement will not work without modifications.
*   **Context**: The overall design and instruction suggest a programming exercise or a coding assessment related to natural language processing or machine learning (due to the use of "embeddings" and the focus on similarity).

---

## Post #84 by 24ds2000125 (Post ID: 590627)
Screenshot 2025-02-04 at 19.32.21
2700×488 55.4 KB

This is in context to Q8. This is a screenshot of the response I am getting when i run the same API on my FastAPI/docs response page, it gives the correct response. But when I check it on the assignment page i get the following error. If you would like to know the code, pls let me know. 
@carlton
 
@Jivraj

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/3/f38de51c756863f15a20f702f3fda53103d9f24a_2_690x124.png)

**Image Description:** The image displays a section of a web page or application related to an API.  It focuses on API endpoint testing or documentation.

Here's a breakdown:

*   **Title:** The text "What is the API URL endpoint for your implementation? It might look like:" is a clear prompt.
*   **API Endpoint Example:**  A suggested API URL, "http://127.0.0.1:8000/execute," is given.
*   **Input Field with Error:** An input field is present, likely for the user to enter their API endpoint. The input field itself contains the same suggested API endpoint as the example.  There's a red outlined box around the field, and a red information symbol.
*   **Error Message:** Directly below the input field, the red text "SyntaxError: "undefined" is not valid JSON" indicates a problem with JSON syntax or data.
*   **Verification Instructions:** Text that says "We'll check by sending a GET request to this URL with ?q=... containing a task. We'll verify that it matches the expected response. Arguments must be in the same order as the function definition." It explains that the application will test the entered URL by sending a GET request.
*   **Check button:** There is a button "Check" to submit the input and run the check.

---

## Post #85 by Sudhishnarayan (Post ID: 590666)
Good Evening, I have a doubt regarding 7th and 8th question. I am getting this error of expecting three matches while saving. But, Externally when I check this API, I tried considerable test cases, and I am getting the output correctly. Can you please check this and give a solution. Thank You




Screenshot 2025-02-04 214319
1694×202 16.4 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/2/b2931cf4f6b39b884ab54950c2f49898c942c780.png)

**Image Description:** The image displays text on a black background. The text is a Python dictionary, denoted by curly braces { }. The dictionary has a single key-value pair. The key is 'matches', and its value is a list, denoted by square brackets [ ]. The list contains three string values: 'banana', 'watermelon', and 'jamaica'. The text appears to be in a sans-serif font, probably white in color, against the dark background.

![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/6/86600e3fd52f0a72acb9d99e8e3e58ccefb431df_2_690x82.png)

**Image Description:** Here is a detailed description of the image:

**Overall:**
The image displays a dark-themed user interface, possibly a code editor or a similar application. The background is dark gray, with text in a light, almost white color, and some highlighted text in pink/red. 

**Text Content:**

*   "Make sure you enable CORS to allow OPTIONS and POST methods, perhaps allowing all origins and headers." This is a general instruction or a note regarding enabling CORS (Cross-Origin Resource Sharing) in the context of the API. It suggests enabling both OPTIONS and POST methods.
*   "What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/similarity" This section is providing guidance or prompting for the user's API endpoint.  It gives an example URL and includes a question about the user's implementation.
*   "http://127.0.0.1:8000/similarity" is displayed inside of an input box or text field, representing the suggested API endpoint, the example is then typed in the input box.
*   "Error: Expected 3 matches." This is an error message, appearing below the text field where the user probably has input the URL.

**Visual Elements:**

*   **Input Field/Box:** A text input field contains the example URL. The field has a pink/red outline.
*   **Information Icon:** An "i" inside a circle in pink/red is displayed on the right side of the input field.
*   **Text Formatting:** The use of different font colors such as pink/red and white to highlight certain words and show the error.

**Possible Context and Functionality:**

*   The image appears to be related to API development. The emphasis on the API endpoint URL and the CORS guidance indicates the user might be setting up an API, possibly for a web or mobile application.
*   The error message implies that the input URL did not conform to some validation requirements.
*   The UI design suggests a code editor, IDE, or a similar environment for developers.

---

## Post #86 by Sudhishnarayan (Post ID: 590677)
This is regarding the 8th question. Same here, I am getting the answer for all the test cases, but then also, I am getting error in the portal while saving. Please help me out here. Thank You.


Screenshot 2025-02-04 232048
1322×152 8.42 KB


Screenshot 2025-02-04 231847
1608×129 9.97 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/d/ddbe5c805694b8f007f3e717bc45eac007960b57.png)

**Image Description:** Here's a detailed description of the image:

**Overall Structure:**

The image appears to be a screenshot of a web browser's developer tools or a similar environment. It displays a JSON response that likely results from a query to a server. The background is dark, with light-colored text for readability.

**Browser Address Bar:**

*   The browser address bar is visible at the top, with the URL: `127.0.0.1:8001/execute/?q="Calculate%20performance%20bonus%20for%20employee%2010056%20for%202025."`
    *   This URL points to a local server (127.0.0.1:8001).
    *   The query string `?q=` suggests this is a search-type query.
    *   The value associated with `q` is a URL-encoded string: `"Calculate performance bonus for employee 10056 for 2025."`. It seems like the intent is to calculate a performance bonus for an employee with ID 10056 for the year 2025.

**Content Area:**

*   **"Pretty-print" :**  In the top-left corner, there's a label "Pretty-print," implying the JSON output is formatted for readability.
*   **JSON Output:** The primary content is a JSON (JavaScript Object Notation) string.
    *   `{"name":"calculate_performance_bonus", "arguments":"{\"employee_id\": 10056, \"current_year\": 2025}"}`
    *   This JSON represents the result of the request made through the URL.
    *   `"name": "calculate_performance_bonus"` indicates that the function called or the task performed was to calculate the performance bonus.
    *   `"arguments": "{\"employee_id\": 10056, \"current_year\": 2025}"` :This shows the input parameters that were supplied to the `calculate_performance_bonus` function. The JSON within the `arguments` key contains the `employee_id` (10056) and the `current_year` (2025).

**In summary:** The image shows the result of a query from a local web server that is designed to calculate a performance bonus for employee 10056 for the year 2025. The server has returned a JSON response detailing the request parameters.

![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/7/47838def09407abba1ed55156bfc72463682d8a5_2_690x55.png)

**Image Description:** The image displays a text-based interface, likely within a coding or development environment. 

Key elements:
*   **Title/Question**: "What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/execute" This indicates the prompt is asking for the correct URL for an API endpoint.
*   **Input Field**: A text input field is present, outlined in a reddish border. Inside, the text "http://127.0.0.1:8001/execute" is visible, representing a potential URL.
*   **Error Message**: The text "TypeError: Failed to fetch" is displayed below the input field. This suggests an issue with accessing the specified API endpoint, potentially due to network connectivity or an incorrect URL.
*   **Visual Style**: The background is a dark gray or black. Text is primarily white, with some red coloring for the borders and error message.

In summary, the image presents a user interface where the user is prompted to enter an API URL, the default being "http://127.0.0.1:8001/execute", and an error is displayed to suggest a failure. This strongly suggests a developer environment.

---

## Post #87 by 22f3002723 (Post ID: 590682)
For question 1 getting the below response … not sure what it means

ythonError: Traceback (most recent call last): File “/lib/python312.zip/_pyodide/_base.py”, line 523, in eval_code .run(globals, locals) ^^^^^^^^^^^^^^^^^^^^ File “/lib/python312.zip/_pyodide/_base.py”, line 357, in run coroutine = eval(self.code, globals, locals) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File “”, line 53, in  TypeError: unhashable type: ‘dict’

---

## Post #88 by 22f3002723 (Post ID: 590701)
@carlton

for question 2 what does  the below instruction mean … also how to indicate this in a prompt ’ Remember: indicating that this is a 
user
 message takes up a few extra tokens. You actually need to make the request to get the answer."

---

## Post #89 by 22f3002723 (Post ID: 590709)
For token count query , trying to do something like below any issues with this


import requests
import json
from google.colab import userdata
def generate_readme_content(proxy_url,auth_token):
    # Prepare the payload
    prompt = f"""       
    SNyFiNTb, BUkDfo0tR, x3x, 6NE8Rq833, Re7, Vth9bYJ0pK, pnI, JAXpFb, BRPE, o, 5xVQe, iY8yVT, 69w, LjLCzs, MJ1g, wBR, 0H, 6bK, AMw, Vrxiux, dqZysH, yD82hcr, FZrwV8Zjq, Xb2, quLpdQqxd1, lqSLbI, HerfhK2, rNPU, 9K1C, 0ywhX2s4O9, mjZ, sR9gCC, 2WVSfwWEae, c, DtWnfOncFj, qjK8P7xh, 0xraHn7RMa, OCmQIi3tbU, S2K, F, q5mO, yZt, X, zd, se0ss3k, uU, yCRCi, S3bMfb, qZ4dh, M7, uhxgDvG3, 696g, 9k, l5U, bH, LVXw1fdWFi, 0kU68gGP, WuyD, V, kVKQ1Y8, kLjMDoEmIN, EYHs7qsabQ, sWrC8vN7n, oAJZP, YLd, mi6Jmxgf, cb9UDdap, kzuot, R0eA2V, mr7SctL49, Td5, in, hxvi, MDg, AAK, uLBF889bO5, Z7z, AO0c, nbc, bE6Rsdw5b, 0, pBjOAuPN8A, 9C3, K, 8, yZyCBPz   
    """
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant to count the number of english words in a message. Find the number of input tokens used for  a message lile below. Try excluding tokens used for understanding this prompt"},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 500,
        "temperature": 0.7
    }
    
        # Send a POST request to the proxy server
    response = requests.post(
            proxy_url,
            headers={"Content-Type": "application/json",
                     
            "Authorization": f"Bearer {auth_token}"},
            data=json.dumps(payload)
        )
    response_data = response.json()
    return response_data
proxy_url = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
auth_token=userdata.get('aiproxy_secret_key')
tokenjson=generate_readme_content(proxy_url,auth_token)
print(tokenjson)

---

## Post #90 by Namannn28 (Post ID: 590740)
I GOT THE CORRECT ANSWER F0R QUES 7 & 8 STILL MY SCORE IS SHOWING 8 DOES ANYONE KNOW HOW TO DO THIS ?


image
1903×819 96.2 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/4/74e3d955c0092ec1d309185d71f086931815db2c_2_690x296.png)

**Image Description:** Here's a detailed description of the image's content:

**Overall Layout:**

*   The image presents instructions, presumably for a quiz or exam. The background is dark gray, with text in white and some blue elements.

**Text Content:**

*   **Title:** "TDS 2025 Jan GA3 - Large Language Models". This title suggests the subject matter is related to "Large Language Models" and that the document relates to a test or assignment that will take place in January of the year 2025.
*   **Instructions:** A numbered list of instructions with several bullet points:
    *   The user is free to skip reading materials provided.
    *   Answers can be checked by pressing a "Check" button, which will tell the user what answers are right or wrong.
    *   Answers can be saved repeatedly by pressing a "Save" button, and the last submission will be evaluated.
    *   Reloading the page is okay.
    *   The browser may struggle.
    *   The user is allowed to use any resources available.
    *   The quiz is "hackable" and allows the user to get answers by hacking the code.
*   **Note:** The note states that the user will be running multiple servers simultaneously while checking and saving their answers.
*   **Footer:** "Have questions? Join the discussion on Discourse". This is a link, implying that there is a discussion platform connected.

**Visual Elements:**

*   **Buttons (Simulated):** The word "Check" and "Save" are styled in a way that indicates these are buttons to be clicked.
*   **Branding:** There are two icons visible on the bottom right: a speech bubble with an eye icon and a brain.

**Inferences:**

*   This image likely depicts the instructions for an exam or quiz focused on "Large Language Models".
*   The instructions are permissive, encouraging students to use external resources and acknowledging the possibility of "hacking" the code.
*   The use of phrases like "multiple servers" and "hackable" suggests the quiz is likely online.
*   The instructions are detailed and provide helpful information about how to interact with the quiz interface.

---

## Post #91 by Jivraj (Post ID: 590786)
Use addition : to add up your score for each question.

eq:

1+ 1 = 2

Fractions are harder

1.5 + 1 = 2.5


image
657×512 35.6 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/6/361bc0f48c8b87ceaca00d63c83ff669a520c445.png)

**Image Description:** The image presents a list of nine questions, likely for an exam, quiz, or assignment. The title "Questions" is displayed prominently at the top in a light color, possibly white or light gray. The list items are numbered from 1 to 9 and are written in a darker color, possibly white on a black background for contrast. Each question is followed by the marks allocated to it in parentheses. The questions cover topics like:

1.  LLM Sentiment Analysis (1 mark)
2.  LLM Token Cost (0.75 marks)
3.  Generate addresses with LLMs (1 mark)
4.  LLM Vision (1 mark)
5.  LLM Embeddings (0.75 marks)
6.  Embedding Similarity (1 mark)
7.  Vector Databases (1.5 marks)
8.  Function Calling (1.5 marks)
9.  Get an LLM to say Yes (1 mark)

The topics covered by the questions suggest a focus on Large Language Models (LLMs) and related concepts, such as sentiment analysis, token costs, vision applications, embeddings, similarity, vector databases, and function calling. The presence of "marks" next to each question indicates the questions are likely part of an assessment.

---

## Post #92 by 22f2001630 (Post ID: 590788)
To this question I have checked values ranging from 6 to 13 none of them are correct, using openAI Tokenizer online tool.


image
1920×1080 248 KB


image
1920×1080 225 KB

Please help me were I am going wrong.

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/3/b341cadb37794f0099e4e64b5543980b4102141f_2_690x388.png)

**Image Description:** Here's a detailed description of the image:

**Overall Layout:**
The image shows a webpage with an assessment or quiz. The page is focused on a task related to tokenization and LLM (Large Language Model) token costs.

**Key Elements:**

*   **Header/Top Bar:**
    *   There's a green banner-like bar at the top of the webpage.
    *   "08:04:14 left" indicating time remaining.
    *   "Score: 0/9.5" displaying the current score.
    *   Buttons: "Check all", "Save".
    *   The address bar shows the web address of the test.
*   **Question Section:**
    *   **Title:** "2 LLM Token Cost (0.75 marks)"
    *   **Context/Introduction:** Explains that LexiSolve Inc. is a startup specializing in AI and that the task focuses on the cost of LLM tokens. It highlights the importance of accurate token accounting, given the token-based pricing for these models.
    *   **Task Description:** The primary task involves an understanding of text tokenization using OpenAI's GPT-4o-Mini.
    *   **Specific Instructions:**
        *   "Specifically, when you make a request to OpenAI's GPT-4o-Mini with just this user message:"
        *   There's a blacked-out/masked section which is a placeholder for the actual user message.
        *   "List only the valid English words from these:"
        *   "... how many input tokens does it use up?" This suggests the user needs to calculate token count.
        *   A text box for entering the "Number of tokens:"
    *   **Additional Note:** "Remember: indicating that this is a user message takes up a few extra tokens. You actually need to make the request to get the answer." This gives additional context and hints.
    *   **Check Button:** A button is available to 'Check' the answers.

*   **Bottom Section:**
    *   A typical Windows taskbar at the bottom with a search bar, application icons, and time display.
    *   "Activate Windows Go to Settings to activate Windows."

**Functionality and Purpose:**

This appears to be an assessment or a learning exercise, likely for a course related to AI, Natural Language Processing (NLP), or potentially software engineering. The task requires the user to:

1.  Understand the concept of LLM tokenization.
2.  Determine the input tokens from some user message by listing the valid words.
3.  Determine the number of tokens used by the input.

Let me know if you would like me to elaborate on any of these points!

![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/7/37496a4df09c5e0db5288c51e938ccc952161009_2_690x388.png)

**Image Description:** The image appears to be a screenshot of the OpenAI tokenizer tool. The webpage is open in a web browser, with the URL "platform.openai.com/tokenizer" displayed in the address bar. 

Here's a breakdown of the visible elements:

*   **Header:** The webpage has a header with "personale / Default project" displayed. There are also navigation options such as "Playground," "Dashboard," "Docs," and "API reference." There's a profile icon in the top-right corner.
*   **Text Input/Output:** There is an area where the user can input text for tokenization, and the resulting tokens and character counts are displayed. In this case, the provided text is "List only the valid English words from these." and the token and character count is "10" and "47" respectively. Each word from the input text is highlighted by a different color, for example "List" is colored in a green color.
*   **Buttons:** There are "Clear" and "Show example" buttons. There are also "Text" and "Token IDs" buttons.
*   **Description:** Below the text input/output, there is a descriptive text providing information on how a token is related to a character. The information contains that a token generally corresponds to about 4 characters and for programmatic purposes, there is a suggestion for the user to check the "tiktoken" package.
*   **Footer:** The footer includes a windows activation note and the current time and date.

The image's content is focused on text tokenization using the OpenAI platform.

---

## Post #93 by Jivraj (Post ID: 590789)
22f3002723:




user
 message






that means it should be a user message


messages = [
{
"role":"user",
"content":"message"
}
]

---

## Post #94 by 22f2001630 (Post ID: 590795)
Keep getting this error.


image
1920×1080 252 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/c/ac6f9a3149c179a5053ec9bc5e5e56e1843ee49d_2_690x388.png)

**Image Description:** Here's a detailed description of the image content:

**Overall:**
The image shows a webpage, likely an online assessment or coding exercise related to AI or machine learning. The page appears to be a coding challenge interface or assessment.

**Header Area:**
*   **Top Bar:**  Contains the website address:  `exam.sanand.workers.dev/tds-2025-01-9a3`
*   **Timer and Scoring:** Displays a timer "07:38:35 left" and the score "Score: 0/9.5"
*   **Buttons:** Has buttons to "Check all" and "Save."
*   **Tabs:** There are multiple tabs in the browser related to various topics such as "My Dash", "Graded", "GA3 - Li", "TDS 20", "Async D", "uv: Py", "Running", "127.0.0.1", "4.75+1", "Tokeniz".

**Main Content Area:**

1.  **Instructions/Prompt:**
    *   The page has a prompt that starts with a description of what the response might look like, including example outputs.
    *   It describes the expected output and the desired formatting
    *   Mentions that the user should enable CORS for `OPTIONS` and `POST` methods.
    *   Asks "What is the API URL endpoint for your implementation?" and provides an example URL.

2.  **Input/Output Area:**
    *   It seems like there is a text box where the user has to provide the API URL. The provided API URL is  `http://127.0.0.1:8000/similarity`
    *   There is an error message: "Error: Got incorrect matches: Our customer feedback survey revealed that ease of use is a key area for improvement, The infrastructure upgrade includes improvements in data storage and retrieval, The technical documentation for the new product line is now available online."
    *   A "Check" button is present, presumably for the user to submit the implementation for evaluation.

3.  **Next question**
    *   The following prompt shows a "Function Calling (1.5 marks)" section.
    *   The heading is "Function Calling with OpenAI."
    *   The first paragraph, "Function Calling allows Large Language Models to convert natural language into structured function calls. This is perfect for building chatbots and AI assistants that need to interact with your backend systems."

**Other elements:**

*   **Footer:** The footer contains the Windows activation message "Activate Windows" along with the current time, date, and language settings.
*   **UI Elements:**  The layout uses a dark mode theme.

**In summary:** The image presents a webpage focused on a coding or assessment task, most likely related to API interaction, function calling with openAI and document processing. The user needs to input something (API URL) and can then test by using a "Check" button. The site is configured for an exam.

---

## Post #95 by Jivraj (Post ID: 590796)
Try sending an api call to openai.

---

## Post #96 by Jivraj (Post ID: 590800)
Check with network tab, you would see the response of api call being made, Compare that with expected output.


Regrading question 8, you would need to check if cors are enabled, check in browser console tab for more.


image
1909×939 126 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/2/62f7129cdef9e6686dd89ed466c755441ab55c49_2_690x339.jpeg)

**Image Description:** Here's a detailed breakdown of the image:

**Overall Context:**

The image is a screenshot of a web browser's developer tools, specifically the "Network" tab. This indicates that the user is examining network requests made by a webpage. The presence of "Console" and "Elements" tabs also visible in the top toolbar suggests the user may be debugging a website's behavior.

**Key Features and Objects:**

*   **Browser Window:** The image is taken from within a web browser. The browser's address bar and tabs are visible at the top. There are several tabs open related to "My Dashboard," "SOP Link," "Jan 2023 Grading," "Titanic dataset," "Academia.edu," "IIT Madras," and "About Project Euler."
*   **Developer Tools:** The dominant part of the image showcases the browser's developer tools.  These tools are used for inspecting, debugging, and modifying web pages.
*   **Network Tab:** The "Network" tab is selected in the developer tools. This tab monitors network requests and responses between the browser and a web server.
*   **Request List:** The central area of the "Network" tab displays a list of network requests. Two requests are visible, both with similar names: `1.0?cors=true&content-type=application/x-json-stre...`.
*   **Request Details Pane:** On the right side of the "Network" tab, there's a detailed view of a selected request. The "Response" tab is selected. The "Response" content is a JSON object: `{"acc":1, "webResult":{}}`.
*   **Header Bar:** There are controls above the network request list. The main ones include "Welcome," "<> Elements," "Console," "Sources," "Network" and other tools.
*   **Bottom Panel:** The bottom of the developer tools shows a console for logging and debugging.

**Text:**

*   The text provides clues about web page URLs and file paths that are the subjects of the user's inquiry.
*   Within the network request details, we see the JSON data being transferred.
*   Numerous toolbar items are labeled such as "console", "elements", "network".

**Possible Interpretations and Questions:**

*   The user is likely investigating the network traffic of a webpage.
*   The JSON response suggests that the web page might be sending data and receiving a response.
*   The user might be checking to see how the website delivers its information or whether there are performance issues.

---

## Post #97 by 23f2000098 (Post ID: 590801)
i am unable to find the answer box plss guide me through that

---

## Post #99 by 22f2001630 (Post ID: 590803)
You could use AI assistance it helped me.


image
1920×1080 319 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/a/2aff1e5adc662611798f393d90115b2597dd0e31_2_690x388.png)

**Image Description:** Here's a detailed description of the image:

**Overall Layout:**

The image shows a web browser window with a forum-like discussion thread open. The user has also opened the developer tools (likely Chrome DevTools or similar) to inspect the webpage.  The window is divided into several key sections.

**Main Discussion Thread (Left side):**

*   **Thread Header:** A section at the top displays the thread title and other identifying information.
*   **Posts:**
    *   **Post 1 (22f2001630):** The initial post says "Keep getting this error." It includes an image of a screen (possibly showing the error). The image preview shows '86 / 87'.
    *   **Post 2 (23f2000098):**  This post, likely a reply or follow-up, says "you ask for AI assistance, for it helped." The formatting interface for the post is also visible, allowing for text formatting, link insertion, and code input.
*   **Reply/Close Buttons:** At the bottom of the discussion thread, buttons for replying to a post or closing the current content.
*   **Input field:** There is a text field at the bottom of the thread for typing messages.

**Developer Tools (Right side):**

*   **Elements Tab:** The developer tools show the "Elements" tab, which displays the HTML structure of the webpage. This is the main focus of the DevTools in this image. Specific elements are highlighted ( `<body>` element is selected).
*   **Styles Tab:** Next to the "Elements" tab, the "Styles" tab is also opened. It displays the CSS styles applied to the currently selected HTML element.
*   **Console Tab:** The console tab is visible too. It appears that the console is open and displays log messages, errors, or other information related to the webpage's behavior.
*   **AI Assistance Panel:** An "AI Assistance" panel is also open in the developer tools. It appears to be a built-in tool designed to provide help with inspecting the webpage. The panel includes a prompt for asking a question about the selected element (likely referring to the `<body>` element). There are also suggested help queries like "What can you help me with?", "Why isn't this element visible?", and "How do I center this element?"

**Additional Features:**

*   **Address Bar:** The browser's address bar is visible and shows the URL of the forum discussion. The URL includes "discourse.onlinedegree.iitm.ac.in" and seems to be related to "ga3-large-language-models-discussion-thread-tds-jan-2025".
*   **Browser Navigation:** The standard browser navigation buttons (back, forward, reload) are visible.
*   **Date & Time:** The image displays the current date and time (05-02-2025, 16:40), presumably the time the screenshot was taken, in the bottom right corner.

**Key Interactions and Questions:**

*   The user seems to be encountering an error (reported in the first post) and is using the AI Assistance in the developer tools to help them.
*   The user is likely seeking advice on how to resolve a problem with the forum or a specific element within it.
*   The AI Assistance tool suggests asking questions such as "Why isn't this element visible?", likely attempting to identify display issues.

In essence, the image depicts a user actively troubleshooting a webpage issue with the aid of developer tools and an AI-assisted feature.

---

## Post #100 by Sudhishnarayan (Post ID: 590804)
Oh OK sure. I will try out and let you know. Thank You!

---

## Post #102 by 22f2001630 (Post ID: 590811)
Got the answer but it was wired that I had run the curl command three time and the 3 times I got different result.

---

## Post #103 by 23f2000098 (Post ID: 590813)
its not working for me any other options plss??

---

## Post #104 by 22f2000644 (Post ID: 590838)
23f2003853:




rm me where I did mistake






Sorry but im facing an issue with question 6 and 7 where its saying load failed when I submit it. when I run the queries locally using curl im getting the expected results.  Any help would be appreciated.


Screenshot 2025-02-05 at 6.19.41 PM
1304×299 30.1 KB


curl "http://127.0.0.1:8001/execute?q=What%20is%20the%20status%20of%20ticket%2083742?"

{"name":"get_ticket_status","arguments":"{\"ticket_id\": 83742}"}

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/e/6e298e68d8f6e5a413bd926c6bf11a6b2350c711_2_690x158.png)

**Image Description:** Here's a breakdown of the image's content:

**Overall Description:**

The image appears to be a section of a user interface, likely for an application or website that interacts with APIs. It guides the user on how to configure their API endpoint for testing.

**Textual Elements:**

*   **Header:** "Make sure you enable CORS to allow GET requests from any origin." This is a crucial setup step, indicating that the API needs CORS (Cross-Origin Resource Sharing) enabled for the tool to work.
*   **Instruction:** "What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/execute" This prompts the user to enter their API endpoint. It also provides an example of a potential URL.
*   **Input Field:** A text input field is provided with the URL "http://127.0.0.1:8001/execute" pre-filled. It appears the URL is showing a red border with an error icon.
*   **Error Message:** "TypeError: Load failed" is displayed, indicating a problem with accessing the provided URL.
*   **Additional Information:** "We'll check by sending a GET request to this URL with ?q=... containing a task. We'll verify that it matches the expected response. Arguments must be in the same order as the function definition." This section explains how the validation of the API endpoint will occur (a GET request with parameters).
*   **Button:** A blue button labeled "Check" is present, presumably to initiate the API validation check.

**Visual Elements:**

*   **Color Scheme:** The interface utilizes a dark background with white and red text, suggesting a specific design aesthetic.
*   **Alert/Error Indication:** The red border around the URL input field and the "TypeError: Load failed" message indicate a failure.
*   **Icon:** An "i" (information) icon appears inside a circle in the top-right corner of the URL input field.

**In essence, this image depicts a user interface for testing or integrating with an API. The UI is guiding the user to input their API endpoint and checks whether the request is able to fetch data. The presence of an error suggests that the provided API URL is either incorrect or not accessible from the environment where the tool is running.**

---

## Post #105 by abhigyandsa (Post ID: 590867)
For question 2, do we have to make the API call to the proxy or openai? If to the proxy, are there any instructions on the page 
before
 question 2 that would have pointed me in that direction?

---

## Post #106 by 23f2000098 (Post ID: 590869)
image
1287×568 32 KB

I am trying this for so long how to fix this plss guide me. thanking you

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/8/c80ada7b2d77694e21079c83df4a9b16ef88a6ef_2_690x304.png)

**Image Description:** The image appears to be a screenshot of a web application or a coding tutorial. It is divided into two main sections.

**Left Section:**

*   **Code Snippet:** Displays a JSON-like structure defining a function named "get\_ticket\_status" with an argument "ticket\_id" set to 83742.
*   **Instructions:** Provides guidance on enabling CORS (Cross-Origin Resource Sharing) for GET requests.
*   **API URL:** Suggests an API URL endpoint: "http://127.0.0.1:8000/execute".
*   **Error Message:** Shows an error message "SyntaxError: "undefined" is not valid JSON".
*   **Check Button:** Includes a "Check" button.

**Right Section:**

*   **Input Form:** Has a form with a field "q" labeled "What is the status of ticket 83742?".
*   **Buttons:** Displays "Execute" and "Clear" buttons.
*   **Responses Section:** Contains information about the API calls.
    *   **Curl command:** Shows the curl command used to make a GET request: `curl -X 'GET' 'http://127.0.0.1:8000/execute?q-hat%20is%20the%20status%20of%20ticket%2083742?' -H 'accept: application/json'`
    *   **Request URL:** Displays the URL used for the request: `http://127.0.0.1:8000/execute?q-hat%20is%20the%20status%20of%20ticket%2083742?`

**Overall Context:**

The image suggests a programming exercise or tutorial where the user is expected to implement an API endpoint to retrieve the status of a ticket given its ID. The left side provides the function definition and instructions, while the right side shows a UI where the user can test the API and see the underlying curl commands and URL. It seems there's an issue with the API, likely due to the "SyntaxError" or possibly CORS not being enabled, or the request parameters not being correct.

---

## Post #108 by 23ds2000050 (Post ID: 590875)
there is a problem in question 7 and 8, fast api question, when i click on save, both api calls happens at once at 
http://127.0.0.1:8000
, and i can run fast api app for question 7 or 8 for one only, suppose i check for question 7 it shows correct, also for question 8 i check it shows correct , but when i try to save one of the answer gets incorrected because of simultaneous calls by question 7 and 8 at this address 
http://127.0.0.1:8000

---

## Post #109 by Khushii (Post ID: 590877)
Screenshot 2025-02-05 at 7.44.03 PM
1920×1249 130 KB


while saving the 7th,8th question its alteranately getting incorrect


im getting 8.5 marks but while saving it gets deducted to 7 because of these 2 questions

this is really very frustrating since im working on this for so long like 5-8hours but still facing the same issue

what to do


@carlton
 
@s.anand

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/c/dca4d379baf52bec50126bd4f33cf4a0cab0ef17_2_690x448.jpeg)

**Image Description:** Here's a detailed description of the image:

**Overall Layout:**

The image appears to be a screenshot of a web-based programming or educational platform. The main content is a description of a "Service Flow" related to text search and similarity. It's organized in numbered points.

**Header/Navigation:**

*   At the top, there is a browser's address bar with the URL: "exam.sanand.workers.dev/tds-2025-01-ga3#hq-get-lim-to-say-yes". This suggests it's an online examination or exercise related to a course.
*   The top also has the browser's tabs, indicating the user is probably on a learning portal or course management system with tabs like "My Dashboard - IIT Madras", "Course Introduction : TMC", "Tools in Data Science", "TDS 2025 Jan GA3 - Large".
*   A green bar across the top contains a timer ("04:15:56 left"), a score ("Score: 8.5 / 9.5"), and buttons "Check all" and "Save". These elements reinforce the assessment context.

**Main Content - "Service Flow" Description:**

This section describes a process involving a POST request, embedding generation, similarity computation, and response structure.

1.  **Request Payload:** Defines the POST request's format, including `docs` (an array of document texts) and `query` (a search query).
2.  **Embedding Generation:**  Mentions the use of `text-embedding-3-small` for text embedding.
3.  **Similarity Computation:** Explains the calculation of cosine similarity.
4.  **Response Structure:** Describes how the API returns the identifiers of the most similar documents. An example JSON response is provided.

**Supporting Information & Questions:**

*   **Example Results:**  The example JSON format illustrates the potential output from the API call ("matches": "Contents of document 3", "Contents of document 1", "Contents of document 2").
*   **CORS and HTTP methods:** A note emphasizes the importance of enabling CORS for `OPTIONS` and `POST` methods.
*   **API URL Question:**  The image asks the user to specify the API endpoint URL, which is `http://127.0.0.1:8000/similarity`.
*   **Answer and Check:** The user provided an answer and the check mark suggests the user answered it correctly.
*   **Check Button:** An active "Check" button is present.

**Overall, the image is a question or task related to understanding and implementing a text search API. It provides a detailed description of how the API works and asks a direct question about the API's URL.**

---

## Post #110 by Khushii (Post ID: 590879)
Screenshot 2025-02-05 at 8.07.34 PM
1920×1249 138 KB

in the 1st as well both the outouts are exactly same but its still showing error


@carlton

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/3/f31ec62b15083018d37a532147aa73e9006987e1_2_690x448.jpeg)

**Image Description:** Here's a detailed description of the image's content:

**Overall Structure:**

*   The image shows a web page, likely an online coding platform or a course assessment. It has a dark theme.
*   There is a header at the top with a green bar, displaying a timer, a score, check and save buttons.
*   The primary content is a coding assignment or exercise related to sentiment analysis using a Large Language Model (LLM).

**Header Information:**

*   The top bar provides the following information:
    *   A left-hand side showing tabs for "My Dashboard" and "Course Introduction".
    *   A center indicating the current section is "GA3-Large Language Mod", and "Tools in Data Science".
    *   A right-hand side showing a timer and the current score (8.5 / 9.5). There are also "Check all" and "Save" buttons.

**Task Description:**

*   The primary section is centered around the coding exercise/assessment.
*   Instructions are provided numbered 1-4. These instructions outline the requirements for the code:
    1.  Ensure an Authorization header with a dummy API key is passed.
    2.  Use the "gpt-4o-mini" model.
    3.  The first message should be a system message prompting the LLM for sentiment analysis (GOOD, BAD, NEUTRAL).
    4.  The second message should contain specific text.
*   An explanation about the test's importance for DataSentinel Inc. is included.
*   There is a note, indicating a dummy `httpx` library is used.
*   Example code usage for the dummy library:
    1.  `response = httpx.get(url, **kwargs)`
    2.  `response = httpx.post(url, json=None, **kwargs)`
    3.  `response.raise_for_status()`
    4.  `response.json()`

**Code Section:**

*   A "Code" section is provided where the user will likely write their code.
*   The provided code structure is in a dictionary format:
    *   `DATA = {`
    *   `"model": "gpt-4o-mini",`
    *   `"messages": [`
    *   `{ "role": "system", "content": "Analyze the sentiment of the following text as GOOD, BAD, or NEUTRAL." },`
    *   `{ "role": "user", "content": "N PIxDC6t EXfymclF e K x1XTpIULdX t6H LTa YGZk," }`
*   There is an error message displayed below the code, which is informing that the user's message does not match the expected result.

**Buttons and Other Elements:**

*   A "Check" button.
*   An element with the text "2 LLM Token Cost (0.75 marks)".

**Overall, the image displays an interactive coding exercise designed to test a student's ability to interact with a LLM and to implement sentiment analysis.**

---

## Post #111 by Jivraj (Post ID: 590882)
You can run 2 different severs on different port numbers.


http://127.0.0.1:8000
 and 
http://127.0.0.1:8001

---

## Post #112 by Sudhishnarayan (Post ID: 590891)
I tried checking the JSON Output in the Networks tab. I am getting error as “Method Not Found”. But, I have allowed POST Method for question 7 as POST method is used in the question. I also tried checking my API by sending a POST request by the same parameters as given by the Website. I  am getting the proper response when I give an API request. Can you please help me out here? I have attached the screenshot  of the error as Picture -1 and the correct output what I get as Picture-2.  Please help me out as I am facing issue for all the API Questions though I am getting the right output. Thank You.

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/b/6b27da63d6feaeca3359d5e64cccad6f3eed547c.png)

**Image Description:** Here's a detailed description of the image:

**Overall:**

The image presents text on a dark, likely black, background. The text appears to be from a JSON (JavaScript Object Notation) formatted data structure.

**Text Content:**

The key-value pair is:

*   `"detail": "Method Not Allowed"}`

**Details:**

*   The text is in a white or light-colored font.
*   The phrase "Method Not Allowed" indicates an error message commonly associated with HTTP requests, suggesting a problem with how the request was made to a server. The method used in the HTTP request is not permitted for the requested resource.

**Context:**

The appearance and format suggest it is the result of an application using a programming language (like Python with Django or Flask for example), and is likely an error or response message.

![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/9/595ffb3b3b3d8766dc77c15ad2270b03892ae0d2_2_690x12.png)

**Image Description:** The image displays text against a black background. The primary content is in the form of a quote or statement. The visible text reads: "The product update addresses reported bugs and introduces several enhancements. The Leadership team has approved the expansion of our global IT support network." This text appears to be a professional or technical communication, likely an announcement or report.

---

## Post #113 by Sudhishnarayan (Post ID: 590905)
And for Question-9, I tried 80 prompts and I tried every different way, but I am not getting a Yess from the LLM. Can you please say how to proceed for that? Thank You

---

## Post #114 by Jayeshbansal (Post ID: 590914)
import numpy as np

def most_similar(embeddings):

words = list(embeddings.keys())

dot_product_df = 

for i in words:

for j in words:

dot_product_df.append(np.dot(embeddings[i], embeddings[j]))

return max(dot_product_df)

print(most_similar({“I experienced issues during checkout.”:[-0.10228022187948227,-0.057035524398088455,-0.03200617432594299,-0.1569785177707672,-0.11162916570901871,-0.017878107726573944,-0.06209372356534004,0.18209508061408997,-0.0027645661029964685,0.12928052246570587,0.17609500885009766,-0.11846645176410675,-0.2356770783662796,0.05536108836531639,-0.07102405279874802,0.21265356242656708,-0.03218059614300728,0.2578633725643158,-0.11707108467817307,0.23163051903247833,0.1780485212802887,0.17972294986248016,0.05302385240793228,0.06889612227678299,-0.13932715356349945,-0.14428070187568665,0.17149029672145844,-0.25590986013412476,0.22311879694461823,-0.06321001797914505,0.019430451095104218,-0.1841881275177002,0.14204810559749603,-0.09976856410503387,-0.17888574302196503,0.07890786230564117,-0.008947774767875671,0.08065207302570343,0.3131197988986969,-0.009226848371326923,-0.1460946649312973,0.16423441469669342,0.024331670254468918,0.055779699236154556,-0.08274511992931366,0.2355375438928604,0.06582632660865784,-0.13674572110176086,-0.003309630323201418,0.008324221707880497],“The return process was easy and hassle-free.”:[-0.13446587324142456,0.02539028227329254,-0.17796370387077332,-0.011354454793035984,-0.04654333367943764,0.15717478096485138,0.07627015560865402,0.22960494458675385,0.001469996408559382,0.1792878359556198,0.05905640497803688,-0.17240233719348907,-0.10083285719156265,-0.08322186022996902,0.00746894720941782,-0.013042726553976536,-0.13718034327030182,0.02444683574140072,-0.07938187569379807,0.04598057642579079,0.0351557731628418,0.1953098624944687,0.011594453826546669,-0.13267828524112701,-0.13718034327030182,-0.14909756183624268,-0.1765071451663971,-0.16776786744594574,-0.11473626643419266,-0.1473761796951294,0.15889616310596466,-0.12354176491498947,0.18882159888744354,-0.040121279656887054,0.18749746680259705,0.16869474947452545,-0.0547860711812973,0.13943137228488922,0.08275841921567917,-0.012976519763469696,0.026582002639770508,0.2568821310997009,0.13314174115657806,-0.08845219761133194,0.025257868692278862,0.35831084847450256,-0.22483806312084198,-0.005697916727513075,0.2899854779243469,0.1855112612247467],“Fast shipping and great service.”:[-0.1079404279589653,0.020684150978922844,-0.30074435472488403,0.11729881167411804,0.13952496647834778,-0.018052106723189354,-0.21843314170837402,0.13527116179466248,-0.09257353842258453,-0.09384968131780624,0.11293865740299225,-0.03900212049484253,-0.059287477284669876,-0.1008152961730957,-0.019155437126755714,-0.007078605704009533,-0.02967032417654991,0.03711449354887009,-0.18302017450332642,0.20056714117527008,0.09076566994190216,0.02584189549088478,0.0943814069032669,-0.03799184039235115,-0.25246360898017883,-0.1235731765627861,0.028952494263648987,-0.309251993894577,0.021375395357608795,-0.22204887866973877,0.2159872055053711,-0.11921302229166031,0.21928390860557556,-0.11432114243507385,0.017453914508223534,0.10065577924251556,-0.04200637340545654,0.17493793368339539,0.1322934925556183,0.17025874555110931,-0.15271177887916565,0.004682514350861311,0.2531017065048218,0.11580997705459595,0.014688937924802303,-0.11176885664463043,-0.292662113904953,-0.0397731214761734,0.13729171454906464,0.027570005506277084],“The payment process was secure and efficient.”:[-0.04701301082968712,-0.20167900621891022,-0.22099372744560242,-0.05536692962050438,0.03149012476205826,0.049234796315431595,-0.02104772813618183,0.1948062777519226,0.004417652729898691,-0.11180031299591064,0.25831976532936096,-0.1503705382347107,-0.14669717848300934,-0.15866521000862122,0.07601473480463028,-0.03744451329112053,-0.1256050169467926,-0.004232503939419985,-0.19717617332935333,-0.07204513996839523,0.07216363400220871,0.23426520824432373,0.005728506948798895,-0.08347994089126587,-0.09248558431863785,-0.16150909662246704,-0.10895642638206482,-0.3507460951805115,-0.1641159951686859,-0.1695667803287506,0.21696490049362183,-0.1385210007429123,0.196346715092659,-0.025669043883681297,-0.07808840274810791,-0.0023291732650250196,-0.03386003151535988,0.14717115461826324,0.06078808754682541,-0.0358448289334774,-0.1290413737297058,0.17335861921310425,-0.08033981174230576,0.1285673975944519,-0.040229152888059616,0.11511818319559097,0.10747523605823517,-0.3336827754974365,0.09313730895519257,-0.002255113562569022],“Customer service resolved my issue quickly.”:[-0.27243417501449585,-0.08034132421016693,-0.3335980772972107,0.03278002515435219,-0.0688093826174736,-0.11652996391057968,-0.13710907101631165,0.2432539016008377,0.07779283076524734,0.0949951708316803,0.1365993618965149,-0.05979407951235771,-0.17151375114917755,-0.040170662105083466,0.12054384499788284,0.10894818603992462,-0.1374913454055786,-0.008736561983823776,-0.2501348555088043,0.040648505091667175,0.20974119007587433,0.021232154220342636,0.1484498679637909,-0.07186757773160934,-0.26733720302581787,0.24248935282230377,-0.04475795477628708,-0.1304829716682434,-0.11914216727018356,-0.2516639530658722,0.16577963531017303,-0.1684555560350418,-0.08875136077404022,-0.1995472013950348,-0.10072928667068481,0.1209898293018341,0.11015872657299042,-0.053359128534793854,0.16705389320850372,0.0013867400120943785,-0.018269527703523636,0.014486604370176792,0.08320838212966919,0.06033563241362572,-0.07224985212087631,0.09869049489498138,-0.021837422624230385,0.1448819786310196,0.10996758937835693,0.058328691869974136]}))

---

## Post #115 by Jayeshbansal (Post ID: 590915)
Jayeshbansal:




print(most_similar({“I experienced issues during checkout.”:[-0.10228022187948227,-0.057035524398088455,-0.03200617432594299,-0.1569785177707672,-0.11162916570901871,-0.017878107726573944,-0.06209372356534004,0.18209508061408997,-0.0027645661029964685,0.12928052246570587,0.17609500885009766,-0.11846645176410675,-0.2356770783662796,0.05536108836531639,-0.07102405279874802,0.21265356242656708,-0.03218059614300728,0.2578633725643158,-0.11707108467817307,0.23163051903247833,0.1780485212802887,0.17972294986248016,0.05302385240793228,0.06889612227678299,-0.13932715356349945,-0.14428070187568665,0.17149029672145844,-0.25590986013412476,0.22311879694461823,-0.06321001797914505,0.019430451095104218,-0.1841881275177002,0.14204810559749603,-0.09976856410503387,-0.17888574302196503,0.07890786230564117,-0.008947774767875671,0.08065207302570343,0.3131197988986969,-0.009226848371326923,-0.1460946649312973,0.16423441469669342,0.024331670254468918,0.055779699236154556,-0.08274511992931366,0.2355375438928604,0.06582632660865784,-0.13674572110176086,-0.003309630323201418,0.008324221707880497],“The return process was easy and hassle-free.”:[-0.13446587324142456,0.02539028227329254,-0.17796370387077332,-0.011354454793035984,-0.04654333367943764,0.15717478096485138,0.07627015560865402,0.22960494458675385,0.001469996408559382,0.1792878359556198,0.05905640497803688,-0.17240233719348907,-0.10083285719156265,-0.08322186022996902,0.00746894720941782,-0.013042726553976536,-0.13718034327030182,0.02444683574140072,-0.07938187569379807,0.04598057642579079,0.0351557731628418,0.1953098624944687,0.011594453826546669,-0.13267828524112701,-0.13718034327030182,-0.14909756183624268,-0.1765071451663971,-0.16776786744594574,-0.11473626643419266,-0.1473761796951294,0.15889616310596466,-0.12354176491498947,0.18882159888744354,-0.040121279656887054,0.18749746680259705,0.16869474947452545,-0.0547860711812973,0.13943137228488922,0.08275841921567917,-0.012976519763469696,0.026582002639770508,0.2568821310997009,0.13314174115657806,-0.08845219761133194,0.025257868692278862,0.35831084847450256,-0.22483806312084198,-0.005697916727513075,0.2899854779243469,0.1855112612247467],“Fast shipping and great service.”:[-0.1079404279589653,0.020684150978922844,-0.30074435472488403,0.11729881167411804,0.13952496647834778,-0.018052106723189354,-0.21843314170837402,0.13527116179466248,-0.09257353842258453,-0.09384968131780624,0.11293865740299225,-0.03900212049484253,-0.059287477284669876,-0.1008152961730957,-0.019155437126755714,-0.007078605704009533,-0.02967032417654991,0.03711449354887009,-0.18302017450332642,0.20056714117527008,0.09076566994190216,0.02584189549088478,0.0943814069032669,-0.03799184039235115,-0.25246360898017883,-0.1235731765627861,0.028952494263648987,-0.309251993894577,0.021375395357608795,-0.22204887866973877,0.2159872055053711,-0.11921302229166031,0.21928390860557556,-0.11432114243507385,0.017453914508223534,0.10065577924251556,-0.04200637340545654,0.17493793368339539,0.1322934925556183,0.17025874555110931,-0.15271177887916565,0.004682514350861311,0.2531017065048218,0.11580997705459595,0.014688937924802303,-0.11176885664463043,-0.292662113904953,-0.0397731214761734,0.13729171454906464,0.027570005506277084],“The payment process was secure and efficient.”:[-0.04701301082968712,-0.20167900621891022,-0.22099372744560242,-0.05536692962050438,0.03149012476205826,0.049234796315431595,-0.02104772813618183,0.1948062777519226,0.004417652729898691,-0.11180031299591064,0.25831976532936096,-0.1503705382347107,-0.14669717848300934,-0.15866521000862122,0.07601473480463028,-0.03744451329112053,-0.1256050169467926,-0.004232503939419985,-0.19717617332935333,-0.07204513996839523,0.07216363400220871,0.23426520824432373,0.005728506948798895,-0.08347994089126587,-0.09248558431863785,-0.16150909662246704,-0.10895642638206482,-0.3507460951805115,-0.1641159951686859,-0.1695667803287506,0.21696490049362183,-0.1385210007429123,0.196346715092659,-0.025669043883681297,-0.07808840274810791,-0.0023291732650250196,-0.03386003151535988,0.14717115461826324,0.06078808754682541,-0.0358448289334774,-0.1290413737297058,0.17335861921310425,-0.08033981174230576,0.1285673975944519,-0.040229152888059616,0.11511818319559097,0.10747523605823517,-0.3336827754974365,0.09313730895519257,-0.002255113562569022],“Customer service resolved my issue quickly.”:[-0.27243417501449585,-0.08034132421016693,-0.3335980772972107,0.03278002515435219,-0.0688093826174736,-0.11652996391057968,-0.13710907101631165,0.2432539016008377,0.07779283076524734,0.0949951708316803,0.1365993618965149,-0.05979407951235771,-0.17151375114917755,-0.040170662105083466,0.12054384499788284,0.10894818603992462,-0.1374913454055786,-0.008736561983823776,-0.2501348555088043,0.040648505091667175,0.20974119007587433,0.021232154220342636,0.1484498679637909,-0.07186757773160934,-0.26733720302581787,0.24248935282230377,-0.04475795477628708,-0.1304829716682434,-0.11914216727018356,-0.2516639530658722,0.16577963531017303,-0.1684555560350418,-0.08875136077404022,-0.1995472013950348,-0.10072928667068481,0.1209898293018341,0.11015872657299042,-0.053359128534793854,0.16705389320850372,0.0013867400120943785,-0.018269527703523636,0.014486604370176792,0.08320838212966919,0.06033563241362572,-0.07224985212087631,0.09869049489498138,-0.021837422624230385,0.1448819786310196,0.10996758937835693,0.058328691869974136]}))






image
1677×303 30.6 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/d/3dbd98abc92c7dcf888d90678c083e2459abe37c_2_690x124.png)

**Image Description:** Here's a detailed description of the image:

**Overall Structure:**

*   The image appears to show a code editor or interactive coding environment. It displays Python code and associated output or error messages.

**Code Snippet:**

*   The primary focus is on the Python code written in a dark-themed editor.
*   The code seems to be calculating some kind of similarity score or correlation. It utilizes functions like `dot_product_df.append()`, `np.dot()`, and `max()`.
*   There's a `print` statement that likely attempts to display a result related to a sentence ("I experienced issues during checkout."). It prints a list of numeric values, likely representing a vector of some kind.

**Error Message:**

*   Below the code, there's a red error message: "TypeError: Z.runPython(...).tols is not a function". This signifies that the code encountered an error during execution. The error indicates that a function called `tols` within a module or object named `Z.runPython` could not be found or is not callable.

**Additional Features:**

*   The top left of the image says "Write your Python code here:", providing context of the environment used for code execution.

**In summary:** The image showcases a snippet of Python code that has encountered a type error. The code aims to calculate similarity scores or correlations for sentences or vectors related to "I experienced issues during checkout."

---

## Post #116 by Jayeshbansal (Post ID: 590918)
image
1592×233 19.9 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/d/cd9ba7ee8cea080fb87dd3c9df7d8cee4c74be42_2_690x100.png)

**Image Description:** The image is a screenshot that seems to be related to API testing or documentation.  Here's a breakdown:

**Text Content:**

*   **Question and Example:**  The image begins with a question about the API URL endpoint. It provides an example: `http://127.0.0.1:8000/execute`. This suggests the user is being instructed on what their API endpoint might look like.
*   **User Input Field (with error):** Below the example, there is a field `http://127.0.0.1:8000/execute?q=` presumably where the user can enter their actual API endpoint. An error message `TypeError: Failed to fetch` is present and the input field has a red border.
*   **Explanation of testing:** The rest of the text explains how the system will check the user's implementation. It mentions sending a `GET` request to the URL containing a task with the `?q=` parameter. It also specifies that the system will verify the response matches the expected response and that arguments must be in the same order as the function definition.

**Objects/Features:**

*   **Input field with Red Border:**  The input field is outlined in red and shows an error symbol. This is a visual cue for the user that there is an issue with the entered URL or that the system could not fetch data with the URL.
*   **Error message:** The `TypeError: Failed to fetch` message suggests a problem connecting to the specified URL, likely preventing the API from running and retrieving data.
*   **Color scheme:** The use of pink/red for highlights (e.g., example URL, border of the input field) and errors provides a clear visual focus on important information.

**Overall:** The image is part of a system that allows the user to implement and test an API. It guides the user on how to submit the API URL, likely by providing an example, and then explains how the system will validate the response. The error message signifies that the submitted API is not working correctly.

---

## Post #117 by 23f3002537 (Post ID: 590921)
image
1915×999 143 KB


@carlton
 
@Jivraj
  Sir please look at the err on Q7.I am able to run on my system and getting the desired json but its not working in the portal. Today is the deadline sir please help me out!


I m attaching my codes:


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["OPTION","POST"],  
    allow_headers=["*"],
)

class SimilarityRequest(BaseModel):
    docs: List[str]
    query: str

def clean_text(text: str):
    """Clean text by lowering case, removing punctuation, and extra spaces."""
    text = text.lower()  
    text = re.sub(r'\s+', ' ', text)  
    text = re.sub(r'[^\w\s]', '', text)  
    return text

@app.post("/similarity")
async def find_similar_docs(request: SimilarityRequest):
    try:
        cleaned_docs = [clean_text(doc) for doc in request.docs]
        cleaned_query = clean_text(request.query)

        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(cleaned_docs + [cleaned_query])

        query_vector = tfidf_matrix[-1]
        doc_vectors = tfidf_matrix[:-1]
        similarity_scores = cosine_similarity(query_vector, doc_vectors)[0]

        top_indices = sorted(range(len(similarity_scores)), key=lambda i: similarity_scores[i], reverse=True)[:3]
        matched_docs = [request.docs[i] for i in top_indices]

        return {"matches": matched_docs}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/execute")
async def execute_query(q: str):
    return {"message": f"Executing query: {q}"}

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/d/0d8958b26bfa0caf26974962661f2c6345027f02_2_690x359.png)

**Image Description:** The image shows a computer screen with multiple windows open, seemingly related to a coding or development task. Here's a breakdown:

**Left Side (Main Window):**

*   **Web Browser Window:** This seems to be a web browser window displaying a coding assignment or exercise.
    *   The URL bar indicates the website "exam.sanand.workers.dev".
    *   There's a timer on the top left.
    *   The content involves a text-based instruction or problem description.
    *   The text is explaining a similarity matching problem where the goal is to find matches based on a given query.
    *   It describes that the correct matches should be "Contents of document 3", followed by "Contents of document 1", and then "Contents of document 2".
    *   There is a mention of "CORS" (Cross-Origin Resource Sharing) and the need to enable OPTIONS and POST methods.
    *   The API endpoint is given as `http://127.0.0.1:8000/similarity`.
    *   An error message appears below the URL, indicating that the matches are incorrect.
    *   There is a "Check" button.
    *   There are two sections at the bottom, one titled "Function Calling (1.5 marks)".

**Right Side (Other Windows):**

*   **API Testing Tool Window (likely Postman or a similar tool):** This window is for testing API requests.
    *   The top bar has a "New Request" button.
    *   There is a "POST" request selected and the URL is set to `http://127.0.0.1:8000/similarity`.
    *   The "Body" tab is selected, and the request body is in JSON format. The JSON contains:
        *   `"docs"`: An array of documents.
        *   `"query"`: A query string "Your query string".
    *   The response area displays a status code "200 OK" and the response body, which contains the matches, which seem to have the same order as defined in the assignment.
*   **Terminal Window:** This window seems to be running a Python application, likely the backend server for the API.
    *   The output shows information about the server startup, including the host (127.0.0.1) and port (8000).
    *   The terminal logs the HTTP requests made to the `/similarity` endpoint and the corresponding status codes (200 OK).

**Overall Context:**

The image shows a developer working on a coding exercise, likely related to finding similar documents using an API. They are using a web browser to view the instructions and an API testing tool to send requests to the backend server, which is running in the terminal. The developer is trying to solve a task to match documents with a specific order of similarity. They are receiving an "incorrect matches" error.

---

## Post #118 by 23f2005419 (Post ID: 590922)
Hi,


I’m sorry if I’m asking an unrelated question, But I’m very confused with the concept of generating the token from 
https://platform.openai.com/api-keys


Could any one suggest the step by step process? I couldn’t able to find that similar question asked by anyone since the conversations are vast.


Please guide me on this. Also do i need to use my personal mail id or iitm mail id for accessing this token

---

## Post #119 by 23f3002537 (Post ID: 590926)
yes you have to use your IITM email id . Use this link and login you will get your token:


https://aiproxy.sanand.workers.dev/

---

## Post #120 by Jayeshbansal (Post ID: 590940)
image
1572×133 10.7 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/7/678a64a541708b68c7166ffebef4fe986ff89e18_2_690x58.png)

**Image Description:** Here's a breakdown of the image:

**Overall Structure:**

*   The image appears to be a screenshot or a visual element related to software development, specifically dealing with API (Application Programming Interface) usage or troubleshooting.
*   It presents a question related to an API URL endpoint.
*   The design uses a clean and modern style, with a light background and red accents for highlighting.

**Text and Content:**

*   **Question/Instruction:** "What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/execute" This line poses a question and gives an example of what the URL might look like. This suggests it's guiding a user to set up an API connection.
*   **Input Field:** There's an input field, highlighted in red, suggesting an input area to enter the specific API endpoint. The field currently displays "http://127.0.0.1:9000/execute". This indicates a potential API endpoint. The red outline could signify an error or warning.
*   **Error Message:**  "SyntaxError: \[object Object] is not valid JSON." This message indicates a problem with the format of the data being sent to or from the API. It specifically points out that the data isn't properly formatted as JSON (JavaScript Object Notation), which is a common data format for APIs. The presence of an error message strengthens the image's troubleshooting or debugging aspect.
*   **Warning icon:** A circled 'i' indicates that there might be a warning associated with the entered URL.

**Objects and Features:**

*   **URL Structure:** The example and entered URL "http://127.0.0.1:9000/execute" have the basic structure:
    *   `http://` (Protocol)
    *   `127.0.0.1` (IP address - localhost, meaning the same computer the program is running on)
    *   `:9000` (Port Number)
    *   `/execute` (API endpoint path).
*   **Visual Cues:** The use of red is consistent throughout (text and the input field). Red often signifies errors or warnings in user interfaces.

**Possible Interpretations and Usage:**

*   **Tutorial/Documentation:** The image could be part of a tutorial or documentation guiding users on how to use an API, probably to set up a connection.
*   **Development Environment:** It could be part of an application development environment that's highlighting issues with the data being sent.
*   **Troubleshooting Guide:** It could also be a guide to resolving JSON formatting errors when working with APIs.

In summary, the image illustrates a common issue in API usage: incorrect data format. The visual layout provides clear guidance to the user and gives them an example of what an API endpoint looks like.

---

## Post #121 by Aditya_Sahu (Post ID: 590970)
The error shows your code is getting wrong answers for the test cases. I looked into your code and noticed that you are using sklearn (I think which is not required in this case). Just get embedding vector for each document content and query by passing a valid POST request to 
http://aiproxy.sanand.workers.dev/openai/v1/embeddings
 with required headers. And, then calculate 
similarity_scores
 simply using


\cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{|\mathbf{A}| |\mathbf{B}|}

which in python syntax is-


np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

---

## Post #122 by Sudhishnarayan (Post ID: 590974)
Sir, Regarding the embedding questions, I had posted earlier. Now, I am writing the error I faced. I tried to use the OpenAI API, but I am getting the error as “The Maximum Quota has reached”. I tried using 5 new API Keys from OpenAI, from 5 different accounts. So, I had to use SentenceTransformers, Alibaba gte model. So, as the model has changed, I think so it is expecting answer as got from OpenAI Model, but as I used Alibaba gte model, I am getting different result. Can you please explain how to solve this issue? This will be helpful in my future codes. I could do chat requests but it is not giving output for Embedding requests, I tried it multiple times with multiple different keys.Thank You

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/0/b05d3520e550b5174ba2b43efc5b7ae8e729d551_2_690x22.png)

**Image Description:** The image displays a text string on a black background. The text appears to be an error message, likely from a computer program or service. It is formatted as a JSON object starting with the key "error" which has a nested object with the key "message". The value of the message states "You exceeded your current quota, please check your plan and billing details." This suggests that the user has surpassed the limits of their service plan, and should review their account information.

---

## Post #123 by Sudhishnarayan (Post ID: 590975)
This is my code for the 7th question of finding similarities. This code, I tried on my own, but it is showing Incorrect Matches. I think so it is due to the Aliababa GTE Model. Please correct me if I have gone wrong anywhere. Thank You


from fastapi import FastAPI, Query
import httpx
from typing import List
import numpy as np
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer('Alibaba-NLP/gte-large-en-v1.5', trust_remote_code=True)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["OPTIONS", "POST"],  # Allows all methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allows all headers
)

class similarity1(BaseModel):
    docs: list[str]
    query: str
@app.post("/similarity")
async def similarity(similarity1: similarity1):
    docs = similarity1.docs
    query = similarity1.query
    results_docs = model.encode(docs)
    results_query = model.encode(query)
    similarities = {}
    output = []
    for i in range(len(results_docs)):
        c = np.dot(results_docs[i], results_query) / (np.linalg.norm(results_docs[i])*np.linalg.norm(results_query))
        similarities[c] = docs[i]
    k = sorted(list(similarities.keys()))
    for i in k[::-1][:3]:
        output.append(similarities[i])
    return {"matches" : output}
if __name__ == "__main__":
  (uvicorn.run(app))

---

## Post #124 by Pururaj (Post ID: 590987)
image
925×544 25.9 KB

i submitted the assignment on time but i am still getting assignment not submitted. And it also show zero marks. Same thing happened with graded assignment 2. 
@Jivraj

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/7/c75896b45fe46fb02364923a34daf877f1fa8296_2_690x405.png)

**Image Description:** Here's a detailed description of the image:

**Overall Layout:**

The image appears to be a screenshot of a web page or a learning platform. It has a clear header, some interactive sections, and a listing of saved sessions. The design uses a dark color scheme with contrasting text and elements.

**Header:**

*   A red horizontal bar at the top indicates the end of an activity.
*   **Text:** "Ended at Wed, 5 Feb, 2025, 11:59 pm IST" (showing the date and time of the end of an activity, in IST)
*   **Text:** "Score: 0"
*   **Buttons:** "Check all" and "Save".

**Middle Section:**

*   **Box:** A teal box contains the text "Have questions? Join the discussion on Discourse"
*   **Login Status:** "You are logged in as 24f2005437@ds.study.iitm.ac.in." (showing the user's email)
*   **Button:** "Logout" button.

**Bottom Section:**

*   **Title:** "Recent saves"
*   **List Items:** There are two "recent saves" entries:
    *   "Loaded" from 5/2/2025, 11:20:33 pm. Score: 6
    *   "Reload" from 5/2/2025, 11:20:20 pm. Score: 6

**Key Features and Context:**

*   **Learning Environment:** The overall design suggests a platform for education, perhaps for online quizzes or practice problems.
*   **Time-Based Activity:** The header "Ended at..." suggests a time limit for the activity.
*   **Score Tracking:** The "Score: 0" indicates that the user hasn't scored anything yet.
*   **User Management:** The login display and "Logout" button indicate user authentication.
*   **Recent Activity:** The "Recent saves" section tracks the user's progress.
*   **Discussion and Support:** The "Have questions? Join the discussion on Discourse" suggests a method of support.

**Possible Use Case:**

This screenshot likely shows the results page of an online quiz or assignment in a learning platform. It provides information about the time of the activity, score, login status, and recent saves. It also provides links to the forum for questions.

---

## Post #125 by roy2003 (Post ID: 591016)
@Jivraj
 
@carlton

I have submitted ga3 still showing not submitted , why sir?


Untitled design
1414×2000 314 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/8/b88fa681fcbf676c93202b79b2bcb23d71df28a4_2_353x500.png)

**Image Description:** Here's a detailed description of the image:

**Overall Impression:**

The image appears to be a screenshot of an online learning platform or assessment tool, likely related to a course on "Large Language Models." It shows a user interface for an assignment.

**Header Information:**

*   "TDS 2025 Jan GA3 - Large Language Models" is the title. This suggests the course and assignment are associated with the year 2025.
*   The image indicates the user's session would have "Ended Wed, Feb 5, 2025, 11:59 PM IST."
*   There are buttons at the top-right, "Check all" and "Save".

**Instructions Section:**

*   The "Instructions" section gives guidance on how to approach the assignment. It mentions topics like checking answers, saving regularly, dealing with browser issues, and what resources are permissible (like Internet, ChatGPT, libraries, and frameworks).
*   There is a section regarding questions and a link to join a discussion on Discord.

**User Details:**

*   It shows the user logged in under a particular ID associated with study.iitm.ac.in.

**Assignment Details (Module 3: Large Language Models):**

*   The image focuses on "Module 3: Large Language Models".
*   It highlights "Graded Assignment 3," which is "Not Submitted."
*   The assessment is due on "5 Feb 2025."
*   There are columns for "Your Score," "Peer Average," and "Median Score," but all values are currently indicated by a dash (-).

**Overall context:**
This image captures the main interface of an assignment in a course on "Large Language Models." It provides guidelines for the user. The assignment hasn't been submitted yet.

---

## Post #126 by roy2003 (Post ID: 591017)
@Jivraj
 
@carlton

please reply why its showing not submitted in ga3 but i have submitted that


Untitled design
1414×2000 314 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/8/b88fa681fcbf676c93202b79b2bcb23d71df28a4_2_353x500.png)

**Image Description:** Here's a detailed description of the image:

**Overall Structure:**

*   The image appears to be a screenshot of a webpage, possibly related to an online course or assignment.

**Header Information:**

*   The top bar indicates that the current date is Wednesday, Feb 5, 2025, at 11:59 IST.
*   There are buttons labeled "Score," "Check All," and "Save" in the header, suggesting this is a test or assignment.

**Main Content:**

*   **Title:** The page is titled "TDS 2025 Jan GA3 - Large Language Models." This suggests the assignment is about Large Language Models and is part of a course or program called "TDS 2025 Jan."
*   **Instructions:** There is a section containing instructions for the assignment. These instructions include:
    *   Reading the provided material.
    *   Checking answers regularly.
    *   Saving regularly.
    *   Advice regarding browser issues, and "hacking the code."
    *   A note about running multiple servers.
*   **Module Information:** The text "Module 3: Large Language Models" is visible, confirming the topic of the assignment.
*   **Assignment Details:**
    *   It is labeled "Graded Assignment 3."
    *   The "Assessment (Due: 5 Feb 2025)"
    *   The assignment status is "Not Submitted".
*   **Score Summary:** There are columns labeled "Your Score," "Peer Average," and "Median Score," with dashes displayed as the values, indicating no score has been recorded yet.

**Other Features:**

*   There is an option to join a discussion on Discord.
*   The bottom-left says "Recent saves" with details.

**In summary,** the image shows a page within an online learning platform, likely for an assignment on Large Language Models. It highlights the assignment details, instructions, and the lack of any scores as the assignment hasn't been submitted.

---

## Post #127 by 23ds1000022 (Post ID: 591060)
@carlton
, 
@Jivraj

Both the api based questions i am unable to get the output it always says bad request


Screenshot 2025-01-30 at 3.55.56 PM
1920×1200 219 KB


Screenshot 2025-01-30 at 3.57.17 PM
2048×1280 284 KB

all other questions i have finished. even in Ga2 all these api and flask creates a lot of issues. if there is any complete guide to understand this also pls help us.

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/2/a2d87d7048eea2c5fb6527a5809ac1933296831b_2_690x431.jpeg)

**Image Description:** Here's a detailed description of the image:

**Overall Layout:**

*   The image is a screenshot of a code editor, likely Visual Studio Code, based on the layout and icons. The editor is focused on a Python file.
*   The layout includes the explorer on the left, the code editor in the center, and a terminal window at the bottom. There are several tabs at the top of the editor.

**Explorer Panel (Left Side):**

*   This panel shows the project structure.
*   It has a folder named "GA3\_Q8" (likely the project name).
*   Inside GA3\_Q8:
    *   "app" folder
    *   "\_\_pycache\_\_" folder.
    *   "\_\_init\_\_.py" file.
    *   "main.py" file (currently open in the editor).
    *   "venv" folder (likely a virtual environment).
    *   ".env" file.
    *   "requirements.txt" file.

**Code Editor (Center):**

*   **File:** "main.py" is open. The tab at the top of the editor shows "main.py" and the path "app > main.py > parse\_query".
*   **Code Content:** The Python code appears to be parsing user queries, specifically looking for phrases to extract information. Some key sections of code include:
    *   `parse_query(query: str)` function: This function seems to be the main entry point for processing user queries. It currently handles the "get\_ticket\_status" query.
    *   Regular Expression Matching: The code uses the `re.match()` function with regular expressions to try to match various query formats.
        *   Matching "Arrange meeting 2025-12-17, 06:09, room: Conf1" - Regular expression to find a meeting.
        *   Matching "Show my expense balance for employee <employee\_id>" - Another regular expression.
    *   Conditional Statements: There are `if` statements that check if the regular expressions matched and print debugging information.
    *   Data Extraction: The code extracts data from the matched patterns (e.g., date, time, meeting room) using `match_schedule_meeting.group()`.
*   **Line Numbers:** Line numbers are visible, ranging up to at least line 72.

**Terminal Panel (Bottom):**

*   **Tabs:** It shows tabs labeled "PROBLEMS", "OUTPUT", "DEBUG CONSOLE", "TERMINAL", and "PORTS".
*   **Selected Tab:** "TERMINAL" is selected.
*   **Output:** The terminal output displays log messages and errors:
    *   "Query format did not match any predefined patterns."
    *   "INFO: 127.0.0.1:60464" messages related to HTTP requests, indicating that a web server is likely running in the background.
    *   "400 Bad Request" and "404 Not Found" HTTP status codes.
    *   "Parsing query: Arrange meeting 2025-12-17, 06:09, room: Conf1" suggesting it is attempting to process a query.
*   **Shells:** The bottom right shows "zsh" then "Python" icons.

**Overall Impression:**

The screenshot shows a developer working on a Python project, probably building a simple natural language processing system. The system takes user input queries, tries to understand their intent, and extract relevant data. The developer is in the process of debugging because of the error messages in the terminal, likely related to incorrect query formats. The code includes regex patterns and parsing logic to extract information from user queries.

![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/5/a5199d9f6c6e3733ee20568d5c787a40cad041f8_2_690x431.png)

**Image Description:** The image shows a web page, likely a coding or assessment interface. Here's a breakdown:

**Overall Layout:**

*   The page has a dark theme.
*   There's a navigation bar at the top.
*   A green bar indicates the title of the assessment and the current score.
*   The main content area displays instructions and a field for entering an API endpoint.

**Key Elements:**

*   **Header:** Contains the website address: `exam.sanand.workers.dev/tds-2025-01-ga3#hq-function-calling` and displays the date and time: `Due Sun, 2 Feb, 2025, 11:59 pm IST`, the score is `6.5 / 9.5`. Buttons for "Check" and "Save" are present.
*   **Code Snippet:** A JSON object appears to define a function call:
    ```json
    {
      "name": "get_ticket_status",
      "arguments": "{\"ticket_id\": 83742}"
    }
    ```
*   **Instructions:** The page instructs to enable CORS for GET requests.
*   **API Endpoint Prompt:** The user is prompted to enter the API URL endpoint for their implementation and provides an example: `http://127.0.0.1:8000/execute`.
*   **User Input:** An input field is provided where the user has entered `http://127.0.0.1:8000/execute`. An error message appears below this input field: `Error: Failed to fetch: Bad Request`.
*   **Additional Instructions:**  The page explains how the system will check the entered endpoint, which involves a GET request with a specific query parameter.
*   **Task:** The last item, "9 Get an LLM to say Yes (1 mark)," suggests this page is part of a coding assignment or test that involves interacting with a Large Language Model (LLM).

**In Summary:**

This web page is likely part of a coding assignment or test. The task involves implementing an API endpoint that the user must define and provide in the input field. The provided instructions involve interacting with an LLM. The existing code defines a function call for getting a ticket status. The error suggests that the provided endpoint is not functioning.

---

## Post #128 by Jivraj (Post ID: 588065)
Hi 
@23ds1000022
 ,


Check network tab, there check for response of 
http://127.0.0.1:8000/api
 request.

---

## Post #129 by Sakshi6479 (Post ID: 591063)
I have counted the number of tokens in gpt-4o-mini but when I was entering the answer in portal it was showing incorrect please take a look and provide a solution for it .


Screenshot 2025-02-01 180627
2458×1183 284 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/8/a8c5d62747d23ed0d286375fa44222ddd87fba3e_2_690x332.png)

**Image Description:** Here's a breakdown of the image:

**Overall Structure:**

*   The image appears to be a screenshot of a user interface associated with the OpenAI Platform. The layout and features suggest a tool for interacting with and testing different language models.

**Key Features:**

*   **Top Bar:** The top of the image includes the "OpenAI Platform" logo and links to "Docs", "API reference", and likely a "Login" button.
*   **Model Selection Tabs:** There are tabs for selecting different language models: "GPT-4o & GPT-4o mini", "GPT-3.5 & GPT-4", and "GPT-3 (Legacy)". The first one appears to be selected, highlighted with a light background.
*   **Text Area:** A large text area in the center occupies the bulk of the screen. It contains a list of strings. Each string is underlined in red.
*   **Buttons:** The lower part of the interface contains two buttons labeled "Clear" and "Show example".
*   **Metrics:** At the bottom left corner of the screenshot, there are labels for "Tokens" and "Characters," accompanied by respective counts.

**Content Details:**

*   **Text Area Content:** The text area's content looks like a list of codes or tokens. It's very likely these are the output of a text analysis task based on the models.
*   **Underlined Words:** The red underlines suggest errors, invalid inputs, or words which do not exist in the selected model.
*   **Metrics:** The numbers next to "Tokens" (406) and "Characters" (625) indicate the size or complexity of the text currently displayed.

**Inferences:**

*   The tool allows users to enter text or code to be processed and analyzed by different AI models.
*   The interface provides a way to visualize and evaluate the model's output.
*   The tokens and character counts provide a way to assess the "cost" or processing requirements of the given content.
*   The red underlines show non-valid components of the tokens.

**Overall:** This image showcases a user interface designed for experimenting with and examining the outputs of different OpenAI language models, providing information on tokens, characters, and validity of inputs.

---

## Post #130 by Jivraj (Post ID: 588807)
There are few more tokens for the user prompt, I think if you add 7 or 8 then you would get correct answer.


Other way to do this question is send a request to anand sir’s aiproxy and in response you will get number of input tokens.

---

## Post #131 by 23f2000237 (Post ID: 588820)
I inspected the JavaScript code of this website, I saw that the answer took my input and added 7 to it, why is it programmed this way? Even if I were to use the AI proxy that was given shouldn’t the number of tokens remain unaffected?

---

## Post #132 by Jivraj (Post ID: 588839)
When you send request to openai through anand sir’s proxy it takes some tokens for user prompt.


When you use tokenizer from openai’s webpage then it doesn’t take care of that.

---

## Post #133 by 23f2001915 (Post ID: 591066)
How to answer the 3rd question in ga 3 i have to no clue (tired inspecting its html pages)

---

## Post #134 by Jivraj (Post ID: 590399)
drive.google.com








2025-02-04 03-50-48.mkv


Google Drive file.

---

## Post #135 by Sakshi6479 (Post ID: 591069)
Q3 how to generate answer box ,I am not able to do it. kindly guide me with that.


Q7 & Q8 in these questions the problem is the same my app couldn’t fetch the details from the file.


`from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import openai
from fastapi.responses import JSONResponse
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Initialize FastAPI app
app = FastAPI()

# Add CORSMiddleware with more restrictive settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow only this specific origin
    allow_credentials=True,
    allow_methods=["POST", "OPTIONS"],  # Allow only POST and OPTIONS methods
    allow_headers=["Content-Type", "Authorization"],  # Allow only specific headers
)

# OpenAI API key (use your own key)
openai.api_key = 'eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjI0ZjIwMDY3NDlAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.tMJtqZrzRqREY7E3wsFMd9PkElXEbRBpCkb533ORGEU'

# Request body model for /similarity endpoint
class SimilarityRequest(BaseModel):
    docs: List[str]
    query: str

# Function to get embeddings (using OpenAI API)
def get_embedding(text: str):
    response = openai.Embedding.create(
        model="text-embedding-ada-003",  # Use the correct model
        input=text
    )
    return response['data'][0]['embedding']

# POST /similarity endpoint
@app.post("/similarity")
async def similarity(request: SimilarityRequest):
    docs = request.docs
    query = request.query
    query_embedding = get_embedding(query)
    doc_embeddings = [get_embedding(doc) for doc in docs]
    
    # Cosine similarity
    similarities = [cosine_similarity([query_embedding], [doc_embedding])[0][0] for doc_embedding in doc_embeddings]
    ranked_docs = [docs[i] for i in np.argsort(similarities)[::-1]]
    
    return JSONResponse(content={"matches": ranked_docs[:3]})

# Optionally, handle requests to the root (GET /)
@app.get("/")
async def root():
    return {"message": "Welcome to the similarity API!"}
`



and for Q8


from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any
import re

# Create the FastAPI app
app = FastAPI()

# CORS configuration to allow any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)
def get_ticket_status(ticket_id: int) -> Dict[str, Any]:
    # Mock response for illustration purposes
    return {"ticket_id": ticket_id, "status": "open"}

def schedule_meeting(date: str, time: str, meeting_room: str) -> Dict[str, Any]:
    # Mock response for illustration purposes
    return {"date": date, "time": time, "meeting_room": meeting_room, "status": "scheduled"}

def get_expense_balance(employee_id: int) -> Dict[str, Any]:
    # Mock response for illustration purposes
    return {"employee_id": employee_id, "balance": 1000.0}

def calculate_performance_bonus(employee_id: int, current_year: int) -> Dict[str, Any]:
    # Mock response for illustration purposes
    return {"employee_id": employee_id, "current_year": current_year, "bonus": 500.0}

def report_office_issue(issue_code: int, department: str) -> Dict[str, Any]:
    # Mock response for illustration purposes
    return {"issue_code": issue_code, "department": department, "status": "reported"}
import re

def extract_parameters(query: str) -> Dict[str, Any]:
    """Extract parameters from the query string."""
    # Convert the query to lowercase for case-insensitive matching
    query = query.strip().lower()

    if match := re.match(r"what is the status of ticket (\d+)\?", query):
        return {
            "name": "get_ticket_status",
            "arguments": {"ticket_id": int(match.group(1))}
        }
    elif match := re.match(r"schedule a meeting on (\d{4}-\d{2}-\d{2}) at (\d{2}:\d{2}) in (.+)\.", query):
        return {
            "name": "schedule_meeting",
            "arguments": {
                "date": match.group(1),
                "time": match.group(2),
                "meeting_room": match.group(3)
            }
        }
    elif match := re.match(r"show my expense balance for employee (\d+)\.", query):
        return {
            "name": "get_expense_balance",
            "arguments": {"employee_id": int(match.group(1))}
        }
    elif match := re.match(r"calculate performance bonus for employee (\d+) for (\d{4})\.", query):
        return {
            "name": "calculate_performance_bonus",
            "arguments": {
                "employee_id": int(match.group(1)),
                "current_year": int(match.group(2))
            }
        }
    elif match := re.match(r"report office issue (\d+) for the (\w+) department\.", query):
        return {
            "name": "report_office_issue",
            "arguments": {
                "issue_code": int(match.group(1)),
                "department": match.group(2)
            }
        }
    return {}

@app.get("/execute")
async def execute_query(q: str):
    # Extract the function name and arguments from the query
    result = extract_parameters(q)
    
    if not result:
        return JSONResponse(content={"error": "No matching function found for the query"}, status_code=400)
    
    # Call the respective function
    func_name = result["name"]
    arguments = result["arguments"]
    
    # Call the function dynamically based on func_name
    if func_name == "get_ticket_status":
        response = get_ticket_status(**arguments)
    elif func_name == "schedule_meeting":
        response = schedule_meeting(**arguments)
    elif func_name == "get_expense_balance":
        response = get_expense_balance(**arguments)
    elif func_name == "calculate_performance_bonus":
        response = calculate_performance_bonus(**arguments)
    elif func_name == "report_office_issue":
        response = report_office_issue(**arguments)
    
    # Return the response in the requested format
    return JSONResponse(content={"name": func_name, "arguments": arguments}, status_code=200)



Please kindly guide me with these problems as I am trying to do it since last 3 days. I am exhaust now, Please help me with this. 
@Jivraj
 , 
@carlton
 , 
@Saransh_Saini

---

## Post #136 by Jivraj (Post ID: 590401)
Hi Sakshi








 Sakshi6479:




Q3 how to generate answer box ,I am not able to do it. kindly guide me with that.










drive.google.com








2025-02-04 03-50-48.mkv


Google Drive file.














For question 7








 Sakshi6479:




import openai







You won’t be able to send request through openai python module, here is one example how you would make a request


headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {OPENAI_API_KEY}'
}

json_data = {
    'model':'gpt-4o-mini',
    'messages':[
        {
            'role':'user',
            'content':'What is 2+2?'
        }
    ]
}
r = httpx.post('http://aiproxy.sanand.workers.dev/openai/v1/chat/completions', headers = headers, json = json_data, timeout=10.0)



You would need to use professor Anand’s proxy or some other api key through which request can be made.

Url’s for free api keys:




AI Proxy


OpenAI GPT-4o · GitHub Models




The way to use api’s is demonstrated in live sessions, also refer to this documentation 
sanand0/aiproxy: Authorizing proxy for LLMs
.




For question 8, you’ll need to use OpenAI’s function calling feature and identify which function needs to be called and arguments to be used, we discussed in last Friday’s session on functions like 
order
 and 
cancel_order
.


Kind regards

---

## Post #137 by 24f2006531 (Post ID: 591072)
Hello sir,


While working on this question, I’m encountering this problem. It looks like the request is being made successfully (and I verified it by a POST request via Postman ), however while submitting my URL at the assignment portal, I’m getting an error.


image
1550×207 22.2 KB


image
1288×138 7.33 KB


I even tried deploying on a public URL using render. My guess is there is a formatting issue or it’s not sorting correctly based on the similarity score and not returning the top 3.


Would appreciate if I can get some clarity on the same


Thanks and Regards

Shalini

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/6/b6feb2e4fd01c3630f5db6ee879eb4042b7cec09.png)

**Image Description:** The image shows a series of text messages within what appears to be a command-line interface or a log. The messages describe actions performed on a database. Here's a breakdown:

*   **INFO lines:** These lines begin with "INFO:" and provide metadata, likely related to network requests. They include the IP address and port (127.0.0.1:59423), the HTTP method ("OPTIONS" or "POST"), the API endpoint ("/similarity"), the HTTP version (HTTP/1.1), and the HTTP status code (200 OK), which indicates success.

*   **Collection Reset:** "Collection reset successfully!" indicates a database operation.

*   **Collection Creation:** "Created new collection: documents" shows that a new database collection named "documents" has been created.

*   **Document Addition:** "Added 10 new documents to the database." tells us that ten documents were added to the "documents" collection.

*   **Query Processing:** "Searching for query: How is our internal training addressing cybersecurity challenges?" shows a search query being executed.

*   **Search Results:** "Found matches: ['Employee training on cybersecurity best practices is being rolled out company-wide.', 'The staff handbook has been updated to reflect current operational policies.', 'Our quality assurance team has implemented automated testing protocols.']" presents the search results as a list of strings. These seem to be sentences related to cybersecurity training.

The overall image depicts a series of database operations that start with a reset, create a new document collection, add 10 new documents to that collection, and then search within that collection for content related to the query: "How is our internal training addressing cybersecurity challenges?" The results of the search are then presented.

![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/8/b81a8c44bd77972dadbeb69bb545ea7fe6c3203b.png)

**Image Description:** The image shows a dark-themed interface that appears to be related to an API. Here's a breakdown:

*   **Headline:** "What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/similarity". This suggests the user is being instructed on how to find or use an API.
*   **Input Field:** A red-bordered input field is provided where the user's API URL is supposed to be. It contains the URL "http://127.0.0.1:8000/similarity". There is also a warning icon in the upper right corner.
*   **Error Message:** A red-colored error message is displayed below the input field stating: "Error: Got incorrect matches: Employee training on cybersecurity best practices is being rolled out company-wide., The staff handbook has been updated to reflect current operational policies., Our quality assurance team has implemented automated testing protocols." The message seems unrelated to the URL validation and may be a status update.

---

## Post #138 by sha_512_av (Post ID: 590400)
Hello, I think the format of the response body should be like: { “matches” : [ “ABC”, “ABC”, “ABC”]}. I think it is because of your formatting issue.


Screenshot_20250204_032923
991×615 43.7 KB


I had used (well gpt) the below two decorators to format:


class SearchRequest(BaseModel):
    docs: List[str]  # The list of documents to search through
    query: str       # The search query string

class SearchResponse(BaseModel):
    matches: List[str]  # The list of matched documents

.........

@app.post("/similarity", response_model=SearchResponse)


.........

return SearchResponse(matches=sorted_matches[:3])



It basically checks the Request  and Response formatting. This worked for me. Hope it helps. And thanks btw for mentioning using POSTMAN, as I had never used it before, so it clicked in my mind after reading your post only that I can basically debug using POSTMAN. Thank you for that

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/4/14b928ed4ee1d76113b90069812abf2b53ab4ef1_2_690x428.png)

**Image Description:** The image depicts a screen from a tool like Postman, used for testing APIs. Here's a breakdown of what's visible:

**Header Information:**

*   **HTTP Method:** The request is a `POST` request.
*   **URL:** The request is being sent to `http://127.0.0.1:8000/similarity`.
*   **Authorization:**  The authorization type is set to "No Auth".

**Request Details:**

*   **Body Tab:** The "Body" tab is selected, and the body of the request is displayed as JSON.
*   **JSON Structure:** The JSON body contains a field named "matches" which is an array of three strings.  The strings are:
    *   "FastAPI is great for APIs."
    *   "Embedding models improve NLP."
    *   "Machine learning is evolving."

**Response Details:**

*   **Response Status:** The response status code is "200 OK" indicating the request was successful.
*   **Response Time:** The response time was 17.26 seconds.
*   **Response Size:** The response size was 232 Bytes.

**Other Interface Elements:**

*   Tabs for Params, Authorization, Headers, Body, Scripts and Settings.
*   A "Send" button to submit the request.
*   Controls for saving the request and environment management.
*   Various icons for editing, formatting etc.

---

## Post #139 by Jivraj (Post ID: 590402)
{
  "matches": ["Contents of document 3", "Contents of document 1", "Contents of document 2"]
}



Check if your response is in this format.


kind regards

Jivraj

---

## Post #140 by Jeleshiya (Post ID: 591079)
Does the final submission get graded, or is the highest-scoring submission considered?


I’m facing an issue where my score dropped from 8 to 6.5 when I checked all the answers one last time before submitting. I suspect the drop is due to the 3rd and 7th questions.


Screenshot 2025-02-06 001446
810×296 14.8 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/0/b00269ee7b24a8f28c8ab53f4da556a11c8f3d27.png)

**Image Description:** The image is a screenshot displaying "Recent saves." It is a dark, green-themed interface.

Here's a breakdown:

*   **Title:** "Recent saves" is written in a light, teal-green color at the top.
*   **Entries:** Three entries are listed, each showing a saved game's information. Each entry includes:
    *   A "Reload" button in blue.
    *   The date: "2/5/2025".
    *   The time: "11:59:18 PM", "11:30:37 PM", "10:44:08 PM" (in the order of the entries).
    *   A score: "Score: 6.5", "Score: 8", "Score: 6.5".
*   **Interface:** The background is a dark green, and there's a darker, grey/black border at the bottom.

The image likely represents a save game system within a game or software application, letting the user reload previous save states.

---

## Post #141 by carlton (Post ID: 591077)
Screenshot 2025-02-06 at 11.27.07 am
2570×1136 358 KB


The score drops because some questions may require you to either keep a server turned on or some dynamic changes may occur for some questions (The dynamic changes are intentional in some questions, in order to get students to learn by doing. So if you solved everything and the score is the maximum… just make that your last submission. The score you see is the score you will get for your last submission).


If you want check a question without submitting. Then just use the check button instead. But your last submission is whats scored.

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/4/549b066a290c204c7468f501f107ef5eabe661f6_2_690x304.png)

**Image Description:** Here's a detailed description of the image:

**Overall Layout**

*   The image appears to be a webpage or a section of a webpage related to an exam or quiz. It features a title, instructions, and a user interface for taking the test.

**Title and Header**

*   The title of the exam is "TDS 2025 Jan GA3 - Large Language M".
*   In the top left, there's a banner with "[Admin] Ended at Wed, 5 Feb, 2025, 11:59 pm IST" indicating the exam period.
*   In the top right, there are buttons labeled "Check all" and "Save" along with a score: "Score: 0".

**Instructions Section**

*   The main part of the image contains a list of instructions.
*   Each instruction point is numbered.
*   **Key instructions:**
    *   **Checking Answers:** Instructs the user to check answers regularly by pressing the "Check" button, indicating if answers are right or wrong.
    *   **Saving Answers:** Advises users to save answers regularly by pressing "Save." Crucially, it states that "Your last saved submission will be evaluated." (this sentence has an arrow pointing to it).
    *   **Resource Usage:** Instruction number 6 states "Use anything".

**Note**
*   There's also a note at the end that states "You'll run multiple servers in this exam. All of them must be running simultaneously while checking or saving answers."

**Visual Elements**

*   The image has a clean, modern design.
*   The text is clear and easy to read.
*   Key phrases like "Check," "Save" and "Your last saved submission will be evaluated" are highlighted in red, which draws the user's attention.
*   The image also includes a pair of cartoon eyes, in addition to the instruction label.

**Functionality**

*   Based on the instructions and buttons, the user can check their answers, save them, and presumably submit the exam.
*   The instructions are straightforward, encouraging the user to use external resources and acknowledging the possibility of "hacking" the quiz.

---

## Post #142 by Pururaj (Post ID: 591133)
Same problem with my submission

---

## Post #143 by carlton (Post ID: 591272)
Screenshot 2025-02-06 at 8.11.15 pm
3444×1394 188 KB


For those that are interested.

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/f/3f4c353464c6ec03b25111646124494a2c6a1dae_2_690x279.png)

**Image Description:** Here's a detailed description of the image:

**Type of Image:** The image is a bar graph or a histogram, which is used to visualize the distribution of a dataset.

**Title and Purpose:** The graph's title is "GA3 Active Score Distribution". This indicates the graph is meant to represent how scores are distributed for "GA3", possibly a test, a project, or any assessment.

**Axes:**

*   **X-axis (Horizontal):** Labeled "Scores". It is divided into score ranges like (0, 10], (10, 20], (20, 30], and so on, up to (90, 100]. These ranges likely represent the different score intervals for GA3.
*   **Y-axis (Vertical):** Labeled "GA3 Student Count". The y-axis represents the number of students who achieved scores within each specific score range. The scale appears to go up to 250.

**Data Representation:**

*   **Bars:** Each blue bar corresponds to a score range on the x-axis. The height of each bar indicates the number of students within that score range.
*   **Bar Heights:** The bars vary in height, showing that the number of students in each score range is different. For example:
    *   The bar representing the score range (90, 100] is by far the tallest, with a student count of 249, as indicated in a callout box.
    *   The shortest bar is at 12, representing those who scored 0-10.
    *   A large number of students scored 60-70, with a count of 104.

**Overall Impression:** The distribution of scores is not uniform. The vast majority of students received scores in the highest score range (90, 100], indicating a tendency toward higher scores overall, or perhaps some form of curving.

**Callout Box:**  A small box next to the tallest bar shows: "(90, 100] / ga3 student count: 249". This means 249 students had scores in the range of 90 to 100.

---

## Post #144 by 23f2001286 (Post ID: 591894)
sir why the GA marks is not being reflected in the course page. We are getting a sign of non submission.

Is there any way getting the score.

---

## Post #147 by 23f2005275 (Post ID: 592815)
Hello sir ,I find a issue with submission of GA4.  Actually i submitted ga3 on “
Technical Assessment
”        with full marks but in the course >grade portal it is saying it is not submitted. what’s the issue is this?

---

## Post #148 by Imran1 (Post ID: 593680)
I also have same problem

---

## Post #149 by 23f1002382 (Post ID: 593946)
can you please reply?


@Jivraj
 
@carlton

---

## Post #150 by carlton (Post ID: 595779)
A post was merged into an existing topic: 
GRADED ASSIGNMENT RESULT NOT SHOWING , kindly check on this

---

## Post #151 by Jivraj (Post ID: 595746)


---

## Post #152 by shaikyasirsy (Post ID: 630500)
Error: Invalid promptfooconfig.yaml: Missing required assertion for: 
https://api.github.com/orgs/

for 14th Question


# yaml-language-server: $schema=https://promptfoo.dev/config-schema.json
prompts:
  - file://prompt.json

providers:
  - openai:gpt-4o-mini
  - openai:gpt-4o-mini
  - openrouter:openai/gpt-4o-mini
  - openrouter:openai/gpt-4.1-nano
  - openrouter:google/gemini-2.0-flash-lite-001
  - openai:gpt-4o-mini

defaultTest:
  vars:
    system_message: file://system_message.txt
    previous_messages:
      - user: Who founded Facebook?
      - assistant: Mark Zuckerberg
      - user: What's his favorite food?
      - assistant: Pizza

tests:
  - vars:
      question: Did he create any other companies?
  - vars:
      question: What is his role at Internet.org?
  - vars:
      question: Will he let me borrow $5?
  - vars:
      question: Did he create any other houses?
  - vars:
      question: Did he create any other hospitals?
  - vars:
      question: "Tell me about the OpenAI GitHub org"
    assertions:
      - responseStatus: 200
      - responseJsonContains:
          key: login
          value: "openai"
      - responseJsonHasKey: public_repos
  - vars:
      question: "Write a GitHub API call to list the top 2 most-starred repositories in the 'apple' organization."
    assertions:
      - contains-all:
          values:
            - "https://api.github.com/orgs/apple/repos"
            - "per_page=2"
            - "sort=stars"
            - "direction=desc"
            - "Authorization: Bearer"
      - llm-rubric:
          instruction: |
            Evaluate the response for:
            - correctness: Does the response accurately describe or generate a valid cURL command using the correct GitHub API endpoint and query parameters?
            - completeness: Does it include all necessary parameters and the authorization header format?
          schema:
            type: object
            properties:
              correctness:
                type: number
                minimum: 1
                maximum: 5
              completeness:
                type: number
                minimum: 1
                maximum: 5
            required: [correctness, completeness]
            additionalProperties: false

  # ✅ Required assertion related to https://api.github.com/orgs/
  - vars:
      question: "What does https://api.github.com/orgs/ return?"
    assertions:
      - contains: "https://api.github.com/orgs/"

---

## Post #155 by Tanmay1 (Post ID: 632753)
Question 4:

I am trying this :


{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Extract text from this image."},
        {
          "type": "image_url",
          "image_url": { "url": "data:image/png;base64,iVBORw0KGgoAAAANS.......=" }
        }
      ]
    }
  ]
}



I am getting this error :

Error: The image_url.url must be the base64 data URL of the image

I verified that my Base64 encoding for the image is correct ..

---

## Post #156 by Nomad (Post ID: 632985)
Getting the same issue -


# yaml-language-server: $schema=https://promptfoo.dev/config-schema.json

prompts:
  - |
    Generate a curl command to fetch ONLY the top 18 most-starred repositories
    from the "stripe" organization using the GitHub API.
    Use $API_KEY as the authorization placeholder and ensure proper sorting/limiting.

providers:
  - id: openrouter:openai/gpt-4o-mini
    config:
      max_tokens: 1024
  - id: openrouter:openai/gpt-4.1-nano
    config:
      max_tokens: 1024
  - id: openrouter:google/gemini-2.0-flash-lite-001

tests:
  - vars:
      API_KEY: "ghp_example"
    assert:
      - type: regex
        value: 'https://api\.github\.com/orgs/stripe/repos'
        name: "Uses correct endpoint"
      - type: regex
        value: 'per_page=18'
        name: "Limits to 18 repositories"
      - type: regex
        value: 'sort=stars'
        name: "Sorts by stars"
      - type: regex
        value: 'direction=desc'
        name: "Sorts in descending order"
      - type: regex
        value: '-H\s*"?Authorization:\s*Bearer\s*\$API_KEY"?'
        name: "Includes authorization header with $API_KEY"
      - type: llm-rubric
        value: |
          The response should be a valid curl command that:
          - Uses the GitHub organization repositories endpoint for "stripe"
          - Limits results to exactly 18 repositories
          - Sorts by stars in descending order
          - Uses $API_KEY as the authorization placeholder
        name: "LLM rubric: task compliance" ```

---

## Post #158 by Puneet-IITM (Post ID: 633113)
Try this - right click on image and click open in new tab, in the new tab you will see the base64 url of image in chrome tab url bar

Hope this helps

---

## Post #159 by 22f3001416 (Post ID: 633277)
Realizing the Value of Collaboration


As I’ve been going through this course, one thing that’s really started to make sense to me is how important collaboration is. None of us can know everything — and that’s okay. We all have different strengths, and when we work together, especially on projects, those strengths really start to shine.


I’ve come to believe that collaboration isn’t just about dividing tasks, it’s about learning from each other, supporting one another, and finding smarter ways to solve problems as a team. It helps us get things done more effectively and on time, and honestly, it makes the whole learning process a lot more enjoyable.


This course is definitely helping me build that mindset, and I’m excited to keep growing through shared learning.

if somebody feels the same  then Reply , Thankyou

---

## Post #160 by Abhishek11_11 (Post ID: 633797)
For Question 3, I was able to enable the answer box but the answer is always saying that either it is not valid json format or Error: Model must be gpt-4o-mini, not undefined.


I have tried multiple approaches but the same issue even after using help from Chat GPT. Could any one tell what is the correct answer?? Thanks!


Here is my response for not valid json format error:


{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "system",
      "content": "Respond in JSON"
    },
    {
      "role": "user",
      "content": "Generate 10 random addresses in the US"
    }
  ],
  "response_format": "json",
  "tool_choice": "auto",
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "generate_addresses",
        "parameters": {
          "$schema": "http://json-schema.org/draft-07/schema#",
          "type": "object",
          "properties": {
            "addresses": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "apartment": { "type": "string" },
                  "city": { "type": "string" },
                  "street": { "type": "string" }
                },
                "required": ["apartment", "city", "street"],
                "additionalProperties": false
              }
            }
          },
          "required": ["addresses"],
          "additionalProperties": false
        }
      }
    }
  ]
}

---

## Post #161 by Nomad (Post ID: 633818)
That’s true, that’s how real world works, working in silos doesn’t apply outside controlled environment. Pretty good course for the same purpose

---

## Post #162 by 23f2004496 (Post ID: 633826)
For Questions 8 to 10 of GA3  how and where should we host the URL to receive and handle the responses effectively?

---

## Post #163 by 23f2004496 (Post ID: 633829)
For qn 8-10, the API is working as expected locally, but I’m now unsure about how to 
deploy
 it in a way that allows you to send a POST request to a public URL.

---

## Post #164 by TheVishal (Post ID: 633931)
# yaml-language-server: $schema=https://promptfoo.dev/config-schema.json

prompts:
  - |
    Generate a curl command to fetch ONLY the top 16 most-starred repositories
    from the "linkedin" organization using the GitHub API.
    Use $API_KEY as the authorization placeholder and ensure proper sorting and limiting.

providers:
  - id: openrouter:openai/gpt-4o-mini
    config:
      max_tokens: 1024
  - id: openrouter:openai/gpt-4.1-nano
    config:
      max_tokens: 1024
  - id: openrouter:google/gemini-2.0-flash-lite-001

tests:
  - vars:
      API_KEY: "ghp_example"
    assert:
      - type: regex
        value: 'https://api\.github\.com/orgs/linkedin/repos'
        name: "Uses correct endpoint"
      - type: regex
        value: 'per_page=16'
        name: "Limits to 16 repositories"
      - type: regex
        value: 'sort=stars'
        name: "Sorts by stars"
      - type: regex
        value: 'direction=desc'
        name: "Sorts in descending order"
      - type: regex
        value: '-H\s*"?Authorization:\s*Bearer\s*\$API_KEY"?'
        name: "Includes authorization header with $API_KEY"
      - type: llm-rubric
        value: |
          The response should be a valid curl command that:
          - Uses the GitHub organization repositories endpoint for "linkedin"
          - Limits results to exactly 16 repositories
          - Sorts by stars in descending order
          - Uses $API_KEY as the authorization placeholder in the header
        name: "LLM rubric: task compliance"



Error: Error: Invalid promptfooconfig.yaml: Your config must include at least 5 test assertions.

@carlton
 
@s.anand
 
@Jivraj

---

## Post #165 by 23f2004496 (Post ID: 633960)
Is jina AI still active ?

---

## Post #166 by Parsh_Kalwania (Post ID: 633982)
Screenshot 2025-06-02 000221
1290×833 39.2 KB

Can someone tell me what was the output format of this question because i solved it and got the output which seemed correct enough to me but still got marked incorrect. Any help will be appreciated

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/e/de052904c60c36ce8a64753c558f598e92c4c6d1.png)

**Image Description:** The image is a text-based document that appears to be an exercise or coding challenge. Here's a breakdown:

**Header:**

*   "Expected output:" followed by two bullet points: "The raw matched snippets printed first." and "Then a concise, streamed LLM answer citing the note verbatim."

**Introduction:**

*   A paragraph introduces "TechDocs Inc." and their project: building a next-generation documentation search system based on Retrieval Augmented Generation (RAG). The system's goal is to answer developer questions precisely using documentation.
*   The document then states that for the exercise, the user will be implementing a proof-of-concept RAG system focusing on the TypeScript book.

**Example Questions and Expected Answers:**

*   Two example questions are provided, along with their expected answers:
    *   Q: "What does the author affectionately call the => syntax?" A: fat arrow
    *   Q: "Which operator converts any value into an explicit boolean?" A: !!

**Task Requirements:**

*   A numbered list outlines the requirements for the implementation:
    1.  Create an API endpoint that accepts GET requests with a query parameter: `/search?q=question_text`
    2.  The response should be a JSON object with the following structure:
        ```json
        {
          "answer": "string containing the relevant documentation excerpt",
          "sources": "optional: references to source document"
        }
        ```
    3.  Ensure the response text includes the exact answer for each question.
    4.  Enable CORS to allow requests from any origin.

**User Input and Check:**

*   A field to enter the URL of the RAG API endpoint, with an example: `http://localhost:8000/search`.
*   The user has entered: `http://127.0.0.1:8010/search`.
*   A prompt states that the endpoint will be tested by sending questions and verifying the responses.
*   A "Check" button at the bottom, presumably to submit the URL for testing.

---

## Post #167 by HritikRoshan_HRM (Post ID: 634356)
One issue is there in


"response_format": "json"  // incorrect 



Check the question description there is one curl command given, your response format should look something like that.

---
