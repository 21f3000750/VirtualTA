# Topic: GA1 - Development Tools - Discussion Thread [TDS Jan 2025]
**Topic ID**: 161083
**Total Posts**: 131

---

## Post #1 by s.anand (Post ID: 575342)
Please post any questions related to 
Graded Assignment 1 - Development Tools
.




Important Instruction


Please use markdown code formatting (fenced code blocks) when sharing code in Discourse posts. This makes the code much easier to read and differentiate from non-code text. It also makes it easier for people to copy code snippets and run it themselves. Visit this link for more details: 
Extended Syntax | Markdown Guide
.


A friendly suggestion: kindly go through 
Discourse Docs
! 




Deadline: 26 Jan 2025, midnight IST


@carlton
 
@Jivraj
 Please keep an eye on this thread for support.

---

## Post #2 by s.anand (Post ID: 575344)


---

## Post #3 by 21f2000370 (Post ID: 575782)
image
1296×158 7.29 KB

For question 16 of GA1, It says "Rename all files replacing each digit with the next "

Accepted answer is working only if file names are renamed as

2h3q9x.txt → 3h4q0x.txt

eb209nmlca.txt → eb310nmlca.txt

That means if digit is 9 then next digit should be 0. 
@carlton
 
@Jivraj
 let me know if this is what is expected. since 9->10 or 209 → 210 is not working

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/8/f8af7c6e2fe001c8bf000605b52c903e1b0e6fe1.png)

**Image Description:** This image contains a programming question related to file manipulation and bash scripting.

Here's a breakdown of the content:

**Header:**

* **16:**  Likely a question number or identifier within a larger assignment or exam.
* **Move and rename files (0.5 marks):**  This clarifies the topic and the weight of the question.


**Instructions:**

* **Download q-move-rename-files.zip and extract it:**  The student is instructed to download a zip file containing files and extract its contents.
* **Use mv to move all files under folders into an empty folder:** The extracted files are to be moved from any subfolders into a single, empty directory.
* **Then rename all files replacing each digit with the next (i.e. a19b.txt becomes a20b.txt):** The filenames should be modified, incrementing each digit.  For example, 'a19b.txt' should become 'a20b.txt'.

**Question:**

* **What does running `grep . * | LC_ALL=C sort | sha256sum` in bash on that folder show?:** This is the core of the problem. The student needs to determine the output of this bash command sequence after completing the file manipulation steps.  Let's break down this command:
    * `grep . *`: This will find all files and directories in the current directory, as `.` matches any character and `*` matches zero or more of the preceding character.
    * `LC_ALL=C sort`: This sorts the output of `grep` using the C locale, which ensures a consistent sort order regardless of the system's locale settings.
    * `sha256sum`: This calculates the SHA256 checksum for each file listed in the sorted output.  The output will show the checksums of all the files (and possibly directories, depending on the behaviour of `sha256sum` with directories) in the directory, sorted alphabetically.

In short, the student must predict the final output of the chained bash command after having moved and renamed the files as instructed.  The answer would likely involve a list of SHA256 checksums, each corresponding to a renamed file in the final folder.

---

## Post #4 by Jivraj (Post ID: 575795)
Hi anant,


Question mentions every digit should be replaced by next one.


In that case 209 would get replaced by 310

---

## Post #5 by 21f2000370 (Post ID: 575815)
Hello Sir, When I am following that logic to rename files, assessment check is giving error “Incorrect. Try again.”

---

## Post #6 by carlton (Post ID: 576111)
@21f2000370
 Since you have managed to get all the answers correct, I presume there are no further issues w/ Q16.

---

## Post #7 by 23f2003790 (Post ID: 576239)
Hi, I am unable to access Graded Assignment 1. Every time I click on the given link, all I can see is this page. Please advise.


tdsga1
1902×919 31.1 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/b/7be5e1eb5ea66bf30d3a3ebb32850f99e077bcb5_2_690x333.png)

**Image Description:** The image shows the header of what appears to be an online quiz or assignment. 


Here's a breakdown of the content:

* **Title:** "Tools in Data Science - Graded Assignment 1" This clearly indicates the subject matter and type of assignment.

* **Deadline:** A blank line follows the title, labeled "Deadline:".  This space is presumably for the instructor to fill in the due date.

* **Note:** Below the deadline is a crucial note: "Every page reload randomizes the quiz. So don't copy answers from previous attempts. You can submit multiple times." This explains the quiz's design, emphasizing that each attempt will have different questions, preventing cheating by copying answers from previous attempts, but allowing multiple submission attempts.


The image shows no actual quiz questions, only the introductory information.  The lack of a deadline is notable and suggests the image is either a template or a snapshot taken before the deadline was added.

---

## Post #8 by Jivraj (Post ID: 576242)
Possible reasons for this issue.




Disable/remove Ad blocker


Disable/remove Tracking blocker (Allow third party cookies)


Use Chrome browser


Disable Browser extensions

---

## Post #12 by 21f2000370 (Post ID: 577689)
As I highlighted earlier, Its not accepting the answer  if I follow correct logic for renaming for example 209->210, but it is accepting if rename as 209->310

---

## Post #13 by Jivraj (Post ID: 577736)
Hi Anant,








 21f2000370:




image
1296×158 7.29 KB






Here in question, it’s mentioned to replace every digit with next digit, that’s why 209 would be 310.

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/8/f8af7c6e2fe001c8bf000605b52c903e1b0e6fe1.png)

**Image Description:** This image shows a computer programming question.  The top line indicates it's question number 16, worth 0.5 marks, and is about moving and renaming files.

The instructions are:

1. **Download:** Download a file named `q-move-rename-files.zip`.
2. **Extract:** Extract the downloaded zip file.
3. **Move:** Use the `mv` command to move all files from subfolders into a single, empty folder.
4. **Rename:** Rename all files in that folder.  The renaming rule is to increment each digit in the filename by one. For example, `a19b.txt` becomes `a20b.txt`.

Finally, the core question asks what the output of a specific bash command would be when run in the newly populated folder:

`grep . \* | LC_ALL=C sort | sha256sum`

This command involves these steps:
* `grep . \*`: This likely finds all files (`.`) in the current directory (`\*`).
* `LC_ALL=C sort`: This sorts the filenames according to the C locale (a standard, consistent way to sort).
* `sha256sum`: This calculates the SHA256 checksum of the sorted filenames.  The output would be the SHA256 hash of a string representing the sorted list of filenames.

In short, the question tests the student's understanding of file manipulation commands (download, extract, move, rename) in a Linux/Unix environment, combined with their knowledge of the `grep`, `sort`, and `sha256sum` commands to produce and verify the results.

---

## Post #14 by 23f1002698 (Post ID: 577946)
In attempting the third question, I’m unable to download the npm package as it requires docker. When trying to install docker from the installer, it freezes in the verifying package stage. Can somebody please help solve my problem?


@carlton
 
@Jivraj

---

## Post #15 by 23f1002630 (Post ID: 577949)
image
1627×202 12.6 KB

Which HTML content we want to take?

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/6/f608128ef0d30f88223b247f1c02394c91943015_2_690x85.png)

**Image Description:** The image shows a programming exercise or quiz question. 


Here's a breakdown of the content:

* **Instruction:** The top section provides instructions.  It asks the user to use CSS selectors to find all `<div>` elements with the class "foo" within a hidden element (presumably present in the code not shown in the image). The goal is to calculate the sum of the `data-value` attributes of these selected `<div>` elements.

* **Answer Input:**  A text input field is provided below the instruction, where the user is expected to enter the calculated sum of the `data-value` attributes.  Currently, it displays "0".  The small red circle with a slash indicates a likely error or that the answer is incorrect.

* **Key Terms:**  The words `<div>`, `data-value`, CSS selectors, and "foo class" are crucial to understanding the task.  These are standard terms in web development and CSS.

In short, the image captures a coding challenge that tests the user's understanding of CSS selectors and attribute manipulation within HTML elements.  The hidden element (not shown) presumably contains multiple `<div>` elements with class "foo" and `data-value` attributes. The user needs to locate these elements using CSS, extract their `data-value` attributes, and compute their sum.

---

## Post #17 by carlton (Post ID: 577987)
Hi Suhani,


npm does not require docker.


Kind regards

---

## Post #18 by carlton (Post ID: 577990)
Hi Hisham,


Its described in the question. There is a hidden element hiding somewhere after that question. You would have to inspect the DOM to find it.

---

## Post #19 by 23F300327 (Post ID: 577991)
Screenshot 2025-01-11 at 10.29.41 PM
1440×900 160 KB


@s.anand
  please guide me through this question, my answer is showing incorrect

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/7/7762e0cad9334545b58855946414228e23ffccae_2_690x431.png)

**Image Description:** The image shows a graded assignment on a website, likely related to a course on web development. 


Here's a breakdown of the key content:

* **Top Bar:** Shows the assignment title ("Graded Assignment 1"), course name ("TDS 2025 Jan GA1 - Develop"), and other browser tabs.

* **Assignment Details:** The assignment is due on Sun, January 26th, 2025, at 11:59 pm IST. The current score is 8.75 out of 10. Buttons labeled "Check" and "Save" are visible.

* **Instructional Content:** A section explaining CSS selectors (Basic CSS selectors, Attribute selectors, Combinators), referencing the Mozilla Developer Network (MDN) as a resource.  It also recommends an interactive learning tool called "CSS Diner".

* **Coding Challenge:** The core of the assignment involves a question about using CSS selectors. The instructions ask to find all `<div>` elements with a class of "foo" within a hidden element and calculate the sum of their `data-value` attributes.  The student's answer (482) is marked incorrect.

* **File Management (Right Side):** A panel displays a list of files, all of which appear to be "Removed." This might suggest they were part of an earlier part of the assignment or are not relevant to the current task.

* **Next Assignment:** At the very bottom, there's a preview of the next task: "Process files with different encodings (1 mark)".

The image is primarily focused on a CSS selector challenge that is part of a larger graded assignment. The incorrect answer and "Try again" message suggest the student is actively working through the problem. The file list on the right indicates some files were provided for the assignment, possibly as data for previous or subsequent parts.

---

## Post #20 by 21f3001993 (Post ID: 578158)
Hello Sir. I am unable to install uv in my windows system. Whenever I run the code provided at the reference link in Powershell, my anti-virus system sends a message that it was blocked. Even after blocking Real-time security, uv does not display. What am I doing wrong?

---

## Post #21 by Samra (Post ID: 578520)
Hi, I’m unable to view assignments. below is the screenshot for your reference.


