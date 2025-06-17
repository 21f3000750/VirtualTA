# Topic: Queries regarding End Term exam solutions
**Topic ID**: 172707
**Total Posts**: 16

---

## Post #1 by 24f2003130 (Post ID: 619552)
Hi 
@carlton
 and 
@Jivraj
 sir,


I appeared for the end term examination held on 13th April 2025 during the FN shift. I would like to bring to your attention that the exam interface did not provide an option for multiple selections. However, a few questions appeared to have multiple correct answers.


I have noted down the specific questions and the corresponding options I believe to be correct.So, kindly review them and let me know if there were any errors in my understanding of the questions. The questions are as follows:


1000042547
1080×578 187 KB


Question 2: Fields needed to filter “POST requests under /images/ from 15:00 to 18:00 on Mondays”


To filter such logs, we need:


Time → for the hour and the day (Monday)

Method → to filter POST

URL → to filter /images/


So, the correct minimal set is:




 Time, Method, URL




Time → needed 

Method → needed 

URL → needed 

Referer → not needed, but not harmful


So this option includes all the necessary fields, just with one extra — which doesn’t invalidate it.


1000042548
1080×301 71.5 KB


Acc to solutions only option 6406534159827 is valid:


Status is numeric (200)

Method (GET), Protocol (HTTP/1.1), and URL (/index.html) are correct


All required fields are present and properly formatted


The other options were as follows:


9825 uses invalid protocol (INVALID)


9826 uses invalid status code (OK instead of numeric)


9824 has no critical issue — it is technically also valid (only uses a private IP 192.168.1.1, which is unusual but not invalid). So both 9824 and 9827 are valid, but the answer marked only 9827


1000042545
1079×468 35.7 KB

Correct Answer(s):


 PUT – Correct: It replaces the resource entirely. Multiple identical PUTs = same result.


 GET – Also correct: It only fetches data, no side-effects. Multiple GETs = same result.


 DELETE – Technically correct: Deleting the same resource multiple times has the same result as deleting once (resource stays deleted).




Incorrect Answer:


 POST – Not idempotent. Each POST usually creates a new resource or changes server state.


(This is the mistake on my part that I put the ans as POST as I thought since 3/4 are idempotent and one is not I should select the odd one out but I hope this could be resolved)


Thank you

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/d/fd08e14665989ccea8f5a547b569521575208ae8_2_690x369.jpeg)

**Image Description:** This image contains a multiple-choice question (MCQ) about identifying a valid log entry.  The question provides four options, each representing a different log entry.  Key features to answer the question include:

* **Question Stem:**  Asks to identify a valid log entry based on a provided (unseen) format.

* **Options (A-D):** Each option displays a potential log entry.  These entries share a similar structure:
    * A numerical ID (e.g., 6406534159824).
    * An IP address (e.g., 192.168.1.1).
    * A timestamp (e.g., [12/Dec/2024:14:05:59 -0500]).
    * An HTTP request method (e.g., GET, POST, PUT).
    * A requested resource (e.g., /image.jpg, /index.html).
    * An HTTP version (e.g., HTTP/1.1).
    * A status code (e.g., 200, OK, INVALID).
    *  Client information including browser details (Mozilla/5.0, Chrome version, Safari version).
    * A hostname (www.s-anand.net)
    * Another IP address (192.254.190.217 or 192.254.190.219).

* **Correct Answer Indication:** A checkmark (✓) next to option D (6406534159827) suggests it is the correct answer.  Incorrect options are marked with an 'x' (×).

To answer the question, one must analyze each log entry and determine which one conforms to the unspecified "provided format". The differences between the options lie in the status code (OK vs. 200 vs. INVALID), the HTTP method (GET, POST, PUT), and possibly other minor variations in formatting or values.  The fact that option D is the only one with a different IP address in the last field is irrelevant for the format check.

![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/0/9062a032d89a4b2b049ca34b23905d501cba7913_2_690x192.jpeg)

**Image Description:** This image contains a multiple choice question related to filtering POST requests. The question asks which fields are necessary to filter POST requests made for pages under `/images/` from 15:00 to 18:00 on Mondays.