Screenshot 2025-01-12 150511
963×632 14.5 KB


Please suggest me a way to view it. I have allowed third-party cookies as well.


Thanks

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/5/95373e67b4815fb1ee37cdb8b9157ed558cffccc.png)

**Image Description:** The image shows a website error message on a dark background.  The main message is "This site can't be reached," followed by the specific website address: `exam.sanand.workers.dev`.  The error message states that this website unexpectedly closed the connection.

Below the main message are troubleshooting suggestions:

*   Checking the connection
*   Checking the proxy and the firewall
*   Running Windows Network Diagnostics

At the very bottom, an error code is displayed: `ERR_CONNECTION_CLOSED`.  Two buttons are visible at the bottom of the page: "Reload" and "Details".  At the top, a small icon resembling a document with a sad face is displayed.  The overall design suggests it's a standard browser error page.

---

## Post #23 by Jivraj (Post ID: 578991)
Hi manmeet,


I don’t know about solution to this.

Some network setting might be causing problem.


Alternatively you can make use of GitHub codespaces which provides 120 hours of free run time in a month. With GitHub codespaces you can use Ubuntu os, and visually it gives you feel of vs code. You can also active your GitHub student developer pack and get 180 hours of GitHub codespaces and some more benefits such as cloud resources and domains.


I have done all questions of week1 and week2 on codespaces only, codespaces works very well if you have good internet connection.

---

## Post #24 by Jivraj (Post ID: 578993)
Hi samra,


Try installing some other browser see if that works.

---

## Post #25 by Jivraj (Post ID: 578994)
Hi mishkat,


Without sharing code, can you pls share your approach how you are trying to solve this question.

---

## Post #26 by 21f3001993 (Post ID: 579005)
Ok, thanks. I turned off many security features including anti-virus system’s security and windows security options etc. Then it allowed me to download uv on the system. Now it is running, and I got output as json for Q2.

---

## Post #27 by Nelson (Post ID: 579120)
2 days ago I  attempted TDS 2025 Jan GA1 - Development Tools and scored 8.5. I didn’t submit as I wanted to attempt incorrect answer questions.

When I logged in today it says score is 0.

Shall I submit or not? Do I have to attempt all questions again?

Why the assignment and submissions are two separate pages/links?

If [seek] (
Nptel Seekh
) can access [TDS exam] (
Technical Assessment
) then why we need to submit from seek?

---

## Post #28 by carlton (Post ID: 579142)
The seek portal question is to confirm that the student has seen the GA. It does not actually give you a score. Otherwise students sometimes claim that they looked and did not find any GAs (this has happened in the past). Hence the two stage verification. You still need to 
 the submissions to get a score for the GA.


The actual GA questions are on 
https://exam.sanand.workers.dev/
 via the seek portal or

on the 
Tools in Data Science
 introduction page.


Its just a more robust way of ensuring that students have indeed viewed the GAs.


As far your submission goes, we have your last submission and the score. 


We will check on our end why your submission has not reloaded into your browser.

Normally these are stored in session storage. So if your browser has deleted them, it might have not loaded from our back end server. 
@s.anand
 will be able to confirm the reason for this problem.


For the time being if you are making a fresh submission, just fill in all the answers in again, so that your latest submission will be marked correctly.


Kind regards

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/6/d67654c30e9fe72ff5970775fa393eaec8204779.png)

**Image Description:** That's a simple image depicting a digital button or icon. 


Here's a breakdown of its content:

* **Background:** A solid, bright blue rectangle forms the main body of the button.

* **Border:** A thin, white, rectangular border surrounds the blue background, giving the button a slightly raised or highlighted appearance.

* **Text:** The word "Save" is centered within the blue rectangle.  The text is in a sans-serif, white font. The font appears slightly blurry or pixelated, possibly due to the image's low resolution.


The overall impression is a standard graphical user interface (GUI) element commonly used to indicate a "Save" function in software or online applications.

---

## Post #29 by Nelson (Post ID: 579152)
Thanks 
@carlton
.

I answered questions on 
https://exam.sanand.workers.dev/
 but didn’t click on the button “Submit Answers” on seek as my answers for 2 questions were incorrect.

My question is whether I need to submit on seek to save answers on Exam? (I checked my score and saved it on the exam site.)

---

## Post #30 by carlton (Post ID: 579182)
Hi 
@Nelson


Your answers on the 
exam
 site that have been submitted will be saved and used as the basis for your score. Saying yes/no on seek does not materially impact scoring. Its just an awareness question. Even if you answered yes on the seek portal, you can still revise your answers on the exam site. The final submission is always whats locked in for the score (until the deadline passes).


Kind regards

---

## Post #31 by carlton (Post ID: 579195)
It might be because you are not adding up the correct tags with attribute 
data-value
. There may be other tags within the same DOM and having the attribute 
data-value
.


Kind regards

---

## Post #32 by Nelson (Post ID: 579264)
I am stuck with the last question. SQLite question.

It gives the error:


Error: Got [[121510.39]]...




Is it possible to have a more descriptive error? It’s a simple SQL query. I tried various options in my query. I didn’t succeed.

---

## Post #33 by Jivraj (Post ID: 579294)
Hi Nelson,


I checked your set of questions, you are using wrong query to get answer.


kind regards

---

## Post #34 by roy2003 (Post ID: 579347)
@carlton
 
@Jivraj

In this picture for the given question i have tried in python and chatgpt both are giving same answer still showing wrong. GA1 question


Neutral Minimal Photo Collage Mood Board Instagram Story
1080×1920 119 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/7/67afef07640f20d467149fad6e77a9edf0bcc0d2_2_281x500.jpeg)

**Image Description:** Here's a description of the image's content:

The image shows a computer screen capturing a programming problem and its solution. 


**Top Section:**

* **Problem Statement:** A dark gray box at the top contains the programming challenge: "Count Wednesdays (2.5 marks)".  The question asks to determine the number of Wednesdays between August 9th, 1986, and June 19th, 2012.  A text input box is provided for the answer.  Instructions below specify the date format (year-month-day) and that any method can be used.

**Middle Section:**

* **Python Code:** The largest part of the image displays Python code designed to solve the problem. The code uses the `datetime` library and iterates through dates, checking if each day is a Wednesday and incrementing a counter.  Line numbers are clearly visible. The code is well-commented, explaining each section's purpose.

* **Code Execution Output:** Below the code, a portion of a terminal window is shown.  The line "Number of Wednesdays: [wednesday_count]" indicates the program's output (although the value is not fully visible). The path to the Python executable file is visible, indicating the operating system is likely Windows.


**Bottom Section:**

* **Answer:** A light gray box at the bottom displays the answer generated by the code (or perhaps from a subsequent manual check) confirming "There are 1349 Wednesdays in the date range from August 5, 1986, to June 19, 2012". There's a slight discrepancy with the dates mentioned in the problem statement, suggesting a possible typo in the problem itself (1986 vs 1906).  A small numbered bracket suggests this response is part of a numbered list of answers.


In summary, the image documents the process of solving a programming problem involving date calculations in Python, from the problem statement to the code and finally to the solution.  The use of comments in the code and clear labeling makes it easy to understand the steps involved.

---

## Post #35 by roy2003 (Post ID: 579358)
@Jivraj
 
@carlton

The same issue is happening in the question 12 of GA1. I have given the answer by using collab and gemini , its giving the proper result but showing wrong.


Minimal Square Photo Collage Photography Instagram Post
1080×1080 126 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/f/cfbf846fed1d092f2fe49741a8bc37821a01c952_2_500x500.jpeg)

**Image Description:** The image shows a split screen.  The left side displays a Python code editor with a program focused on reading and processing data from CSV files. The code is divided into functions: one to read CSV files, handling potential encoding issues, and another to process the data, summing values associated with a specific symbol.  The code includes error handling (try-except blocks) for file not found and decoding errors.  The bottom of the code editor shows the path to the CSV files used and the calculated sum (31512).


The right side of the image shows a screenshot of a web page.  A video from a channel called "Computer Stuff They Didn't Teach You" is prominently featured. The video title refers to "Code Pages, Character Encoding, Unicode, UTF-8 and the BOM." Below the video thumbnail is text describing the accompanying exercise: to download three files, process them (paying attention to encoding), and find the sum of values associated with a specific symbol. This exercise seems directly related to the Python code on the left, suggesting the code is a solution to the problem presented in the video/exercise.

---

## Post #36 by Jivraj (Post ID: 579359)
Hi Shouvik,


Your code seems correct to me. I think there is an extra space before your answer in input box.


Btw instead of using a while loop, there is a much more optimal, which uses difference of dates and doesn’t require a loop at all. Try to figure it out.


kind regards

---

## Post #37 by roy2003 (Post ID: 579363)
yeah thank you sir. now please say for the 2nd problem

---

## Post #38 by Jivraj (Post ID: 579370)
Try copy pasting exact symbols 
— OR † OR €
 Can you share code in code block, it’s difficult to read symbols that are present.


Also have a look at what 
all_content
 variable contains, see if there are some problem with content.

---

## Post #39 by roy2003 (Post ID: 579372)
!pip install chardet==5.1.0  # Install the chardet library



import chardet
def read_files():
  """Gets two CSV files and one TXT file from the user and reads them.

  Returns:
    A tuple containing the contents of the three files.
  """
    # Get the file paths from the user.
  csv_file_1_path = input("Enter the path to the first CSV file: ")
  csv_file_2_path = input("Enter the path to the second CSV file: ")
  txt_file_path = input("Enter the path to the TXT file: ")

  # ... (Get file paths from user - same as before)

  # Read the CSV files.
  try:
    with open(csv_file_1_path, 'rb') as f:  # Open in binary mode
      rawdata = f.read()
      encoding = chardet.detect(rawdata)['encoding']  # Detect encoding
    with open(csv_file_1_path, 'r', encoding=encoding) as csv_file_1:  # Use detected encoding
      csv_data_1 = csv_file_1.read()

    # Repeat for csv_file_2_path using the same pattern
    with open(csv_file_2_path, 'rb') as f:
        rawdata = f.read()
        encoding = chardet.detect(rawdata)['encoding']
    with open(csv_file_2_path, 'r', encoding=encoding) as csv_file_2:
        csv_data_2 = csv_file_2.read()

  except FileNotFoundError:
    print("Error: One or both of the CSV files could not be found.")
    return None
  except UnicodeDecodeError:
    print("Error: Could not decode one or both of the CSV files.")
    return None

  # Read the TXT file.
  try:
    with open(txt_file_path, 'rb') as f:  # Open in binary mode to detect encoding
        rawdata = f.read()
        encoding = chardet.detect(rawdata)['encoding']  # Detect encoding
    with open(txt_file_path, 'r', encoding=encoding) as txt_file:  # Open in text mode with detected encoding
        txt_data = txt_file.read() # Read the content of the file
  except FileNotFoundError:
    print("Error: The TXT file could not be found.")
    return None
  except UnicodeDecodeError:
    print("Error: Could not decode the TXT file.")
    return None

  # Return the contents of the files.
  return csv_data_1, csv_data_2, txt_data