Four options are provided, each with a unique set of fields:

* **Option 1 (Correct):** Time, Request, Method, URL. This option is marked with a checkmark (✓).
* **Option 2 (Incorrect):** Time, Method, Status, Size. This option is marked with a cross (✕).
* **Option 3 (Incorrect):** Time, Method, URL, Referer. This option is marked with a cross (✕).
* **Option 4 (Incorrect):** Time, Status, URL, Server. This option is marked with a cross (✕).

Each option is preceded by a unique alphanumeric ID (e.g., 6406534159828).  The question focuses on filtering log data based on specific criteria (time, request type, location, and potentially other server details).  The correct answer highlights the fields necessary to effectively filter the specified POST requests.

![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/3/03aec49b7ba39078f204ef24fefa80dae8e9b373_2_690x299.jpeg)

**Image Description:** This image shows a multiple-choice question about HTTP methods.  The question asks which HTTP method is idempotent, meaning that sending the same request multiple times has the same effect as sending it once.

The options provided, each with a unique ID number, are POST, PUT, GET, and DELETE.  The correct answer is marked as PUT.

Additional metadata is provided:

* **Correct Marks:** The question is worth 2 marks.
* **Question Label:** It's classified as a Multiple Choice Question.
* **Sub-Section Number:** 4
* **Sub-Section Id:** 640653189815
* **Question Shuffling Allowed:** Yes (meaning the order of this question relative to others might change).

The long numbers preceding each option appear to be unique identifiers for each choice within a larger question bank or assessment system.

---

## Post #2 by koustubhr (Post ID: 619868)
Agree & second all thoughts shared by 
@24f2003130
 above.






I also wanted to clarify on this question on filtered entries. The question mentions that a list filtered_entries is being created , and with the way the question is structured it seems like the filtering conditions mentioned in the question have already been applied. In that case 
len(filtered entries)
 seems to be correct. However the right answer is marked ‘None of these’ .


image
1108×394 81.9 KB






The valid log entry had me stumped too, option 1 and 4 both look absolutely fine yet only option 4 is marked correct.






Also, only POST request is not idempotent, all other requests are idempotent yet only PUT is marked correct.






Request you to please clarify and consider these points.

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/5/f5f549e906df1006709b3257742fff4b52f416d0_2_690x245.png)

**Image Description:** The image contains a multiple choice question (MCQ) from a test or exam.  The question is about programming, specifically how to count the number of items in a filtered list.

Here's a breakdown of the content:

* **Question Details:** The question number is 309, the question ID is 6406531231230, and it's an MCQ worth 1 mark.  The question type is specified as MCQ.

* **Question Text:** The question asks how to best count the number of requests with a 404 status code (a common HTTP error code) within a filtered list named `filtered_entries`.  The filter is implied to already contain only entries for pages under the `/error/` path.

* **Options:** Four options are provided, each with a unique ID and a code snippet:
    * `6406534159860.  Use len(filtered_entries)` -  This suggests using the built-in `len()` function to get the length of the filtered list. This is likely the correct answer.
    * `6406534159861. Use len(entries)` -  This uses the `len()` function on the unfiltered list `entries`, which wouldn't accurately reflect the count after filtering.
    * `6406534159862. Use sum(1 for entry in entries)` - This uses a generator expression with `sum()` to count items in the unfiltered list, similar to option 2.
    * `6406534159863. None of these` - This option indicates that none of the previous options are correct.

* **Correct Answer:** A checkmark (✔) next to option 6406534159863 indicates that "None of these" is the correct answer.  There's a discrepancy in the image because option 6406534159860 (`Use len(filtered_entries)`) is likely the intended correct answer.  This suggests there may be an error in the provided answer key.  The correct answer is to use `len()` on the already filtered list.

In summary, the image shows a programming question where the challenge lies in understanding how to efficiently use Python's built-in functions (`len()` and `sum()`) to count elements in a list after applying a filter.  There's an apparent inconsistency between the provided answer key and the expected solution.

---

## Post #3 by 22f3000819 (Post ID: 619891)
Yes 
@carlton
 the wording of the question made it seem like the filters were already applied on the list 