# Call the function to read the files.
file_contents = read_files()
if file_contents:
  csv_data_1, csv_data_2, txt_data = file_contents
  #print("Content of the first CSV file:\n", csv_data_1)
  #print("\nContent of the second CSV file:\n", csv_data_2)
  #print("\nContent of the TXT file:\n", txt_data)

  # Combine the content of all files into a single string
  all_content = csv_data_1 + csv_data_2 + txt_data

  # Split the content into lines
  lines = all_content.split('\n')

  # Initialize the total sum
  total_sum = 0

  # Iterate through each line
  for line in lines:
    # Split the line into symbol and value, handling potential extra spaces
    try:
      parts = line.strip().split(',')
      symbol = parts[0].strip()  # Remove leading/trailing spaces from symbol
      value = parts[1].strip()   # Remove leading/trailing spaces from value

      # Check if the symbol matches the criteria (using a more robust check)
      if symbol in ['€', 'ˆ', '’'  # Euro symbol variations
                     # Add any other known variations of the target symbols
                   ]:
        # Convert the value to a number and add it to the total sum
        total_sum += float(value)

    except (IndexError, ValueError):
      # Ignore lines with incorrect formatting or non-numeric values
      pass

  # Print the total sum
  print("The sum of all values associated with the specified symbols is:", total_sum)

---

## Post #40 by roy2003 (Post ID: 579373)
i have given all the symbols correctly sir

---

## Post #41 by Samra (Post ID: 579413)
Hi Jivraj,


I have tried with a different browser, but still not working. Below is the screenshot for your reference.


Screenshot 2025-01-13 224057
1005×714 27.3 KB


Thanks

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/d/0d763aca30ffeed7a3f4758aa70e06baff508f77_2_690x490.png)

**Image Description:** The image shows a dark gray screen displaying a connection error message.  The main text reads:

**Your connection was interrupted**

Below this, in smaller text, it says:

**A network change was detected.**

Even smaller text underneath indicates an error code:

**ERR_NETWORK_CHANGED**

There is a blue button labeled **Refresh**.

At the top of the screen, there is a stylized graphic of two rounded, colorful objects connected by a cord, possibly representing a network connection that has been broken.  The colors are shades of purple, blue, and teal.  The overall style is somewhat playful or friendly despite the error message.

---

## Post #42 by Nelson (Post ID: 579457)
One unicode character is in both UPPERCASE and lowercase. Do a case sensitive search.

---

## Post #43 by s.anand (Post ID: 579585)
@Samra
 this is almost certainly due to a (typically corporate) firewall or antivirus. Please try with a personal laptop from a public / home network.


(I face this problem at office often. Once, our company’s firewall blocked our own company website 
)

---

## Post #44 by Jivraj (Post ID: 579626)
Hi Nelson,


I checked with your dataset for this particular question. Using correct query I am able to get correct answer. Pls check sql query that you are using.


Kind regards

---

## Post #45 by siva.bhaskaran (Post ID: 579703)
What is the windows equivalent of sha256sum?


npx -y prettier@3.4.2 README.md | sha256sum.
sha256sum. : The term 'sha256sum.' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct 
and try again.
At line:1 char:35
+ npx -y prettier@3.4.2 README.md | sha256sum.
+                                   ~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (sha256sum.:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

---

## Post #46 by Samra (Post ID: 579750)
@s.anand
 Actually, I’m using a personal laptop. Is this country dependent or restricted?

---

## Post #47 by jkmadathil (Post ID: 579774)
Check 
this link from akamai

---

## Post #48 by jkmadathil (Post ID: 579779)
Did you try the following:




ping exam.sanand.workers.dev


tracert exam.sanand.workers.dev




This is what I got while doing this:


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



tracert exam.sanand.workers.dev

Tracing route to exam.sanand.workers.dev [104.21.31.149]
over a maximum of 30 hops:

  1     2 ms     2 ms     2 ms  192.168.18.1
  2     5 ms     6 ms     4 ms  10.122.0.1
  3     *        *        6 ms  172.17.0.2
  4     5 ms     5 ms     4 ms  172.17.0.109
  5    16 ms     8 ms     8 ms  10.8.1.2
  6    21 ms     8 ms     8 ms  103.70.37.171
  7    10 ms     8 ms     8 ms  104.21.31.149

Trace complete.



You could also 
try switching Google Public DNS
 and see if the site is getting picked up in your next query.


Helpful Resources




Ping+Tracert
 for troubleshooting network connections


Product pages
 for 
err_network_changed
 error


Network Troubleshooting
 skills and commands

---

## Post #49 by siva.bhaskaran (Post ID: 579782)
Thank you JK. I have another question. I should have asked that before this


npx -y prettier@3.4.2 README.md 
npm ERR! code E404
npm ERR! 404 Not Found - GET https://registry.npmjs.org/README.md - Not found
npm ERR! 404 
npm ERR! 404  'README.md@latest' is not in the npm registry.
npm ERR! 404 Your package name is not valid, because 
npm ERR! 404  1. name can no longer contain capital letters
npm ERR! 404
npm ERR! 404 Note that you can also install from a
npm ERR! 404 tarball, folder, http url, or git url.

npm ERR! A complete log of this run can be found in:
npm ERR!     C:\Users\sivab\AppData\Roaming\npm-cache\_logs\2025-01-14T17_22_04_622Z-debug.log
Install for [ 'README.md@latest' ] failed with code 1



This is throwing an error. Please help

---

## Post #50 by siva.bhaskaran (Post ID: 579784)
This is regarding Question 11.


I have extracted all the elements and added them manually. Tried all the options. Not even one appears to be correct . I evne tried ChatGPT which gave the answer as 411. Which of the following should be chosen?


<div class="d-none" title="This is the hidden element with the data-value attributes">
        <div class="bar baz" data-value="17">
          <div class="baz foo" data-value="29"></div>
          <div class="foo" data-value="20"></div>
        </div>
        <div class="bar foo baz" data-value="71">
          <div class="foo" data-value="48"></div>
          <span class="foo" data-value="30"></span>
          <div class="foo bar" data-value="90">
            <div class="bar" data-value="8"></div>
            <div class="" data-value="48"></div>
          </div>
        </div>
        <div class="baz foo" data-value="58">
          <div class="baz foo" data-value="19"></div>
          <div class="foo bar" data-value="76"></div>
        </div>
        <div class="bar baz" data-value="89">
          <div class="foo bar" data-value="38"></div>
          <div class="foo bar" data-value="9"></div>
        </div>
      </div>

---

## Post #51 by jkmadathil (Post ID: 579785)
siva.bhaskaran:




npx -y prettier@3.4.2 README.md






Shouldn’t it be 
npx -y prettier@3.4.2 --write README.md
 or 
npx prettier README.md
 (Depending on whether to write or read)?


Apologies, I may not know full context of the question, as I haven’t attempted GA1 fully yet

---

## Post #52 by 23f2000237 (Post ID: 579869)
I had this same doubt, I tried by adding the “span” tag’s value too it showed correct for me. I’d suggest you to try that.

---

## Post #53 by s.anand (Post ID: 579893)
Oh, good catch, 
@23f2000237
 and 
@siva.bhaskaran
 - I made a mistake in the evaluation script. It included the 
span
.


I fixed it. Note: None of the earlier answers are affected, i.e. if you got it right earlier, it’ll stay right.

---

## Post #54 by 23f1002382 (Post ID: 580021)
It’s hackable
. It’s possible to get the answer to 
some
 questions by hacking the code for this quiz. That’s allowed.




What does exactly mean, if someone could elaborate without giving it away, please?


@carlton

---

## Post #55 by daksh76 (Post ID: 580630)
I have tried but still am unable to do only that question if someone can help me with the code because everytime im getting a different answer its my last question

---

## Post #56 by daksh76 (Post ID: 580631)
@21f2000370
 i hope you wouldve completed it

---

## Post #57 by 23F3002987_J_SRI_BAL (Post ID: 580955)
Use Git bash the problem will be resolved

---

## Post #58 by Jivraj (Post ID: 581403)
Hi Daksh,


Did you solve it or still facing some issues with it ?


Kind regards

---

## Post #59 by daksh76 (Post ID: 581546)
im still facing issue in that questioneven after watching the youtube video given and taking help of chatgpt im unable to solve that question only

---

## Post #60 by 24DS1000121_ULAGAOOZ (Post ID: 581584)
Hello Gentlemen Instructors,


In all the video lectures, I am first required to download the tools, install them on my computer ? Is it not going to overload my computer’s RAM etc.,

In one of the classes, you said that there is something  - colab like cloud wherein we can go and practice without overloading our own computers. Will you please let me know how to go about it ??

Thanks and regards,

ULAGAOOZHIAN,

France

24ds1000121

---

## Post #61 by 24f1002359 (Post ID: 581612)
Screenshot 2025-01-18 154321
1317×630 30.9 KB


In question 3 of GA-1 while checking the answer  it’s showing incorrect answer.


216375D6F5A1DAF9EB6350251E9F0A7395A0B2988D58ED6E57D9568E8B1AD175


This was the output which I got after the execution of the given code in the question.Kindly guide If I did some error or error in entering the value.

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/a/4a91f864fac32edea97935f0456d5b93a5ebc4f4.png)

**Image Description:** This image shows a PowerShell terminal session.  The user is calculating the SHA256 hash of a file named `formatted.md` located in the `C:\Users\kaiff` directory using three different methods:

1. **`Get-FileHash` cmdlet:** This is a built-in PowerShell cmdlet used directly to compute the hash.  The output shows the algorithm (SHA256) and the resulting hash value. The path to the file is also shown.

2. **`npx prettier` and then `Get-FileHash`:** The user first uses `npx` to run the `prettier` code formatter on a file (likely a markdown file) located at "F:\BS DATA SCIENCE\Diploma Level\TERM 2\TDS\README.md", redirecting the output to `formatted.md`. Then, they use the `Get-FileHash` cmdlet again to calculate the SHA256 hash of the newly formatted `formatted.md` file. The output is again the SHA256 hash and the file's path.

3. **`certutil`:**  The user uses the `certutil` command-line utility (often part of Windows) to calculate the SHA256 hash of `formatted.md`. The output includes the explicit statement "SHA256 hash of formatted.md:" and the hash value, followed by a success message.

In all three cases, the SHA256 hash value for `formatted.md` is consistent, providing verification that the file's content has not changed after the formatting operation.  The image shows the commands executed and the corresponding outputs, demonstrating a simple way to verify file integrity using hashing.  The top bar shows the different panes of the PowerShell IDE.

---

## Post #63 by Divya1 (Post ID: 581723)
how to calculate How many Wednesdays are there in the date range 1981-08-30 to 2017-07-17?


The dates are in the year-month-day format. Include both the start and end date in your count. You can do this using any tool (e.g. Excel, Python, JavaScript, manually).

---

## Post #64 by huzaifa (Post ID: 581819)
=SUM(TAKE(SORTBY({3,7,13,8,7,7,11,11,13,14,0,13,9,14,10,7}, {10,9,13,2,11,8,16,14,7,15,5,4,6,1,3,12}), 1, 16))


I do not have the required excel version can someone please tell how can I find the solution to this one?

---

## Post #65 by 23f2005067 (Post ID: 581952)
@carlton
 
@Jivraj

Sir i have saved the answers 2 days ago and scored around 7.5 . now when i open the portal today it is showing as 0 and all the answers has been cleared. how can i restore it.

---

## Post #66 by 23f2003751 (Post ID: 581956)
yes same issue with me as well.2 3 days back i have answered and saved all the questions and today it is showing me 0 and all the answers are gone

---

## Post #67 by s.anand (Post ID: 581980)
@23f2005067
 
@23f2003751
 I added a “Recent saves” feature.


This will show the time and score for the last 3 times you saved. You can load from any of these.


image
368×152 5.35 KB


Do remember to click the “Check” button to calculate your score. That is not automatic.


Please check this out and let me know if there are any bugs. Thanks.

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/e/ce7bbb617fc5997babd5910bd19e8ac3f9c3fe07.png)

**Image Description:** The image shows a list of "Recent saves," each entry containing a button labeled "Reload", a timestamp, and a score.  The background has a light teal color.

Specifically:

* **Header:**  The text "Recent saves" is prominently displayed at the top.

* **Entries:** The list contains three entries, each formatted identically:
    * **Reload Button:** A blue button with the text "Reload" is present at the beginning of each entry.
    * **Timestamp:** The date and time of the save are given in DD/MM/YYYY, HH:MM:SS pm format (e.g., "19/1/2025, 8:17:25 pm").
    * **Score:** A numerical score is listed for each save (e.g., "Score: 1.25").

The dates are all in January 2025, with two saves on the 19th and one on the 14th.  The scores are 1.25, 0.25, and 0.  The "Reload" buttons presumably allow the user to load the saved data from the respective timestamps.

---

## Post #69 by 23f2005067 (Post ID: 582040)
Screenshot_2025-01-19-19-15-29-055_com.android.chrome
1080×2400 172 KB

Sir i might already clicked 3 save todays. So the previous clicks dates are of today. And the same 0 score is showing this.

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/5/954ce1ef1cc6d0d6de0f540ac0215c8b45099527_2_225x500.jpeg)

**Image Description:** The image shows a mobile phone screen displaying a quiz or assignment. 


Here's a breakdown of the content:

* **Top Bar:** Shows the time (7:15 PM), signal strength, and a "Score" field (presumably for the quiz).  The deadline for the assignment is clearly displayed: "Due Sun, 26 Jan, 2025, 11:59 pm IST".

* **Recent Saves Section:** This section lists three recent saves with timestamps (all from January 19th, 2025) and a score of 0 for each.  Each save has a "Reload" button next to it. The timestamps use the DD/MM/YYYY HH:MM:SS format.

* **Questions Section:** This is the main part, listing 17 questions with their respective point values (in marks). The questions cover a range of topics, seemingly related to programming and data handling, including:

    * Using various software tools (VS Code, uv, npx, Google Sheets, Excel, DevTools, GitHub)
    * Working with different file formats (CSV, JSON, ZIP)
    * Web development concepts (HTTP requests, CSS selectors)
    * Data manipulation and analysis (counting specific days, processing files with various encodings)
    * Basic file management tasks (moving, renaming, comparing files)


The overall appearance suggests a mobile application used for learning or assessment, potentially for a coding course or similar.  The questions' point values indicate that it is a graded assignment.

---

## Post #70 by Rohitkumar7463 (Post ID: 582261)
Sha256sum is not recognized as an internal or external command how to solve this plzz answer


@carlton

---

## Post #71 by 23f2003845 (Post ID: 582210)
If you are on windows, you might not be able to use sha256sum.


Here are two disussions that might help you out.




Discussion 1


Discussion 2

---

## Post #72 by carlton (Post ID: 582264)
@Rohitkumar7463
 
@23f2003845


If you are on Windows Powershell

Then instead of 
sha256sum
 you can simply use 
Get-FileHash


Send the output of the 
npx -y prettier@3.4.2 README.md
 to a text file eg. 
output.txt
 and then use 
Get-FileHash
 on powershell with the 
output.txt
 and it will use sha256 by default and give you the exact same output.

You might be able to pipe the data directly to 
Get-FileHash
 but I have not tried direct piping. The above method works guaranteed.


Kind regards

---

## Post #73 by iamsarthak (Post ID: 582366)
@s.anand
 Sir


as you said in the previous post, the evaluation script is also updated based on errors other students point out.


I am submitting my answers as soon as the GA is released and stopping once I get 10/10.


Will you reevaluate the answers once the deadline is over? Or the marks I see right now will be set in stone?


If you will, then it will be based on the updated evaluation script which can reduce my marks.


image
742×336 21.3 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/1/b14fdd8db7fa7f4f811065f54b5b478db50f61ac.png)

**Image Description:** Here's a description of the image's content:

The image shows a screen capture, likely from a software application or website that tracks saves and scores.  

The top section displays a green banner with the following information:

* **Date and Time:** "6 Jan 2025 at 11:59 PM IST"  (indicating a date, time, and time zone – likely Indian Standard Time).
* **Score:** "Score: 10 / 10" suggesting a perfect score.


Below the banner, a light-green section shows the user's "Recent saves".  This section lists at least one save:

* **"Reload" button:** A button labeled "Reload" is present.
* **Save details:** "from 20/1/2025, 6:05:24 PM. Score: 10" indicates a previous save's date, time, and score (again, a perfect 10). There is space below this entry suggesting further entries in the saves list.

Overall, the image implies a system where users can save their work, track their scores, and reload previously saved items.  The dates suggest this is a future date, and could be part of a planning or testing environment.

---

## Post #74 by s.anand (Post ID: 582375)
@iamsarthak
 – as long as you don’t save again, your score will stay 10, even if I modify the evaluation script  


We don’t re-evaluate previous results in the graded assignments.

---

## Post #75 by 23f2000573 (Post ID: 582382)
@s.anand
 sir,


Question 15 is under the section for linux


I got the file which needs to be processed to answer the question


image
583×167 4.09 KB


I can solve this now using pandas.


From learning perspective, is this question aimed at making students to use something like awk or is it fine if i can carry on with pandas?

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/5/154ddd789fc2694e567f62d6d84d71a87a863af4.png)

**Image Description:** The image shows a table-like structure with four columns, likely representing file information.  The columns are labeled "Length," "Date," "Time," and "Name."  Each row contains information for a different file.

Here's a breakdown of each column:

* **Length:** This column displays a numerical value representing the size of each file, likely in bytes.

* **Date:** This column shows the date each file was created or last modified, formatted as YYYY-MM-DD.

* **Time:** This column provides the time each file was created or last modified, formatted as HH:MM (24-hour clock).

* **Name:** This column displays the filename, which in this example, are all text files ("*.txt").

The data suggests a list of four text files with their respective sizes, creation/modification dates, and times.  The file sizes vary significantly, from 4094 to 9748 bytes. The dates span from 2000 to 2010.

---

## Post #76 by s.anand (Post ID: 582391)
@23f2000573
 You can solve it with any tool you’re comfortable with, including pandas.


But since you 
already
 know how to do it with pandas, I suggest you explore how to do it with something like 
awk
 (or any other tool) to get a broader exposure into different approaches.

---

## Post #77 by Rohitkumar7463 (Post ID: 582427)
20250120_203950
1920×1440 168 KB

Sir is it right of sha sum question

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/5/259fe82da0a001abf9302adbc16f3ceb4e1a1d1c_2_666x500.jpeg)

**Image Description:** The image shows a screenshot of a Windows PowerShell console.  The console displays a series of commands and their output.

Here's a breakdown of the relevant content:

* **Top Line:**  The top line indicates the user is trying the new cross-platform PowerShell and provides a URL: `https://aka.ms/pscore6`.

* **Directory Issues:** The console initially attempts to change directories (`cd`) to `C:\Users\HP\downloads\Downloads`, but receives an error because the directory `Downloads` doesn't exist within the `downloads` directory.

* **Command Execution:** The user then executes the following commands:

    * `npx -y prettier@3.4.2 README.md > output.txt`: This command likely uses `npm` (Node Package Manager) to install and run a code formatter (`prettier`) on a file named `README.md` and redirects the output to a file named `output.txt`.

    * `Get-FileHash .\output.txt`: This PowerShell command calculates the SHA256 hash of the `output.txt` file.

* **Hash Output:** The output of the `Get-FileHash` command is displayed, showing the SHA256 algorithm and the resulting hash value: `7EA1921069EAA2FDA9F6B5143A291C894CDC59E6CF6DBAA9EC8FFD4449A8F7E5`.  The path `C:\Users\HP` is shown as the location of the file. This hash is repeated further down, likely a repetition of the command.

* **Overall:** The image demonstrates a user attempting to work with files in the `downloads` directory, encountering an initial directory error, and subsequently generating a file and its SHA256 hash value for verification or integrity purposes.

---

## Post #78 by Divya1 (Post ID: 582480)
to pass the graded 1 how much points are required for 10 ?

---