filtered_entries
.

---

## Post #4 by iamprasna (Post ID: 620130)
Clarifications on Queries






Which of the following is a valid log entry based on the provided format?

Due to a technical issue in the portal, both options 1 and 4 are correct answers. The final scoring has been adjusted accordingly, and full marks will be awarded for either response.






HTTP method is idempotent

This question has been excluded from scoring as three methods (GET, PUT, and DELETE) are idempotent, with only POST being non-idempotent.






Entries with 404 status code

Although the instructions did not explicitly state that filters applied for status code 404, we acknowledge this ambiguity. Full credit will be awarded for both option 1 and option 4.






Which of the following fields are necessary to filter “POST requests made for pages under /images/ from 15:00 to 18:00 on Mondays”?

Option A (Time, Request, Method, URL) is correct because:








Option B includes Size and Status, which aren’t needed for filtering by time, method, and URL


Option C includes Referer, which is unnecessary unless filtering by source page


Option D includes Status and Server, which aren’t relevant for this specific filtering requirement

---

## Post #5 by 24f2003130 (Post ID: 620133)
Thank you for the clarification provided regarding Question 4 and resolution of errors in other questions. I understand the reasoning behind choosing Option A (Time, Request, Method, URL). However, I respectfully believe Option C (Time, Method, URL, Referer) is more accurate for the following reasons:






Redundancy in Option A:

The Request field already contains the HTTP method, URL, and protocol (e.g., “POST /images/logo.png HTTP/1.1”). Including both Request and separate Method and URL fields introduces redundancy. If we already extract Method and URL separately for filtering, the full Request field becomes unnecessary.






Simplicity in Filtering:

Filtering for “POST requests under /images/” from 15:00 to 18:00 on Mondays can be done using:






Time → for checking the hour and weekday.


Method → to filter only POST.


URL → to ensure the request is under /images/.


Thus, Option C (Time, Method, URL, Referer) already includes all needed fields. While Referer is not essential, it doesn’t interfere with the filtering and might be useful in future extended filtering cases (e.g., source tracking). Therefore, Option C is complete and accurate without being redundant.




Consistency with Log Parsing Practices:

In most log analysis scripts or systems (e.g., Python’s re or pandas parsing of logs), Method and URL are parsed from Request for separate use. This further supports the idea that including Request alongside Method and URL is not best practice.

---

## Post #6 by 22f3000819 (Post ID: 620467)
Sir, regarding point 3, score-checker tells a different story. While all the other changes have been made with the same reflecting in the score, that question still says “The question and answer remain the same . No changes required”, which is different from your post.




image
923×352 72 KB


Can you please look into it?


Thanks

Regards,

Shivaditya

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/0/404e7b25f4155d41d4939b07fd45fa3c120beadd_2_690x31.png)

**Image Description:** The image shows a row from a table, likely a log or record of some kind.  The row contains the following information:

* **31:**  This appears to be a sequential number, an identifier for the row or entry.

* **6406531231230:** A long numerical code or identifier.

* **MCQ:** An abbreviation, possibly standing for "Multiple Choice Question."

* **W:** A single letter, the meaning of which is unclear without more context.  It might represent a status, category, or other attribute.

* **0:** A numerical value, potentially representing a count or some other metric.

* **6406534159860 and 6406534159863:** Two more long numerical codes or identifiers that are very similar, suggesting a version or related items.

* **1.00:** A numerical value that could represent a score, version number, or some kind of weighting.

* **Not Modified:** Indicates that some element hasn't been changed or altered.

* **"The question and answer remain the same. No changes required":** A textual explanation accompanying the "Not Modified" status.  This confirms that the entries are unchanged.


The numerical codes likely relate to specific questions and answers.  The "MCQ" strongly suggests that the data deals with multiple choice questions and their associated answers or IDs.  The "W" value and the numerical values 0 and 1.00 would require additional contextual information to fully understand their meaning within the table's overall purpose.

![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/1/91a843fad0075c603424114af0cfca114941a304_2_690x263.png)

**Image Description:** This image contains a multiple-choice question (MCQ) from an exam or test.  Let's break down the content:

* **Question Metadata:** The top line provides identifying information:
    * **Question Number:** 309
    * **Question Id:** 6406531231230 (This is a unique identifier for the question)
    * **Question Type:** MCQ (Multiple Choice Question)
    * **Correct Marks:** 1 (One point is awarded for a correct answer)

* **Question Label:**  Specifies the question type as a "Multiple Choice Question."

* **Question Stem:** This is the core of the problem:  "After filtering the log entries (in a list `filtered_entries`), which of the following is the best way to count the number of requests with a 404 status code for pages under `/error/`?"  This asks for the most efficient method to count specific entries in a filtered list.  The phrasing implies the filtering process has already removed irrelevant entries, leaving only those potentially matching the criteria.

* **Options:** Four possible answers are provided, each with an ID:
    * 6406534159860. `Use len(filtered_entries)`: This suggests using the length (number of elements) of the filtered list.
    * 6406534159861. `Use len(entries)`: This option proposes using the length of the *unfiltered* list, which would be incorrect as it includes irrelevant entries.
    * 6406534159862. `Use sum(1 for entry in entries)`: This suggests iterating through the *unfiltered* list and summing 1 for each entry – an inefficient method.
    * 6406534159863. `None of these`: This is the final option, indicating that none of the above methods are the best approach.  (A checkmark next to this option signifies it's correct)

In short, the question tests understanding of efficient list processing and specifically how to leverage a pre-filtered list (`filtered_entries`) for counting items meeting particular criteria, rather than processing the entire, unfiltered dataset.  The correct answer is "None of these" because the question requires additional logic (not shown in the options) to only count the filtered entries that specifically correspond to a "404" status code and the path `/error/` .

---

## Post #7 by 24f2003130 (Post ID: 620472)
@iamprasna
 sir , the scores have been updated on the dashboard as well and the answer for the question in point 3 is still the same


Additionally , sir I have attached the snapshot of a dec’24 TDS PYQ which is a replica of this question and the answer for the same is mention the first option.


1000042796
1080×538 84.7 KB


The link for the same has been attached for your referance




drive.google.com








IIT M FOUNDATION DIPLOMA FN EXAM QDF2 22 Dec 2024.pdf


Google Drive file.

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/d/fda110de0ada74e60ba0e160ab21463c4ebdbd44_2_690x343.jpeg)

**Image Description:** The image contains a multiple-choice question (MCQ) from an exam or quiz.  The question is about programming and specifically how to count successful GET requests after filtering log entries.

Here's a breakdown of the key content:

* **Question:** After filtering log entries (stored in a list called `filtered_entries`), what is the best method to count the number of successful GET requests for pages under the path `/telugump3/`?

* **Options:** Four options are provided, each representing a different method in a programming language (likely Python):
    * `len(filtered_entries)` - This uses the `len()` function to get the length of the `filtered_entries` list.  This is marked as the correct answer.
    * `len(entries)` - This uses `len()` on the unfiltered list `entries`, which is incorrect because it doesn't account for the filtering.
    * `sum(1 for entry in entries)` - This iterates through the unfiltered `entries` list and sums 1 for each entry, which is inefficient and doesn't use the filtered data.
    * `count(filtered_entries)`-  This option is syntactically incorrect in most common programming languages.  `count()` typically requires an argument specifying the element to count.


* **Question Details:** The top of the image includes metadata such as the question number (351), question ID (6406531040283), question type (MCQ), and the marks awarded for a correct answer (1).  The "Question Label" clarifies it is a multiple-choice question.


In essence, the question assesses understanding of efficient list manipulation and filtering in a programming context.  The correct answer leverages the `len()` function on the already-filtered list to directly obtain the count.

---

## Post #8 by 22f3000819 (Post ID: 620477)
That’s a great find. They’re the same question with just different parameters. Please look into it 
@iamprasna
 sir.

---

## Post #9 by 24f2003130 (Post ID: 620539)
@carlton
 sir and 
@Jivraj
 sir please look into this question and clarify this


Thank you

---

## Post #10 by swatikap (Post ID: 620540)
Hi,