## Post #79 by 23f1002382 (Post ID: 582510)
use chatgpt for the solution(sum(take(sortby))), it will give you the wrong answer but explain the concepts, use that go to colab and code one solution(will take abt 2 mins)

---

## Post #80 by 23f2000573 (Post ID: 582511)
I used


https://www.microsoft365.com/launch/excel?auth=1

---

## Post #81 by carlton (Post ID: 582562)
@Rohitkumar7463
 The hash code is exactly what you see under the column Hash,


7E…E5


Thats the Hash code for the file output.txt


A Hash is a 
nearly
 unique representation of some data within some range dependent on the type of hashing algorithm and the amount of unique pieces of data that need to be encoded. (just my colloquial definition of it, i am sure you are able to ask GPT to give you a much better explanation)


Kind regards

---

## Post #82 by 22f1000535 (Post ID: 582689)
Time Zone Issues with the “List Files and Attributes” Question


quick heads‐up about Question 15 (the one asking for files at least 8143 bytes, modified on or after Sun, 19 Nov 2006, 7:38 am GMT‑5). I’m physically in a different time zone, but I eventually discovered the question seems to expect you to be located in India and to interpret that files date/time accordingly.

I got the correct answer once i localized the files timestamp to IST.


thanks

---

## Post #83 by gokulvasudevan.s (Post ID: 582989)
GA1 Q18. What is the total sales of all the items in the “Gold” ticket type? Write SQL to calculate it.


I always get the answer in a nested array. Error: Got [[51006.69]]…

I could not use cursor in that shell, to extract the value also.


@carlton
 
@Jivraj
 Please help me with this.

---

## Post #84 by 24f1001769 (Post ID: 582996)
image
1327×464 18.1 KB

I am getting error in the uv question.

I have got the output json but I cant understand what part do I need to submit in the answer section.

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/6/569cac03bc51f8ce553a5e554619379466e0aeae.png)

**Image Description:** The image contains a JSON-formatted string, likely representing a HTTP request.  Let's break down the key parts:

* **`args`:** This section contains the request's arguments.  Crucially, it includes:
    * **`"email"`:**  "241001769@ds.study.iitm.ac.in" - This is an email address, likely the main piece of data being sent in the request.  It suggests a connection to an institution (possibly the Indian Institute of Technology Madras, judging by the ".iitm.ac.in" domain).

* **`headers`:**  This section specifies the HTTP headers of the request. These headers provide information about the client making the request and the type of content it expects.  Key headers include:
    * **`"Accept"`:** Specifies the acceptable content types.  It shows support for various formats like HTML, XML, and image types (avif, webp, apng).
    * **`"Accept-Encoding"`:** Indicates the compression methods the client supports (gzip, deflate, br, zstd).
    * **`"Accept-Language"`:** Shows the preferred languages: English (US and a general English variant).
    * **`"User-Agent"`:**  This is extremely important. It reveals the browser and operating system used to send the request: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0".  This string clearly indicates the request originated from a Windows 10 machine using Google Chrome (version 132) and Microsoft Edge (also version 132).
    * **`"Sec-Ch-Ua"`**, **`"Sec-Ch-Ua-Mobile"`**, **`"Sec-Ch-Ua-Platform"`**: These headers provide information about the browser and platform.

* **`origin`:**  "45.118.156.154" - This is an IP address from where the request was sent.

* **`url`:** "https://httpbin.org/get?email=241001769%40ds.study.iitm.ac.in" - This is the complete URL of the request, confirming that the email address is being sent as a query parameter to the `httpbin.org/get` endpoint.  `httpbin.org` is a website often used for testing HTTP requests.


In summary, this JSON represents a GET request from a Windows 10 machine using Chrome and Edge, likely from within the Indian Institute of Technology Madras network, sending an email address to a testing service (`httpbin.org`).  The email address is likely the most important piece of information.

---

## Post #85 by 23f3002537 (Post ID: 583634)
image
1641×356 26.7 KB

Sir I’m facing issue in this question even though i have done every thing as it mentioned. Can I get hint of the mistake for my code snippet.

My code: -