From where are you checking the transcripts? I’m not able to see the answer transcripts in the score checker app.


image
1891×622 31.7 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/d/3d54127deb9243fce2a75dace8f4b52f14f9057f_2_690x226.png)

**Image Description:** Here's a description of the image:

The image shows a webpage titled "SCORE CHECKER" with a dark-grey header containing a logo (a circular emblem with indistinct details), and navigation links for "Transcript," "Home," and "Logout."  Below the header is a light-teal informational bar stating, "This is before the sign-off of scores; it may change after the sign-off."

The main content of the page is a table displaying student score information. The table's headers are "EMAIL," "HALLTICKET," "COURSE CODE," "TOTAL SCORE," and "VIEW."  The table body shows one row of data:

* **EMAIL:** 23ds3000185@ds.study.iitm.ac.in
* **HALLTICKET:** S2DAD23DS3000185
* **COURSE CODE:** SE2002
* **TOTAL SCORE:** 70
* **VIEW:** A teal circular icon (likely a link to view more details).


The overall design is clean and simple, utilizing a dark-grey and teal color scheme. The information displayed suggests this is a student portal or system for checking academic scores.  The warning about score changes after sign-off indicates that the displayed score might be provisional.

---

## Post #11 by 24f2003130 (Post ID: 620544)
Click on the eye button …then you will be able to view your transcript

---

## Post #12 by swatikap (Post ID: 620546)
Thanks for the reply, but I only see the question id’s and answer id’s, not able to find the transcripts.


image
1867×923 94.1 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/7/f7adba30daf6dbdfda4884a7b821a593557a466a_2_690x341.png)

**Image Description:** The image shows a score checker table.  The table displays the results of a multiple choice question (MCQ) assessment.  Each row represents a single question.

The columns are:

* **S.NO.:** Serial number of the question.
* **Question ID:** A unique identifier for each question (e.g., 6406531252398).
* **Question Type:**  Indicates that all questions are "MCQ" (Multiple Choice Question).
* **Result:** The student's answer (e.g., C, W - where W might stand for wrong).
* **Score:** The points awarded for the question (either 0 or 1.00).
* **Selected Option:** The option selected by the student (e.g., 6406534219005).  These IDs likely correspond to specific answer choices within each question.
* **Correct Option:** The correct option for the question (e.g., 6406534219005).
* **Mark:** The score given to the question (again 0 or 1.00).
* **Modification of Question:**  States if the question was modified (all show "Not Modified" except row 4).
* **Remarks:**  Additional notes, mainly empty except for row 4, which explains a marking discrepancy, and row 9, which states that the remark "Remains the same".

Row 4 is highlighted in yellow.  The remarks column for this row indicates that options 3 and 2 should both be awarded marks, implying a grading error or a change in the marking scheme after the initial evaluation.  The Question ID in this remark references the same question in the row.

The top of the image displays "SCORE CHECKER" as the title and has buttons for "Transcript," "Home," and "Logout." A logo is also present in the upper left corner.  The overall style suggests an online assessment platform or grading system.

---

## Post #13 by 24f2003130 (Post ID: 620547)
It seems that the option to download the answer key has been removed. However, you could consider reaching out to someone in the group or checking the dashboard for  solution pdf of question paper. You can then match the questions in order, even if the IDs don’t align exactly—it should still give you a general idea. From there, you can proceed accordingly.

---

## Post #14 by 22f3000819 (Post ID: 621044)
@iamprasna
 
@carlton
 Please look into it once. According to point 3 of 
@iamprasna
’s post, I should get full credit for that question and it will take me to a perfect 100 score in ET from the current 97. I brought this into attention before the scores were pushed to the dashboard.


Regards,

Shivaditya

---

## Post #15 by iamprasna (Post ID: 621914)
The correction has been done to the following question for both the FN and AN sessions. You must be able to see the change in scores shortly




Entries with 404 status code

Although the instructions did not explicitly state that filters applied for status code 404, we acknowledge this ambiguity. Full credit will be awarded for both option 1 and option 4.

---

## Post #16 by 24f2003130 (Post ID: 621957)
Thank you sir for acknowledging our requests and resolving the error

---