mkdir all_files
find parent/ -type f -exec mv {} all_files/ \;
for file in all_files/*; do
    new_name=$(echo "$file" | sed 's/[0-9]/\n&\n/g' | awk '
    { 
        if ($0 ~ /^[0-9]$/) print ($0 == "9") ? 0 : $0+1; 
        else print $0 
    }' | tr -d "\n")
    mv "$file" "$new_name"
done

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/1/01b4483a493dface204efbc60ad43d487c00ccae_2_690x149.png)

**Image Description:** This image shows a computer science or programming exercise.  The task is to:

1. **Download a zip file:** The user needs to download a file named `q-move-rename-files.zip`.

2. **Extract and Move Files:**  The downloaded zip file needs to be extracted. Then, the `mv` command should be used to move all files from subfolders into a single, empty folder.

3. **Rename Files:** All files within the folder must be renamed.  The renaming rule is to increment each digit; 1 becomes 2, 2 becomes 3, and 9 becomes 0.  An example is provided: `a1b9c.txt` becomes `a2b0c.txt`.

4. **Execute a Bash Command:** The user needs to run the command `grep . | LC_ALL=C sort | sha256sum` in the folder containing the renamed files and enter the output.

The user has attempted this and provided an answer (`f1056c0b734ac835d17e8129fe9dc9a85ebcca45a82de42b13d18b7816808b7d*`), but it's marked as incorrect.  The asterisk at the end of the answer might indicate that there's a trailing character issue. The output of the command is a SHA256 hash sum of the sorted filenames.

---

## Post #86 by Sudhishnarayan (Post ID: 583746)
Good Evening, I have a doubt regarding the SQL Question I have attached my query. Please clarify me where I got wrong. I tried changing the gold string to lower and checking it. Even,  that didn’t work.


Screenshot 2025-01-22 231718
1599×362 19.1 KB

Thank You.

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/e/bef378c05a79402b232e3f9a7741394ea99462d0_2_690x156.png)

**Image Description:** The image shows a coding problem and its attempted solution.  The problem asks for an SQL query to calculate the total sales of items with the "Gold" ticket type.

The image contains:

* **A problem statement:**  "What is the total sales of all the items in the 'Gold' ticket type? Write SQL to calculate it." This clearly defines the task.

* **An attempted SQL query:** `SELECT SUM(Units*Price) FROM tickets WHERE TYPE == 'Gold';` This is an attempt at solving the problem, but it contains an error.  Note the multiplication operator `*` between Units and Price which is correct.

* **An error message:** "Error: Got [[42810.5]].."  This indicates the SQL query executed but returned an error.  The number 42810.5 is likely the result it was attempting to return, but that the query structure was not quite right for the data structure.

* **Further instructions:** "Get all rows where the Type is 'Gold'. Ignore spaces and treat mis-spellings like GOLD, gold, etc. as 'Gold'. Calculate the sales as Units * Price, and sum them up." This gives additional details on how to handle variations in the 'Type' column (case-insensitivity and extra spaces) and how to compute sales.

The core issue seems to be that the initial SQL query, while conceptually correct, might have a syntax problem or be incompatible with the underlying database schema (the `tickets` table).  The supplementary instructions highlight the need for robust handling of variations in the data.

---

## Post #87 by Sudhishnarayan (Post ID: 583765)
I have another doubt regarding the CSS Selector question. I know how to select elements using CSS Selector but i don’t know how to get the sum using CSS Selectors as it cannot perform arithmetic operations. And also, I didn’t understand the question completely about the ‘hidden element’. Please clarify it. Thank you so much.


Screenshot 2025-01-22 232338
1621×255 13.9 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/4/3488d91f7599c325bc0dfe148df9e5dd37df0908_2_690x108.png)

**Image Description:** The image shows a code challenge or quiz question.  The instructions ask the user to use CSS selectors to find all `<div>` elements with the class "foo" within a hidden HTML element (not shown in the image).  The goal is to calculate the sum of the `data-value` attributes of those found `<div>` elements and enter the sum into the provided text input field.  The image shows that an incorrect answer has been submitted, as indicated by the "Incorrect. Try again." message.  The text input field itself is empty, indicating the user's attempt at a solution was wrong.

---

## Post #88 by Yogesh1 (Post ID: 583848)
It can be GOLD,gold, or even GoLD.


"  Get all rows where the Type is “Gold”. Ignore spaces and treat mis-spellings like GOLD, gold, etc. as “Gold”. Calculate the sales as Units * Price, and sum them up.  "

---

## Post #89 by 23f3002537 (Post ID: 583940)
Try to go through the given video of css selector and go through all foo classes carefully(using inspect) and sum them up!

---

## Post #90 by 23f3002537 (Post ID: 583941)
Try to remove the White spaces in your code!

---

## Post #92 by 22f2001175 (Post ID: 584306)
@carlton
 
@Jivraj

sir i have gone through the process of solving the ques but still ans is showing wrong even i have used chatgpt and used cmd also. the cmd is is showing the result still ans is wrong


Untitled design
1414×2000 349 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/1/51e466de36ab81daac1abc2ff6f89471b3c5bf91_2_353x500.png)

**Image Description:** The image contains a split screen. The top half shows a large amount of text in a monospace font, typical of a computer terminal or code editor. The text appears to be a log or output of a command, possibly listing files and directories with their associated metadata (sizes, timestamps, and possibly permissions).  There are repeated lines which suggest a loop or iterative process is happening.


The bottom half displays a light-grey rectangular box, likely a user interface element from a web application or online learning platform. The text within the box is structured as follows:

* **Top Line:**  A title or instruction: "List files and attributes (375 marks)"  and a small download icon is also present.  A file name `list_files_attributes.zip` is highlighted, indicating a downloadable file relevant to the task.

* **Second Line:** An instruction explaining the task: "Download `list_files_attributes.zip` and extract it. Use `l` with options to list all files in the folder along with their date and file size". This indicates a programming exercise involving file listing and manipulation.

* **Third Line:** A question presented to the user: "What's the total size of all files at least 1275 bytes large and modified on or after Wed, 6 Nov, 2019, 10:48 am (GMT)". There's a text input field where a numerical answer should be provided ( `907142` is shown as an example).

* **Fourth Line:** A "Try again" button or link, suggesting the user can submit their answer and receive feedback.

* **Fifth Line:** A warning or instruction: "Don't unzip from inside the ZIP file or use Windows Explorer to unzip. That destroys the timestamps. Extract using `7zip`, `unzip`, or similar utilities and check the timestamps." This warns against using certain methods for unzipping the file, as it will affect the result.


In summary, the image presents a programming assignment or quiz that tests the ability to list and analyze files using a command-line tool (possibly a shell or script based on the top half's output), highlighting the importance of correct file handling and attention to detail (timestamps). The provided answer in the input field suggests the assignment has already been attempted.

---

## Post #94 by 23f1001754 (Post ID: 584470)
In GA1, Question no: 9.

when i sort the json it says incorrect. but i validated that json using validator and also manually


admin : could you pls validate my answer pls

---

## Post #95 by Jivraj (Post ID: 584693)
You need to submit whole json becausae In this image 
headers
 is part of response, not request headers.

---

## Post #96 by Jivraj (Post ID: 584707)
Hi Arnav,


I tried your script on your dataset.

Problem might be you are not executing 
grep . * | LC_ALL=C sort | sha256sum
 in correct directory, you would need to execute it from 
all_files
 directory also there should not be any extra file other than that gets generated.

---

## Post #97 by Jivraj (Post ID: 584709)
22f2001175:




Untitled design
1414×2000 349 KB


Untitled design1414×2000 349 KB






Time of modification of each of these files is 14 Jan 2025 which might be the day you unzipped them. Depending upon what software you use it might change modification date while unzipping. use unzip command line tool or winrar extractor, these are 2 tools we have tested.


kind regards

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/1/51e466de36ab81daac1abc2ff6f89471b3c5bf91_2_353x500.png)

**Image Description:** Here's a description of the image content:

The image shows a computer screen displaying a coding exercise or assignment.  The screen is primarily divided into two sections:

**Top Section:** This section displays a large block of text in a dark-colored terminal or command-line interface. The text is primarily white or light-colored and appears to be the output of a command, likely listing files and their attributes. The file names contain variations of "file.txt," suggesting a potential file structure for testing.  The code also contains parts that seem to be extracting file information such as size, date, etc.  It’s likely written in a scripting language like Python due to some visible syntax.

**Bottom Section:** This section contains a light-colored rectangular box, probably from a web interface or application.  It presents a programming problem or task.  The text within this box is as follows:

* **Heading:** `List files and attributes (37.5 marks)`
* **Instruction 1:** `Download  ` followed by a link or file name (partially visible: `list_files_attributes.zip`)  ` and extract it. Use ` ` with options to list all files in the folder along with their date and the file size.`
* **Instruction 2:**  `What's the total size of all files at least 1275 bytes large and modified on or after Wed, 6 Nov, 2019, 10:48 am (GMT)?`  This is followed by an input box where a numerical answer should be entered. A value of `907162` is already present.
* **Instruction 3:** `Don't `unzip` from inside the ZIP file or use Windows Explorer to unzip. That destroys the timestamps. Extract using `7zip`, `unzip`, or similar utilities and check the timestamps.`


In essence, the image shows a student or programmer working on a problem that requires them to use a command-line tool (possibly a script they downloaded) to list, filter, and calculate the total size of files based on their size and modification date. The provided answer in the input box suggests that the problem has been attempted and the student believes the answer is 907162 bytes.

---

## Post #98 by Jivraj (Post ID: 584719)
Hi Saravanan,


I noticed an issue with your submission. In the question, there is a name 
Bob
, but it doesn’t appear in your answer after applying the required sorting. Since the data for each student is dynamically generated and unique, the answer you submitted seems inconsistent with your dataset.


We encourage collaboration among students, but copying answers is not acceptable. Instead, I suggest reaching out to your friend to understand the script they used, run it on your dataset, and ensure you fully grasp the solution.


kind regards

---

## Post #99 by 23f1001754 (Post ID: 584730)
Thanks lot jivraj. i updated my script and answers too


Thanks

---

## Post #100 by Sakshi6479 (Post ID: 584732)
Screenshot 2025-01-24 184222
2677×1066 294 KB

In the question 10 what should be the correct format for jason data as I edited the data according to given conditions but in Hash I am facing problem again and again


Also, in Q11 What is meaning of element below given in the question " Let’s make sure you know how to select elements using CSS selectors. Find all 
<div>
 s having a 
foo
 class in the hidden element below. What’s the sum of their 
data-value
 attributes?"

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/7/3738985d0d94f735a4c51462d37072bed8a7a1c9_2_690x274.png)

**Image Description:** The image shows a screenshot of a code editor or similar tool displaying a JSON parsing error.

**Key elements:**

* **Title:** The text "JSON Hash" at the top indicates that the purpose is to generate a hash from JSON data.

* **Data Input:** A large text box contains a long string of seemingly random alphanumeric characters. This string is the input data intended for JSON parsing and likely represents a JSON object, though it's malformed.  The data is presented in key-value pairs separated by colons, with commas separating the pairs. The entire string appears to be a single line, causing the error.

* **"Hash" Button:** A button labeled "Hash" suggests that there's functionality to calculate a hash value from the input data once it's correctly formatted.

* **Error Message:** A prominent red banner displays the error message: "Error: Expected property name or ')' in JSON at position 1 (line 1 column 2)". This signifies a syntax error in the JSON input, specifically at the very beginning of the string.  It suggests that the input lacks proper JSON formatting, such as missing curly braces `{}` to define an object or square brackets `[]` to define an array.  The error indicates the problem is in the first character of the first line.

* **Data Collapse:** The input data text box has scrollbars, implying that the entire input data may not be visible in the screenshot and there is more data than shown.

In summary, the image depicts an attempt to hash JSON data that has a syntax error preventing successful parsing.  The error message clearly indicates the location and nature of the problem, and the overall context suggests a tool designed for JSON hashing.

---

## Post #101 by 25ds1000038 (Post ID: 584798)
image
1590×466 29.3 KB

what sort of response am i supposed to put ?? the response i am getting ,it says incorrect, basically  after doing code -s ,i get like info about the version of vs code and info about cpu gpu etc…

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/e/fe3d66c57d75b16c2ea6f06dd66adbdfe8eb9466_2_690x202.png)

**Image Description:** This image shows a screen capture of a coding challenge or tutorial.  The top section introduces AI code editors like Cursor, Cody, and GitHub Copilot, stating that they're built on top of VS Code and are now standard developer tools.

The core of the image is an instruction followed by a text input field:

* **Instruction:**  The user is instructed to install and run Visual Studio Code, then in the terminal type `code -s` and press Enter. They are then asked to copy and paste the entire output into the text box provided.  The `code -s` command is highlighted in the instruction, suggesting it is a command the user needs to execute.


* **Text Input Field:** A large empty text box is where the user should paste the output of the `code -s` command.  A small red circle with an "i" inside, indicating an error or informational message is next to the text box.


* **Feedback:** Below the text box, the message "Incorrect. Try again." confirms that the user's previous attempt(s) to provide the correct output were unsuccessful.

In summary, the image shows a step in a coding lesson or exercise that requires the user to execute a specific command and then provide the console output. The provided response was deemed incorrect.

---

## Post #102 by 23f2002592 (Post ID: 584906)
Screenshot 2025-01-25 171014
1631×309 22.2 KB


The answer is wrong but I have done every step correctly. Help

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/6/1660ff1343e3f3b9fb21bb962f6be949238c62f5_2_690x130.png)

**Image Description:** The image shows a code challenge or exercise within a dark-themed interface.  The instructions are:

1. **Download:** Download the file `q-replace-across-files.zip`.
2. **Unzip:** Unzip the downloaded file into a new folder.
3. **Replace:** Replace all instances of "IITM" (regardless of case) with "IIT Madras" in all files within that folder.  Crucially, the instructions emphasize *not* changing line endings.
4. **Verify:** Use the command `cat * | sha256sum` in the bash shell within that folder.  The output of this command is the SHA256 checksum of the concatenated contents of all the files in the directory.  The user is expected to enter this checksum as the answer.

The user's answer (`63144b28ad1d2bd5b9b4b0855cab6a4a4fa8d57ed2ed826b4f5b36d12ae97347`) is marked as incorrect. The interface provides feedback indicating the need to try again.

---

## Post #104 by 23f2000098 (Post ID: 585183)
image
1613×702 193 KB

Not sure how to resolve this error… any sugessions ?

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/6/d64710c6f1d82d385c603313620a99ddcc9dfef0_2_690x300.jpeg)

**Image Description:** Here's a description of the image content:

The image shows a split screen. The top half displays a vibrant promotional image or screenshot for a Python package/project manager, possibly named "uv". The image features a person (likely a presenter or developer) gesturing towards text on a screen that says "package/project manager" and "uv". The color scheme is purple, pink, and white, with a Python logo visible.  The bottom half contains a coding problem and its solution (or attempted solution).

The text in the bottom half provides details of a coding challenge:

* **Instructions:** The user is asked to send an HTTPS request to a specific URL (`https://httpbin.org/get`) with a URL-encoded email parameter.  The challenge emphasizes only submitting the JSON body of the response, excluding headers.  The provided command using `uv run --with httple` is meant to install the `httpie` package and execute the request.

* **Attempted Solution:**  A JSON response is partially provided. However, a `SyntaxError` indicating an error in the JSON structure is also displayed. The error message points to an issue on the first line, second column of the JSON.


In short, the image depicts a programming tutorial or assignment focusing on using a Python package to send HTTP requests and handle JSON responses. The visual element at the top serves as branding or context for the programming challenge in the bottom half. The error message implies that the user's JSON output is not correctly formatted.

---

## Post #105 by 23f2001188 (Post ID: 585200)
first convert in into jason using bash or other terminal then paste the converted json content to this page and generate the json hash

---

## Post #106 by 23f2000098 (Post ID: 585208)
I am getting errors for the host part please guide me

---

## Post #107 by Sakshi6479 (Post ID: 585216)
But I have converted the file as it says in the question still i am getting error that I am unable to understand. Can you just tell me please what formatted answer should be that is just the type of answer it’s asking?

---

## Post #108 by sarvan108 (Post ID: 585248)
I tried this. For me still the answer is incorrect.


image
1677×358 22.2 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/a/2add60640ef2f000fddb670ed7f9dd132e195b81.png)

**Image Description:** This image shows a command-line interface (CLI) session, likely from Windows PowerShell or a similar shell.  The session demonstrates the process of generating and verifying a SHA256 hash of a file named `README.md`.

Here's a breakdown of the content:

* **Commands Executed:** The image shows a series of commands executed in the `C:\Users\sarva\downloads` directory.

    * `cd downloads`: Changes the current directory to the "downloads" folder.
    * `certutil -hashfile C:\Users\sarva\downloads\README.md SHA256`: This command uses the `certutil` utility to calculate the SHA256 hash of the `README.md` file. The resulting hash is displayed.
    * `npx -y prettier@3.4.2 README.md > output.txt`: This command uses `npx` (a Node.js package runner) to run the `prettier` code formatter (version 3.4.2) on `README.md` and redirects the output to a file named `output.txt`.  This is likely unrelated to the hashing process itself but shows additional file manipulation.
    * `Get-FileHash -Algorithm SHA256 output.txt`: This command (appears to be a PowerShell cmdlet) calculates the SHA256 hash of the `output.txt` file.

* **Hash Values:** The output shows two SHA256 hash values:

    * One generated by `certutil` for the `README.md` file: `eef23369e30d7bd99173ef4988c65a59b80bf56f60da4c9ab95c1903be312317`
    * One generated by `Get-FileHash` for the `output.txt` file: `CECFD0A2DC971DE14A28CABF98ED854A9E6C7A94BD788AB0D10F5D991A4FA054`

* **Summary Table:** At the bottom, a simple table summarizes the algorithm (SHA256), the hash for `output.txt`, and the path to that file.

**In essence, the image documents a procedure to:**

1. Generate a SHA256 hash of a file (`README.md`).
2. Process that file with a formatter (`prettier`).
3. Generate a SHA256 hash of the processed file (`output.txt`).

The purpose might be to verify the integrity of `README.md` before and after formatting.  The difference in the two hashes shows that the formatting process changed the file's content.

---

## Post #109 by sarvan108 (Post ID: 585249)
Finally. Got the correct one in bit dash.

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/c/0c8befb5185c68f63c51334b862b93b39fb13b58.png)

**Image Description:** The image shows a terminal window displaying a command and its output.  Let's break down the components:

* **Username and Machine:** `sarva@SURIYA MINGW64` indicates the username is "sarva", the machine name is "SURIYA", and the operating system is a Windows-based system using the Minimalist GNU for Windows (MinGW64) environment.

* **Directory:** `~/downloads` shows the current working directory is the user's downloads folder.

* **Command:** `$ npx -y prettier@3.4.2 README.md | sha256sum` is the command executed.  This command uses `npx` to install and run `prettier` version 3.4.2 to format a file named `README.md`.  The output of `prettier` is then piped (`|`) to `sha256sum`, which calculates the SHA-256 checksum of the formatted file.

* **Output:** `2ccd877ded5f031c251d3319bc1b266018635156db88e63105943dbef7e106a1 *-` is the SHA-256 checksum generated by `sha256sum`. The `*-` at the end suggests that there may be additional output truncated from the image or that the process did not yet complete.


In summary, the image depicts the verification of a formatted `README.md` file using a SHA-256 checksum after formatting it with `prettier`.  The checksum provides a way to ensure the integrity of the file hasn't changed.

---

## Post #110 by sarvan108 (Post ID: 585252)
I ran this directly in the console and got the correct answer.


// Select all 
 and 
 elements with the ‘foo’ class

const fooElements = document.querySelectorAll(“div.foo, span.foo”);


// Initialize a variable to store the sum

let sum = 0;


// Iterate through the selected elements

fooElements.forEach(element => {

// Get the ‘data-value’ attribute and convert it to a number

const value = parseFloat(element.getAttribute(“data-value”));


// Add the value to the sum

if (!isNaN(value)) {

sum += value;

}

});


console.log(“Sum of data-value attributes:”, sum);

---

## Post #112 by 24f1001769 (Post ID: 585506)
@Jivraj
 Sir I have tried pasting the entire json but I am still getting incoorect answer

---

## Post #113 by 23f2001188 (Post ID: 585530)
6630ecbfc252fa2bd39d26737fc1d4e1d22574c8792112b28cdf4ff128d4c605

---

## Post #114 by 23f2001188 (Post ID: 585575)
image
846×347 28.4 KB

help me with this

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/b/bb3290cba8963cf5a776b6e8a2e1cd1e13d6f1a3.png)

**Image Description:** The image shows a computer screen displaying a problem and a user's incorrect answer.  The problem involves a zipped file, `q-list-files-attributes.zip`. The instructions state to download this file, extract it (using a program like `unzip` or `7-Zip`, not Windows Explorer), and then use the `ls` command (likely in a Linux or Unix-like environment) with appropriate options to list all files.

The question asks for the total size of all files that meet two criteria:
1.  File size is at least 2404 bytes.
2.  The files were modified on or after Monday, March 18th, 2002, at 1:02 AM IST (Indian Standard Time).

The user answered "485969", which is marked incorrect.  A warning message is displayed, emphasizing that extracting the zip file using Windows Explorer will destroy the timestamps needed to answer the question correctly.  The correct method is to use command line utilities like `unzip` or `7-Zip`.

---

## Post #115 by 23f2003921 (Post ID: 585991)
Q18 GA1


I don’t get what’s wrong with this:


image
1269×561 42 KB


Can anyone help me understand? Thanks

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/2/62881746149d177049834111811ad5e0e0c1ffae_2_690x305.png)

**Image Description:** This image shows a problem and its solution related to SQL queries and database manipulation.  Here's a breakdown of the content:

**1. Problem Setup:**

* **Table Description:** The top section describes a SQLite database table named "tickets". This table has three columns:  `type` (representing ticket type), `units` (number of units purchased), and `price` (price per unit).  Each row represents a customer's bid for a concert ticket.
* **Sample Data:** A table displays sample data from the `tickets` table, showing various ticket types (Silver, gold, BRONZE), corresponding units, and prices.

**2. Problem Statement:**

* The question asks for the total sales of all "Gold" tickets.  The instruction is to write an SQL query to calculate this.

**3. Attempted Solution and Error:**

* An SQL query is presented:  `select sum(units*price) from tickets where type='gold' collate nocase;`
    * This query attempts to sum the product of `units` and `price` for rows where the `type` column is 'gold', using `collate nocase` to perform a case-insensitive comparison.
* An error message is displayed: `Error: Got [[124944.59]]...` This suggests the query ran, but there might be an issue with the result's format or interpretation.

**4. Clarified Problem and Hints:**

* Below the error, the problem is restated more explicitly. It emphasizes ignoring extra spaces in the 'type' column and handling various spellings of "Gold" (e.g., GOLD, gold) as equivalent to "Gold" during the calculation.


**Key Features for Answering the Question:**

* The sample data in the table is crucial for verifying the correctness of any SQL query.
* The error message indicates the query produced a numerical result (around 124944.59), though it was apparently flagged as an error.
* The clarified problem statement points to potential issues with case sensitivity and whitespace handling in the original query.  A correct solution would need to address these.


In short, the image presents a database problem involving calculating a sum based on certain conditions and shows an attempt at solving it with SQL, along with an error that needs further debugging.  The provided hints aim at generating a more robust and accurate SQL query that accounts for variations in the 'type' column's values.

---

## Post #116 by 23f2000098 (Post ID: 586432)
image
1199×236 8.5 KB

i dont know what is the error is plss guide me

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/f/af0b396ddcc078c59f6929d66745080d531c0adc.png)

**Image Description:** This image shows a text-based tutorial or quiz related to using the `npx` and `prettier` command-line tools.  The instructions describe a process:

1. **Download a file:** Download a file named `README.md`.
2. **Verify filename:** Ensure the downloaded file is actually called `README.md`.
3. **Run a command:** Execute the command `npx -y prettier@3.4.2 README.md | sha256sum`. This command uses `npx` to run a specific version of `prettier` (3.4.2) on the `README.md` file and pipes the output to the `sha256sum` command to generate a SHA256 hash.
4. **Identify output:** A question asks for the output of the command, specifically the SHA256 hash.

The answer, displayed in a box, is the SHA256 hash: `AC06784D6825497650083DDFD6746A2CDD561B6A1FF45241C6A354035244A75C`.  There is a small warning symbol (①) next to the answer box, possibly indicating some form of validation or feedback mechanism.  The words `npx` and `prettier` are highlighted in pink, likely to emphasize their importance in the instructions.  A button-like element labeled `README.md` might be a clickable download link in the original source.

---

## Post #117 by Nomad (Post ID: 586473)
I have attempted the quiz, but missed marking this question - I have seen the Graded Assignment 1 available at 
this link
 and have attempted it. Hope the scores saved would be considered

---

## Post #118 by 21f3000745 (Post ID: 586528)
image
1635×317 28 KB

i am not getting why my answer is showing incorrect.

can you help me in this ? 
@Saransh_Saini
 
@Jivraj

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/6/e60748f8290e5bf6a7fedca9e4555355e48947f6_2_690x133.png)

**Image Description:** This image shows a coding question and answer interface.  The question is worth 0.5 marks and asks the user to perform the following steps:

1. **Download a file:** Download a file named `q-multi-cursor-json.txt`.
2. **Edit the file:** Use "multi-cursors" to edit the downloaded file and convert its key-value pairs into a single JSON object in the format `{key: value, key: value, ...}`.
3. **Hash the JSON:** Paste the resulting JSON into the website `tools-in-data-science.pages.dev/jsonhash` and click the "Hash" button.
4. **Provide the hash:** Enter the resulting hash value into the provided text box.


The user has attempted to answer with `c0b9426a7f358720f193d3806497ec0d81d10d835085d0f284f804bf3a6a1536`, but the system indicates this is incorrect.  A small information icon is displayed next to the answer box, suggesting there might be further information available upon clicking.  The overall context suggests this is an online learning or assessment platform.

---

## Post #119 by Saransh_Saini (Post ID: 584795)
Check the structure of your json object. It should be {key1: value1, key2: value2}. Also make sure you enclose the keys and values in double-quotes, and after every key-value pair put a comma.

---

## Post #120 by 21f3000745 (Post ID: 585081)
i am doing so only … i can send u the example -

{   “0”: “wEfsmtde”,

“83”: “NghqzO3DL”,

“NqN7EcM”: “I”,

“vFD2C”: “KAB”}

i am not able to find what’s the mistake

---

## Post #121 by Saransh_Saini (Post ID: 585113)
Your format seems to be correct, but cause you are still facing that problem then these are the few reasons I can think of




Check the entire JSON object and make sure that each and every element follows this format.


Use Chrome for getting that hash code, it could be the case that some other browser may not be pasting the object as intended.

---

## Post #122 by 21f3000745 (Post ID: 585132)
Okay, i will go through my json object once.

And for hash code i am using chrome only

---

## Post #123 by 21f3000745 (Post ID: 585414)
It worked.

Thank you

---

## Post #124 by Divya1 (Post ID: 586795)
After passing the deadline , my scores aren’t there …Is it same for all?


image
1359×878 78.5 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/3/a3e1cb26a8cb2f09ad3defcbce281bdf06a6438b_2_690x445.png)

**Image Description:** The image shows instructions for a quiz titled "TDS 2025 Jan GA1 - Development To".  The instructions are numbered and include the following key points:

* **Learning Material:**  Reading material is provided, but skipping it is acceptable.
* **Checking Answers:** Answers can be checked multiple times using a "Check" button.
* **Saving Answers:** Answers are saved regularly using a "Save" button; the last saved submission is evaluated.  Saving is done in the browser, not on a server.  Reloading the page is fine.
* **Browser Issues:**  If the browser struggles to load, it's suggested to disable security restrictions or try a different browser.
* **Resource Usage:**  Any resources, including the internet, ChatGPT, and friends, are permitted.  Libraries and frameworks are also allowed.
* **Hacking:**  Hacking the code to get answers is explicitly allowed.

The instructions also include a section titled "Should you take TDS this term?", offering two informal guidelines:

* Completing the assignment in under 2 hours suggests success in the TDS course.
* Scoring above 8/10 suggests the possibility of an S or A grade.

The top of the image displays the quiz's end time: "Ended at Sun, 26 Jan, 2025, 11:59 pm IST".  The words "Check" and "Save" are highlighted in the instructions, likely indicating clickable buttons within the quiz interface.

---

## Post #125 by 23f3004114 (Post ID: 586819)
wow, thats so true…

---

## Post #126 by carlton (Post ID: 587077)
3 posts were merged into an existing topic: 
Graded assignment 1 - Submission not shown

---

## Post #127 by 22f3001740 (Post ID: 587385)
image
552×414 18 KB


Hi Sir,


I completed the GA 1 before the time and saved it as mentioned above, but forgot to give “submit”  button on iit bs week 1 graded assignment portal.


Will it might be a problem ?


I

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/6/1621b44baa27eac7754e1d0f48bf5f8de30f133d.png)

**Image Description:** The image shows a computer screen displaying a login status and recent saves.

At the top, it states, "You are logged in as 22f3001740@ds.study.iitm.ac.in."  A red "Logout" button is next to this information.

Below this, a light green box displays "Recent saves".  Inside this box are three entries, each showing:

* A blue "Reload" button.
* The date and time of a save (all on January 23rd, 2025,  with times around 9:33 PM).
* A score of 8 for each save.

The consistent date, times, and scores suggest that the same data was saved multiple times in quick succession.  The email address suggests an academic or institutional login. The "Reload" buttons probably allow the user to restore the saved data.

---

## Post #128 by 23f1000751 (Post ID: 587512)
I have seen the Graded Assignment 1 available at 
this link
 and have attempted it.


Yes


No


i have forgot the submit  here on the portal but i have got 9 marks on the test will it be a problem  in my marks?

---

## Post #129 by 22f3001740 (Post ID: 588093)
Hi 
@Jivraj
  sir,


For me, in dashboard , it is showing the assignment was not submitted.


image
809×560 51.9 KB


But I have completed it and got saved before the deadline


I havent answered the (yes / No ) in seek portal. If that might be a reason ?


Can you please help me resolve this issue

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/2/42a17ff0b02a49ce4061f3976c99e7f19336bedd_2_690x477.png)

**Image Description:** This image shows a portion of a web page, likely from an online learning platform. 


Here's a breakdown of the content:

* **Top Section:** This section displays information about "Module 1: Development Tools".  There's an assignment called "Graded Assignment 1" with a due date of January 26, 2025. The status shows "Not Submitted".  A table to the right shows the user's score ("-"), the peer average (99%), and the median score (100).

* **Middle Section:** This section displays the user's login information: "You are logged in as 22f3001740@ds.study.iitm.ac.in." There is a "Logout" button.

* **Bottom Section:** This section displays "Recent saves". Three entries show that the user reloaded something three times on January 23rd, 2025, at 9:33:02 PM, 9:32:59 PM, and 9:32:55 PM, each time achieving a score of 8.  Each entry has a "Reload" button.


The overall context suggests a student's view of their progress in an online course. The user has not submitted their graded assignment, yet has saved their work multiple times.  The scores in the "Recent Saves" section likely refer to attempts to complete the assignment.

---

## Post #130 by carlton (Post ID: 588096)
Dear Sai,


This is NOT the picture of your dashboard.








 22f3001740:




image
809×560 51.9 KB






This picture is the score in your seek portal.


The dashboard has the final correct score. Please check your dashboard.

The dashboard has all your courses on it, when you log in.


Kind regards

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/2/42a17ff0b02a49ce4061f3976c99e7f19336bedd_2_690x477.png)

**Image Description:** The image shows a screen capture of what appears to be an online learning platform or assessment system. 


Here's a breakdown of the content:

* **Module Information:** The top section displays "Module 1: Development Tools".  Below this, there is an "Assignment" section showing a "Graded Assignment 1" that is due on January 26th, 2025, and is marked as "Not Submitted".

* **Score Information:** A table presents the user's score ("-"), the peer average (99%), and the median score (100) for the graded assignment.

* **Login Information:**  The text "You are logged in as 22f3001740@ds.study.iitm.ac.in" confirms the user's identity, indicating an email address associated with the IIT Madras domain. A "Logout" button is also available.

* **Recent Saves:** A light green box displays "Recent saves" followed by three entries. Each entry shows a "Reload" button and indicates the date and time of a save (all on January 23rd, 2025, around 9:33 PM) and a score of 8 for each save.  The repeated saves suggest the user might have been working on the assignment and saving their progress multiple times.

In summary, the screenshot likely depicts a student's view of their progress in a graded assignment within a course on development tools.  The student has not yet submitted the assignment, but has saved their work several times. The peer and median scores suggest that the assignment is quite challenging, and achieving a perfect score is rare.

---

## Post #131 by 22f3001740 (Post ID: 588128)
Got it , Thank you sir

---

## Post #132 by 23f3001601 (Post ID: 596939)
Hello Sir,

I am writing to bring to your attention a discrepancy I’ve noticed regarding my Week 1 graded assignment for the Tools in Data Science course.


I successfully completed the assignment and received a score of 
80 out of 100
. However, when I checked the course portal, it is showing my status as “
absent
” for this particular assignment.


I wanted to ensure that this information is corrected in the system to accurately reflect my participation and performance. Could you please look into this matter and update my grade accordingly?


Screenshot 2025-02-18 191335
881×835 44.5 KB


Screenshot 2025-02-19 145423
961×615 73.7 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/c/1c53ba70eb3926a812741579345ed5e333a899f9_2_527x499.png)

**Image Description:** This image shows a web page, likely an online exam or quiz results interface. Here's a breakdown of the content:

**Top Section:**

* **URL:** The URL bar displays `exam.sanand.workers.dev/tds-2025-01-ga1`, indicating a development or testing environment related to an exam ("tds" possibly stands for "test data set" or similar).
* **Exam Completion Time:** "Ended at Sun, 26 Jan, 2025, 11:59 pm IST" shows the exam's end time and time zone (Indian Standard Time).
* **Score:** "Score: 0" displays the current score.  Note that the user has made saves with a score of 8.
* **Buttons:** "Check all" and "Save" buttons suggest the possibility of reviewing all questions or saving answers.

**Middle Section:**

* **Discussion Link:** A message "Have questions? Join the discussion on Discourse" with a link to a Discourse forum offers help and discussion opportunities.
* **Login Information:** "You are logged in as 23f3001601@ds.study.iitm.ac.in." displays the user's email address, likely associated with the Indian Institute of Technology Madras ("iitm.ac.in").
* **Logout Button:** A "Logout" button is present.

**Bottom Section:**

* **Recent Saves:** A section titled "Recent saves (most recent is your official score)" shows three entries:
    * Three instances of "Reload" buttons with timestamps and scores. Each shows the exam was saved with a score of 8 on January 26th and 27th, 2025.


**Overall:**

The page appears to be from an online exam platform.  The user, 23f3001601@ds.study.iitm.ac.in, has completed the exam with a final score of 0 (shown at the top), but it appears they may have saved some progress earlier with a higher score (8) that was not submitted.  The multiple "Reload" buttons and timestamps suggest the user reviewed or resubmitted the exam multiple times before submitting their final 0 score.  The Discourse link suggests that the exam is part of a learning management system or course.

![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/0/f099a2b729be7a10b157f84651045fb6becaaab7_2_690x441.jpeg)

**Image Description:** Here's a description of the image:

The image is a screenshot of what appears to be a learning management system (LMS) or online course platform. 


The upper portion shows a dark maroon background with a pattern of lighter maroon dots. Over this background, the following text is displayed in white, sans-serif font:

* **Tools in Data Science** (largest font size)
* **NEW COURSE** (smaller font size, below the first line)


The bottom portion of the image shows a lighter gray or off-white area with the following text:

* **Week 1 Assignment - Absent**


The overall impression is that this is a promotional image or announcement for a new "Tools in Data Science" course. The "Absent" status for the Week 1 assignment suggests that the screenshot is taken from a student's view, likely indicating that they haven't yet completed the first assignment.

---

## Post #133 by 23f1003186 (Post ID: 596943)
@s.anand
 Linking 
this tutorial
 for markdown. Maybe you can consider including it in the next iteration of the course?


I’ve created a PR for the same on GitHub! Please have a look and let me know what you think Prof!

---

## Post #134 by Jivraj (Post ID: 597013)


---

## Post #135 by 23f2001286 (Post ID: 597151)
I also came here for the same issue…

---

## Post #136 by 23f2001286 (Post ID: 597152)
Sir i have scored 9.25 in the week 1 assingment but now it is showing absent…

---

## Post #137 by carlton (Post ID: 597162)
@23f3001601
 Dont worry, it is 8 on our backend server. The dashboard will have the result soon.


Kind regards.

---

## Post #138 by carlton (Post ID: 597163)
@232001286


Yes our backend server shows that it is 9.25 dont worry. It will be fixed in the dashboard soon.


Kind regards

---

## Post #140 by carlton (Post ID: 625648)
2 posts were merged into an existing topic: 
GA2 - Deployment Tools - Discussion Thread [TDS May 2025]

---

## Post #142 by carlton (Post ID: 625644)


---

## Post #143 by carlton (Post ID: 625645)


---

## Post #144 by carlton (Post ID: 625649)


---
