# Topic: GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]
**Topic ID**: 165959
**Total Posts**: 370

---

## Post #1 by s.anand (Post ID: 588325)
Please post any questions related to 
Graded Assignment 4 - Data Sourcing
.


Please use markdown code formatting (fenced code blocks) when sharing code (rather than screenshots). It’s easier for us to copy-paste and test.


Deadline: 
Sunday, February 9, 2025 6:29 PM


@Jivraj
 
@Saransh_Saini
 
@carlton

---

## Post #2 by s.anand (Post ID: 588326)


---

## Post #3 by 22f3001315 (Post ID: 588589)
Screenshot 2025-02-01 132301
331×314 12.3 KB

what is the error here?? sir 
@Jivraj

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/0/0007976ca3410205e4fa403a71b9a1ac79bf5192.png)

**Image Description:** The image shows a code snippet and a test result. 


Here's a breakdown:

* **Top Section:** The text "What is the JSON data?" serves as a title or question.

* **Middle Section:** This section contains a JSON object within curly braces `{}`.  The JSON object has four key-value pairs:

    * `"id": "tt7144296"`: An ID, likely a movie or film ID.
    * `"title": "1. Kiss and Kill"`: The title of a movie or film.
    * `"year": 2017`: The year of release.
    * `"rating": 2.9`: A numerical rating (presumably out of 10 or a similar scale).

* **Bottom Section:** This section displays a test result:  "Error: Expected: 2.9 Actual: 2.9". This indicates a successful test; the expected and actual values for a "rating" variable match.  This suggests the image is part of a larger testing process (likely unit testing of code that handles JSON data).

In summary, the image shows sample JSON data representing information about a movie or film ("1. Kiss and Kill," released in 2017, with a rating of 2.9) and a successful test verification of the rating value.

---

## Post #5 by 24ds2000024 (Post ID: 588867)
I have the Same doubt.

---

## Post #6 by s.anand (Post ID: 589057)
@22f3001315
 
@21f3002277
 
@24ds2000024
 – please try again after reloading the page. The new error message will be clearer, like this:


Error: At [0].rating: Values don't match. Expected: "7.4". Actual: 7.4



FYI, we expect all values as strings, not numbers. That’s because the year can sometimes be a range for a TV series (e.g. 2021 - 2024) and the rating can sometimes be missing.

---

## Post #7 by 23f2000237 (Post ID: 589067)
In Question 2, it is specifically said to filter the movies however, the evaluator is expecting a TV show there. Should we also include TV shows now?


edit:  This is an everchanging dataset, so will our answers be saved, as, this json might not be in this order tomorrow?

---

## Post #8 by s.anand (Post ID: 589072)
@23f2000237
 A good point. Yes, please include 
all
 titles. I’ve reworded the question accordingly. Thanks.

---

## Post #9 by 21f3002277 (Post ID: 589120)
Q3. How to handle the error ? 
@Jivraj


TypeError: Cannot read properties of null (reading ‘0’)


http://127.0.0.1:8000/api/outline?country=Russia

{"outline":"## Contents\n# Russia\n## Etymology\n## History\n### Early history\n### Kievan Rus'\n### Grand Duchy of Moscow\n### Tsardom of Russia\n### Imperial Russia\n#### Great power and development of society, sciences, and arts\n#### Great liberal reforms and capitalism\n#### Constitutional monarchy and World War\n### Revolution and civil war\n### Soviet Union\n#### Command economy and Soviet society\n#### Stalinism and modernisation\n#### World War II and United Nations\n#### Superpower and Cold War\n#### Khrushchev Thaw reforms and economic development\n#### Period of developed socialism or Era of Stagnation\n#### Perestroika, democratisation and Russian sovereignty\n### Independent Russian Federation\n#### Transition to a market economy and political crises\n#### Modern liberal constitution, international cooperation and economic stabilisation\n#### Movement towards a modernised economy, political centralisation and democratic backsliding\n#### Invasion of Ukraine\n## Geography\n### Climate\n### Biodiversity\n## Government and politics\n### Political divisions\n### Foreign relations\n### Military\n### Human rights\n### Corruption\n### Law and crime\n## Economy\n### Transport and energy\n### Agriculture and fishery\n### Science and technology\n#### Space exploration\n### Tourism\n## Demographics\n### Language\n### Religion\n### Education\n### Health\n## Culture\n### Holidays\n### Art and architecture\n### Music\n### Literature and philosophy\n### Cuisine\n### Mass media and cinema\n### Sports\n## See also\n## Notes\n## References\n## Sources\n## Further reading\n## External links"}




error resolved

---

## Post #11 by 22f3001315 (Post ID: 589293)
in my output which is correct

there are two \n instead of one .

---

## Post #12 by 21f3002277 (Post ID: 589307)
it should one(for newline), my code is working now

---

## Post #13 by 24ds2000024 (Post ID: 589366)
Dear Sir,

I was at 2/10 yesterday. After pasting JSON file of IMDB & reloading as suggested My marks updated to 3/10. Kindly confirm if I have got whole of IMDB question.

---

## Post #14 by 21f3002277 (Post ID: 589408)
Q4. How to handle the error ? 
@Jivraj


Error: At 2025-02-05: Values don’t match

---

## Post #15 by 23f2003853 (Post ID: 590055)
There is no submit button is available in below screen. Is it fine to save the link url only. Please clarify (unless we click submit button the log of Graded Assignment 4 remains red)


image
1920×1080 337 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/9/699d94f19d189a93a67fb813a5eeed3d1f73abf3_2_690x388.png)

**Image Description:** The image shows a screen capture of a web browser displaying a graded assignment page for a course offered by the Indian Institute of Technology Madras. 


Here's a breakdown of the content:

* **Top Bar:** Shows the browser's address bar with the URL of the assignment, indicating it's part of an online degree program ("seek.onlinedegree.iitm.ac.in"). The title bar displays "Graded Assignment 4" and the name of the institution.

* **Left Sidebar:** Displays a course navigation menu, showing modules and a "Grades" section. The modules listed include "Course Introduction," "Module 1: Development Tools," "Module 2: Deployment Tools," "Module 3: Large Language Models," "Project 1," and "Module 4: Data Sourcing." The "Graded Assignment 4" is listed as an assignment under the modules.

* **Main Content Area:**  Contains the details of Graded Assignment 4, including:
    * **Due Date:** Clearly states the due date and time (2025-02-09, 23:59 IST).
    * **Submission Policy:**  Specifies that multiple submissions are allowed before the deadline, with only the final submission being graded.
    * **Troubleshooting Instructions:** Provides a list of common reasons why students might have trouble accessing the assignment (ad blockers, cookies, JavaScript, browser extensions, antivirus software, network restrictions).  It explicitly recommends using Chrome.
    * **Student ID Requirement:** Emphasizes the necessity of using the student's ID for submission to ensure the score is counted.
    * **Assignment Link:**  Provides a direct link to the assignment: `https://exam.sanand.workers.dev/tds-2025-01-ga4`.


* **Bottom Bar:** The Windows taskbar is visible at the bottom, showing the time and date.


In summary, the image provides all the necessary information for students to access and complete their graded assignment, including the due date, submission guidelines, troubleshooting advice, and the direct link to the assignment itself.

---

## Post #16 by 23f2000237 (Post ID: 590227)
I have a doubt regarding the bonus mark. Suppose someone were to get 10/10 in the assignment, would their mark be recored as 11/10 or just 10?

(Assuming they have interacted in this thread)

---

## Post #17 by s.anand (Post ID: 590239)
Anyone scoring 10/10 on GA4 and replying with a 
relevant
 message on this thread will get 11/10

---

## Post #18 by 23f2003853 (Post ID: 590243)
For me I just made filter of rating between 2 and 7 in site and typed in console as per  video. with that data got in console worked fine.

copy the coding and save in place use it for data extract when finally submit

---

## Post #19 by 22f2000113 (Post ID: 590374)
For question 2 getting Error: At [8].title: Values don’t match. Expected: “9. Un matrimonio di troppo”. Actual: “9. You’re Cordially Invited” But this movie is not found when searched by name


image
1414×295 19 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/b/1b7f2ec2868a09d8b4ed3fc50afa02f8416dad93_2_690x143.png)

**Image Description:** The image shows a search results page displaying "No results found".  The main content is divided into two sections:

**Left Section:** This section contains search filters.  Specifically:

* **"Search filters"**: This heading is at the top.  There is a link that says "Expand all" which presumably shows additional filters.
* **"Title name"**: This label is above a text input field where the user has entered "Un matrimonio di troppo".  This appears to be a title in Italian.
* **"Title type"**: This label is above another text input field, which is currently empty.  Small upward-pointing arrows are next to both text input fields, suggesting they can be expanded to show more options.

**Right Section:**  This section shows a message indicating that the search returned no results.

* **A greyed-out magnifying glass icon with a cross mark over it**: This visually reinforces the "No results found" message.
* **"No results found"**: This text clearly states that the search query produced no matches.
* **"Please adjust your filters or start a new search"**:  This provides guidance to the user on how to proceed.

In summary, the image shows a search interface with a search query ("Un matrimonio di troppo") that yielded no results, prompting the user to refine their search criteria or initiate a new search.  The language used suggests the platform is likely multilingual or at least caters to users who might search using Italian.

---

## Post #20 by nilaychugh (Post ID: 590429)
how to get the BBC weather API key?

---

## Post #21 by JoelJeffrey (Post ID: 590455)
Just a quick query on the Bonus mark.


Would this be added to the final grade? Say for example, Someone get a full score in the first 4 assignments. So the total comes up to 39.5/39.5, and would be converted to 0.15 or 15 marks. Would the bonus mark be additional to that 15 or would the score change to 40.5/39.5 and then get normalised to 15?

---

## Post #22 by s.anand (Post ID: 590467)
@JoelJeffrey
 It will be added to the GA4 marks, not the final grade. So, it’s roughly worth 0.15% on the total - not a full 1% on the total.

---

## Post #23 by 23f2003751 (Post ID: 590495)
you can go and login using your email id in this below mentioned link


https://home.openweathermap.org/api_keys

---

## Post #24 by JoelJeffrey (Post ID: 590508)
Error: At [10].year: Values don’t match. Expected: "2025– ". Actual: “2025–”


Can someone help me with this?

Thanks


Edit: Resolved

---

## Post #25 by 23f2003853 (Post ID: 590528)
Q8 I got the Error: No executed job step matches 23f2003853@ds.study.iitm.ac.in. the .yml file contains the following

" name: Daily Commit


on:

schedule:

- cron: ‘0 12 * * *’ # Runs daily at 12:00 PM UTC

workflow_dispatch:  # This allows manual trigger


jobs:

commit:

runs-on: ubuntu-latest


steps:
- name: Checkout repository
  uses: actions/checkout@v2

- name: Make a dummy change with email 23f2003853@ds.study.iitm.ac.in in the commit
  run: |
    echo "This is a daily commit" > daily_commit.txt
    git config --global user.email "23f2003853@ds.study.iitm.ac.in"
    git config --global user.name "23f2003853"
    git add daily_commit.txt
    git commit -m "Daily commit from 23f2003853@ds.study.iitm.ac.in"
    git push"



@Jivraj
 can help me to fix the issue

---

## Post #26 by 23f2000237 (Post ID: 590642)
Have a step with your email id as its name. (Instead of checkout repository)

Also make sure you give read and write permission so it commits without any error

---

## Post #27 by daksh76 (Post ID: 590658)
name: Daily Commit


on:

schedule:

- cron: ‘0 0 * * *’  # Runs once a day at midnight UTC

workflow_dispatch:  # Allows manual triggering of the workflow


jobs:

commit:

runs-on: ubuntu-latest


steps:
- name: Checkout repository
  uses: actions/checkout@v3

- name: Make daily commit by 23f3000264@ds.study.iitm.ac.in
  run: |
    echo "Daily commit by 23f3000264@ds.study.iitm.ac.in" >> daily_commit.txt
    git add index.html
    git commit -m "Daily commit"
    git push
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}



sir this is my code and im getting a error in this


image
703×137 9.75 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/7/f740be2ffaea5957ca053368c20e28f7045362d0.png)

**Image Description:** The image shows a text input field with an error message.  Let's break down the content:

* **Top Line:** "Enter your repository URL (format: https://github.com/USER/REPO):" This is a prompt instructing the user to enter a GitHub repository URL in the specified format.  The format shows that the URL should contain the username (`USER`) and repository name (`REPO`).

* **Input Field:**  The input field contains the URL `https://github.com/dakshagarwal76/daily-update`. This is the GitHub repository URL that the user has entered.

* **Error Message:** "Error: No executed job step matches 23f3000264@ds.study.iitm.ac.in" This is an error indicating that the system could not find a matching job step for a specific identifier (`23f3000264@ds.study.iitm.ac.in`).  This suggests a problem with the workflow or configuration, not necessarily the repository URL itself. The error message contains an email address-like string, which might be a user ID or job identifier.

In short, the user has entered a GitHub repository URL, but the system is unable to process it due to a mismatch in a job step identifier.  The problem lies within the system's configuration or workflow, not with the provided GitHub repository.

---

## Post #28 by 22f2000113 (Post ID: 590665)
dont remove the space after year- for example “year”: "2023- "

---

## Post #29 by 23f2004752 (Post ID: 590696)
Please anyone help me in doing q1 , my doubt is when i open the website 
Advanced search
 , i have click on movies and then do the coding part if not how to select titles of the movies as there is no movies on the page.

---

## Post #31 by 23f2004752 (Post ID: 590699)
In q4 i got this error someone pls expalin “Error: At root: Property name mismatch”

---

## Post #33 by 23f2003751 (Post ID: 590732)
Student marks - Group 100

| Maths | Physics | English | Economics | Biology |
| ----- | ------- | ------- | --------- | ------- |
| 48    | 51      | 15      | 47        | 65      |
| 74    | 70      | 23      | 17        | 70      |
| 81    | 50      | 59      | 45        | 51      |
| 80    | 63      | 43      | 99        | 28      |
| 85    | 72      | 82      | 79        | 14      |
| 76    | 50      | 15      | 55        | 13      |
| 21    | 86      | 25      | 14        | 64      |
| 54    | 72      | 98      | 30        | 96      |
| 15    | 24      | 67      | 19        | 35      |
| 68    | 82      | 16      | 70        | 67      |
| 64    | 94      | 42      | 26        | 10      |
| 31    | 79      | 98      | 21        | 24      |
| 90    | 32      | 88      | 39        | 56      |
| 36    | 72      | 79      | 86        | 96      |
| 91    | 61      | 57      | 28        | 23      |
| 81    | 40      | 95      | 74        | 30      |
| 60    | 31      | 66      | 36        | 83      |
| 81    | 16      | 67      | 25        | 90      |
| 40    | 96      | 57      | 84        | 47      |
| 53    | 92      | 10      | 10        | 82      |
| 33    | 40      | 20      | 68        | 95      |
| 95    | 48      | 69      | 24        | 42      |
| 93    | 84      | 79      | 33        | 17      |
| 40    | 81      | 39      | 31        | 60      |
| 31    | 44      | 96      | 78        | 54      |
| 58    | 21      | 98      | 58        | 44      |
| 47    | 22      | 91      | 77        | 46      |
| 61    | 93      | 75      | 25        | 79      |
| 18    | 19      | 47      | 20        | 58      |
| 77    | 51      | 28      | 14        | 97      |



This is the piece of  markdown that is being generated for the last question of ga4.Even after using the prettier of the mentioned version i am getting incorrect answer.

Anyone like to help.


@Jivraj
 
@carlton
 
@s.anand

---

## Post #34 by JoelJeffrey (Post ID: 590733)
For Q10, I am extracting the text first using PyMuPDF (fitz) and then using markdownify to convert it to markdown and finally prettier. However despite trying changing it from PyMuPDF to other text extraction libraries, I end up getting




Incorrect. Try Again




errors

---

## Post #35 by 23f2000237 (Post ID: 590735)
I think you have used the wrong document, because, this is the marks list for Q9

---

## Post #36 by 23f2003751 (Post ID: 590739)
which tool you are using ?

---

## Post #37 by Namannn28 (Post ID: 590742)
HOW TO GET BBC API KEY


image
1888×868 75.5 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/2/e2e304a859382b51deb2992386d3dfc8cbae3a77_2_690x317.png)

**Image Description:** The image shows a coding assignment or exercise displayed on a computer screen.  The assignment involves three steps:

1. **API Integration and Data Retrieval:**  Fetching weather data for Tel Aviv using the BBC Weather API.  This requires sending a GET request to a locator service to get a location ID, and then using that ID in a GET request to the weather broker API.

2. **Weather Data Extraction:** Retrieving the forecast data from the API response.

3. **Data Transformation:**  Transforming the extracted data into a JSON object.  The keys in this JSON object are `issueDate` values (dates), and the values are the corresponding `enhancedWeatherDescription` (weather descriptions for those dates).  An example of the expected JSON output is provided: a curly-braced object with date strings as keys and weather descriptions as values.

Below this instruction is a text box where the user should input their answer—the JSON weather forecast for Tel Aviv.  Currently, the box is empty. Below the box, an error message "SyntaxError: Unexpected end of JSON input" is shown, indicating that the user's attempt at creating the JSON object is invalid, likely due to being incomplete or improperly formatted.  The top of the screen displays a due date, a score (1/10), and buttons labeled "Check all" and "Save".

---

## Post #38 by 23f2003751 (Post ID: 590747)
in the bbc question what should be starting and the ending date

---

## Post #39 by 22f3001315 (Post ID: 590764)
you dont need the key you need that file used in 2 lecture videos just look for it.

---

## Post #40 by 23f2003853 (Post ID: 590779)
Please find below the screen shot showing the committed with step name my iitm email id


image
1366×768 79.8 KB

But the answer says


image
602×164 21 KB

Please help to fix the issue

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/a/7ae7951e4e7d3ea76248632715b376e23d3b0a76_2_690x387.png)

**Image Description:** This image shows a screenshot of a GitHub Actions workflow run. 


Here's a breakdown of the key elements:

* **Top Browser Bar:** Shows the GitHub URL indicating a specific workflow run (`github.com/23f2003853/workflows/actions/runs/13154595741/workflow`).  The username `23f2003853@ds.study.iitm.ac.in` is prominently displayed, along with run number #13.

* **Left Panel (GitHub Actions Run Details):** This section displays information about the workflow run:
    * **Summary:** A collapsible section (currently closed).
    * **Jobs:** Shows a single job named "daily-commit" which has successfully completed (indicated by a green checkmark).
    * **Run details:** A collapsible section (currently closed).
    * **Usage:** A collapsible section (currently closed).
    * **Workflow file:** A button that's likely used to expand/show the workflow file's YAML code.

* **Right Panel (Workflow File Content):**  This displays the YAML code defining the workflow. Key parts include:
    * **`name`:** Defines the workflow's name using the user's email address.
    * **`on`:** Specifies the workflow trigger.  It runs daily at 10:00 AM UTC (`cron: '0 10 * * *'`) and allows for manual triggering (`workflow_dispatch`).
    * **`permissions`:** Sets the permissions to write (`contents: write`).
    * **`jobs`:** Defines the jobs to be executed.  In this case, there's a single job named "daily-commit" which runs on the `ubuntu-latest` runner.
    * **`steps`:** Details the steps within the "daily-commit" job.  It includes checking out code using the `actions/checkout` action. `persist-credentials: false` suggests that credentials aren't persistently stored.

* **Bottom Bar (Windows Taskbar):** Displays the Windows taskbar, showing the time, date, language, and system tray icons indicating an unactivated Windows installation and current weather conditions (32°C Haze).


In summary, the image depicts a successful GitHub Actions workflow run named "daily-commit," triggered daily and configured to check out code from a repository associated with the user `23f2003853@ds.study.iitm.ac.in`. The workflow is simple, consisting of a single job with a few steps, and uses the Ubuntu latest runner.

![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/9/d9fb33c07548b8cb0f740e38585a1b1b277de791.png)

**Image Description:** The image shows a section of a web page, likely a troubleshooting or debugging interface related to GitHub workflows. 


Here's a breakdown of the content:

* **Instructions:** The top section provides instructions on how to set up and verify a GitHub workflow.  Key steps include placing the workflow file in the `.github/workflows/` directory, triggering the workflow, ensuring it's the most recent action in the repository, and verifying a commit is created within 5 minutes.

* **Repository URL Input Field:** A text input field prompts the user to enter their repository URL. The format is specified as `https://github.com/USER/REPO`. A URL is already partially filled in: `https://github.com/23f2003853/workflows`. This seems to be an incomplete or incorrect URL, which might be a cause of the error.

* **Error Message:** A red error message displays below the input field: "Error: No executed job step matches 23f2003853@dsstudy.itm.ac.in". This indicates that the system cannot find any matching job steps for the provided (or implied) repository and user information.  The `23f2003853@dsstudy.itm.ac.in` part appears to be an email or user identifier.

* **"Check" Button:** A button labeled "Check" is present, suggesting that the user can submit the provided information for verification or further processing.

In short, the image depicts a troubleshooting scenario where a user is trying to validate their GitHub workflow setup, but is encountering an error because either the repository URL is wrong or there's a problem with the workflow execution itself. The error message provides a clue about the user and potential location of the issue.

---

## Post #41 by 23f2003853 (Post ID: 590781)
Still the issue is there. Have posted screen shot.

---

## Post #42 by 23f2003853 (Post ID: 590782)
what Mr. Sakthivel S said is correct. could you tell me what tool did you use to convert .md file. I have done as per links in question and used chatgpt also. but nothing is correct

---

## Post #43 by 23f2003751 (Post ID: 590798)
Please give the solution if you got any…have you been able to solve the bbc weather question?

---

## Post #45 by 23f2004752 (Post ID: 590870)
@s.anand
 
@carlton

In question 8 i got error

“Enter your repository URL (format: 
https://github.com/USER/REPO
):


https://github.com/Ansh205/github-actions

Error: No workflow runs found”

But i have successfully commited


Screenshot 2025-02-05 193233
1462×642 38.4 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/e/4e52f03ba17a95acf60684f40c4115cf1a385153_2_690x302.png)

**Image Description:** This image is a screenshot of a workflow run list, likely from a CI/CD (Continuous Integration/Continuous Delivery) platform or similar system.  Here's a breakdown of the content:

* **Header:** The top shows "All workflows" indicating a view of all currently running workflows, with a subheading "Showing runs from all workflows".  A search bar labeled "Filter workflow runs" is present in the top right corner.

* **Workflow Runs:** The main section lists four workflow runs, each with the following information:

    * **Status Icon:** A green checkmark (✓) indicates a successful run, while a red 'x' (✕) indicates a failed run.

    * **Workflow Name:** All four runs are named "Daily Commit Workflow," suggesting a recurring automated process triggered by commits.

    * **Workflow Run Number:** Each run is numbered sequentially (e.g., #4, #3, #2, #1), implying a chronological order with #4 being the most recent.

    * **Run Details:** A subtext provides additional details: "Manually run by Ansh205". This clarifies the workflow was initiated manually by a user with the username "Ansh205".

    * **Branch:**  All runs are on the "main" branch. This is a common term in version control systems, indicating the primary development branch.

    * **Time Since Run:** Two time indicators are shown for each run:
        * A calendar icon displays the time elapsed since the run started (e.g., 5 minutes ago, 1 hour ago).
        * A clock icon shows the run duration (e.g., 19s, 14s).

* **Table Headers:**  Above the workflow run list, columns are labeled "Event," "Status," "Branch," and "Actor," providing context for the data shown in each row.

**In summary:** The image shows four recent runs of a "Daily Commit Workflow," all initiated manually by a user named "Ansh205" on the "main" branch. The runs have varying durations and success/failure status.  The screenshot likely comes from a platform designed to monitor and manage automated workflows.

---

## Post #46 by gouthamnischay (Post ID: 590937)
Just follow the links and notebooks given in the references.

---

## Post #47 by roy2003 (Post ID: 591019)
@Jivraj
 
@carlton

sir i have submitted my GA3 but its showing not submitted why?


Untitled design
1414×2000 314 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/8/b88fa681fcbf676c93202b79b2bcb23d71df28a4_2_353x500.png)

**Image Description:** The image shows a computer screen displaying an online assessment or quiz. 


Here's a breakdown of the content:

* **Title:** The main title at the top is "TDS 2025 Jan GA3 - Large Language Models." This suggests it's a graded assignment (GA3) related to Large Language Models within a course or program titled "TDS 2025" (possibly referring to a year and course code).  "Jan" likely indicates the month.

* **Instructions:** A section titled "Instructions" provides guidelines for completing the assignment.  These instructions mention:
    * Reading material is provided.
    * Answers can be checked multiple times.
    * Time limits apply.
    * Restrictions on using unauthorized tools or frameworks are implied.
    * Multiple submissions are allowed.

* **Module Information:** A section labeled "Module 3: Large Language Models" clearly indicates the topic of the assessment.

* **Assignment Details:** The lower portion details the assignment:
    * **Assignment:** "Graded Assignment 3"
    * **Due Date:** "Due 5 Feb 2025" (Note that the year is likely 2025, given the title)
    * **Submission Status:**  "Not Submitted"

* **Score Information:** A table shows spaces for "Your Score," "Peer Average," and "Median Score," all of which are currently blank, indicating that the assessment has not yet been graded or submitted.

* **Browser Information (Top):** The top of the image shows a browser window with URLs that are partially visible, suggesting it's an online learning platform.

* **Discussion Forum Link:** There's a button or link that says "Join the discussion on Discourse," providing a way to engage with classmates.

* **User Login:** The bottom of the instructions section shows the logged-in user's ID (partially visible).

In summary, the image depicts an online graded assignment focused on Large Language Models, currently not submitted, with instructions and space for scores to be displayed later. The assignment is part of a larger course or module.

---

## Post #48 by 23f2003853 (Post ID: 591027)
@s.anand
 Sir no submit button is available. On the top of it say submission is required. Could you clarify us


image
690×388 46.5 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/8/d851d2f20816a37ba11ac45568e329bf914ea0b4.png)

**Image Description:** The image shows a screenshot of a web browser displaying a graded assignment page for a course at the Indian Institute of Technology Madras. 


Here's a breakdown of the content:

* **Top Navigation Bar:** A standard browser address bar shows the URL, indicating an online course platform. The title of the assignment is visible in the tab title: "Graded Assignment 4: IITM".

* **Left-Hand Sidebar:** This section displays a course menu with the following items:

    * "Modules": A collapsible list of course modules.  Visible modules include: "Course Introduction," "Module 1: Development Tools," "Module 2: Deployment Tools," "Module 3: Large Language Models," "Project 1," and "Module 4: Data Sourcing."
    * "Grades": A section likely showing grades for the course (partially visible).

* **Main Content Area:** This is where the assignment information is displayed.

    * **"Graded Assignment 4" Heading:** This clearly labels the assignment.
    * **Due Date:** The assignment's due date is explicitly stated as "2025-02-09, 23:59 IST".
    * **Submission Policy:** Students are informed they can submit multiple times before the deadline; only the final submission will be graded.
    * **Troubleshooting Information:** A section providing troubleshooting tips for students facing access issues. It highlights common causes like ad blockers, cookies, JavaScript requirements, specific browser recommendations (Chrome), and potential conflicts with browser extensions or antivirus software. It also suggests trying a different network.
    * **Student ID Requirement:** It mandates using the student ID in the format "22f3xxxxxx@ds.study.iitm.ac.in" to access the assignment. Failure to do so will result in a score not being considered.
    * **Assignment Link:**  A direct link to the assignment is provided: "https://exam.sanand.workers.dev/tds-2025-01-ga4".

* **Bottom Bar:** A standard Windows taskbar is visible at the bottom of the screen.


The information contained within the image clearly points to an online course assignment with specific instructions, deadlines, and troubleshooting guidance for students.

---

## Post #49 by 21f3002277 (Post ID: 591032)
what’s your directory structure, is it (.github/workflows/<filename.yaml>) and public

---

## Post #50 by 23f2003853 (Post ID: 591035)
As per instruction we need to create a directory in that we should have .yml file. But I tried with there were two issues (1) Github has not allowed to run the file (as there was no menu is available to run manually) (I checked with Copolit AI it says it is not correct to have cron jobs in a directory, I am not sure) (2) when I submit the url to iitm I got the following error


image
602×135 24.8 KB

I removed the directory and submitted the same url I got the following error


image
1122×184 5.81 KB

I do not know what to do next. Can TA help us

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/f/6fd287b966b7a580fabd12762ac0e6592b0190b5.png)

**Image Description:** This image shows a snippet of text providing instructions, likely related to setting up a GitHub workflow. 


Here's a breakdown of the content:

* **Instructions:** The top section outlines steps to follow after creating a GitHub workflow. These steps involve triggering the workflow, waiting for completion, verifying its appearance as the most recent action in the repository, and confirming a commit is created within 5 minutes.

* **Repository URL Input:** A text box prompts the user to enter their repository URL in the format `https://github.com/USER/REPO`.  Below this, a sample URL, `https://github.com/23f2003853/workflows`, is displayed, indicating a potential example or a user’s specific repository.

* **Error Message:** At the bottom, a YAML parsing error is shown:  `YAMLParseError: Implicit keys need to be on a single line at line 1, column 1: <!DOCTYPE html>`.  This strongly suggests the user encountered a problem with their workflow's YAML configuration file, specifically that implicit keys (likely in the first line) need to be written on a single line. This is a common issue when using YAML syntax for configuration.

In short, the image captures a user's interaction with what is likely a web interface for managing GitHub workflows. The user has input a repository URL, and a YAML parsing error suggests a problem with their workflow definition file.

![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/b/7ba477a0682a8af40b3fbd474ee66eff108d2ab8.png)

**Image Description:** Here's a description of the image content:

The image shows a web interface, likely part of a continuous integration/continuous deployment (CI/CD) system or a similar tool for managing software projects.  The primary function appears to be verifying or connecting to a GitHub repository.

**Key elements:**

* **Instruction:**  At the top, it says "Enter your repository URL (format: https://github.com/USER/REPO):". This indicates the user needs to provide a GitHub repository URL in a specific format.

* **Input Field:** A text input field (outlined in pink/red) is below the instruction. It contains the URL `https://github.com/23f2003853/workflows`. A small exclamation mark icon (①) inside a circle indicates there's an issue with the input.

* **Error Message:** Below the input field, an error message is displayed: "Error: No executed job step matches 23f2003853@ds.study.iitm.ac.in". This suggests the system is unable to find any matching job steps based on the provided repository URL and potentially another identifier (`23f2003853@ds.study.iitm.ac.in`).  The error suggests the problem is not just with the repository URL.

* **"Check" Button:** A blue button labeled "Check" is at the bottom.  This button likely triggers the system to verify the provided repository URL and perform the related checks.

In summary, the image displays an error state where the system failed to connect to or validate the GitHub repository given by the user, possibly due to a mismatch between the provided repository URL and some internal job identifier. The error message provides clues for debugging the problem.

---

## Post #51 by carlton (Post ID: 591037)
The submission is on the Actual assignment page like for all the previous GAs in TDS. This is the 
ONLY
 valid submission button for GA1, GA2, GA3, GA4, GA5.


Screenshot 2025-02-06 at 10.43.15 am
1390×1146 113 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/5/758c516fa4ae8cd2e15a7c42c3059ef4465cf544_2_606x500.png)

**Image Description:** Here's a description of the image's content:

The image shows a web page, likely an online exam or quiz. 


**Key Elements:**

* **Browser Address Bar:** Shows the URL `exam.sanand.workers.dev/tds-2025-01-ga4`, indicating a development or testing environment related to an exam ("tds") in January 2025.

* **Header Bar:** A blue bar displays:
    * `[Admin]` suggesting administrative access.
    * The due date and time: `Due Sun, 9 Feb, 2025, 11:59 pm IST` (Indian Standard Time).
    * `Score: 0` indicating the current score.
    * Buttons: `Check all` and `Save`. The "Save" button is highlighted with a red arrow, indicating its importance.

* **Main Content:**
    * Large text: `TDS 2025 Jan GA` – likely a title or identifier for the exam.
    * `Instructions` heading followed by a numbered list:  The instructions explain that the user should check answers regularly using the "Check" button, save frequently using the "Save" button, and that reloading the page is acceptable. It also acknowledges potential browser issues and permits the use of external resources, even suggesting that the exam is "hackable."

The overall impression is that this is a timed online exam or assessment with a deadline of February 9th, 2025, and which allows the use of external resources. The highlighted "Save" button emphasizes the importance of saving answers regularly to avoid data loss.

---

## Post #52 by 21f3002277 (Post ID: 591042)
try with this




name: Set up Git user (23f2003853@ds.study.iitm.ac.in)

run: |

git config --global user.name “GitHub Actions Bot”

git config --global user.email “23f2003853@ds.study.iitm.ac.in”

---

## Post #53 by 23f2004752 (Post ID: 591052)
Thank you  for your help , my repo was not public before and can you also help me in g4 i got this “Error: At root: Property name mismatch”

---

## Post #54 by 21f3002277 (Post ID: 591057)
In g4 which Question have that error you are getting

---

## Post #55 by 23f2003751 (Post ID: 591084)
In the last two question of the ga,it is mentioned including both groups.so what is the meaning of this .


image
1622×601 85.5 KB


@Jivraj
 
@carlton

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/a/1a9317fe7d6814de3d65512fa7b3121c5a3c8710_2_690x255.png)

**Image Description:** The image contains a problem statement and a description of how to solve it using data analysis techniques.

**The Problem:**

The core task is to calculate the total Biology marks for students who achieved 17 or more marks in Physics, specifically within groups 43-66 (inclusive).  The data is stored in a PDF file named `q-extract-tables-from-pdf.pdf`.

**The Steps to Solve the Problem:**

The image outlines a four-step process:

1. **Data Extraction:**  Extract the data from the PDF using a PDF parsing library like Tabula, Camelot, or PyPDF2. The extracted data should be converted into a usable format such as CSV, Excel, or a DataFrame.

2. **Data Cleaning and Preparation:**  Convert the marks from the extracted data into numerical data types to ensure accurate calculations.

3. **Data Filtering:** Filter the data to identify only those students who scored between 17 and (presumably) a maximum Physics score in groups 43-66. The phrasing in the image is slightly unclear on the upper bound of the Physics score filter ("between 17 and Physics").

4. **Calculation:** Sum the Biology marks of the filtered students to find the total.

**Additional Information:**

The image also explains how automating this process benefits Greenwood High School by allowing for quicker identification of performance trends, more effective resource allocation, enhanced reporting efficiency, and the use of data-driven strategies in education.  The final line reiterates the question: What is the total Biology marks?

**Key Objects:**

* **File Name:** `q-extract-tables-from-pdf.pdf` - This is crucial as it indicates the location of the raw data.
* **Subject Names:** Maths, Physics, English, Economics, and Biology - These are the subjects included in the student marks table.
* **Group Numbers:** 43-66 - This specifies the relevant groups for filtering.
* **Score Threshold:** 17 - This is the minimum Physics score for inclusion in the calculation.
* **Target Subject for Summation:** Biology - The total marks to be calculated are those from the Biology column.


In summary, the image presents a data analysis problem involving extracting, cleaning, filtering, and calculating data from a PDF to answer a specific question about student performance.

---

## Post #56 by carlton (Post ID: 591083)
Hi Tushar,


If you looked at the PDF you might have realised that students have been grouped. The question gives you a range for the groups 43-66. Including both groups implies both group 43 and 66 are included in your calculation.


kind regards

---

## Post #57 by 23f2004752 (Post ID: 591089)
Question 4 "

Sample output


{

“25-02-04”: “Sunny intervals and light winds”,

“25-02-05”: “Light rain and light winds”,


}

Error: At root: Property name mismatch"

---

## Post #58 by 21f2000588 (Post ID: 591092)
Hi, even i’m facing the same issue,


image
1564×715 34.2 KB


image
1916×882 65.1 KB


image
1605×320 26.5 KB


@Jivraj


@Saransh_Saini


@carlton

Can anyone please help to fix this issue and submit this correctly.

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/1/a17230380d3428649017c6e760ea0ece0b99bf39_2_690x315.png)

**Image Description:** This image shows a GitHub Actions workflow run summary. 


Here's a breakdown of the key information:

* **Repository:** The workflow is running in the repository `DigvijaysinhChudasamaliTM/TDS_GA_4`.

* **Workflow Name:** The workflow is named "Daily Commit". This is a recurring workflow, as indicated by the naming convention.

* **Run Number:** This is run number 10 of this workflow.

* **Trigger:** The workflow was manually triggered 16 hours prior to the screenshot.

* **Status:** The workflow run was successful ("Success").

* **Duration:** The workflow completed in 18 seconds.

* **Workflow File:** The workflow is defined in a file named `daily-commit.yml`, triggered by a workflow dispatch event.

* **Jobs:**  The workflow consists of a single job named `daily-commit`. This job also shows a success status.

* **User:** The workflow was triggered by user `DigvijaysinhChudasamaliTM`, possibly via the GitHub interface. The commit SHA is visible as `e9aef97` on the `main` branch.


The image shows sections for "Summary", "Jobs", "Run details", "Usage", and "Workflow file".  The large blank space below the `daily-commit.yml` section might be a log area that is empty because the workflow finished successfully and without errors.  The numbers "7s" next to the final `daily-commit` suggests some kind of timing or duration detail within that job.

![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/7/67b187b35695e941e3bdf04461e4c4fa050c6e4d_2_690x317.png)

**Image Description:** The image shows a GitHub repository's contents.  The repository belongs to user `DigvijaysinhChudasamaliTM` and is named `TDS_GA_4`.  The primary focus is on a file named `daily-commit.yml` located within the `.github/workflows` directory.

**`daily-commit.yml` Content:** This file is a GitHub Actions workflow definition. It's designed to perform a daily automated commit to the repository.

* **`name: Daily Commit`**:  Specifies the workflow's name.
* **`on: schedule`**: Defines a schedule trigger.  Specifically, the `cron` expression `0 0 * * *` runs the workflow daily at 00:00 UTC.
* **`workflow_dispatch`**: Allows manual triggering of the workflow.
* **`jobs`**: Defines a job named `daily-commit` that runs on the `ubuntu-latest` runner.
* **`steps`**: A sequence of actions within the job:
    * **`Checkout repository`**: Checks out the repository's code.
    * **`Set up git configuration`**: Configures git user email and name for the commit.  The email is dynamically set using the GitHub Actions actor's email.
    * **`Create a file with a daily commit message`**: Creates a file named `daily-commit.txt` with the message "This is an automated daily commit".
    * **`Commit changes`**: Commits the changes to the repository.

**Other Notable Features:**

* The left panel displays the repository's file structure.  Besides `daily-commit.yml`, there's a `daily-commit.txt` file (likely created by the workflow), showing the file structure of the project.
* The top right indicates that the last commit to `daily-commit.yml` was made 17 hours prior to the screenshot, by `efuef57`.
* The interface strongly suggests this is a GitHub repository viewed through the GitHub website or a similar interface, with the usual Github interface components (code editor, file list, etc).


In short, the image shows a simple GitHub Actions workflow automating a daily commit to the repository, creating a file with a timestamped message.

![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/d/5d7f290214dcf1065f3b373c28d04671ef69f7c6_2_690x137.png)

**Image Description:** The image shows a dark-themed interface, likely from a software development tool or platform, providing instructions and displaying an error message. 


Here's a breakdown of the content:

* **Instructions:** The top section gives a three-step guide on how to interact with a workflow:
    1. Trigger the workflow and wait for completion.
    2. Verify it's the most recent action in the repository.
    3. Confirm a commit is created within 5 minutes of the workflow run.

* **Input Field:**  Below the instructions, there's an input field labeled "Enter your repository URL (format: https://github.com/USER/REPO)". A GitHub repository URL is already entered: `https://github.com/DigvijaysinhChudasamalITM/TDS_GA_4`.

* **Error Message:** At the bottom, an error message is displayed: "Error: No executed job step matches 21f2000588@ds.study.iitm.ac.in".  This indicates a problem in a specific job step within the workflow, referencing a particular email address or identifier (`21f2000588@ds.study.iitm.ac.in`).


In summary, the image shows the steps to verify a GitHub workflow and highlights an error encountered during its execution. The error message suggests a mismatch between expected and actual job step execution, likely related to authentication or permissions.

---

## Post #59 by 23f2003853 (Post ID: 591093)
21f3002277:




Set up Git user (23f2003853@ds.study.iitm.ac.in)






Still the same error appears

---

## Post #60 by 23f2003853 (Post ID: 591098)
Thanks for providing clarification Sir

---

## Post #61 by 22f2001640 (Post ID: 591102)
I am also facing same issue can’t resolve.

---

## Post #62 by 21f2000588 (Post ID: 591103)
@Jivraj
 
@carlton
 
@Saransh_Saini

In ques 4 Scrap the BBC Weather API,

I scraped the locationId for my city (i.e Mumbai)


and post that also mapped each 
issueDate
 to its corresponding 
enhancedWeatherDescription
 .


The sample output mentioned was:

The output would look like this:


{
  "2025-01-01": "Sunny with scattered clouds",
  "2025-01-02": "Partly cloudy with a chance of rain",
  "2025-01-03": "Overcast skies",
  // ... additional days
}



And My Output after scraping (And as explained by professor in Video 2 BBC weather was)


{

“2025-02-05”: “A clear sky and light winds”,

“2025-02-06”: “A clear sky and light winds”,

“2025-02-07”: “A clear sky and light winds”,

“2025-02-08”: “A clear sky and light winds”,

“2025-02-09”: “A clear sky and light winds”,

“2025-02-10”: “A clear sky and light winds”,

“2025-02-11”: “A clear sky and light winds”,

“2025-02-12”: “A clear sky and light winds”,

“2025-02-13”: “A clear sky and light winds”,

“2025-02-14”: “A clear sky and light winds”,

“2025-02-15”: “A clear sky and light winds”,

“2025-02-16”: “A clear sky and light winds”,

“2025-02-17”: “A clear sky and light winds”,

“2025-02-18”: “A clear sky and light winds”,

“2025-02-19”: “A clear sky and light winds”

}


But it’s giving Error::

Error: At root: Different number of properties


Can you please help how to fix this issue.

---

## Post #63 by 22f2001640 (Post ID: 591108)
Issue resolved for me after following below step

After creating the workflow:




Trigger the workflow and wait for it to complete


Ensure it appears as the 
most recent action
 in your repository


Verify that it creates a commit during or within 5 minutes of the workflow run

---

## Post #64 by 23f2004752 (Post ID: 591109)
In place of “name: Setup up GIT config” change to “name: add commit {your_email}”

---

## Post #65 by 21f3002277 (Post ID: 591114)
use this 
Google Colab
 with the city name to get the Json Body just change the date format.


@23f2004752

---

## Post #66 by JoelJeffrey (Post ID: 591127)
@carlton
 
@Jivraj
 could you please help me with this?

---

## Post #67 by 21f2000588 (Post ID: 591132)
On running this colab with city = Mumbai,


I’m gettingh this error: Error: At root: Property name mismatch

---

## Post #68 by 21f3002277 (Post ID: 591138)
it’s getting,


{
    "2025-02-06": "Sunny and a gentle breeze",
    "2025-02-07": "Sunny and a gentle breeze",
    "2025-02-08": "Sunny and a gentle breeze",
    "2025-02-09": "Sunny and a gentle breeze",
    "2025-02-10": "Sunny and a gentle breeze",
    "2025-02-11": "Sunny and a gentle breeze",
    "2025-02-12": "Sunny and a moderate breeze",
    "2025-02-13": "Sunny and a gentle breeze",
    "2025-02-14": "Sunny and a gentle breeze",
    "2025-02-15": "Sunny and a gentle breeze",
    "2025-02-16": "Sunny and a gentle breeze",
    "2025-02-17": "Sunny and a gentle breeze",
    "2025-02-18": "Sunny and a gentle breeze",
    "2025-02-19": "Sunny and a gentle breeze"

}

---

## Post #69 by 23f2003853 (Post ID: 591145)
can tell me in your .yml which are all place did you use your iitm email id.  Because I got the error No executed job step matches 23f2003853@ds.study.ittm.ac.in. My commit was completed in 11 seconds

---

## Post #70 by 22f2001640 (Post ID: 591152)
@s.anand
 
@carlton
 
@Jivraj

Is there any way to crack this , I tired multiple time no improvement.

Also what does this " It is 
very hard
 to get the correct Markdown output from a PDF. Any method you use will likely require manual corrections. Reformatting with Prettier helps standardize the output format for comparison." mean.


image
1327×743 41.6 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/f/7f9f1180300c81f729381ebb2a3391c53648a28f.png)

**Image Description:** The image shows a coding exercise with instructions and a response area.  The exercise focuses on converting a PDF file (`q-pdf-to-markdown.pdf`) into a Markdown file, formatting it using Prettier (version 3.4.2), and submitting the formatted file.

**Instructions:**

The instructions are clearly laid out in three steps:

1. **Convert the PDF to Markdown:**  Extract the content from the PDF, maintaining its structure and formatting as accurately as possible.

2. **Format the Markdown:** Use Prettier 3.4.2 to format the Markdown.

3. **Submit the Formatted Markdown:** Submit the final, formatted Markdown file.

The instructions also explain the impact of the exercise—contributing to EduDocs Inc.'s mission of providing high-quality, accessible educational resources by automating the PDF-to-Markdown conversion process.  It highlights the benefits of automation, including enhanced productivity, improved quality, scalability, and easier integration with various digital platforms.

**Response Area:**

The user is asked to provide the Markdown content of the PDF, formatted with Prettier. A text box is provided for input.  The user's initial attempt is shown:

`Ater vulnero solio tabula.
Auctus benigne coaegresco defetiscor delinquo.
Talio balbus cultura vae. Sint deripio tener adfectus agnitio aro cruentus arbustum. Abstergo alii sollers.`

This attempt is marked as "Incorrect. Try again."  Below this, there is an explanation of the inherent difficulty in converting PDFs to Markdown perfectly, emphasizing that manual corrections are often necessary, and that using Prettier helps standardize the output.

**Other Features:**

* **File Name:** The PDF file name, `q-pdf-to-markdown.pdf`, is prominently displayed.
* **Prettier Version:** The specific version of Prettier to use (3.4.2) is clearly stated.
* **Error Indicator:** A small red circle with an exclamation mark (`!`) in it is visible in the response area, indicating an error.


In summary, the image depicts a coding challenge involving PDF to Markdown conversion and formatting, providing context, instructions, a response area, and feedback to the user.

---

## Post #71 by 22f3001315 (Post ID: 591173)
Same problem please help me too if you get it right.

---

## Post #72 by 21f2000588 (Post ID: 591190)
Yes followed all these steps, and still the error is being seen,


Error: No executed job step matches 21f2000588@ds.study.iitm.ac.in

---

## Post #73 by 21f2000588 (Post ID: 591191)
Yes true,


Here’s the output:

{

“2025-02-05”: “Sunny and a gentle breeze”,

“2025-02-06”: “Sunny and a gentle breeze”,

“2025-02-07”: “Sunny and a gentle breeze”,

“2025-02-08”: “Sunny and a gentle breeze”,

“2025-02-09”: “Sunny and a gentle breeze”,

“2025-02-10”: “Sunny and a gentle breeze”,

“2025-02-11”: “Sunny and a moderate breeze”,

“2025-02-12”: “Sunny and a gentle breeze”,

“2025-02-13”: “Sunny and a gentle breeze”,

“2025-02-14”: “Sunny and a gentle breeze”,

“2025-02-15”: “Sunny and a gentle breeze”,

“2025-02-16”: “Sunny and a gentle breeze”,

“2025-02-17”: “Sunny and a gentle breeze”,

“2025-02-18”: “Sunny and a gentle breeze”

}


But unfortunately this error persists,


Error: At root: Property name mismatch

---

## Post #74 by 23f2003853 (Post ID: 591192)
Now re-check you answer. May it will give link where the issue exists. if it gives url browsers the link and address.

---

## Post #75 by 21f2000588 (Post ID: 591193)
Yes true same happened with me.

---

## Post #76 by 23f2003853 (Post ID: 591194)
re-check your answer again it may give an url. check the url

---

## Post #77 by 21f2000588 (Post ID: 591195)
Now on rechecking, the error message has changed to – “TypeError: Failed to fetch”

---

## Post #78 by 21f2000588 (Post ID: 591196)
No its giving such error:


image
1729×278 15.2 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/d/ad4d5271fd3d95f8e832eaa212705300b96245cc_2_690x110.png)

**Image Description:** The image shows a dark-themed interface, possibly from a web application or software, with a form for entering a GitHub repository URL.

**Key elements:**

* **Instruction Text:**  "Enter your repository URL (format: https://github.com/USER/REPO)" This clearly indicates the expected input format.

* **Input Field:** A text input field where a user is supposed to enter a GitHub repository URL. The URL "https://github.com/DigvijaysinhChudasamalITM/TDS_GA_4" is already partially filled in.  A small, circular "i" icon is visible in the upper-right corner of the input field, suggesting there might be additional help or information available.

* **Error Message:** Below the input field, an error message is displayed: "TypeError: Failed to fetch". This indicates that the application was unable to retrieve information from the entered (or partially entered) repository.

* **Check Button:** A blue button labeled "Check" suggests a process for validating or accessing the provided repository URL.

**Overall interpretation:**

The user attempted to enter or verify a GitHub repository URL, but the system encountered an error during an attempt to fetch information from the repository.  The error message suggests a problem during the data retrieval process, likely network related or a problem with the repository itself. The “i” button may give more detail about the input field.

---

## Post #79 by 21f2000588 (Post ID: 591197)
Here’s the action’s:


image
1921×467 45.4 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/5/35164c425fd9bac93a22a798ceb50aff9245edfc_2_690x167.png)

**Image Description:** The image shows a screenshot of a GitHub Actions interface.  Here's a breakdown of its content:

**Left Panel (Actions):** This section lists various categories within GitHub Actions:

* **Actions:**  The main heading.
* **All workflows:** A search bar or filter for workflows.
* **Daily Commit:** A specific workflow listed.
* **Management:** A category likely containing settings and configurations.
* **Caches:**  Likely related to caching build artifacts.
* **Attestations:**  Relates to verifying software components.
* **Runners:** The machines used to execute workflows.
* **Usage metrics:** Statistics about resource consumption.
* **Performance metrics:**  Metrics for workflow speed and efficiency.
* **New workflow:** A button to create a new workflow.

**Right Panel (All Workflows):** This section displays information about currently running and recently completed workflows.

* **All workflows:** The heading indicating the section shows all workflows.
* **Showing runs from all workflows:**  Clarifies that the data shows runs from all workflows, not just a selection.
* **Help us improve GitHub Actions:** A feedback request from GitHub.
* **15 workflow runs:** Indicates the number of workflow runs shown.
* **Two workflow entries:** Each entry shows:
    * A green checkmark indicating successful completion.
    * The workflow name ("Daily Commit").
    * The workflow run number ("#15" and "#14").
    * Who manually triggered the run ("DigvijayChudasamaTM").
    * The branch ("main").
    * The time since completion ("13 minutes ago").
    * An icon showing percentage of workflow completion (16% and 17%).
    * A three-dot menu icon for more options.

**Top Right Corner:**

* **Filter workflow runs:** A search bar to filter the displayed workflow runs.
* **Give feedback:** A button to provide feedback to GitHub.

In summary, the image depicts a portion of a GitHub Actions dashboard showing a list of recently completed workflow runs, primarily from a workflow titled "Daily Commit," alongside options for managing workflows and providing feedback. The screenshot suggests a user regularly runs the "Daily Commit" workflow manually.

---

## Post #80 by 23f2003853 (Post ID: 591199)
Check you Github account and browse Action for your repo. then check All Work flows. Ensure the first item is schedule triggered confirmation

---

## Post #81 by 21f2000588 (Post ID: 591200)
What you meant by " Ensure the first item is schedule triggered confirmation"? You meant the latest one should be this right?


image
1920×889 82 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/8/3812c6855de7c05b79750c6f57eed987122e24f4_2_690x319.png)

**Image Description:** The image shows a GitHub Actions workflow runs page.  The top shows the repository name `DigvijaysinhChudasamaliTM/TDS_GA_4`.  The left sidebar lists various sections: Code, Issues, Pull requests, Actions (selected), Projects, Wiki, Security, Insights, and Settings. Under "Actions," we see "All workflows" and then a list of options under "Management," including Caches, Attestations, Runners, Usage metrics, and Performance metrics.

The main content area shows "All workflows" and then the following:

* **A banner asking for feedback:** "Help us improve GitHub Actions. Tell us how to make GitHub Actions work better for you with three quick questions."  There's a "Give feedback" button.

* **A list of 15 workflow runs:**  Each run displays:
    * **Status:** A green checkmark (successful) or a red X (failed).
    * **Workflow name:** "Daily Commit" for all listed runs.
    * **Run number:**  A number indicating the specific run (e.g., #15, #14, etc.).
    * **Trigger:**  Indicates whether the run was manually triggered ("Manually run by DigvijaysinhChudasamaliTM") or scheduled ("Scheduled").
    * **Branch:** "main" is shown for each run.
    * **Time since run:** Displays time elapsed since the run completed (e.g., "18 minutes ago," "4 hours ago").
    * **Run duration:** Shows how long the run took (e.g., "16s").

The top right shows a search bar,  and  a filter box to filter workflow runs.  The user interface is dark-themed.  Overall, the screenshot displays a typical GitHub Actions page showcasing recent workflow run statuses and details.

---

## Post #82 by 23f2003853 (Post ID: 591204)
check this type of screen


image
1000×286 16.8 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/c/3c228c6f00a24b93336be15b4aa8f8c04c13f168_2_690x197.png)

**Image Description:** This image shows a section of a GitHub Actions workflow run interface.  Here's a breakdown of the content:

* **Top Section (Feedback Request):**  A banner invites the user to help improve GitHub Actions by answering three quick questions. A "Give feedback" button is present.

* **Middle Section (Workflow Runs Summary):**  This section states that there are "71 workflow runs" in total.

* **Bottom Section (Specific Workflow Run):** This section details a specific workflow run:

    * **Username/Email:** `23f2003853@ds.study.iitm.ac.in` is identified as the user who initiated the run.
    * **Run Details:** A more detailed description shows that this is run #23, and it was manually triggered by the same user (`23f2003853@ds.study.iitm.ac.in`).
    * **Branch:** The `main` branch is specified.
    * **Time Elapsed:** The run finished 23 minutes ago and lasted for 19 seconds.
    * **Event, Status, Branch, Actor Columns:** The presence of these columns indicates a table view, allowing for filtering and sorting of the workflow runs.  The dropdown arrows suggest filtering options are available.


In short, the image provides a snapshot of recent GitHub Actions activity, highlighting a specific manually triggered run and inviting the user to provide feedback. The email address suggests a possible university or educational setting (`iitm.ac.in`).

---

## Post #84 by 23f2004752 (Post ID: 591209)
use name:email inside yml page

---

## Post #85 by 21f2000588 (Post ID: 591212)
Yep done, thank you!

---

## Post #87 by 24ds3000090 (Post ID: 591251)
Depopulo amoveo curo.
Concego creatinue ancilla vesper conicio cinimatico eribro.  
Custodia anica arbustum coniceto suma corporis aduno commenoro curiositas augero.  
Uredo thesis ancilla alter eun tener vomito praesentium templum.  
Magni deprimo celebre.

### Bellum pelor cornu vorax perspiciatis.

Labore elus umerus voluntarius.  
Vicissitudo cilíctum cicuta campana.  
Desino perspiciatis comodo.

### amarttudo tabesco crinis amissio

tui qui decumbo vobis  
audacia charismatubineus contigo  
aro eum talio elus  
coniuratio cubo ab vere  
validus tam patria deficio  
agnosco spectaculumcoerceo  
spectaculum vulpes valetudo  
minima cado suffragium  
asperiores thesaurus cometes  
vesica amplus cimentarius  
volum curiositas cornu

## Paupertrucido confido triduana ante sublime

# Consequatur comminor

Coadunatio delectus atqui placeat atque copia ventosus aer quae.  
Tatillo causa damatico validus torrena tivpinca.  
Adside nisi atavus aspiente.

[soius tam](https://tds.s-anand.net/#/markdown)

Ceno usilio desino velociter sit aut. Concedo accedo vac congregatio sperno venia sum sordeo animi tametsi. Accusamus suppellex turpis dedecor uliam vaco venusit:

- tu! amicitia ante suppellex studio
- utor debilito suasoria odio
- antea desino despecto magni

[coadunatio voco](https://tds.s-anand.net/#/markdown)

[incidunt aliquam](https://tds.s-anand.net/#/markdown)

Tametsitenuis conscendo.

- tempore vorner aestas commentoro
- absconditus coruscus

## Blanditiis tabula animi succedo

Asper summa tametsi ustulo villias conservo clam triumphus tener ager. Audax conforto adopto vesco arbustum deorsum terror impedit iure. Adsum atrox caries acc

Beatae ducimus aperio amarttudo caries

- cinis solvo unde unde arbustum
- canis civitas viro
- thorax pax demens
- arbustum suficco thorax testimonium ex.
- vinliter sumptus

Explicabo defico adfectus.

Comedo cattus justo tamdiu tumultus confido thesaurus coadunatio volutabrum. Succedo tabula audax copia vinculum.

**cogo audio suffragium**

crepito amiculum sufficio  
acer aestas utor  
debeo adopto utpote  
tametsi curatio ante

## Maxime vulgo depulso decipio atrox

## Career debeo

**conatus cui admoneo**

theatum pauper tego
pecco caeous vulgo
cursim desino arceo
balbus comminor et 



In the question no. 10, I have tried numerous time to get it right markdown content but it was incorrect all the time.


I have tried these steps:


import pymupdf4llm
md_text = pymupdf4llm.to_markdown("/content/q-pdf-to-markdown.pdf")

import pathlib
pathlib.Path("output.md").write_bytes(md_text.encode())



Then i run this in bash


prettier --write output.md



And what i got frankly telling was far from this, I did some manual touchups, and this what i have now. This is the best version i could come up with. Saw the preview, it does matches with the pdf.


#Can
 someone please advise me a better approach?

---

## Post #89 by 23f2004752 (Post ID: 590704)
hey, can you help me in doing this i can’t able to do this.

---

## Post #90 by carlton (Post ID: 591265)
@24ds3000090


We will be changing this question. Even we found it hard 


Kind regards

---

## Post #91 by carlton (Post ID: 591266)
@JoelJeffrey


We will be changing this question. Even we found it pretty hard 


Kind regards

---

## Post #92 by daksh76 (Post ID: 591276)
sir in the weather question could you provide from where do we get the bbc api because i have searched a lot and havent been able to find it

---

## Post #93 by carlton (Post ID: 591280)
https://tds.s-anand.net/#/bbc-weather-api-with-python

---

## Post #94 by gouthamnischay (Post ID: 591290)
try manually inspecting the output of the api and compare it with your script output.

Or else try refreshing the browser and check.

---

## Post #95 by 23f2004752 (Post ID: 591301)
@carlton

Previously i got correct on q2 but now i am getting the error when i refresh the page “TypeError: Cannot read properties of null (reading ‘textContent’)”

---

## Post #96 by 23ds3000149 (Post ID: 591322)
Please try city=“Mumbai” as a string literal.

---

## Post #97 by Nelson (Post ID: 591331)
Q4 BBC Weather


I don’t understand why I am getting




Error: At root: Different number of properties




Is it because of different dates? Shall I match the dates?


@carlton
 Please guide. Thank you.


BBC weather
565×781 30.5 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/7/e7c12cee82eccb262d1c2752a98e95c3c3a94457.png)

**Image Description:** Here's a description of the image's content:

The image shows a coding exercise or a debugging problem within a user interface.  The top section describes a task involving the BBC Weather API.  The task is broken down into three steps:

1. **API Integration and Data Retrieval:**  Fetching weather data using the API and `locationId`.
2. **Weather Data Extraction:** Retrieving weather forecast data.
3. **Data Transformation:** Extracting `issueDate` and `enhancedWeatherDescription` and creating a JSON output.

An example of the expected JSON output format is provided:  A JSON object where dates (like "2025-01-01") are keys, and weather descriptions are values.  There's a slight error in the example JSON provided, with "202" instead of "2025" in two lines. A red arrow points to these lines indicating a possible source of confusion or error.


Below this is the coding challenge:  "What is the JSON weather forecast description for Osaka?". The user has inputted a JSON object, attempting to answer the question.  However, at the bottom, there's an error message: **"Error: At root: Different number of properties"**. This suggests the user's JSON input has a different number of key-value pairs than what is expected. A "Check" button is available, presumably to validate the answer.

The key elements are:

* **Task instructions:**  Clearly define the three stages of the API interaction, including specific field names like `locationId`, `issueDate`, and `enhancedWeatherDescription`.
* **Example JSON:** Shows the structure of the expected output, indicating key-value pairs of date and description.
* **User's input:** The JSON object that the user has provided as a solution.
* **Error message:** Indicates that the provided JSON is incorrect, specifically due to a mismatch in the number of key-value pairs.
* **City name:** The location whose weather data needs to be retrieved and formatted.  Here it is "Osaka".

The image strongly suggests a programming assignment or a debugging scenario focused on JSON data handling and API interaction.  The error message points to a common problem in JSON validation.

---

## Post #98 by 23F300327 (Post ID: 591418)
thema coruscus




cupiditate celebrer


argentum alius voro soluta


sto decor capto suffoco acs tempus deludo deleo ventus odio




Sordeo tergo beatae coniecto ambitus carus. Vae tamdiu debilito verto confugo

territo acies vos patria. Versus surgo degero vester tersus paulatim chirographum










abeo


super


valetudo adhuc










conatus


comptus


spiculum summisse






alienus


addo


demergo conturbo






uberrime


subseco


altus & ea






apto


cursus


infit & summa










tabula necessitatibus beneficium concido


adhaero tepesco ars


adnuo beatae


cursim ahsens culpa animi aestivus




Solium vulgus commodo claro curriculum valens


Aut ipsum spiritus tantillus vacuus adsum crebro animus pel paulatim. Tunc vallum

torqueo aequus valens triduana illo. Uredo cursus fuga vir.


Cultellus adipiscor incidunt tondeo benevolentia capto contabesco bene tardus

harum.


Bos subnecto beatae abeo vulnus terra verus balbus




arguo via vallum usus aliquid


tempus balbus videlicet acquiro




attonbitus tardus versus cuppedia

derelinctuo curatio stalla solen

comburo commodo caveo at

deporto aliquid thymum

confero sortitus ago

triduana umquam acies


Beneficium doloremque aspernatur dolor dolorum despecto attonbitus unus alienus

Capto optio dolores.

Commodi sono denuo molestiae terebro

Benigne anser vulgus brevis coaegresco vinum debeo.

Cras aut ullam error terreo absque aro adstringo sublime thymum


Triumphuslaudantium curto certus


Callide stabilis subito claudeo occaecati depono. Turba thymum bis deludo una.

Sumo consuasor necessitatibus vix solitudo dolorum dolorem vinco inflammatio




apparatus spero sulum desino ultra


nauner necessitatibus bos calculus nlaceat


animadverto defessus triumphus


acquiro artificiose minima sortitus terminatio




Aegrus tot tot aetas. Clinís volva tamen sumptus. Solutio deludo suscipio deputo

demens vero audeo annus alo accendo.


I am getting error: Incorrect. Try again.


@Jivraj
 
@carlton
 can you please explain the reason for this error

---

## Post #99 by carlton (Post ID: 591417)
Hi Mishkat


Please refer to this post.










GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]
 
Tools in Data Science






@JoelJeffrey
 
We will be changing this question. Even we found it pretty hard 
 
Kind regards
  




Kind regards

---

## Post #100 by ShahbaazSingh (Post ID: 591469)
@s.anand
 Sir the question 10 of the Graded Assignment 4 is very tough I have tried everything from custom python codes using different libraries to online converted and also formatted using prettier. Please sir guide me how to do the question.

---

## Post #101 by 21f2000588 (Post ID: 591471)
Yep figured that, and after matching the data solved the error and got that question correct.

Though thank you.

---

## Post #102 by ShahbaazSingh (Post ID: 591472)
@s.anand
 Sir I have done the question 2 of the graded assignment but I am very curious to know why the answers language gets periodically change. Is there some kind of backend code which is responsible for that or is something else ?

---

## Post #103 by 21f2000588 (Post ID: 591473)
Yes we’ll were facing this issue.


@carlton
 sir mentioned yesterday that they will change the question.


"We will be changing this question. Even we found it hard 


Kind regards"


So need to worry about that question for now.

---

## Post #104 by ShahbaazSingh (Post ID: 591475)
OK, that is good to hear, you won’t believe that yesterday I was trying this question for 2 hours literally, it can be more also.

---

## Post #105 by 21f2000588 (Post ID: 591476)
I was stuck at that question for 2 days, I tried multiple ways but was not able to format the content with prettier as expected, every time I was getting the error “Incorrect. Try again.”

---

## Post #106 by s.anand (Post ID: 591487)
On popular demand, I’ve made Q10 of GA4 easier (converting from PDF to Markdown). The question remains the same, but the check is more liberal and the error messages are more helpful. Please give it a shot now.


(FYI, one person 
did
 solve it. A colleague, not someone from the IITM DS program.)

---

## Post #107 by 21f2000588 (Post ID: 591503)
Hello Sir, i tried but unfortunately after extracting the contents and formatting the contents and submitting it, it’s showing various errors like Missing links, Missing tables…


But on checking the file i wasn’t able to find any single table in the contents in that case what could be done to fix these errors?


@Jivraj
 
@carlton
 
@Saransh_Saini

---

## Post #108 by 23f2003751 (Post ID: 591517)
same issue with me as well

---

## Post #109 by 23f2003853 (Post ID: 591544)
Sir I checked the pdf file, there is only one place unorder list is given and the same is available in my answer. But the system throws error Missing List (I tried with other symbols * and + also) . Please inform me where I made mistake


image
1108×271 5.87 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/1/b12c7242be994f334d445739cf3b6ffe1b36c25f.png)

**Image Description:** Here's a description of the image content:

The image shows a code editor or similar interface displaying a question and a result.  The question at the top asks: "What is the markdown content of the PDF, formatted with prettier@3.4.2?".

Below the question is a large, mostly empty white rectangular box with a thin maroon border. Within this box, a list of four lines of Latin text is visible, each preceded by a hyphen:

* `cuppedia tamquam facilis confugo`
* `conservo depereo`
* `consectetur arx`
* `aeternus celebrer`

Each word in these lines is underlined in red with a wavy line, suggesting an error or a warning.  The large box appears to be where the formatted markdown output should be, but it is blank.  

At the very bottom, outside the maroon box, an error message reads: "Error: Missing lists".  There's also a small, dark gray vertical bar on the right edge of the image, which looks like the typical scrollbar in a code editor.  Near the top of that scroll bar is a small red circle containing an exclamation mark (!), indicating an error.

---

## Post #110 by 23f2003853 (Post ID: 591545)
this is table. Check it


image
313×136 5.2 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/d/7d3c3c9414b2bc8323097d34e3ff54b8234f535e.png)

**Image Description:** The image contains three columns of Latin words.  Each column appears to be a list of related vocabulary words.  There are no other features or objects in the image besides the text.  The words are arranged neatly in three columns with a clear space between them.  The words at the top of each column are in a slightly bolder font, suggesting they may be headings or titles for each list.

---

## Post #111 by Nelson (Post ID: 591549)
Q 10 - PDF to Markdown.


Why it is saying




Incorrect. Try again?




Do I need to add CSS?


Carbo ventosus tametsi patior. Recusandae ciminatio alienus nisi ventosus apud. Theatrum abutor aperio spargo vestrum virga placeat adulescens. Deripio alveus creator omnis tabula patria cupiditate in virga speculum. Acidu`s alienus vehemens vapulus.


earum clamo collum

curtus careo curatio

tendo sunt culpo

Suus sit magni traho tempora.


Depraedor vae dedecor conturbo. Curia vigor vinco terebro alii tantum clam. Modi veniam alveus clementia sumo iusto adfero truculenter.










cresco


solio


ademptio


terreo


bis










tardus


carpo


allatus


depono


benevolentia






tunc


atavus


barba


urbs


considero






adulescensamplitudo




verbum


cultura


id






cenaculum


ipsum


sursum


conturbo


nemo






damno


arbitro


quibusdam


articulus


animadverto










ustulo crudelis depraedor


sophismata tener apostolus suus adopto


coniecto maxime rerum


acceptus virga confero comes




cresco vomito


deputo ceno


Cuppedia uberrime socius atque paens


Sto theca testimonium aestus debitis


valde vulgus

---

## Post #112 by Nelson (Post ID: 591551)
I checked many times. For me it says “Incorrect. Try again.”

---

## Post #113 by 21f2000588 (Post ID: 591572)
Ya i know, i added tables, list, blockquote, code, tables have all been added still it’s showing errors. Not sure where am I going wrong.

---

## Post #114 by 23f2003853 (Post ID: 591573)
Please refer video and document relating to Question 1 of Assignment 3. There it is mentioned how to mark bold, table etc., use those marks

---

## Post #115 by Nelson (Post ID: 591580)
I have added all those and pasted the markdown and it appears as 
above
.


`` Carbo ventosus tametsi patior.
Recusandae ciminatio alienus nisi ventosus apud.
Theatrum abutor aperio spargo vestrum virga placeat adulescens.
Deripio alveus creator omnis tabula patria cupiditate in virga speculum.
Acidu`s alienus vehemens vapulus. ``

**earum clamo collum**
curtus careo curatio
tendo sunt culpo
Suus sit magni traho tempora.

Depraedor vae dedecor conturbo. Curia vigor vinco terebro alii tantum clam. Modi veniam alveus clementia sumo iusto adfero truculenter.

| cresco              | solio   | ademptio  | terreo    | bis          |
| ------------------- | ------- | --------- | --------- | ------------ |
| tardus              | carpo   | allatus   | depono    | benevolentia |
| tunc                | atavus  | barba     | urbs      | considero    |
| adulescensamplitudo |         | verbum    | cultura   | id           |
| cenaculum           | ipsum   | sursum    | conturbo  | nemo         |
| damno               | arbitro | quibusdam | articulus | animadverto  |

- ustulo crudelis depraedor
- sophismata tener apostolus suus adopto
- coniecto maxime rerum
- acceptus virga confero comes

[cresco vomito](;;;)

[deputo ceno](;;;)

# Cuppedia uberrime socius atque paens

# Sto theca testimonium aestus debitis

[valde vulgus](;;;)




Below is the screenshot of provided PDF. That font colour strains my eyes. Any particular reason for that PDF?


image
541×439 20.9 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/c/5c7b1a8077a70f4a4dc9a91b49a22dd26d960153.png)

**Image Description:** The image contains a text written in a serif font, likely Latin.  The text appears to be broken into several sections.

**Top Section:** This section contains longer sentences, appearing to be complete grammatical structures. It includes words like "Carbo ventosus," "Recusandae ciminatio," "Theatrum abutor," and "Acidus alienus."

**Middle Section:** This section is formatted differently, with lists of words, seemingly pairs or small groups of words, grouped together.  Some examples are:  "cresco solio ademptio," "tardus carpo allatus," and "adulescensamplitudo verbum."  There are also some bullet points with phrases such as "ustulo crudelis depraedor."

**Bottom Section:**  This section contains two lines of text. The first line reads "Cuppedia uberrime socius atque paens" and the second line reads "Sto theca testimonium aestus debitis".  Some words are highlighted in blue, indicating they may be important or hold a specific meaning within the context of the larger text. The highlighted words in this section include "cresco vomito", "deputo ceno", and "valde vulgus".

The overall appearance suggests a scholarly or academic document, possibly a linguistic study, a collection of phrases or vocabulary from an ancient language (possibly Latin). The formatting and organization might indicate an attempt to categorize or analyze the words, possibly based on their root, meaning or grammatical function.  The highlighted words could be key terms for a particular study or a specific focus of the research.

---

## Post #116 by 22f2001590 (Post ID: 591584)
I am getting missing link error. I checked in the pdf file also, the blue color text seems a link but its not clickable.

Any suggestion to move nearer to the actual solution.

---

## Post #117 by Nelson (Post ID: 591585)
You may try like this: 
cresco vomito


[cresco vomito](;;;)

---

## Post #118 by swatikap (Post ID: 591596)
Even I’m getting a similar error in Q2, it is expecting a foreign title whereas my search result gives only English titles.


image
1614×250 14.4 KB

Please help.

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/7/f771adcf2eab4ec0113e32a15b3200bd8e1a30dc_2_690x106.png)

**Image Description:** The image shows a JSON data snippet and an error message.

The JSON data represents information about a TV show:

* **id:** "tt8712204"  (Likely an identifier from an external database like IMDb)
* **title:** "25. Batwoman" (Suggests this is episode 25 of the show Batwoman)
* **year:** "2019-2022" (Indicates the show's run period)
* **rating:** "3.6" (A numerical rating, possibly out of 5 or 10)

Below the JSON data, there's an error message:  "Error: At [12] title: Values don't match. Expected: "13. Pideme lo que quieras". Actual "13. Ask Me What You Want""

This error message indicates a discrepancy in the 'title' field. The system expected the title to be "13. Pideme lo que quieras" (Spanish for "13. Ask Me Whatever You Want"), but the actual value was "13. Ask Me What You Want".  This suggests a validation or data consistency check failed.  The number 12 likely refers to the line or index where the error occurred within the larger dataset from which this snippet is extracted.

---

## Post #119 by Siddhu3050 (Post ID: 591636)
I think the idea behind this font is to make it difficult for people to manually work on the markdown file from scratch. I guess they want us to use the tools (like PyMuPDF4LLM, markitdown) they provided as resources to convert pdf into a markdown and then may be we can do some manual intervention to make it to the result as the scraping tools are not 100% accurate.


Could be another reason too. TAs’ can feel free to pitch in.

---

## Post #120 by carlton (Post ID: 591802)
A post was merged into an existing topic: 
Tds: assignment is not submitting

---

## Post #121 by 23f2004752 (Post ID: 591805)
your last saved score (i.e.6 of your’s) will be official score and forgot about seek portal , it is not meant for this type of assignment.

---

## Post #122 by 23f2004644 (Post ID: 591812)
Thank you for the update! I gave Q10 another shot, and I was able to solve it this time. The more liberal checks and improved error messages made a big difference in understanding where I was going wrong.

Thank again.

---

## Post #123 by 23f2004636 (Post ID: 591815)
Can we use hacking to get answers to some questions? Has anyone ever done it?

---

## Post #124 by 23f3003594 (Post ID: 591818)
What format is required for the “missing links” here


image
1973×849 93.6 KB


Here is my markdown


- statua demulceo amaritudo tametsi

- tam ante

- dens spiritus

- thema succurro sollers audio

Conforto conor tum deputo caecus cervus coepi aegrotatio totam xiphias. Repudiandae ducimus acerbitas ademptio . Delectatio tamquam suus.

Centum usitas tamen cedo auctus turpis video clibanus. Correptius beatus crepusculum decens succedo alias aperte decumbo trado. Talio universe deduco caute sui u

vester undique

- subito umbra

- caritas saepe

- taceo concido bos

Tenetur exercitationem numquam ultio tyrannus aeger vindico. Subvenio ambulo vacuus. Quidem quam tactus tracto aureus cupiditas.

thema astrum

# Spero uter

Harum cometes damnatio theologus virgo aperiam velut cursim.

**venustaspeccatus adsum**

acidus quisquam torrens

clam adeptio virga

Depulso claro consectetur concedo aveho bis pectus traho nobis. Cura adicio colligo corporis eligendi soluta ducimus carus. Allatus sapiente summa atqui deludo cur




Terebro vallum rem velociter currus suppellex.

Viduo damno ustilo valetudo.

Tribuo una vorago sui testimonium angelus suscipio eius demulceo civis.



Delectus coniecto repellendus amoveo amissio incidunt




Audax teneo centum cilicium vigor venio.

Patria credo tonsor.

Defessus pax volup vomito creator video campana cedo vita votum.

Laudantium victoria aer via tepidus.

Adulescens corporis triumphus coruscus sordeo trans dolorum.



- doloremque cum allatus aduro

- inventore thalassinus

- aperiam tergiversatio

- contigo alienus aranea cito cogo

Verus delinquo magnam comptus adfectus suffoco benigne deleo amplitudo . Cura deleniti theologus vestigium aranea denique vester doloribus . Venio cimentarius cr

depereo subvenio

---

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/6/d6aa4b0f5bcd99eccd628b708f0821f56116e4f4_2_690x296.png)

**Image Description:** The image contains a coding exercise or quiz related to converting PDF content to Markdown format.

**Key Text and Information:**

* **Title:** "Impact" - This is likely the title of the exercise or section.
* **Introduction:**  A paragraph explains the context:  automating PDF to Markdown conversion for educational resources provided by EduDocs Inc.  It highlights benefits like enhanced productivity, improved quality, scalability, and integration.
* **Exercise Question:** "What is the markdown content of the PDF, formatted with prettier@3.4.2?"  This is the core question of the exercise.
* **PDF Content (to be converted):** A block of Latin text is presented, representing the content of the PDF file. This text is:

```
Audax teneo centum cilicium vigor venio.
Patria credo tonsor.
Defessus pax volup vomito creator video campana cedo vita votum.
Laudantium victoria aer via tepidus.
Adulescens corporis triumphus coruscus sordeo trans dolorum.
```

* **Error Message:**  "Error: Missing links" indicates a potential problem in the automated conversion process.
* **Explanation:** A concluding paragraph explains the difficulty of perfect PDF-to-Markdown conversion and clarifies that the exercise is simplified to check only basic aspects.


**Objects and Relevant Features:**

* **Code Block/Text Box:** The Latin text is presented within a distinct code block or text box.
* **Bullet Points:** The benefits of the automated conversion are clearly listed using bullet points.
* **Version Number:** "prettier@3.4.2" specifies the version of the "prettier" tool used for formatting the Markdown output.  Prettier is a code formatter.

In short, the image shows a programming-related question asking the user to convert a given snippet of Latin text from a hypothetical PDF to its Markdown equivalent using a particular formatting tool.  The "missing links" error suggests a challenge within the automated conversion that the user needs to potentially address manually.

---

## Post #125 by 23f2004644 (Post ID: 591829)
In the pdf you see some blue color font for specific words write that word in format


[word](#)

---

## Post #126 by 23f2004042 (Post ID: 591830)
There are only four texts which look like link texts in the pdf.

All four properly coded in link markdown syntax, in the preview, they appear as  link texts same as in pdf.




Link text


Even after chaning all the 4 texts which appered in blue color in the pdf to link texts,

below error is still observed.


Error: Missing links


Did anyone else face same issue ?




Also, no text in the pdf looks like a code block.

But, Missing Code error was seen and after changing one of the paragraph by using markdown code syntax that error is gone.




Appreciate any suggestions on the link error.

---

## Post #127 by 23f2004644 (Post ID: 591834)
Replace actual text to expected text until you got correct

---

## Post #128 by 23f2003268 (Post ID: 591838)
same kind of error is arising with me too.Any suggestion what is wrong with it??

---

## Post #129 by 23f2004042 (Post ID: 591840)
the rating should be treated as string.

Format is as “2.9” instead of number 2.9

---

## Post #130 by sha_512_av (Post ID: 591850)
Yes it can be done. Got the 10th one correct by implementing breakpoint by printing the expected answer which is being used to validate the user answer in the js script.

---

## Post #131 by 23f2004941 (Post ID: 591866)
i am facing a similar issue


image
1746×766 56.3 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/d/7df67bc891ce85e7851b39a7a09749013a2040a0_2_690x302.png)

**Image Description:** This image shows a coding exercise or test.  The top section displays an example of correctly formatted JSON (JavaScript Object Notation) weather data:

```json
{
"2025-01-01": "Sunny with scattered clouds",
"2025-01-02": "Partly cloudy with a chance of rain",
"2025-01-03": "Overcast skies",
// ... additional days
}
```

This example shows date strings as keys and weather descriptions as values within a JSON object.

Below this example, the question asks to provide a JSON weather forecast description for Shanghai. The user has attempted to answer with their own JSON data:


```json
{
"2025-02-07": "A clear sky and a moderate breeze",
"2025-02-08": "Sunny and a moderate breeze",
"2025-02-09": "Sunny and a gentle breeze",
"2025-02-10": "Sunny and a gentle breeze",
"2025-02-11": "Sunny intervals and a moderate breeze",
}
```

However, an error message "Error: At root: Different number of properties" indicates that the user's answer is incorrect, likely because it has a different number of key-value pairs than expected, or is missing some structural element of the example.  A "Check" button is present, implying that the user can resubmit their answer after making corrections.  The city "Shanghai" is specified in the question, suggesting the answer should be relevant to Shanghai's weather forecast.

---

## Post #132 by 23f2005275 (Post ID: 591868)
image
1678×892 43.3 KB

succesfully completed GA4 with 10/10 Marks

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/b/3b485ccad1b9c76027319c759cb72bd212d17925_2_690x366.png)

**Image Description:** The image shows a web page, likely a student assignment platform. 


Here's a breakdown of the content:

* **Top Navigation Bar:** Contains links to various resources like YouTube, an academic calendar, a quiz master, and other projects/tools related to data science. The URL indicates it's part of a course named "tds-2025-01-ga4".

* **Assignment Due Date & Score:**  Clearly displays "Due Sun, 9 Feb, 2025, 11:59 pm IST" and the current score as "Score: 10/10," with buttons to "Check all" and "Save."

* **Discourse Discussion:** A prominent section encourages students to participate in a discussion on Discourse for bonus marks. It specifies the topic: "GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]".  It states that a relevant question or reply will earn one bonus mark.

* **User Login Status:**  Confirms the logged-in user as "23f2005275@ds.study.iitm.ac.in" with a "Logout" button.  This suggests a university-related system (IITM possibly stands for Indian Institute of Technology Madras).

* **Recent Saves:** Shows a history of saved assignment submissions with timestamps (07/02/2025) and corresponding scores (10, 5, and 3).  Each entry has a "Reload" button, implying the ability to revert to a previous save.

The overall context strongly suggests an online learning environment where students complete graded assignments, participate in discussions, and track their progress. The emphasis on Discourse participation indicates the importance of collaborative learning.

---

## Post #133 by daksh76 (Post ID: 591873)
sir how will we know if we have been awarded with the bonus mark. Will it be reflected in our ga score and the marks would be 11/10 or will it be added later

---

## Post #134 by 21F1005510 (Post ID: 591875)
In Q2. getting , able to fix most of the errors but


image
1920×1080 159 KB


Error: At [18].title: Values don’t match. Expected: “19. Graymail”. Actual: “19. The Recruit”


this kind of errors for some titles, even though i only applied Rating filter and nothing else, then why i’m getting different titles then the test cases?

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/6/36bd8aa62d975eb34268da85d1125bcdd130ac93_2_690x388.jpeg)

**Image Description:** The image shows a screenshot of a MacOS computer screen.  The main focus is split between two browser windows.

**Left Window:** This window displays a webpage, likely IMDb, showing a list of movies.  Each movie entry (numbered 15-19) includes:

* **A movie poster thumbnail.**
* **The movie title.**
* **IMDb rating (star rating and numeric score).**
* **Year of release.**
* **Runtime.**
* **Rating (e.g., R).**
* **A brief synopsis of the movie's plot.**

**Right Window:**  This window appears to be a browser's developer tools console, showing a large segment of what appears to be JSON formatted data.  This data is structured with nested curly braces `{}` and contains key-value pairs, several of which seem to correspond to information from the movies listed in the left window (e.g.,  `"title":"Anora"`, `"year":"2024"`).  The keys suggest the data includes movie titles, years, ratings, and other metadata.  The tab bar at the top of the screen indicates this section is labeled "Elements", "Console", "Sources", "Network", "Performance", "Memory", "Application", and "Security".


**Other features:**

* **Top browser bar:** The top bar of the browser displays common browser elements like the back button, address bar (showing a partial IMDb search), and tab buttons.  The address bar shows a search query that includes "user rating".
* **Dock:** The bottom of the screen shows the MacOS dock with icons for several applications.
* **Time:** The top right corner of the screen shows the date and time as "Sat Feb 18 12:36AM".

The overall context suggests someone is working on a project that involves scraping or analyzing data from IMDb, possibly for a movie recommendation system or database.  The JSON data in the right window strongly suggests that data extraction is in progress.

---

## Post #135 by 23f2005138 (Post ID: 591877)
Hello Sir, thank you for changing the question.


@carlton
 I’m getting the below error:


Words like https, webbed, impact are missing (or not separated as words). 



However, in the source PDF file itself these words are not available.


image
657×106 7.78 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/5/9592fa553c00b5fa2d2540ef4933814690026709.png)

**Image Description:** The image shows a dark-themed code snippet or log output.  It displays a list of Latin words, each enclosed within vertical bars (`|`).  Underneath each word, some words have a wavy red underline. The words with underlines are: `utrum`, `tredecim`, `valetudo`, `cras`, `laudantium`, `aetas`, and `canis`.

At the bottom, a red error message indicates that words like "https," "webbed," and "impact" are missing from the input or not properly separated. This suggests the image is from a system that processes or analyzes text, likely for linguistic purposes or language processing.  The error message implies that the system expects to handle these modern English terms, which are not present amongst the provided Latin vocabulary.

---

## Post #136 by Atif01 (Post ID: 591880)
Copy the row name that is use to change and paste it in your answers

---

## Post #137 by 23f2001413 (Post ID: 591884)
the ranking changes from time to time. you might need to scrape the data again.

---

## Post #138 by 23f2004941 (Post ID: 591885)
i am facing issue in Q7.


I am using this command : “
https://api.github.com/search/users?q=location:Seattle+followers:
>120&sort=created&order=desc”


and the output on evaluating is : 2011-05-07T08:30:48Z


But i am getting the error :


image
1889×848 113 KB


Can someone please help me on this ?

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/8/a8b774a9913c5ffd2941af7d0ba271f79309575c_2_690x309.png)

**Image Description:** This image shows a screen capture of a coding challenge or exercise.  The challenge involves using the GitHub API to find the newest GitHub user in Seattle with over 120 followers.

The text provides step-by-step instructions:

1. **API Integration and Data Retrieval:** Use the GitHub API to search for users based on location (Seattle) and follower count (over 120).
2. **Data Processing:** Filter the results to only include users matching the criteria.
3. **Sort and Format:** Sort the filtered results by the `created_at` date (the date the profile was created) and format the date according to the ISO 8601 standard (YYYY-MM-DDTHH:MM:SSZ).

The user has attempted to answer with "2011-05-07T08:30:48Z", but this answer is marked as incorrect.  Further instructions below explain that the search should use 'location:' and 'followers:' filters, sort by 'joined' descending, fetch the first URL, and then use the `created_at` field.  It also specifies ignoring users who joined after February 7th, 2025, at 11:00:55 PM.

The "Impact" section describes the benefits of automating this data retrieval process, highlighting advantages such as targeted recruitment, competitive intelligence, efficiency gains, and data-driven decision-making.  The highlighted words "seattle", "GitHub API", and "created_at" are relevant keywords to the challenge.

---

## Post #139 by 23f2001413 (Post ID: 591886)
I am also facing the same issue. What is the problem here?


image
1788×908 77.9 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/6/067aa8362e39ff9020d2cf42d3b7605bcbb0bcf2_2_690x350.png)

**Image Description:** The image shows a coding assessment or exercise.  The top section displays a due date and time (Sun, 9 Feb, 2025, 11:59 pm IST) and a score (9/10).  There are three numbered steps outlining a process involving API calls to retrieve and transform weather forecast data for London:

1. **API Integration and Data Retrieval:**  This involves using the BBC Weather API to fetch a weather forecast for London using a GET request and the `locationId`. Necessary query parameters like API key, locale, filters, and search term are mentioned.

2. **Weather Data Extraction:**  This step retrieves weather data using the obtained `locationId` from a weather broker API endpoint via another GET request.

3. **Data Transformation:** This describes transforming the data into a JSON object. It specifically extracts `issueDate` and `enhancedweatherDescription` from each day's forecast and maps them to create a JSON where `issueDate` is the key and `enhancedweatherDescription` is the value.

Below this is an example of the expected JSON output showing key-value pairs of dates and weather descriptions.


There's a question asking for the JSON weather forecast description for London. A JSON snippet is provided as an answer in a text box. An error message "Error: At root: Property name mismatch" is displayed, likely indicating an issue with the JSON formatting provided.  A "Check" button is present, suggesting this is a step in an online coding assessment.

---

## Post #140 by s.anand (Post ID: 591968)
@21F1005510
 Actually, some IMDb titles have multiple names. For example, 
The Recruit
 is 
also known as Graymail in India
. My server checks from a different region from yours. Hence the need for manual corrections for a few titles.


Why didn’t I pick an exercise that could be fully automated?
 Because this is how real-life data sourcing is. It’s never perfect. You often need to create workflows where you’re able to quickly correct such errors in automation.

---

## Post #141 by s.anand (Post ID: 591972)
To evaluate the bonus mark for replying to this Discourse topic, At around the time of the deadline, we’ll close this thread, load all posts here, and run this in the Console:


[...new Set($$('.names a[href^="/u/"]').map(d => d.textContent))]



… to get the Discourse IDs who posted. Then we’ll match it to the email IDs and pass it to the operations team who will add it to the portal by 
2025-02-22T18:30:00Z
.

---

## Post #142 by 23f1001174 (Post ID: 591982)
I am getting the error in Q4 as “Error: At root: Property name mismatch”


what could me the cause of this error? Any please help.


@carlton


image
716×402 23.3 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/8/1865f8e1b730ba9148ccdea4be94bcb314eaa2bc.png)

**Image Description:** The image shows a coding challenge or exercise related to JSON (JavaScript Object Notation) data.  The challenge asks for the JSON weather forecast description for Sao Paulo.

The user has attempted to provide a JSON response in the text box.  The response is a series of key-value pairs, with the keys being dates in YYYY-MM-DD format (February 2025) and the values being descriptive weather forecasts.

However, there is an error message displayed below the response:  "Error: At root: Property name mismatch". This indicates that the JSON formatting is incorrect, likely due to an issue with how the keys are structured or the syntax of the JSON object.  There is a "Check" button that presumably allows the user to submit their JSON for validation or checking against an expected result.  The location "Sao Paulo" is specified at the top, indicating the weather forecast is supposed to be for that city.

---

## Post #143 by 23f2005138 (Post ID: 591998)
This is the only thing which worked for me.


@carlton
 Sir, can I suggest to replace the snapshot of example output which expects the year to be an integer and the ratings as to be floats (instead of actual evaluation which expects them to be strings). Also, it would help to clarify that “Movie 1” should carry the numerical prefix as reported in IMDB.  The current example on the portal is:


image
1580×196 4.81 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/0/e051d55928f7df633f0a14ed8c7aaa33712cdecf.png)

**Image Description:** The image shows a snippet of what appears to be JSON (JavaScript Object Notation) data, likely representing a list of movies.  The data is formatted as a JSON array containing JSON objects. Each object represents a movie and includes the following key-value pairs:

* **`"id"`:** A string that seems to be a unique identifier for each movie (e.g., "tt1234567").  The "tt" prefix suggests it might be from a database like IMDb.
* **`"title"`:**  The title of the movie (e.g., "Movie 1").
* **`"year"`:** The year the movie was released (e.g., 2021).
* **`"rating"`:** A numerical rating for the movie (e.g., 5.8).


The `// ... more titles` comment indicates that there are more movie objects in the complete dataset beyond what's shown in the image. The surrounding square brackets `[]` signify a JSON array, and the curly braces `{}` enclose each individual movie's data as a JSON object. The overall structure suggests that this is part of a larger data set, potentially used for a movie database or recommendation system.

---

## Post #144 by 23f2004907 (Post ID: 592004)
Your dot of 2.9 may be the dot from alphabet or numeric one

Try to copy the value and then replace it

---

## Post #145 by 23f2004907 (Post ID: 592006)
Try to copy the error data

The problem might be off dot

check one dot is on right of m and other right of 0 in keyboard

these two dots may represent different meanings

---

## Post #146 by 23f1000422 (Post ID: 592007)
is it resolved?

i too am getting the same error,even if it was working fine yesterday.

---

## Post #147 by 23f1001174 (Post ID: 592008)
https will be part of the link (provided ‘link’ is one of the checkpoints of evaluation)

---

## Post #148 by lakshaygarg654 (Post ID: 592019)
Sir, In Graded Assignment - 4 >> Q2, the year I extracted appears as “2024,” whereas the expected value on the portal is “2024–”. I have manually adjusted several values based on the expected format. This issue is specific to the year field.


I use different classes to extract values for various fields. Could there be any other element on the portal affecting this extraction?


In Q4, one of my classmates is encountering a “root property” error despite using the same extraction method as I do. Upon checking, I found that this issue occurs because the city’s time is displayed as the previous day compared to our time. The portal results seem to be based on the city’s actual time rather than IST.

I would appreciate your guidance on these issues.

---

## Post #149 by s.anand (Post ID: 592021)
Good idea 
@23f2005138
 and thanks. I fixed this. The example now reads:


[
  { "id": "tt1234567", "title": "Movie 1", "year": "2021", "rating": "5.8" },
  { "id": "tt7654321", "title": "Movie 2", "year": "2019", "rating": "6.2" },



… with the year and ratings quoted.

---

## Post #150 by 21f2000709 (Post ID: 592049)
lakshaygarg654:




In Graded Assignment - 4 >> Q2, the year I extracted appears as “2024,” whereas the expected value on the portal is “2024–”. I have manually adjusted several values based on the expected format. This issue is specific to the year field.






I guess for the year part, there are certain series having multiple seasons, for which hyphenated “years” are given.


For the particular instance - 
“2024–”
, it appears another season/part is announced, thats why it is written that way.

---

## Post #153 by lakshaygarg654 (Post ID: 592057)
Thanks 
@21f2000709
 for this information. I figure out where i made mistake. During writing console code I added to remove non numeric values in year field which i guess removed that hyphen (“–”). I will rectify that.

---

## Post #154 by 21f3001379 (Post ID: 592059)
GA 4 Q2


My JSON matches the titles of the movies as in the website, but in portal it is showing error and expecting something different from what is given in the website. How to handle this ?


image
501×151 37.6 KB


image
1226×258 13.2 KB


contradiction :

" 2. Winnie-the-Pooh: Blood and Honey" (in web page) & ( delivered by the JSON)

" 2. Winnie the Pooh: Blood and Honey" (expected in portal ) & ( raising error statement )


Regards

GOVADHANAN N

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/c/fcac5869001b59aa0b36666aa5096fd3ebfd8a0f.png)

**Image Description:** The image is a screenshot of a movie listing, likely from a website or app that aggregates movie information. 


Here's a breakdown of the content:

* **Left Side:** A poster image for the movie "Winnie-the-Pooh: Blood and Honey" is shown. The poster depicts a menacing, horror-themed version of Winnie-the-Pooh. The title "Winnie the Pooh: Blood and Honey" is visible on the poster. A plus symbol (+) is in the upper left corner of the poster image.

* **Right Side:** This section contains information about the movie:

    * **Title:**  A red rectangular box highlights the movie title: "2. Winnie-the-Pooh: Blood and Honey".  The "the" in "Winnie-the-Pooh" is underlined in blue, likely indicating a link or clickable element.

    * **Year, Runtime, Rating:** "2023" (release year), "1h 24m" (runtime), and "Not Rated" (MPAA rating) are listed.

    * **User Rating:** A yellow star icon followed by "2.9 (33K)" indicates a user rating of 2.9 out of 5 stars, with 33,000 user ratings. A clickable "Rate" star icon allows the viewer to submit their rating.

    * **Metascore:** A red box displays "16," likely the Metascore (a weighted average from multiple critics) for the movie. "Metascore" is labeled next to the numerical score.


In short, the image provides a quick overview of the horror film "Winnie-the-Pooh: Blood and Honey," including its poster art, release date, runtime, ratings from users and critics, and the option to submit a user rating.

![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/6/b60003a16d034748f4e97674a5ce778a4c6686d4_2_690x145.png)

**Image Description:** The image contains a JSON data snippet and an error message.

The JSON data shows a movie record with the following fields:

* **title**: "25. Battlefield Earth"
* **year**: "2000"
* **rating**: "2.5"

Below the JSON data is an error message that states:

"Error: At [1].title: Values don't match. Expected: "2. Winnie the Pooh: Blood and Honey". Actual: "2. Winnie-the-Pooh: Blood and Honey""

This error indicates a mismatch in the `title` field. The expected value was "2. Winnie the Pooh: Blood and Honey", but the actual value was "2. Winnie-the-Pooh: Blood and Honey".  The only difference appears to be a hyphen instead of a space in the "Winnie-the-Pooh" part of the title.

---

## Post #155 by 22f3001315 (Post ID: 592064)
so just exchange it.

---

## Post #156 by 21f3001379 (Post ID: 592065)
Thanks for your response.

Many such titles have contradiction from what is expected and what is there in the website. This case the samples are 25 your approach is accepted to some extent, but on a larger sample space, need to work it right !

---

## Post #157 by yasharabhavi (Post ID: 592071)
thanks for this, was wondering why it wasn’t working!

---

## Post #158 by 23f3003871 (Post ID: 592074)
question4
692×539 36.3 KB


sir,  we are getting this error. My  Actual output is after get request on the given api i get only one day forcast data. I have show in above image

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/4/94da9d1e5e22ec3b7a7d0bd8017fae76736aa5c8_2_641x500.jpeg)

**Image Description:** Here's a description of the image content:

The image shows a coding problem related to JSON (JavaScript Object Notation) data representing a weather forecast.

**Top Section:**

* **Headline:** "The output would look like this:"  This introduces an example of correctly formatted JSON.
* **JSON Example:** A block of code displays a sample JSON object.  This object uses key-value pairs where the keys are dates ("YYYY-MM-DD") and the values are corresponding weather descriptions (strings).  The example includes three entries for January 1st, 2nd, and 3rd, 2025 and notes that additional days' data would follow.  The structure is a JSON object enclosed in curly braces `{}`.


**Middle Section:**

* **Question:** "What is the JSON weather forecast description for Kuala Lumpur?"  This poses the problem.
* **Answer Attempt:** A text box contains a JSON object representing a weather forecast for a single date ("2025-02-01"), describing "Thundery showers and light winds".  This represents an attempt to answer the question.


**Bottom Section:**

* **Error Message:** "Error: At root: Different number of properties". This indicates that the user's answer in the text box has a different structure than the example JSON object shown in the top section;  likely because the example has multiple entries while the answer only has one.

In essence, the image presents a coding challenge involving correctly formatting JSON data for a weather forecast, highlighting an error that arises from inconsistent JSON structure. The problem lies in the difference in the number of key-value pairs between the example and the attempted solution.

---

## Post #159 by 21f3000745 (Post ID: 592115)
yes replace manually until you got correct ans . Error will suggest you what to change.

---

## Post #160 by 22f3002771 (Post ID: 592123)
{

“2025-02-08”: “Light snow and light winds”,

“2025-02-09”: “Light snow and light winds”,

“2025-02-10”: “Light cloud and light winds”,

“2025-02-11”: “Sunny intervals and a gentle breeze”,

“2025-02-12”: “Sunny and light winds”,

“2025-02-13”: “Sunny and light winds”,

“2025-02-14”: “Light snow and a gentle breeze”,

“2025-02-15”: “Light snow and a gentle breeze”,

“2025-02-16”: “Sleet and a gentle breeze”,

“2025-02-17”: “Light rain and a gentle breeze”,

“2025-02-18”: “Light rain showers and a gentle breeze”,

“2025-02-19”: “Drizzle and a gentle breeze”,

“2025-02-20”: “Light rain and light winds”,

“2025-02-21”: “Light rain and light winds”

}

i got this after running my python script for question 4 but, got

Error: At root: Property name mismatch" this error message

---

## Post #161 by sarvan108 (Post ID: 592125)
@s.anand
 sir,

I don’t understand this error. In the website, the movie name doesn’t have a colon “:”, but in the result it is expecting so.


image
1005×250 15.4 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/6/b67037a225011416ec63654326f63aa3ee1542c4_2_690x171.png)

**Image Description:** The image contains a JSON-like data structure, with key-value pairs enclosed in curly braces `{}`.  The keys are enclosed in double quotes and the values are also string literals enclosed in double quotes. The data appears to represent metadata about a movie or film.  The key-value pairs are:

* `"id": "tt8790086"`:  This likely represents a unique identifier for the film (possibly an IMDb ID).
* `"title": "11. Kraven the Hunter"`: This is the title of the film. The "11." prefix might indicate a numbered entry in a series, though this is not explicitly stated.
* `"year": "2024"`: The year of release for the film.
* `"rating": "5.4"`:  A numerical rating, possibly out of 10.


Below the JSON-like structure, an error message is displayed:

`Error: At [10].title: Values don't match. Expected: "11. Kraven: The Hunter". Actual: "11. Kraven the Hunter"`

This error message indicates that a validation check failed. The `title` field ("11. Kraven the Hunter")  did not match the expected value ("11. Kraven: The Hunter").  The difference lies in the use of a colon in the expected title versus a space in the actual title.  The error message also suggests a line number or index of `[10]` where the mismatch occurred within a larger data set.

---

## Post #162 by lakshaygarg654 (Post ID: 592126)
For this question, you may use the Google Colab file referenced in the assignment. This file will provide you with the date and description. Additionally, you can generate a weather location ID for the city specified in your assignment. Using this ID, you will obtain the weather URL, which you can then use to verify the date and description.

---

## Post #163 by 21f3000745 (Post ID: 592139)
here is the difference of  ‘:’ in the expected ans. so make it manually correct . i did the same and got correct ans .

and in the question also it is mentioned that may be manually you need to correct.  just give a try.

---

## Post #164 by 21f3000745 (Post ID: 592141)
run your console script again and match the description.

---

## Post #165 by 21f3000745 (Post ID: 592144)
yes, same happened with me . correct it manually.

---

## Post #166 by 22f3000079 (Post ID: 592148)
In q10 links are not accessible through pdf and also creating problems while converting to markdown

---

## Post #167 by akashkunwar (Post ID: 592154)
image
1358×1151 179 KB


Why question 4 starts failing. It was working correct yesterday. Because of it I am getting 9/10 marks.

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/e/7ec5aaa6e3eba1d39679fd60881fea0623932254_2_589x500.png)

**Image Description:** The image contains a technical document describing a task involving weather data integration. The task is to develop a system that automates the process of retrieving and transforming weather forecast data from the BBC Weather API for Manila.

The document outlines three main steps:

1. **API Integration and Data Retrieval:** This involves using the BBC Weather API to fetch the weather forecast for Manila by sending a GET request to the locator service to get the city's `locationId`.  Necessary query parameters (API key, locale, filters, search term) are to be included.

2. **Weather Data Extraction:** This step involves retrieving the weather forecast data using the obtained `locationId` by sending another GET request to the weather broker API endpoint.

3. **Data Transformation:** This crucial part focuses on extracting the `issueDate` and `enhancedWeatherDescription` from each day's forecast. The extracted data is then used to create a JSON object where `issueDate` serves as the key and `enhancedWeatherDescription` is the value.  An example of the expected JSON output is provided.

A sample JSON output is given, showing a series of dates (keys) and their corresponding weather descriptions (values).  There's also a separate example of what the JSON for Manila should look like as a question, with a series of dates in February 2025, all reporting "Sunny and a gentle breeze".  Finally, there's a "Check" button, presumably to submit the completed JSON.  The overall tone is instructional, providing a clear description of the problem and the expected solution.

---

## Post #168 by 21f3001379 (Post ID: 592167)
The result is dynamic with changes made in the API. So try re-executing your code today and it will automatically solve. Your code is right ! Just make a re-run and things will work out

---

## Post #169 by 23f2000926 (Post ID: 592168)
try running the console again and it will work, make sure the data matches with the one in api as it changes regularly

---

## Post #170 by sarvan108 (Post ID: 592172)
Thanks!.

It is working now. I had to manually correct 5 movie titles to get it correct.

---

## Post #171 by Deepanshutomar (Post ID: 592174)
Screenshot 2025-02-08 at 7.41.55 PM
2576×420 32.3 KB

What 's the solution?

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/6/66bbdf1b8a6c5661e0a95e9e9515f41a1d96816d_2_690x112.png)

**Image Description:** The image shows a code editor or similar interface displaying JSON data and an error message.

**The JSON data (partially visible):**

The JSON data is a dictionary (or object) with three key-value pairs:

* `"id"`: `"tt10078772"`
* `"title"`: `"9. Flight Risk"`
* `"year"`: `"2025"`

A fourth key-value pair, starting with `"season":`, is partially visible but incomplete.

**The Error Message:**

Below the JSON data, an error message is displayed:

`Error: At [10] year: Values don't match. Expected: "2025-". Actual: "2025- "`

This indicates a validation error. The system expected the value of the `"year"` key to be `"2025- "` (note the trailing space), but the actual value was `"2025-"`, which is slightly different.  The error message highlights a discrepancy in the expected and actual values of the `year` field, specifically the presence or absence of a trailing space.

**Overall:**

The image suggests a situation where JSON data is being processed or validated, and a minor discrepancy (a missing trailing space in this case) causes a validation error. The error message and its location below the JSON snippet clearly indicate the source of the problem.

---

## Post #172 by Neelakandan (Post ID: 592175)
Titles (from the output json) should be replaced by the titles which shows in the error message “Expected”. It can only be done manually. There may be multiple titles need to be translated by this method.


Please refer the instruction.


1000095240
1080×183 43.8 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/5/159cfd274231dd9585ac818265479de56b3544fd_2_690x116.jpeg)

**Image Description:** The image contains a text box with a message explaining potential issues when using IMDb search results:

* **Regional Differences:**  IMDb search results vary depending on the geographical region.
* **Manual Translation:**  Titles may require manual translation.
* **Periodic Changes:**  The search results themselves change over time.
* **Code Rerun:**  Users may need to re-run their code (implying this relates to data scraping or automated searches of IMDb) to account for the changes.

Below the text box, a partially visible blue button labeled "Check" is present, suggesting a mechanism to verify or update the data.  The overall context suggests this is a message from a data scraping or data analysis tool dealing with information obtained from IMDb.

---

## Post #173 by 23f2002291 (Post ID: 592176)
you can manually add space after the hyphen

---

## Post #174 by 23ds3000149 (Post ID: 592210)
I face the same error, also thinking of issueDate, the value seems to be constant in every loop inside forecasts array (is it because the data is issed on that particular date) that gives same issue date key across the json outcome. Anyways the new json with same issueDate also gives the same Root error

---

## Post #175 by 23f1001839 (Post ID: 592233)
Double-check that the rating field in the JSON is indeed a float (
2.9
) and not a string (
"2.9"
) in your code.

---

## Post #176 by 24f2003130 (Post ID: 592234)
That is perhaps to ensure we don’t manually write the markdown for the pdf. Converting the pdf to markdown and getting the correct output is extremely hard, I tried doing that multiple times yet wasn’t able to get that right by the original method.


But since it is mentioned that the GAA is hackable and we are allowed to do so, for some of the questions, therefore you can try solving that by establishing a breakpoint in the sources and then write the code in the console to get the expected output.

---

## Post #177 by 24f2003130 (Post ID: 592235)
Write the code referencing the provided collab file and make sure to use the API key

The output actually changes once in a while so you might need to run the code a few times before getting in right


https://tds.s-anand.net/#/bbc-weather-api-with-python

---

## Post #178 by 23f2001738 (Post ID: 592259)
your most recently saved score will be evaluated

---

## Post #179 by 22f2000008 (Post ID: 592263)
I am getting this error again and again after running the code in collab this city  
Nur-Sultan
?


image
936×343 26 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/a/7a2329cd855e0e0b8018cbfb2c426b91e57fa23d_2_690x252.png)

**Image Description:** The image shows a Python code snippet and error messages.  The core issue is a `NameError` indicating that the variable `location_id` is undefined.

Here's a breakdown:

* **Top Line:**  An initial error message: "Error: Could not find location ID for Nur-Sultan". This suggests the code was trying to find a location ID for Nur-Sultan (the capital of Kazakhstan), and it failed.

* **Middle Section:** This shows the traceback from the error.  The relevant lines are:

    * Lines 33-37: This is a portion of a Python script.  Line 35 is attempting to create a URL string for the BBC Weather website using an f-string. The `{location_id}` within the f-string is intended to be replaced with the value of the `location_id` variable.  The comment on line 34 indicates that this URL is intended for retrieving weather data.

    * `weather_url = f'https://www.bbc.com/weather/{location_id}'`: This is the line causing the error.  It's trying to use a variable named `location_id` but that variable hasn't been defined or assigned a value earlier in the code.


* **Bottom Line:** The final error message: "NameError: name 'location_id' is not defined".  This explicitly states the cause of the problem:  The program is trying to use a variable that does not exist.


In summary, the image shows a Python error caused by a missing variable (`location_id`) needed to construct a URL for fetching weather data from the BBC Weather website.  The code likely needs to be modified to define and assign a value to `location_id` before it's used in the URL string.

---

## Post #180 by 22f3002034 (Post ID: 592271)
In the second question are we supposed to edit the JSON manually until we reach a correct answer ? I think the expected result has some difference from what shows up in the website

---

## Post #181 by 22f3001840 (Post ID: 592280)
Not able to get the missing links in Q10

Any suggestions welcome please

---

## Post #182 by anu2023 (Post ID: 592287)
For question 10 I’ve tried everything. Links and headings work fine, but I’m not able to fix the “missing tables” issue (I’ve also tried using pdfplumber and tabulate). In the pdf as well, I don’t see any tables, any hints or suggestions would be very helpful. Thanks!

---

## Post #184 by Jayeshbansal (Post ID: 592289)
there is no location id mentioned as it is mentioned of the different city. please check the city for which you need to find the location id and then proceed

---

## Post #185 by swatikap (Post ID: 592290)
I’m getting the same error in Q4:


image
1631×641 34.2 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/6/b610004bc77d8cb653c10708ce962742396a0d2e_2_690x271.png)

**Image Description:** Here's a description of the image content:

The image shows a coding/programming interface or exercise.  It presents two key sections:

**Section 1: Example JSON Output**

This section displays a code snippet illustrating the desired format of a JSON (JavaScript Object Notation) weather forecast.  The example shows three entries, each with a date ("YYYY-MM-DD") and a corresponding weather description.  The comment `// ... additional days` indicates that more entries would follow in a complete forecast. The example is:

```json
{
"2025-01-01": "Sunny with scattered clouds",
"2025-01-02": "Partly cloudy with a chance of rain",
"2025-01-03": "Overcast skies",
// ... additional days
}
```

**Section 2: User Input and Error**

This section poses a question: "What is the JSON weather forecast description for Los Angeles?".  Below it is a text box where a user is expected to provide their JSON weather forecast for Los Angeles.  The user's attempt is shown, displaying a series of entries with dates and "Sunny and light winds" descriptions. However, there's a crucial error message: "Error: At root: Property name mismatch". This error message indicates that the dates in the user's JSON (which start with "23" then "25") are not correctly formatted as dates according to the expected format shown in the example (starting with "2025").

**Overall:**

The image depicts a coding problem where the user is tasked with creating a valid JSON weather forecast in a specified format but has made a mistake. The error highlights a common issue in JSON: incorrect data types or structure.  The "Check" button likely submits the user's code for evaluation.

---

## Post #186 by 24f2000695 (Post ID: 592293)
How to actually do the HNRSS one…i can’t find much.

---

## Post #187 by 24f2000695 (Post ID: 592296)
How did u do the links? I’m unable to do links

---

## Post #188 by tanmaysahu295 (Post ID: 592312)
Just copy paste the expected value in place of actual value in json. Keep doing this eventually it would be the answer would be correct.


This is a format issue when the json is scrapped from the browser.

---

## Post #189 by koustubhr (Post ID: 592316)
Request help on Q4 aboutBBC weather data, the instructions in the question tell us to use BBC broker API and get issueDate & enhancedWeatherdescription value pairs. However, it seems there are only 2 unique values of issueDate (not the expected 14 days)


Please clarify, sharing code and output below for reference.


Code:


import requests

url = "https://weather-broker-cdn.api.bbci.co.uk/en/forecast/aggregated/" + getlocid('Bogota')
response = requests.get(url)
json_data=response.json()
print(f"The number of days data is {len(json_data['forecasts'])}")

weather_data = {}

for i in range(len(json_data['forecasts'])): # Use range to create an iterable sequence of indices
  issue_date = json_data['forecasts'][i]['summary']['issueDate']
  weather_description = json_data['forecasts'][i]['summary']['report']['enhancedWeatherDescription']
  weather_data[issue_date]=weather_description
  print("Iteration No. " + str(i))
  print(issue_date)
  print(weather_description)
  
print("Final Weather Data json below")
print(weather_data)



Output


The number of days data is 14
Iteration No. 0
2025-02-08T04:00:00-05:00
Light rain showers and a gentle breeze
Iteration No. 1
2025-02-08T04:00:00-05:00
Thundery showers and a gentle breeze
Iteration No. 2
2025-02-08T04:00:00-05:00
Thundery showers and a gentle breeze
Iteration No. 3
2025-02-08T04:00:00-05:00
Thundery showers and light winds
Iteration No. 4
2025-02-08T04:00:00-05:00
Light rain showers and light winds
Iteration No. 5
2025-02-08T04:00:00-05:00
Light rain showers and light winds
Iteration No. 6
2025-02-08T04:00:00-05:00
Light rain showers and light winds
Iteration No. 7
2025-02-08T04:00:00-05:00
Thundery showers and a gentle breeze
Iteration No. 8
2025-02-08T16:01:58-05:00
Thundery showers and a gentle breeze
Iteration No. 9
2025-02-08T16:01:58-05:00
Thundery showers and light winds
Iteration No. 10
2025-02-08T16:01:58-05:00
Thundery showers and a gentle breeze
Iteration No. 11
2025-02-08T16:01:58-05:00
Thundery showers and light winds
Iteration No. 12
2025-02-08T16:01:58-05:00
Thundery showers and light winds
Iteration No. 13
2025-02-08T16:01:58-05:00
Thundery showers and a gentle breeze
Final Weather Data json below
{'2025-02-08T04:00:00-05:00': 'Thundery showers and a gentle breeze', '2025-02-08T16:01:58-05:00': 'Thundery showers and a gentle breeze'}



Edit: For now, I have worked around with code posted by 
@21f3002277
. But the doubt about the question remains

---

## Post #190 by Suhani (Post ID: 592318)
same with me. In the project it is written that the form should be submitted but there’s no question in the portal.

---

## Post #191 by 23ds3000149 (Post ID: 592323)
I have got the same error as well, verified there are workflows run in my repo/actions/runs

When I checked the reasons, it could be due to API limit exceeded in a hour, but tried even after some time but no workflows found.


image
1345×424 23.7 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/f/3f6454e8cc98f502f9844114ea02cb8d6cd523c4_2_690x217.png)

**Image Description:** This image shows a GitHub Actions workflow runs page. 


Here's a breakdown of the content:

* **Header:** "All workflows" and "Showing runs from all workflows" indicate the page displays all workflow runs within a GitHub repository.  A search bar ("Filter workflow runs") is present at the top right.

* **Feedback Request:** A section titled "Help us improve GitHub Actions" prompts the user to provide feedback with three quick questions. A "Give feedback" button is also visible.

* **Workflow Runs Table:** This section lists the workflow runs. The table has the following columns:

    * **Event:** (Not populated in the screenshot)  This would show what triggered the workflow run (e.g., push to a branch, scheduled event).
    * **Status:** (Implicit) Green checkmarks next to the workflow names indicate successful runs.
    * **Branch:** Shows the branch the workflow ran on ("main" in both cases).
    * **Actor:** (Implicit)  One run was scheduled and the other manually run by user Rajalakshmi12.
    * **Run Details:** Each row shows the workflow name ("Action runs everyday"), the run number (#6 and #5), how the run was triggered (Scheduled vs. Manually), the time since completion ("2 hours ago"), and the duration ("15s" and "14s").


In summary, the image shows two recently completed GitHub Actions workflows, both running on the "main" branch. One was scheduled, and the other was manually triggered.  The screenshot also includes a prompt for user feedback on GitHub Actions.

---

## Post #192 by 23f2003853 (Post ID: 592324)
Manual correction will not work. Try to extract - from the console. I did it like that it was not working then I extracted from console then it worked

---

## Post #193 by 23f2003853 (Post ID: 592325)
Please ensure that your .yml file should have step name as your email Id. then Manually trigger the task (don’t wait till the scheduled time), ensure it was committed within 5 minutes and that commit should be top most item in all workflows. Then check it, it will work

---

## Post #194 by 23f2003853 (Post ID: 592326)
You can find some text blue in color and underline use some dumy url it will work

---

## Post #195 by 23f2003853 (Post ID: 592327)
You can find some lines having second, third words are uniformly aligned. Those are tables

---

## Post #196 by Suhani (Post ID: 592337)
When I resave the questions, the previously correct questions turn wrong which is extremely frustrating and time taking. I wish there is an option which saves the correct answer and does not require us to have multiple processes running in our pc even after getting the answer right previously.

---

## Post #197 by Udipth (Post ID: 592338)
In Q 6 I checked all the startups link at 
Hacker News - Newest: "Startup"
… none is greater than 81 then how to submit that link… is there something i am missing

---

## Post #198 by 23f2000573 (Post ID: 592343)
@Jivraj
 
@carlton
 ,for question 3, even a random response is shown correct


image
1765×472 29.1 KB


image
766×237 12.2 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/b/2b7de6bb9536ce1199eae286b610bb4cde7c34e5_2_690x184.png)

**Image Description:** The image shows a section of a web interface, likely part of a tutorial or testing process related to CORS (Cross-Origin Resource Sharing). 


Here's a breakdown of the content:

* **Heading:** "5. Enabling CORS: Configure the web application to include appropriate CORS headers, allowing GET requests from any origin." This explains the purpose of the section; it's about setting up CORS correctly.

* **Input Field and Validation:**  A text input field asks for "What is the URL of your API endpoint?". The URL `http://127.0.0.1:8000` is entered, and a green checkmark indicates it's been accepted as correct.  This suggests a local development environment address.

* **Explanation:** "We'll check by sending a request to this URL with `?country=...` passing different countries." This explains that the system will test the CORS configuration by making requests to the specified URL with a `country` parameter.

* **Action Button:** A "Check" button is available, presumably to initiate the CORS test described in the explanation.


In summary, the image captures a step in a process where a user provides the URL of their API endpoint for a CORS test. The provided URL appears to be a localhost address and has been validated by the system.  The test involves sending requests with varying country parameters.

![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/f/af2fbee5353a1ff49e1bb73c3188f58894cb2dab.png)

**Image Description:** Here's a description of the image content:

The image shows a screenshot of a web browser window, likely a Jupyter Notebook interface. 


Here's a breakdown of the visible elements:

* **Browser Address Bar:** The address bar displays `127.0.0.1:8000/?country=india`. This indicates a local server is running (127.0.0.1 is the localhost address), on port 8000, and possibly has a parameter specifying the country as India.

* **Browser Tabs:** Several tabs are visible, with partially truncated titles.  We can see "Mathematics for Da...", "BS-DS_Jan 2025 Gr...", and "Untitled1.ipynb - Co...". The "... " indicates that the tab titles are longer than what is shown.

* **Notebook Content:** The main part of the window shows a Jupyter Notebook cell.  The text "Pretty-print" suggests this is a Python code cell (or similar), and the number `44` is likely the output from the code in this cell.  The checkbox next to "Pretty-print" is likely used for controlling the output formatting.

* **Browser Controls:** Standard browser controls are visible (back, forward, refresh, home).

In summary, the image shows a Jupyter Notebook running locally, possibly for a data science course (given "BS-DS" in the tab title), working with data related to India, and currently displaying the output `44` from a "Pretty-print" operation.

---

## Post #199 by 23f2001286 (Post ID: 592344)
Sir I have solved  Q2, But a problem arises that, At the index 11, in the IMdb website it is listed “The Recruit” but it is showing Expected: “Graymail”.


problem
621×159 42.4 KB


How to fix this?

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/2/e2c041886709fd37323cae0daebdb4426d85c7fc.jpeg)

**Image Description:** The image contains a snippet of what appears to be JSON data representing a list of items. Each item has an "id", "title", "year", and "rating".  The titles appear to be movie or show titles, each with a numerical prefix (e.g., "8. Companion"). The years are mostly four-digit years but include a trailing hyphen in some cases, indicating a potential ongoing or incomplete year. The ratings are decimal numbers.

Below the JSON data is an error message:

`Error: At [11].title: Values don't match. Expected: "12. Graymail". Actual: "12. The Recruit"`

This error indicates a data mismatch at the 11th item in the list. The expected title was "12. Graymail", but the actual title found was "12. The Recruit".  This suggests a problem with data consistency or accuracy in the dataset.

---

## Post #200 by 23f2000573 (Post ID: 592346)
you have to manually change for a few mismatch.








 s.anand:




@21F1005510
 Actually, some IMDb titles have multiple names. For example, 
The Recruit
 is 
also known as Graymail in India
. My server checks from a different region from yours. Hence the need for manual corrections for a few titles.


Why didn’t I pick an exercise that could be fully automated?
 Because this is how real-life data sourcing is. It’s never perfect. You often need to create workflows where you’re able to quickly correct such errors in automation.

---

## Post #201 by 24f2003130 (Post ID: 592368)
Yes …due to the location difference the search results are different for everyone therefore you need to adjust it accordingly

It might need around 6-7 amendments

---

## Post #203 by 24f2003130 (Post ID: 592375)
The API is returning 14 days of forecast data, as evidenced by the output However, the issueDate values are not unique for each day. Instead, they represent the time when the forecast was issued or updated.

In your output, there are only two unique issueDate values:

2025-02-08T04:00:00-05:00

2025-02-08T16:01:58-05:00

This means the forecast was updated twice on February 8, 2025, once at 04:00 AM and again at 4:01 PM (both in EST timezone) …To get a unique weather description for each day, you  need to modify your approach by using the actual forecast day for each day instead.

---

## Post #204 by rabbaniIITB (Post ID: 592378)
While submitting solution, do I need to keep all the local servers running/local URLs like 127.0.0.0 stuff, else I am getting one question as correct & the other one mentions unable to fetch data!? So that means I need to run them in different different ports?

---

## Post #205 by 21f3001993 (Post ID: 592386)
I posted this error message but now the first issue got resolved but I am still keeping it in my post so that if anyone faces same issue, they can try if they can fix it similar to how it worked for me.


Please help with the second issue.




For Q8, the workflow is running on Github and commiting the scraped results to the json file (which is so amazing for me btw!). But I am getting this error for my public repo.

How it got resolved: I set up fixed time for cron schedule instead of every 5 min. Now it works.






Error: No daily scheduled triggers found in workflows.






I had all correct results for Q1 to Q7 till yesterday but it keeps giving errors even when I reload same file for some questions. Do I need to keep addressing those errors or if once correct and saved, I can ignore those?

---

## Post #206 by sharma_abhay (Post ID: 592389)
image
706×257 17.3 KB

I have tried several times but still recieving this as error. Please help

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/b/3bfb8c846507bcd4e7847f27efbfbffac65ca91e.png)

**Image Description:** The image contains a question "What is the JSON data?" followed by a block of code showing a JSON array.  Each element of the array is a JSON object representing movie data, with the keys "id", "title", and sometimes "year" and "rating".

The JSON data includes information for three movies:

* **"The Good, the Bad and the Ugly"**:  ID: tt0060196, Year: 1966
* **"Fight Club"**: ID: tt0137523, Year: 1999, Rating: 8.8
* **"The Lord of the Rings: The Fellowship of the Ring"**: ID: tt0120737

Below the JSON data is an error message:

**Error: At [0].id: Values don't match. Expected: "tt20221436". Actual: "tt0437179"**

This indicates a problem with the first element ([0]) of the JSON array.  The `id` value ("tt0437179") doesn't match the expected value ("tt20221436").  This suggests there is a data mismatch or a bug in the system processing this JSON data.

---

## Post #207 by 22ds3000157 (Post ID: 592391)
Screenshot 2025-02-09 at 12.28.48 PM
1304×943 182 KB

I’m able to see the markdown response for different countries for question 3, GA 4 on my browser but I’m unable to submit it probably because of network issues. Can someone help me with a fix. Thank you.

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/4/d4d7660a2abfcf04327d7b6a5aadd25ae098f4f1_2_690x498.png)

**Image Description:** The image shows a browser's developer tools console displaying errors related to a web application.  The main section shows instructions for developing a web application that fetches data from Wikipedia and generates a Markdown outline. 


Here's a breakdown of the key features:

* **API Development Instructions:**  A numbered list outlines five steps for creating the web application.  This involves choosing a framework (e.g., FastAPI), fetching Wikipedia content via API, parsing HTML to extract headings, converting the headings to a Markdown outline, and enabling CORS.

* **API Endpoint Input Field:** There's a text input field where the user specifies the API endpoint URL, which is `http://localhost:8000/api/outline`.  Below it, an error message "TypeError: Load failed" is displayed.

* **"Check" Button:** A button labeled "Check" is present, presumably to test the API endpoint.

* **Console Output:** The lower section displays multiple error messages in the browser's developer console.  These errors are consistently stating that a `Fetch API` cannot load the specified URL (`http://localhost:8000/api/outline?country=The+Bahamas`) due to "access control checks."  This indicates a CORS (Cross-Origin Resource Sharing) issue. The console also shows multiple instances of "blocked" messages, confirming the CORS problem.

* **File References (fetch.js):** The error messages reference `fetch.js:75` repeatedly, indicating the error originates from line 75 of a file named `fetch.js`.

In summary, the image shows a developer encountering a CORS error while testing their web application. The application correctly fetches data from Wikipedia, but the browser blocks the response due to missing or incorrect CORS headers on the server-side. The developer needs to adjust the server's configuration to allow cross-origin requests.

---

## Post #208 by 23f3001601 (Post ID: 592394)
image
1701×699 64.6 KB

how to tackle this error  as in 10 th movie year is 2025 but it is showing 2021

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/2/72c35e3d167b724daf8acafdb49ef67425a1d992_2_690x283.png)

**Image Description:** Here's a description of the image content:

The image shows a code editor or similar interface with instructions and a JSON data entry field.  The main text explains that the task is to simulate a streaming service's content acquisition strategy, using JSON data to represent movie titles.  The user is asked to enter JSON data into a text box.

Specifically:

* **Instructions:** The top section explains the assignment's purpose: to help StreamFlix make informed licensing decisions based on subscriber preferences.

* **JSON Data Entry:** A text box contains incomplete JSON data representing a movie. This JSON includes:
    * `"id"`: `"tt26584495"` (a movie ID, likely from IMDb)
    * `"title"`: `"10. Companion - Die perfekte Begleitung"` (a title, potentially a German translation)
    * `"year"`: `"2025"` (the release year)
    * `"rating"`: `"7.4"` (the rating, likely out of 10)

* **Error Message:** Below the JSON box is an error message: `Error: At [10] year. Values don't match. Expected: "2021-". Actual: "2021"`. This indicates a problem with the year field; the system expected a year in the format "2021-" but received "2021".

* **Additional Notes:**  A final section provides additional context about IMDb search results potentially varying by region, the need for manual translation, and the possibility that results might change, requiring the code to be re-run.

In short, the image captures a user's attempt to submit JSON data related to a movie, encountering a validation error regarding the year value.  The context is a coding assignment involving data scraping and content acquisition strategy.

---

## Post #209 by 22f2000008 (Post ID: 592398)
City in my question is 
Nur-Sultan
 .When i search  
Nur-Sultan
 city name in BBC weather page .its show nothing . when i search in google then show Nur Sultan become Astana . then i am going this city  name "Astana ". and got location id 1526273. after i run in collab then showing error.


WhatsApp Image 2025-02-09 at 12.42.40_7957510c
1280×720 109 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/9/5936d1d70999c4944a8f11097d2e36da3047c086_2_690x388.jpeg)

**Image Description:** The image shows a screenshot of a computer screen displaying Python code and a resulting error message.

**The Code:**  The majority of the image shows Python code within a code editor.  The code appears to be designed to:

1. **Create a date range:** It uses the `pandas` library (`pd`) to generate a list of dates.
2. **Format dates:** It formats the dates into 'YYYY-MM-DD' format.
3. **Map dates to descriptions:** It suggests a dictionary is being created where dates are keys and weather descriptions are values, likely obtained from an external source.
4. **Convert to JSON:** It converts the data into a JSON format using the `json` library, using an indent of 4 spaces for readability.
5. **Fetch Weather Data:** This section uses the `requests` library to fetch data from a URL, which is dynamically constructed using the result of a previous API call (to `bbc.com/weather`).  It seems to attempt extracting an 'id' from a nested JSON response to build the full weather API URL.

**The Error:** The code execution encountered an `IndexError: list index out of range` error.  The traceback indicates the error occurs on line 24. This error means the code is trying to access an index in a list (or potentially a nested list) that doesn't exist—likely because the `result['response']['results']['results']` list is either empty or doesn't have an element at index 0.

**Relevant Features:**

* **Line Numbers:** The line numbers (22-26) in the traceback clearly pinpoint the problematic code section.
* **Error Message:**  The `IndexError: list index out of range` is crucial; it's the core problem preventing successful code execution.
* **URL:** The URL `'https://www.bbc.com/weather/'` is significant as it points to the data source the code attempts to access.
* **`result['response']['results']['results'][0]['id']`:** This line shows exactly where the code is failing within the JSON structure. It's trying to get an 'id' from the 0th element of a nested list, which is missing.  The structure it expects is not present in the JSON received from `bbc.com/weather`.
* **Bottom of Screen:** The bottom of the screen shows a timestamp ("completed at 12:42 PM"), indicating the time of the error and some browser icons.

In summary, the image shows Python code attempting to fetch and process weather data from the BBC, but it fails because the JSON response from the BBC weather API doesn't have the expected nested structure, causing an index error.  The developer needs to examine the actual JSON response from the BBC to understand why the expected nested list `result['response']['results']['results']` doesn't contain at least one element at index 0.

---

## Post #210 by 23f1000299 (Post ID: 592420)
this error comes, whenever you answer the other ones and click save. Please answer this question lastly, and submit immediately. it changes within a second. If it continues means, do manual correction and change according to the “expected”

---

## Post #211 by 22f3001315 (Post ID: 592421)
while searching dont put any other filter other than asked in Problem statement.

---

## Post #212 by 23f1000299 (Post ID: 592422)
image
1618×513 46.3 KB

Can anyone help me with the 10th question. Whatever I changed with the code , it is asking something. I checked that these words are not present in the pdf itself

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/8/585776edda81a8af482544acd571fbbdc3c42992_2_690x218.png)

**Image Description:** The image shows a question and answer relating to converting a PDF file to Markdown format using the `prettier` tool (version 3.4.2).  The core of the image displays an example of the Markdown output, showing some errors.  Here's a breakdown:

* **Question:** The top line asks for the markdown content of a PDF file, formatted using the specified `prettier` version.

* **Markdown Attempt:** The main section shows an attempt at a Markdown representation of the PDF's contents. It includes:
    * A level 1 heading (`# Pauci Audentia Sperno Eum`).
    * A paragraph of Latin text (`Tracto adeptio somnus. Neque tantum desidero porro est civitas caute laboriosam valetudo.`).  This line has some words underlined in red, indicating potential errors in the OCR or interpretation of the PDF.
    * A level 2 heading (`## Key Points`).
    * A bulleted list containing two Latin phrases (`Vomito antiquus consequuntur` and `Amplus curis subnecto`). Again, some words are underlined in red here, suggesting issues.

* **Error Message:** An error message points out that words like "back," "legislature," and "info" are missing or not correctly separated in the Markdown output.  This highlights a limitation in the PDF to Markdown conversion process.

* **Disclaimer:** A final paragraph explains that accurately converting PDFs to Markdown is very difficult and usually requires manual correction.  The question is simplified to only test a few basic aspects of the conversion process.


In short, the image showcases a common challenge in document conversion, highlighting the inaccuracies that can arise and the need for manual review to achieve a perfect result. The red underlines serve as visual cues for the parts needing attention during manual correction.

---

## Post #213 by 23f1001231 (Post ID: 592426)
I didn’t get any error for Astana.

The error may be due to incorrect loops in your code that’s why it’s going out of range, check for that.


image
1860×703 133 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/1/011280b40bf86e32b458005e1fa0a98d3213106f_2_690x260.png)

**Image Description:** The image shows a Jupyter Notebook code cell containing data related to weather conditions.  The top section displays a table-like structure in the code editor, listing dates (in DD-MM-YY format) along with high and low temperatures (in Celsius), and a summary of the weather conditions for each day.

The dates range from 25-02-16 to 25-02-22.  The weather descriptions include "Thick cloud and a gentle breeze," "Light cloud and a gentle breeze," "Light snow and a gentle breeze," and "Sunny and a moderate breeze."  Temperature values show a range of freezing and below-freezing temperatures.

The bottom section shows a line of code `df.to_json(orient='records')` which appears to be converting a Pandas DataFrame (presumably named `df`) into a JSON format with the `records` orientation, which structures data as a list of dictionaries, each dictionary representing a row from the dataframe.  Below this, a large portion of the generated JSON data is visible, showing the same weather data structured in JSON format.  This JSON output corroborates the data shown in the table at the top.  The partially visible JSON shows  dates, high and low temperatures, and summary descriptions, consistent with the upper portion of the screenshot.  The use of `\u80b0` and `\u00b0` suggests possible encoding issues with the degree symbols.

The notebook's title bar indicates the file name `bbc-weather-scraping.ipynb`, suggesting this code is part of a project scraping weather data from the BBC website.  The "Cannot save changes" message in the title bar suggests the notebook might be opened in a read-only mode or a restricted environment.  The "Share" button indicates collaborative capabilities.

---

## Post #214 by lakshaygarg654 (Post ID: 592433)
It worked for me; only 4–5 values caused errors, which I fixed manually. Additionally, I corrected the console code, which now provides the correct result.

---

## Post #215 by 23f3004114 (Post ID: 592437)
what is this magic trick… please elaborate …


Error: At [10].id: Values don't match. Expected: "tt16027074". Actual: "tt8008948"



i dont see that value in data …

---

## Post #216 by 23f1001231 (Post ID: 592439)
You can manually edit that. I also have to manually edit one entry to get the correct answer.

---

## Post #217 by swatikap (Post ID: 592443)
Hi,

As mentioned in the question, you have to sort by “joined” so it should be “
https://api.github.com/search/users?q=location:Seattle+followers:
>120&sort=joined&order=desc”

---

## Post #218 by sarvan108 (Post ID: 592444)
There are two “Vienna”. The question4 is referring to which one?

---

## Post #219 by 23f2003853 (Post ID: 592453)
Manually make correction in your answer as provided in the error message. If no such words are available insert those and check

---

## Post #220 by 22f3000586 (Post ID: 592462)
check if the action is commited

---

## Post #222 by tarundude02 (Post ID: 592470)
try copying the expected result and pasting it inside the quotations

---

## Post #223 by 22f3000519 (Post ID: 592471)
Check the log of the daily commit .

---

## Post #224 by ShivaniAdhiyaman (Post ID: 592472)
Ahh, I have the same doubt too!

---

## Post #225 by anu2023 (Post ID: 592476)
For the links, this format worked for me:

[ < link text > ] (#)

---

## Post #226 by anu2023 (Post ID: 592477)
Yes I got it now. Thank you!

---

## Post #227 by HARISH.S (Post ID: 592478)
it should be “2.9” instead of 2.9

---

## Post #228 by 24ds1000082_Vivek (Post ID: 592480)
looks like formatting or the passed conditions have some issue… can you check and verify it once and see?

---

## Post #229 by 21f2000296 (Post ID: 592497)
Error: At [3].title: Values don’t match. Expected: “4. 365 Days - Noch Ein Tag”. Actual: “4. The Next 365 Days”


{“id”: “tt21106646”, “title”: “4. The Next 365 Days”, “rating”: “2.9”, “year”: “2022”}


my result , there is no any entry with “4. 365 Days - Noch Ein Tag” on IMDB

---

## Post #230 by nayonika (Post ID: 592498)
I am getting missing links as error in the 10th question. How to do it?

---

## Post #231 by 23f1002571 (Post ID: 592507)
Mine is giving 1/10 on running without even writing anything? This is happening for Q3? Is it just a glitch?

---

## Post #232 by 23f1002571 (Post ID: 592509)
Yes happened to me too, refresh the page, mine got fixed!

---

## Post #233 by 23f2003853 (Post ID: 592511)
Check you pdf you can find a word with blue colour and underline. Give some dummy link and use link mark with the word

---

## Post #234 by 23f3004114 (Post ID: 592515)
Best way to solve Q2 is , look at the network tab in dev tools and get the url used for assessment and get data from it .

---

## Post #235 by 22f3001754 (Post ID: 592522)
u have used a apace (_) after 2.9  which is not visible at front that’s why it is throwing error , it should be just (“2.9”) not ("2.9 ")

---

## Post #236 by koustubhr (Post ID: 592534)
Agreed and I have tweaked my approach to get the correct answer. But I feel the question instructions should be adjusted accordingly - the question says to get every issueDate and enhancedweatherDescription key value pair - but only 2 such pairs exist ; whereas in the final answer it is forecast date & weather description total 14  pairs.

---

## Post #237 by ABHIJITH_VS (Post ID: 592536)
Screenshot (7)
1366×768 243 KB




Open the BBC Weather website.


Press 
Ctrl + Shift + I
.


Select the ‘Network’ menu.


Select ‘Fetch/XHR’.


Type ‘Karachi’ in the input field on the website. 
Do not press Enter
 while entering the location; just type the location. Pressing Enter might cause ‘location?api_key=…’ to disappear.


‘location?api_key=…’ will appear in the inspect menu.


Double-click it to open a web page (
https://locator-service.api.bbci.co.uk/locations?api_key={api_key}
). This will give the API.


Alternatively, single-clicking ‘location?api_key=…’ will open headers where you can see the Request URL and the API key.

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/5/954c6fa15e0841c485fc497035ecb4805336f0cb_2_690x387.png)

**Image Description:** The image shows a computer screen displaying a BBC Weather website and a browser's developer tools.

**BBC Weather Website:** The main part of the screen shows the BBC Weather website.  The search bar shows "karachi" as the current search, with "Karachi, Pakistan" listed below.  A world map is displayed with several city locations pinpointed, including London, Chicago, Tbilisi, San José, Dakar, Brasilia, and Mombasa.  Each city has a small weather icon indicating the conditions.  A "Book Now" button is visible on a banner image.  The website's headline reads "Weather forecasts for thousands of locations around the world".

**Browser Developer Tools:** To the right, the browser's developer tools are open showing the "Network" tab. This tab provides detailed information about network requests made by the webpage.  Specific details visible include:

* **`locationsTapi keyAGbFAKx58hyjQSCXIY...`:** This appears to be an API key used to fetch location data.
* **`Status: 200`:** This indicates a successful HTTP response from the server.
* **`Type: xhr`:**  Indicates an XMLHttpRequest, a common method used for making asynchronous requests to servers.
* **`Initiator: search.js`:**  Shows the JavaScript file responsible for initiating the network request.
* **`Size: 436 B`:**  The size of the data received from the server.
* **`Time: 2.31 s`:**  The time taken for the request and response.

A graph visually represents the timing and size of multiple network requests.  The graph shows a series of small, light blue bars, each representing a data request.

**Windows Activation Prompt:**  At the bottom of the screen, a Windows activation prompt appears, reading "Activate Windows" and "How can I help you?".  This suggests that the operating system is not currently activated.  Further details about the AI-powered chat feature used for assistance is given.

In summary, the image shows a user looking up weather information for Karachi, Pakistan, while simultaneously inspecting network requests within the browser's developer tools.  The inclusion of the Windows activation prompt implies this could be part of a troubleshooting or development process.

---

## Post #238 by HARISH.S (Post ID: 592546)
type 2025 instead of only using 25 for the year

---

## Post #239 by 23f3004024 (Post ID: 592548)
HOW TO DO SCRAPING USING GITHUB ACTIONS

I’m getting no workflow runs error Sir

---

## Post #240 by 22f3000657 (Post ID: 592553)
How to resolve “Error: Incorrect latitude. Check OSM ID ending with 2077”

---

## Post #241 by iamsarthak (Post ID: 592556)
@22f3000657


you can try this-


https://nominatim.openstreetmap.org/search?format=jsonv2&city=Chennai&country=India


change the city and country in the url


there will be a bounding_box field: [min_lat, max_lat, min_long, max_long]

---

## Post #242 by 24ds3000032 (Post ID: 592560)
#question
 10

Hi, Can anyone help me with Question 10?

No matter how i try to post the markdown, it is always showing that either the words are missing or are different from the original. I have tried every possible way i could think of but it is not working.

---

## Post #243 by 24f2003130 (Post ID: 592586)
Getting this question right is a tough nut to crack…so I would rather suggest you to do using the developer tools by inspecting the source code and  putting the breakpoint followed by writing the code in the console to retrieve the expected answer

---

## Post #244 by AryanTikam (Post ID: 592591)
Screenshot from 2025-02-09 17-40-58
1599×155 26.4 KB

Can’t seem to get this working, have tried many variations by now like including my email in each of the name sections in every possible permutation. Probably just some silly mistake I haven’t noticed yet but any help would be appreciated. On Linux Mint if that’s relevant.


main.yml:


name: Daily Commit Workflow

on:
  schedule:
    - cron: '10 17 * * *' 
  workflow_dispatch:

jobs:
  commit:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Add commit using 23f2001216@ds.study.iitm.ac.in
        env:
          PAT: ${{ secrets.PAT }}  # PAT stored as a secret
        run: |
          git config --global user.name "Aryan"
          git config --global user.email "23f2001216@ds.study.iitm.ac.in"

          echo "Daily commit on $(date)" >> daily-log.txt

          git add daily-log.txt
          git commit -m "Automated daily commit on $(date)"

          ls -la
          git status

          git push origin main  
          git push "https://${{ secrets.PAT }}@github.com/${{ github.repository }}.git" main

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/5/f5ae54f911b5d605c241abb9be7073563156a5a8_2_690x66.png)

**Image Description:** The image shows a form field for entering a repository URL, specifically a GitHub repository.  The top line provides instructions: "Enter your repository URL (format: https://github.com/USER/REPO):".

Below this, there's a text input field.  The user has entered "https://github.com/AryanTikam/AryanTikam"  into this field. However, there is a small red circle with a white exclamation mark inside indicating an error.

At the bottom, an error message explains: "Error: Latest run does https://github.com/AryanTikam/AryanTikam/actions/runs/13225425496 not include 23f2001216@ds.study.iitm.ac.in in the name".  This suggests the provided repository URL is not associated with the email address "23f2001216@ds.study.iitm.ac.in". The error likely stems from an authentication or authorization issue.

---

## Post #245 by 23f2005419 (Post ID: 592604)
Hi Team,


I have made the JSON from the IMDB website using JS, But do i miss any filter conditions,


image
1640×302 20.4 KB

I took first 25 films which 5 to 6 rating, but json seems to be different.


Could anyone please tell me what i did wrong here?

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/7/67d552f9ef5b8b06cae0421fe8d91bcdf4352af7_2_690x127.png)

**Image Description:** Here's a description of the image content:

The image shows a code snippet and an error message related to JSON data and an IMDb scraper.

**Key Elements:**

* **Question:**  The top line asks, "What is the JSON data?".

* **JSON Data Snippet:** A box displays a partial JSON object.  Visible key-value pairs are:
    * `"year": "2024"`
    * `"rating": "6.0"`
    * `"id": "tt30292390"`

* **Error Message:** Below the JSON, a crucial error message is highlighted in red:  `Error: At [10]title: Values don't match. Expected: "11. Sebastian Fitzeks Der Heimweg". Actual: "11. The Calendar Killer"`. This indicates a discrepancy between the expected and actual title retrieved from IMDb.  The expected title is in German ("Sebastian Fitzeks Der Heimweg"), while the actual title is in English ("The Calendar Killer").

* **Disclaimer:** At the bottom, a message explains that IMDb search results vary by region, titles might require manual translation, and results change periodically, necessitating code re-runs.  This strongly suggests the code is part of a web scraping project attempting to pull data from IMDb.

In summary, the image documents a problem encountered while scraping data from IMDb. The scraper expected a German title, but received an English one, highlighting the challenges of working with internationalized data and the need for robust error handling in web scraping.

---

## Post #246 by 23f2005419 (Post ID: 592607)
Solved the above issue, please ignore it.

---

## Post #247 by 23f2003717 (Post ID: 592616)
Believe it or not, I solved it


image
657×516 26.1 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/1/414417f047a85a16fdcf3ef8d9f1e0ac38298e91.png)

**Image Description:** The image shows a programming or coding exercise.  The question asks for the markdown content of a PDF, formatted using `prettier@3.4.2`. The answer box contains a series of markdown elements:

* **`|adficio|chirographum|`**: This line uses pipes (`|`) to create a table-like structure, with "adficio" and "chirographum" as the contents of two columns.
* **`|---|---|`**:  This line continues the table structure by defining separators between columns.
* **`|vitae|ipsam|`**:  Another row in the table.
* **`|spectaculum|claudeo|`**: Another row in the table.
* **`|comes|celebrer|`**: Another row in the table.
* **`Decumbo decumbo suadeo totidem apto.`**: This is plain text, not part of the table.


A green checkmark indicates that the answer is correct.

Below the answer box, there's an explanation noting the difficulty of accurately converting PDF content to markdown and stating that this question only tests basic markdown functionality.

---

## Post #248 by 23f2001177 (Post ID: 592618)
In the 10th question, how do we add headings and links to the markdown output?(getting error: Headings missing)

---

## Post #249 by 23f2003717 (Post ID: 592624)
first convert it roughly to md file then use ai and tell it to add (all the errors one by one). and slowly it will solve all the errors


yes i know it is not the correct way to convert pdf to md file but its just a way to trick the checking system.


but i have an issue it gave me error that it does not contains the word “bash, javascript, whole  redesign, net, suasoria” which is not in the actual pdf, but i added it and it worked. it was just pure trial and error.

---

## Post #250 by Vedant22 (Post ID: 592625)
this is a changing dataset so make changes to your answer accordingly and you will get it correct

---

## Post #251 by Vedant22 (Post ID: 592629)
Do the necessary changes as it is said below as it is an everchanging dataset.

You will get the answer correct once you make the changes asked after checking.

---

## Post #252 by Vedant22 (Post ID: 592631)
check you code and do the changes like max_latitude

replace [0] to [1]

---

## Post #253 by 23f3002537 (Post ID: 592632)
image
835×606 34.6 KB

sir in Q4 i am getting this error:


TypeError: Cannot read properties of undefined (reading 'id')



please help me out with it.

Additionally even if i write anything in the code block the err remains same!


@Jivraj
 
@carlton
 
@s.anand
 sir please help me out as only this question left.

anyone facing this issue? let me know



{
     "25-02-09": "Partly cloudy and a moderate breeze",
     "25-02-10": "Sunny intervals and a moderate breeze",
     "25-02-11": "Sunny and a gentle breeze",
     "25-02-12": "Light snow and a fresh breeze",
     "25-02-13": "Light snow and a fresh breeze",
     "25-02-14": "Light snow and a gentle breeze",
     "25-02-15": "Light snow and a gentle breeze",
     "25-02-16": "Light snow and a gentle breeze",
     "25-02-17": "Light snow and a gentle breeze",
     "25-02-18": "Sunny intervals and a gentle breeze",
     "25-02-19": "Light cloud and a gentle breeze",
     "25-02-20": "Light cloud and a gentle breeze",
     "25-02-21": "Sunny and a moderate breeze"
}

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/4/f450d51580b01f5c78c74fda3d31e33c39d5e4cd.png)

**Image Description:** The image shows a coding exercise or problem.  The user is asked to provide a JSON weather forecast description for Nur-Sultan.

**Key elements:**

* **Two JSON snippets:** The top snippet shows a partial JSON object representing a weather forecast for January 1st, 2nd, and 3rd of 2025. The bottom snippet contains a JSON object for several dates in February 2025 (14th, 18th, 19th, 20th, and 21st), also specifying weather conditions for each. The February snippet is marked with an error alert icon.  There's also a date `2023-02-13` listed before the JSON but not formatted as a JSON key-value pair.

* **The Question:** The prompt clearly asks: "What is the JSON weather forecast description for Nur-Sultan?"

* **The Error Message:**  A `TypeError: Cannot read properties of undefined (reading 'id')` is displayed below the JSON, indicating a coding error likely in how the provided JSON is being accessed or processed.

* **"Check" button:** A button labeled "Check" suggests this is an interactive coding environment where the user can submit their answer for validation.

In essence, the image presents a coding challenge where the user needs to correctly format and provide a JSON weather forecast based on the given examples and then likely integrate it into a larger program without causing the observed error.

---

## Post #254 by 23f2000098 (Post ID: 592641)
in my dashboard there is no submit button for ga2,3,and 4 as well and if i check for scores in grades tab for ga2 and ga3 it was given as not submitted , does everyone facing the same ?? if the submit button is visible for anyone plss guide me to rectify that.

regards and thanks.

---

## Post #255 by 23f2000098 (Post ID: 592647)
image
1224×540 18.9 KB

it is showing correct but if i reload the page or press ctrl+c in my terminal its showing this error what should i do now ??

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/f/ef219ad49e61451fe1acd27ae7ca8e29282183ec.png)

**Image Description:** The image shows a coding assignment or exercise, likely related to web development and API creation.  The top section displays a table of contents-style list with headings related to Vanuatu, including "Contents," "Vanuatu," "Etymology," "History," and "Prehistory."

The main body of the image presents a numbered list of five steps outlining the task:

1. **API Development:** Create a web application API endpoint (example: `/api/outline`) that takes a `country` query parameter.
2. **Fetching Wikipedia Content:** Retrieve the HTML from the Wikipedia page for the specified country.
3. **Extracting Headings:** Parse the HTML to extract all headings (H1 to H6), maintaining their original order.
4. **Generating Markdown Outline:** Format the extracted headings into a Markdown outline, starting each heading with a `#`.
5. **Enabling CORS:** Configure the application to allow Cross-Origin Resource Sharing (CORS) to accept GET requests from any origin.

Below the instructions is a text input field labeled "What is the URL of your API endpoint?".  The user has inputted `http://127.0.0.1:8000/api/outline?country=france`.  Below the input field, an error message is displayed:  "TypeError: Failed to fetch". This indicates that the API endpoint the user provided failed to successfully retrieve the data.

The overall context suggests a programming task involving web scraping, data parsing, and API development using a framework like FastAPI. The error message highlights a problem in fetching data from the specified Wikipedia page through the created API.

---

## Post #256 by Haricharan (Post ID: 592684)
image
1150×776 54.1 KB


Respected Sir,

How can I Solve this, I’m not able to solve this one

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/1/71457b8edf035cb36daa79ab63829130b5308c5e.png)

**Image Description:** The image contains a programming challenge.  The top section describes a company, TechInsight Analytics, that uses Hacker News data to gain market intelligence.  Manually monitoring Hacker News is inefficient, so they've built an internal tool using the Hacker News RSS API (HNRSS API) to automate the process.  This tool performs three tasks:

1. **Topic Monitoring:**  Continuously monitors Hacker News for posts about specified technology topics.
2. **Engagement Filtering:** Filters posts based on a minimum point threshold (votes), ensuring only highly engaging and relevant content is selected.
3. **Data Extraction:** Extracts key details, including the post's link, from the qualifying posts.

The **Your Task** section presents a challenge: using the Hacker News RSS API, find the URL of the most recent Hacker News post mentioning "WebRTC" and having at least 30 points.  The steps involved are:

1. **Automate Data Retrieval:** Use the HNRSS API to get the latest Hacker News posts, filtering by topic and minimum points.
2. **Extract and Present Data:** Extract the `<item>` tag containing the `<link>` from the API response.
3. **Share the result:** Enter only the URL into the answer box.

A text box is provided for the answer, initially containing `https://news.ycombinator.com/item?id=41699323`, which is marked as "Incorrect link".  A "Check" button is below to submit the answer.  The overall image is dark-themed and clearly presents a structured problem and its solution process.

---

## Post #257 by 23f2005419 (Post ID: 592689)
Hi,

For the 4th question, We can get the necessary information issueDate and its description from Summary itself right? or am I seeing the stuff in the wrong place?

---

## Post #258 by H1Dd3n_xx (Post ID: 592691)
Change it manually.

add the expected answer

---

## Post #259 by 23f3002537 (Post ID: 592704)
when you press ctrl+c it turns off the server and same goes for refresh.

also you dont need to manually write ?country… just write till outline and turn on the server n you are good to go.

---

## Post #260 by 23f2000098 (Post ID: 592707)
ok this is fine for now and its showing correct also but at the time of evaluation will my server runs??

---

## Post #261 by 23f1001231 (Post ID: 592721)
It is written in the ques to get the link in the link tag. Not the post link.  Like this


image
1464×560 115 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/f/1feee64a40176f409c30dd00704be9b67c9b32e7_2_690x263.png)

**Image Description:** The image shows a snippet of XML code, specifically an RSS feed item.  Key features and text that help understand the content include:

* **`title`:**  The title of the news item is "DoppelBot: Replace Your CEO with an LLM".  This suggests the article discusses using Large Language Models (LLMs) as a CEO replacement.

* **`description`:** This section contains embedded HTML showing a link to the article itself (`https://modal.com/docs/examples/slack-finetune`),  a link to the Hacker News comments section, the number of points (232), and the number of comments (116).

* **`link`:** This tag contains the URL of the main article: `https://modal.com/docs/examples/slack-finetune`. This is likely a tutorial or documentation about fine-tuning a model for Slack.

* **`pubDate`:** Indicates the publication date of the RSS item: Tue, 24 Feb 2025 15:08:21 +0000

* **Overall Structure:** The code is well-formed XML, part of an RSS feed, likely from Hacker News, describing a news item.  The `<item>` tags delineate a single entry within the RSS feed.  The `dc:` and `atom:` namespaces suggest usage of the Dublin Core and Atom syndication formats respectively.

In summary, the image shows an RSS feed entry detailing a Hacker News article about using an LLM called "DoppelBot" to replace a CEO, with links to the article and its comments section on Hacker News, and metadata like publication date and point/comment counts.  The key takeaway is the article's focus on using LLMs within Slack.

---

## Post #262 by Haricharan (Post ID: 592725)
Thank you bro, I will try this

---

## Post #263 by 23f3002537 (Post ID: 592727)
not at all. your last saved marks will be considered

---

## Post #264 by 23f3004162 (Post ID: 592730)
just replace value instead of it. same problem I also that time I check code and modify serval time I faced same error. so just ignore it and replace expected value instead of actual value in our Json.

---

## Post #265 by 23f3004024 (Post ID: 592734)
extract the pdf to markdown format using chatgpt then add links,tables and one blockquote

---

## Post #266 by 23ds3000149 (Post ID: 592736)
Try to use the key ‘enhancedWeatherDescription’ parsing through the summary object (or) use the BeautifulSoup to find ‘div’ with attributes of

class: wr-day-summary

---

## Post #267 by 23ds3000149 (Post ID: 592750)
Hi, please  ensure that your repository is public, if private the response would be 404. If workflow runs is not found, it might be that the number of API calls to your profile/repo might have exceeded, it usually gets reset at the end of the day. Please try again after sometime)

---

## Post #268 by GIRISH_VISHVESHVAR_B (Post ID: 592768)
In question 1 i am getting this error


 {
    "id": "tt21227864",
    "title": "2. You're Cordially Invited",
    "year": "2025",
    "rating": "5.5"
  }



my answer is in above format i tried changing to “2024-”, "2024- " to number tried after reloading the page but still i am getting

Error: At [11].year: Values don’t match. Expected: “2024”. Actual: "2024– "

---

## Post #269 by Sagan (Post ID: 592801)
You have to manually change these thing

from actual change to expected.

For me, error was almost 10 times.

---

## Post #270 by Sagan (Post ID: 592803)
on your 11th or 12th instance change it

write the actual value

---

## Post #271 by 22f1000120 (Post ID: 592809)
If you have submitted on the assignment site and saved it in time, then that score is the actual score and will be updated directly on the student dashboard.

---

## Post #272 by 22f3000639 (Post ID: 592820)
Your answer is correct. Just add a space after the hyphen—it will resolve the problem. Or you can copy and paste from here: '2025– '.

---

## Post #273 by Haricharan (Post ID: 592821)
image
1895×975 73.4 KB

i wrote everything that was there in the pdf file after converting to markdown, there is no code inside the pdf file then how does it expect to have code in markdown, can anyone help

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/e/3e2860ae2ae9e6113188a70581f1c1ce7e7913b4_2_690x355.png)

**Image Description:** The image shows a screen capture of an online coding exercise or quiz.  The primary content is text-based instructions and a coding problem.

**Key features:**

* **Timer:**  A timer in the top left corner displays "03:08:26 left," indicating a time limit for the exercise.
* **Score:** A score indicator shows "Score: 7/10," suggesting a multiple-part question or a series of questions.
* **Exercise Title (implied):** The text focuses on converting a PDF file ("q-pdf-to-markdown.pdf") into Markdown format, then formatting it using Prettier 3.4.2.
* **Instructions:**  Three numbered steps clearly outline the process:
    1. Extract content from the PDF and convert it to Markdown, preserving formatting.
    2. Use Prettier 3.4.2 to format the Markdown.
    3. Submit the formatted Markdown file.
* **Impact Statement:** This section explains the broader purpose of the exercise—to help automate PDF to Markdown conversion, improving productivity, quality, scalability, and integration for EduDocs Inc.
* **Coding Problem:** The core task is to provide the Markdown content of the sample PDF ("q-pdf-to-markdown.pdf") after formatting it with Prettier.  A partially correct answer is already present, showing Markdown links and plain text.  It highlights an "Error: Missing code," indicating the user needs to complete the code.
* **Buttons:** "Check all" and "Save" buttons are visible, suggesting the user can check their answer and save their progress.


The overall context indicates a learning platform or assessment where users practice converting PDF content to Markdown and learn about code formatting tools. The use of a sample PDF and partial solutions is a common instructional technique.

---

## Post #274 by Rrishit (Post ID: 592851)
Yeah! His issue is genuine. Arnav’s JSON seems to be correct, yet these are some issues faced by him.

---

## Post #275 by Rrishit (Post ID: 592864)
Yeah! even I am facing this issue. Despite lot of efforts, last question markdown seems to always incorrect. It is always throwing any sort of error for no reason.

---

## Post #276 by sandeepstele (Post ID: 592869)
The IMDB and weather questions was a pain along with the 10th question, wasted so much time 
@s.anand
 , the questions were nowhere tough, it was the problems with the evaluation part i had spend hours just to  sit and correct the JSON file and no comments on the 10th question’s part.


I am fine with the academia being challenging to study not the evalation making me manually edit solutions


@Jivraj
 
@carlton

---

## Post #278 by 21f3000745 (Post ID: 592877)
yes change manually, there are slight changes which we have to do

---

## Post #279 by 22f3001011 (Post ID: 592879)
For the 8th question, i am getting an error that tells me i have not run the action, though i manually triggered it and confirmed the commit was made. Cant figure out whats wrong.

---

## Post #280 by 22f3002723 (Post ID: 592886)
for second query i am getting this result as row 4 and 5 (Screenshot)… but when testing the results it shows


{"id":"tt22804850","title":"3. The Sand Castle","year":"2024","rating":"4.7"},
{"id":"tt10128846","title":"4. Megalopolis","year":"2024","rating":"4.8"},
{"id":"tt2322441","title":"5. Fifty Shades of Grey","year":"2015","rating":"4.2"},
{"id":"tt4978420","title":"6. Borderlands","year":"2024","rating":"4.6"},



Error: At [4].title: Values don’t match. Expected: “5. Cinquanta sfumature di grigio”. Actual: “5. Fifty Shades of Grey”


image
784×492 91.3 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/3/03e20670dbfaddeb6f2f989235b64cdb9ef7f5c4_2_690x433.png)

**Image Description:** The image contains information about two movies, presented in a list-like format.  Each movie entry includes:

* **A movie poster thumbnail:** A small image representing the film.  For "Megalopolis," it shows a dramatic scene with multiple actors; for "Fifty Shades of Grey," it shows a close-up of the male lead.  Both thumbnails have a "+" symbol in the top-left corner, likely indicating a "more info" or "add to list" function.

* **A movie title:** "Megalopolis" and "Fifty Shades of Grey" are prominently displayed with a numerical prefix indicating their position in a list (4 and 5 respectively).

* **Release year:** The year the movie was released (2024 for "Megalopolis" and 2015 for "Fifty Shades of Grey").

* **Runtime:** The movie's length (2h 18m for "Megalopolis" and 2h 5m for "Fifty Shades of Grey").

* **Rating and number of ratings:** A star rating out of 5 (4.8 for "Megalopolis" and 4.2 for "Fifty Shades of Grey"), followed by the number of ratings in parentheses (33K for "Megalopolis" and 344K for "Fifty Shades of Grey").  There is also a "Rate" button next to each rating, allowing the user to provide their own rating.

* **Metascore:** A numerical score out of 100 (55 for "Megalopolis" and 46 for "Fifty Shades of Grey"). The scores appear in a gold-colored box, suggesting it comes from a critical review aggregate.

* **A brief synopsis:**  A short description of the movie's plot.  For "Megalopolis," it describes a political conflict in the city of New Rome.  For "Fifty Shades of Grey," it summarizes the life-changing encounter of a literature student.

In short, the image displays a section from a movie database or review website, providing essential details for each of these two films.

---

## Post #281 by 21f3000745 (Post ID: 592901)
image
606×293 20.3 KB

sir earlier it was correct and now i submit it again after running my code it shows error.  sir i have done it correct two times earlier. but now again as i click on save button it changed. these tasks are taking too much time and creating more difficulties. please look into this 
@s.anand
 
@Jivraj
 
@Saransh_Saini

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/5/f57651c1c8662de593d35d1771ddf8eb5f3f2cc2.png)

**Image Description:** The image shows a question asking for a JSON weather forecast description for Vienna.  Below the question is a code snippet that appears to be an attempt at creating a JSON object, but it's flawed.


Here's a breakdown of the content:

* **The Question:** "What is the JSON weather forecast description for Vienna?" This is the main query.

* **Attempted JSON Object:**  The code snippet is intended to be a JSON object representing a weather forecast. It uses dates (YYYY-MM-DD) as keys and weather descriptions as values.  The format is almost correct; each key-value pair is properly formatted.


* **Dates and Descriptions:** The forecast covers February 10th to 14th, 2025, with descriptions like "Sunny and a gentle breeze," "Sunny intervals and a gentle breeze," and "Light cloud and a moderate breeze."

* **Error Message:** The crucial part is the error message: "Error: At root: Different number of properties". This indicates that the JSON is malformed.  In proper JSON, each key-value pair within an object must have matching opening and closing curly braces (`{}`). The image does not contain the closing curly brace for the entire JSON object.  This likely caused the error.

---

## Post #282 by 22ds2000011 (Post ID: 592902)
image
2100×400 38.1 KB


Hi Team ,


Are we expecting the result to match exactly as per the benchmark of qa4.

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/3/03c2659de1532aefc02ea8eaa831c0955bf85b5d_2_690x131.png)

**Image Description:** The image shows a code snippet and an error message.  The top part displays a question: "What is the JSON data?".  Below that, a section of JSON data is presented, contained within a light-pinkish border:

```json
"title": "1. The Night Agent",
"year": "2023-",
"rating": "7.5"
},
{
```

This JSON data represents a data structure with the fields "title," "year," and "rating."  The values are strings, indicating the title of something ("1. The Night Agent"), a partial year ("2023-"), and a rating ("7.5").  Note the incomplete structure, indicated by the trailing comma and open curly brace.


At the bottom, an error message is displayed:

`Error: At [8].title: Values don't match. Expected: "9, Incorrect answer jalement invités". Actual: "9. You're Cordially Invited"`

This indicates a testing or validation error.  The error message is specifically referencing the "title" field at index [8] (implying this is part of an array of JSON objects).  The expected value was `"9, Incorrect answer jalement invités"`, but the actual value received was `"9. You're Cordially Invited"`.  The difference lies in the punctuation and phrasing, indicating a discrepancy in the data.

---

## Post #283 by 23f3002537 (Post ID: 592913)
just edit some of the spellings in answers manually as per errors you get n you are good to go.

---

## Post #284 by 23f1000625 (Post ID: 592917)
22f3002723:




Cinquanta sfumature di grigio






It is just a translation of the same movie… it’s not different

Copy paste the Expected: “title” and click on check

It’ll work

---

## Post #285 by 23f2001305 (Post ID: 592924)
image
1802×751 40 KB


Saved responses are not being displayed and also page keeps refreshing…

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/2/221c84f86d6febf296e0a4a6903bb70c607afd41_2_690x287.png)

**Image Description:** This image shows a dark-themed interface, possibly for an online quiz or assignment. 


Here's a breakdown of the content:

* **Top Bar:** Displays "02:23:44 left" indicating a time limit, "Score: 0," buttons for "Check all" and "Save,". There is also a small piece of text stating that looking at the code is allowed.

* **Discourse Section (Two Boxes):**
    * **Box 1:** A teal button with "Have questions? Join the discussion on Discourse" encourages participation in a forum named Discourse.
    * **Box 2:** Explains that IITM BS students can earn a bonus mark on the graded assignment by participating in a Discourse discussion thread. It specifically mentions the discussion's topic: "GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]".

* **Login Information:** Shows the user is logged in as "23f2001305@ds.study.iitm.ac.in". A "Logout" button is also present.

* **Loading Indicator:** A spinning loading circle is visible at the bottom, suggesting an ongoing process.

The overall context suggests an academic setting, possibly a course at the Indian Institute of Technology Madras (IITM), where students are taking a graded assignment involving data sourcing and using the Discourse platform for discussion and bonus points.

---

## Post #286 by namanshyamsukha (Post ID: 592925)
@all
, in q4 Actually the answer data is sync with current weather description therefore the answer changes. Make sure to update your json file before submitting.

---

## Post #287 by gouthamnischay (Post ID: 592928)
try refreshing the page and re-run the script. as the data gets updated the answer also changes.

---

## Post #288 by 21f3002277 (Post ID: 592934)
refer to the link post,










GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]
 
Tools in Data Science





    use this 
Google Colab
 with the city name to get the Json Body just change the date format. 

@23f2004752

---

## Post #290 by rohitgarg (Post ID: 592938)
i 'm here for the bonus marks,


But since i am here. Just want to appreciate the course and your efforts towards this.


We need more “teachers” like you, who really puts an extra effort in the course.


And i have never seen any course cool as this,




like appreciating tweaking things, using dev console to tweak things, keep the code checks on client side (
and as S Anand’s Student i have leveraged that freedom  
, gave client side answer checks’s code to 
o1
 and it reverse engineered the minifed code, and lots of question were solved by that only, but really curious on how others are doing this
)


keeping the cutting edge tech in course, like function calling from OpenAI.

( 
i have seen some students solutions, they were using regex to solve that problem 
)




image
1483×687 48.1 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/5/45b8773aa8f61abb7b67eaa7e81ae42fcfc0e576_2_690x319.png)

**Image Description:** Here's a description of the image's content:

The image shows a dark-themed interface, likely from an online learning platform or grading system.  The text is primarily light teal on a dark green/black background.

The key elements are:

* **Discourse Invitation:** A banner at the top invites users to join a discussion on Discourse, a platform for online forums.

* **Bonus Marks Information:** A box explains that IITM BS students can earn a bonus mark on a graded assignment by participating in a specific Discourse discussion thread related to GA4 - Data Sourcing. The thread is identified as "TDS Jan 2025".

* **Login Status:**  The interface displays the user's login information:  `2212001394@ds.study.iitm.ac.in`.  A "Logout" button is visible.  This suggests a student logged into the system.

* **Recent Saves:** A section shows recent saved scores, indicating a graded assignment with three attempts.  Each entry includes a "Reload" button (presumably to reload the submission), a timestamp (all on February 9th, 2025), and the score achieved (10, 8, and 8).  The text clarifies that the most recent score is the official one.

In summary, the image depicts a student's view of an assignment system. It emphasizes the opportunity to earn bonus marks by participating in a Discourse forum and displays their saved scores for the assignment.  The student's ID and timestamps are prominently shown.

---

## Post #291 by Abhay222 (Post ID: 592942)
why everytime question 2 answer is showing error in json?

---

## Post #292 by rohitgarg (Post ID: 592949)
What error are you getting 
@Abhay222
 ?


Can you post a screenshot or error details ?

---

## Post #293 by Jeleshiya (Post ID: 592950)
Is it safe to skip Q4 for those who got the city named Nur-Sultan, since it has been renamed to Astana, and the answer for Astana is incorrect in the portal?

---

## Post #294 by parthpatel (Post ID: 592953)
@s.anand

There is possibly wrong evaluation in q6 as it is taking in 2nd latest link as the correct answer. I might be wrong, but the latest one is giving me incorrect evaluation while the 2nd latest is giving me the correct score.

---

## Post #295 by 22f3002184 (Post ID: 592954)
getting the same issue Error: At [12].year: Values don’t match. Expected: "2024– ". Actual: “2024”

---

## Post #296 by Abhay222 (Post ID: 592960)
yes this kind errors.

---

## Post #297 by rohitgarg (Post ID: 592968)
@Abhay222
 
@22f3002184


if you look closely the expected value is 
2024- 
 and actual that you are supplying is 
2024
.

Difference ? your value does have a 
-
 and a space at the end.

reason ? you might be scraping it ? 
trim()
 or maybe using 
innerText
 to get tag’s text ?

---

## Post #298 by adeepu.here (Post ID: 592971)
it seems we are intended to provide country specific versions for Individual students simulating being an analyst for MNC in various locations. Clearly you got Spain and I seem to have gotten France, although it doesn’t seem to be mentioned in the question itself.

---

## Post #299 by Saransh_Saini (Post ID: 592973)
Thank you Tanya for pointing out this issue.

Just tell me this, has your city changed? If yes then what was it earlier and what is it now.

---

## Post #301 by 23f2000098 (Post ID: 592978)
any reply regarding this please

---

## Post #302 by 23f1001301 (Post ID: 592982)
22f2000113:




For question 2 getting Error: At [8].title: Values don’t match. Expected: “9. Un matrimonio di troppo”. Actual: “9. You’re Cordially Invited” But this movie is not found when searched by name






the movie may have  different title on IMDb (perhaps in another language) according to region which is why there isnt an exact match u can manually format it to get marks

---

## Post #303 by Saransh_Saini (Post ID: 592984)
GA2 - Deployment Tools - Discussion Thread [TDS Jan 2025]
 
Tools in Data Science





    We have removed that button, cause it was causing confusion among the students. 
If you have saved your answers on the TDS portal then you need not worry, you will be marked. The button was just there to ensure you saw the assignment on the TDS portal. 
Regards, 
TDS TA
  





Read this

---

## Post #304 by nayonika (Post ID: 592991)
Try changing it manually. Some values keep changing due to change in server.

---

## Post #305 by 23f1001126 (Post ID: 592995)
Alright so in Q4 of W4, We have to extract weather forecast data from bbc servers for a given city. The city I have been given Nur-Sultan is not present in the bbc data base, it appears the city is now known as Astana and is listed in the bbc database as Astana.

Since Nur-Sultan doesn’t exist in the bbc database, all of my attempts to extract data for it were meet with failure. So I extracted the data for Astana and pasted it in the portal but that doesn’t work as well and throws the following error “TypeError: Cannot read properties of undefined (reading ‘id’)”

What am I suppose to do? 
@carlton
 
@Jivraj
 
@Saransh_Saini


Screenshot 2025-02-09 175948
1823×850 82.3 KB


Below is the data for Astana that I was able to extract, Since Nur-Sultan doesn’t exist in the bbc database:

{

“2025-02-09”: “Partly cloudy and a moderate breeze”,

“2025-02-10”: “Sunny intervals and a moderate breeze”,

“2025-02-11”: “Sunny and a gentle breeze”,

“2025-02-12”: “Light snow and a fresh breeze”,

“2025-02-13”: “Light snow and a fresh breeze”,

“2025-02-14”: “Light snow and a gentle breeze”,

“2025-02-15”: “Light snow and a gentle breeze”,

“2025-02-16”: “Light snow and a gentle breeze”,

“2025-02-17”: “Light cloud and a gentle breeze”,

“2025-02-18”: “Sunny intervals and a gentle breeze”,

“2025-02-19”: “Light cloud and a gentle breeze”,

“2025-02-20”: “Light cloud and a gentle breeze”,

“2025-02-21”: “Sunny and a moderate breeze”,

“2025-02-22”: “Light snow and a moderate breeze”

}

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/b/cb0483e0b093e1e994ba44b8136f6b4f5865cdc7_2_690x321.png)

**Image Description:** The image shows a coding challenge or quiz interface.  The top section displays a timer (06:00:20 left), a score (3/10), and buttons to "Check all" and "Save".

The main part of the image consists of three numbered steps describing an API-based task:

1. **API Integration and Data Retrieval:**  This step instructs the user to use the BBC Weather API to get a weather forecast for Nur-Sultan, Kazakhstan, and to use a location ID obtained from a GET request to a locator service.  It highlights the need for API keys, locales, filters, and search terms.

2. **Weather Data Extraction:** This step describes retrieving the forecast data using the `locationId` obtained in step 1, again using a GET request to a weather broker API.

3. **Data Transformation:** This step focuses on transforming the API response into a JSON object. It specifies extracting `issueDate` and `enhancedweatherDescription` for each day's forecast and mapping them to create a JSON object where `issueDate` is the key, and `enhancedweatherDescription` is the value.  An example of the expected JSON output is given.

Below this, the challenge presents the question:  "What is the JSON weather forecast description for Nur-Sultan?". The user is to construct the correct JSON object based on the given instructions. A partially completed, incorrect JSON response is shown with a "TypeError: Cannot read properties of undefined (reading 'id')" error message.  The code shows some correct entries, suggesting the error arises later in the code not displayed.  A "Check" button is visible, presumably to submit the answer.

---

## Post #306 by AnvithaV (Post ID: 592996)
same problem, could anyone help what is wrong.

---

## Post #307 by rohitgarg (Post ID: 593009)
@AnvithaV
  check this out

---

## Post #308 by 21f3000745 (Post ID: 593014)
No the city is same as before. But i think it fetches the latest data. As i saved it yesterday it was correct. But today when i  clicked on save button again it got wrong.

---

## Post #309 by 21f3000745 (Post ID: 593020)
What error are you getting ?

---

## Post #310 by vidya19 (Post ID: 593023)
how to approach question 8 of ga4

---

## Post #311 by 23ds3000040 (Post ID: 593024)
For question 
#8
. Can I use the .github/workflows that I created for the previous assignments or i need to create a new workflow?

---

## Post #312 by 22f3002184 (Post ID: 593028)
still the same   {“id”:“tt24871974”,“title”:“12. Subservience”,“year”:“2024”,“rating”:“5.4”},

Error: At [12].year: Values don’t match. Expected: "2024– ". Actual: “2024”

---

## Post #313 by 23f1002534 (Post ID: 593029)
Change the value manually

---

## Post #314 by 24ds2000108 (Post ID: 593030)
I am still not sure why the github action question is not working for me. I have manually triggered the workflow multiple times but i keep getting the same ‘name’ error even though it has been specified in the code. Can somebody kindly help?

---

## Post #315 by 21f3000745 (Post ID: 593031)
Have you given your email id in name ?

---

## Post #316 by jashmevada (Post ID: 593034)
image
1865×789 48 KB

Completed GA4 with 10/10.

I have also use tweak that the some answer and question are check and generate on client side.

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/1/21dbd684835d5255b1520553a57a871933d026c3_2_690x291.png)

**Image Description:** This image shows a screen capture of an online quiz or assessment platform. 


Here's a breakdown of the content:

* **Top Bar:** A green bar at the top displays "01:37:59 left", indicating a remaining time of 1 hour, 37 minutes, and 59 seconds.  It also shows the current score as "Score: 10/10," buttons labeled "Check all" and "Save," and a small icon suggesting settings or options.

* **Login Information:** Below the top bar, the text "You are logged in as 23f2003807@ds.study.iitm.ac.in" displays the user's login credentials, suggesting a university or educational institution affiliation. A "Logout" button is also present.

* **Recent Saves:** A dark-green box labeled "Recent saves" shows three entries, each indicating a time, date (all on February 9th, 2025), and a score. The most recent save is highlighted as the official score. The "Reload" button next to each entry suggests that these scores can be reviewed.

* **Questions:** Below the "Recent Saves" section, the heading "Questions" is displayed.  A single question is visible: "1. Import HTML to Google Sheets (1 mark)," indicating a question related to data import and possibly worth one mark.

The overall design suggests a clean, dark-themed interface typical of online learning management systems or testing platforms. The information strongly points to an academic setting.

---

## Post #317 by 21f3000745 (Post ID: 593036)
See there is difference of hyphen . Correct it manually.

---

## Post #318 by Saransh_Saini (Post ID: 593039)
Just try re-running your code once and paste in the current response. Check if its working or not.

---

## Post #319 by 23f1002534 (Post ID: 593040)
Change the slight differences manually accordingly with the expected values

---

## Post #320 by 23f1003139 (Post ID: 593043)
I haven’t done MLP and BDM so should I drop TDS now

---

## Post #321 by 23f2005419 (Post ID: 593053)
Hi,


I couldn’t able to create markdown from pdf, it showing missing links, but i couldn’t able to find the link in pdf either. I think i’m missing something.


anyone suggest some way how to do pdf to markdown correctly?

---

## Post #322 by 23f2000573 (Post ID: 593060)
if it says something is missing, just add the same. refer to week-2 question 1 for markdown syntax if necessary

---

## Post #323 by 24ds2000108 (Post ID: 593062)
yes

But still doesnt work

---

## Post #324 by 21f3000745 (Post ID: 593068)
In q10 i am geeting …missing links- error

Any idea how to correct this

---

## Post #326 by 22f1000535 (Post ID: 593073)
Beyond the specific tools mentioned (like 
IMPORTHTML
 in Google Sheets or 
httpx
 and 
lxml
 in Python), what are the broader 
ethical considerations
 when scraping data from websites, and how can developers ensure they are acting responsibly and respecting website owners’ rights and resources?

---

## Post #327 by 23f2000098 (Post ID: 593075)
image
1104×369 21.3 KB

is everything fine with the answer format?? i am trying this for so long anything i want to change ??

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/b/eb807d6c56fc02a8517f9390f49d9b582b1f8150.png)

**Image Description:** The image shows a coding challenge or assignment.  The task is to find the link to the most recent Hacker News post that mentions "WebAssembly" and has at least 86 points.  The user needs to use the Hacker News RSS API to accomplish this.

The instructions are broken down into three steps:

1. **Automate Data Retrieval:** Use the API to fetch the latest Hacker News posts, filtering by the minimum points requirement.
2. **Extract and Present Data:** From the API's response, extract the most recent post `<item>` and get the `<link>` tag from within it.
3. **Share the result:**  Enter only the URL into the answer box provided.

A text box is provided where the user enters their answer. The user has entered `https://news.ycombinator.com/item?id=38790552`, but this answer is marked as incorrect with a red "Error: Incorrect link" message and a warning symbol.  This suggests the user's attempt at solving the problem was unsuccessful.

---

## Post #328 by 21f3000745 (Post ID: 593085)
What is the error are you facing ?

---

## Post #329 by 22f3000804 (Post ID: 593088)
can someone  help through this error!!


Capture
1119×204 37.9 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/5/e5e41010e6ca37b8390b22c4c9ea80d49ea2394d_2_690x125.jpeg)

**Image Description:** The image shows a code snippet displaying JSON data and an error message.

The JSON data consists of six entries, each representing a movie or show.  Each entry contains four fields:

* **`id`**: A unique identifier, seemingly a tt-prefixed alphanumeric string.
* **`title`**: The title of the movie or show.
* **`year`**: The year or year range in which the movie or show was released or aired.
* **`rating`**: A numerical rating for the movie or show.


The error message, "Error: At [10]year: Values don't match. Expected: "2021-". Actual: "2021-", indicates a problem with the `year` value in the tenth entry of the JSON data.  The system expected the value to match "2021-", but the actual value was also "2021-". While this *appears* to match, there may be a difference not visible (e.g. whitespace).  This suggests a discrepancy in data formatting or expectations concerning the year field, which should be investigated further for proper data validation.

The JSON data is displayed within a dark-themed text box, highlighted by a maroon border.  A small, circular icon with an exclamation mark inside is present in the upper right corner of this text box, further signaling an error or warning.

---

## Post #330 by 23f2000573 (Post ID: 593093)
Check if you have made the query proprly. also, check if you taken the correct link from the item

---

## Post #331 by 21f3000745 (Post ID: 593094)
in q10 i am getting error- missing links.

can i get any explanation about this error so that i can figure out this ?


@Saransh_Saini
  as i left with this question only

---

## Post #332 by jashmevada (Post ID: 593095)
Pdf content one link, I think your converting method was unable to convert link into markdown format , add it manual from pdf.

---

## Post #333 by 21f3000745 (Post ID: 593097)
I have done that also but still getting same error

---

## Post #334 by 21f3000745 (Post ID: 593099)
The one with blue line must be link here in the pdf.

---

## Post #335 by 23f2005419 (Post ID: 593102)
After that it asking to add tables, i added the same but the issue ‘Missing Tables’ exists

---

## Post #336 by 23f2000573 (Post ID: 593103)
23f2000573:




if it says something is missing, just add the same. refer to week-2 question 1 for markdown syntax if necessary






refer to this 
@21f3000745








 22f3000804:




can someone help through this error!!






if it is saying something has a mismatch, just spot the mismatch one by one and manually change it 
@22f3000804

---

## Post #338 by 21f3001797 (Post ID: 593125)
Here for the bonus marks, it was great solving the GA4.

---

## Post #339 by Megha (Post ID: 593130)
After you click the link, a page containing all the questions will appear. Attempt them and save it on that particular page using your IITM email ID. Through your ID, submissions will be taken.

---

## Post #340 by 21f3000745 (Post ID: 593144)
Thankyou , but now i am getting missing code error. What it means? 
@23f2000573

---

## Post #341 by 23f3001752 (Post ID: 593151)
You just have to add a space after a hyphen

---

## Post #342 by Saransh_Saini (Post ID: 593157)
Check if you are using table formating where there is a table, also there is perhaps a code block in the pdf where a small section of text is in different font than the rest.

---

## Post #343 by 21f3000745 (Post ID: 593167)
No there is no code block in the pdf. Now i m getting missing code error. Why this error can arise 
@Saransh_Saini

---

## Post #344 by 21f2001369 (Post ID: 593171)
I am also facing the same error in this question

---

## Post #345 by vidushi (Post ID: 593188)
the answer format is correct the link is probably not the latest one, I had the same issue because my code was working only for the first 100 entries… you should try paginating your code so it can cover more entries

---

## Post #346 by Adityism (Post ID: 593189)
just change the values as itis coming in the error

---

## Post #347 by vidushi (Post ID: 593207)
change the name manually as the name is diiferent on imdb according to the region, I had the same issue…

---

## Post #348 by 23f3002537 (Post ID: 593208)
are you able do it now? Reload and check

---

## Post #349 by 22f3002184 (Post ID: 593210)
yes facing the same thing

---

## Post #350 by 23f2000573 (Post ID: 593218)
you are missing code block


Normal : print(123)

Code Block : 
print(123)


you can refer to week 2 q1  for the syntax of code block

---

## Post #351 by 22f3000910 (Post ID: 593220)
Screenshot 2025-02-09 234028
1910×314 56.7 KB

anyone have idea about this error?

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/b/2b416c389edbb461f8f61e84d1ab68d273774860_2_690x113.png)

**Image Description:** The image shows a code snippet and an error message.

The code snippet appears to be a JSON array of movie data.  Each object in the array represents a movie and contains the following keys:

* `"year"`: The year the movie was released (integer).
* `"rating"`: The movie's rating (float).
* `"id"`: A movie ID (string, appears to be an IMDb ID starting with "tt").
* `"title"`: The movie's title (string), often including a sequential number.

The error message below the JSON data,  `TypeError: Cannot read properties of null (reading 'textContent')`, indicates a JavaScript error.  This means the code trying to access the `textContent` property of a variable or object that is currently `null` (meaning it doesn't have a value).  This error is unrelated to the JSON data itself, but rather to the code that is attempting to use it.  The JSON itself is syntactically valid.

---

## Post #352 by 22f3002184 (Post ID: 593228)
image
1757×367 48.3 KB

getting this error

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/d/dd7e129ca76ee1af2b83f85ed831e58c5010f861_2_690x144.png)

**Image Description:** The image shows a webpage section discussing the impact of automating bounding box data processing for a company called UrbanRide.  The section lists four key benefits: optimizing routing, improving fleet allocation, enhancing market analysis, and scaling operations.

Below this, there's a question asking for the maximum latitude of Riyadh, Saudi Arabia's bounding box, as determined by the Nominatim API.  A text box contains a user's answer: "27.7020999".  Below the answer, an error message indicates that the provided latitude is incorrect and suggests checking an OSM ID ending with "8390".  The "①" symbol likely indicates an information icon or tooltip related to the error message.

---

## Post #353 by 21f3000745 (Post ID: 593231)
Yes thankyou i noticed that code block.

But now getting missig heading 
@Saransh_Saini

---

## Post #354 by 23f3002537 (Post ID: 593232)
@carlton
 sir what about this question.

---

## Post #355 by 23f3001752 (Post ID: 593233)
You have to go to the Settings tab, select Actions from the left panel and choose General from the drop-down list. Then scroll down completely and choose “Read and Write Permission” under the Workflow Permission section

---

## Post #356 by 22f3002723 (Post ID: 593240)
Getting at root differnt number of properties for below



"2025-02-10": "Sunny intervals and a gentle breeze",
"2025-02-11": "Light rain showers and a gentle breeze",
"2025-02-12": "Thundery showers and a gentle breeze",
"2025-02-13": "Thundery showers and a moderate breeze",
"2025-02-14": "Sunny intervals and a gentle breeze",
"2025-02-15": "Drizzle and a gentle breeze",
"2025-02-16": "Sunny and a gentle breeze",
"2025-02-17": "Sunny intervals and a gentle breeze",
"2025-02-18": "Sunny intervals and a gentle breeze"}

---

## Post #357 by 23ds3000241 (Post ID: 593242)
I’m assuming it’s occurring because the text formatting for the JSON is incorrect. Try and put it in the correct format

---

## Post #358 by 23f1001126 (Post ID: 593247)
I’ve reloaded a dozen time and even extracted the data again and again to account for any changes but it still doesn’t work.

---

## Post #359 by 22f3002723 (Post ID: 593249)
22f3002723:




{"2025-02-10": "Sunny intervals and a gentle breeze",
"2025-02-11": "Light rain showers and a gentle breeze",
"2025-02-12": "Thundery showers and a gentle breeze",
"2025-02-13": "Thundery showers and a moderate breeze",
"2025-02-14": "Sunny intervals and a gentle breeze",
"2025-02-15": "Drizzle and a gentle breeze",
"2025-02-16": "Sunny and a gentle breeze",
"2025-02-17": "Sunny intervals and a gentle breeze",
"2025-02-18": "Sunny intervals and a gentle breeze"}







{“2025-02-09”: “Partly cloudy and light winds”,

“2025-02-10”: “Sunny intervals and a gentle breeze”,

“2025-02-11”: “Light rain showers and a gentle breeze”,

“2025-02-12”: “Thundery showers and a gentle breeze”,

“2025-02-13”: “Thundery showers and a moderate breeze”,

“2025-02-14”: “Sunny intervals and a gentle breeze”,

“2025-02-15”: “Drizzle and a gentle breeze”,

“2025-02-16”: “Sunny and a gentle breeze”,

“2025-02-17”: “Sunny intervals and a gentle breeze”,

“2025-02-18”: “Sunny intervals and a gentle breeze”}

---

## Post #361 by 23ds3000241 (Post ID: 593254)
There needs to be two weeks worth of data so if it’s starting from the 9th it should be till the 22nd

---

## Post #362 by shivanshgupta0007 (Post ID: 593259)
make the edits clearly in the repository and then open it, the url that is then showed. Just copy and paste it into the box, it will work

---

## Post #363 by mohiit (Post ID: 593261)
what problem is their in ques 2 and 3

---

## Post #364 by 23f3002537 (Post ID: 593262)
yeah same for me. seems we were unlucky

---

## Post #365 by 22f3002175 (Post ID: 593265)
What can I refer to for proper steps to solve Question 10?

Thanks!

---

## Post #367 by Rohitb (Post ID: 593270)
Q10 is giving errors even after doing everything

---

## Post #368 by 22f3002723 (Post ID: 593271)
23ds3000241:




o if it’s






getting values dont match for below now

{“2025-02-09”: “Partly cloudy and light winds”,

“2025-02-10”: “Sunny intervals and a gentle breeze”,

“2025-02-11”: “Light rain showers and a gentle breeze”,

“2025-02-12”: “Thundery showers and a gentle breeze”,

“2025-02-13”: “Thundery showers and a moderate breeze”,

“2025-02-14”: “Sunny intervals and a gentle breeze”,

“2025-02-15”: “Drizzle and a gentle breeze”,

“2025-02-16”: “Sunny and a gentle breeze”,

“2025-02-17”: “Sunny intervals and a gentle breeze”,

“2025-02-18”: “Sunny intervals and a gentle breeze”,

“2025-02-19”: “Light cloud and a gentle breeze”,

“2025-02-20”: “Sunny intervals and a moderate breeze”,

“2025-02-21”: “Light rain showers and a moderate breeze”,

“2025-02-22”: “Light cloud and a moderate breeze”}

---

## Post #369 by 22f3002723 (Post ID: 593274)
thanks for the help…

---

## Post #371 by carlton (Post ID: 593345)
@23f3002537
, 
@21f3000745
, 
@Jeleshiya


Anyone who received the Nur-Sultan parameter for this question and at least attempted it will get a mark.


Kind regards

---

## Post #372 by 23f3002537 (Post ID: 593528)
sir what about bonus marks cuz my score was 9/10 due to q4(Nur-sultan).

---

## Post #373 by carlton (Post ID: 593703)
The bonus mark will be processed afterwards. That is checked before the scores are pushed to portal.

---

## Post #374 by vaishnavi.k (Post ID: 593777)
Nominatim API gives me the bounding box of the location. How exactly the bounding box helps me to find the details of the location?

---

## Post #375 by Rehbar (Post ID: 593779)
I am facing issues in Q9 , can you help me out?

---

## Post #376 by Lokkiii (Post ID: 593781)
const movies = 
;


document.querySelectorAll(‘.sc-d5ea4b9d-0.ejavrk’).forEach((item, index) => {

if (index >= 25) return; // Stop after collecting 25 movies


const titleElement = item.querySelector('.ipc-title__text');
const yearElement = item.querySelector('.sc-d5ea4b9d-7.URyjV.dli-title-metadata-item');
const ratingElement = item.querySelector('.ipc-rating-star--rating');

if (titleElement && yearElement) {
    const idMatch = item.querySelector('a[href*="/title/tt"]')?.href.match(/tt(\d+)/);
    const id = idMatch ? `tt${idMatch[1]}` : null;
    const title = titleElement.innerText.trim();
    //const yearText = yearElement.innerText.replace(/\D/g, "").trim(); // Remove non-numeric characters
    const yearText = yearElement.innerText.trim();
    const year = yearText ? yearText : null; // Keep year as a string
    const rating = ratingElement ? ratingElement.innerText.trim() : null; // Keep rating as a string

    if (id && title && year && rating && parseFloat(rating) >= 3 && parseFloat(rating) <= 5) {
        movies.push({ id, title, year, rating });
    }
}



});


// Output JSON data with no spaces after colon

console.log(JSON.stringify(movies, (key, value) => typeof value === ‘string’ ? value.trim() : value, 0));

---

## Post #377 by HARISH.S (Post ID: 593895)
image
1903×808 62.7 KB

sir i have completed and saved the test but it shows score 0. and also


image
1735×772 124 KB

the graded assignment is showing like i didn’t submit it. please check on this.

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/3/43e1fb12da806e25ca6f883d5d24726944c0fb38_2_690x292.png)

**Image Description:** This image shows a screen capture of what appears to be an online grading system or assignment platform.  Here's a breakdown of the content:

* **Header:**  The top bar shows the date and time the screen was captured ("Ended at Sun, 9 Feb, 2025, 11:59 pm IST"), a current score of "0", and buttons to "Check all" and "Save".

* **Bonus Marks Section:**  This section details a bonus marking scheme. IITM BS (presumably Indian Institute of Technology Madras Bachelor of Science) students can earn one bonus mark on a graded assignment by participating in a discussion thread on Discourse.  The discussion topic is specified as "GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]".

* **Login Information:** The platform displays the logged-in user's email address: "23f3000975@ds.study.iitm.ac.in" and a "Logout" button.

* **Recent Saves Section:** This section shows a history of saved scores, indicating that the user saved their work three times on 9/2/2025.  The times and corresponding scores are listed:
    * 8:04:05 pm - Score: 8
    * 8:03:25 pm - Score: 8
    * 4:03:58 pm - Score: 4

The overall appearance suggests a dark theme interface common in many online applications.  The information strongly suggests an academic context, potentially for a course on GA4 (Google Analytics 4) data sourcing.  The "Reload" buttons likely indicate the user's ability to revert to specific saved versions of their work.

![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/c/6c41591b6b3db0e9e48a14f4e11e3a21719ee2ce_2_690x307.png)

**Image Description:** This image shows a screen capture of an online learning platform's interface.  The main content is divided into two sections:

**Left Section:** This section displays a list of modules and a graded assignment. The modules include:

* Module 2: Deployment Tools
* Module 3: Large Language Models
* Project 1
* Module 4: Data Sourcing
* Graded Assignment 4 (highlighted)
* Module 5: Data Preparation

The "Graded Assignment 4" is highlighted, indicating it might be the focus of the user's current activity.

**Right Section:** This section contains information about "Graded Assignment 3".  Key details include:

* **Due Date:** The due date for submission has passed (2025-02-05, 23:59 IST).
* **Multiple Submissions:** Students can submit the assignment multiple times before the due date.  The final submission will be graded.
* **Troubleshooting:**  It provides troubleshooting steps for access issues. These include:
    * Disabling ad blockers.
    * Enabling cookies and JavaScript.
    * Using Chrome browser.
    * Disabling browser extensions.
    * Deactivating overly aggressive antivirus software.
* **Student ID Requirement:**  It explicitly states that using the student ID (with an example format) is mandatory for submission; otherwise, the score will not be counted.
* **Assignment Link:** It provides a link to access Graded Assignment 3: `https://exam.sanand.workers.dev/tds-2025-01-ga3`


In summary, the image displays a student's view of an online course platform, where the focus is on a past due assignment (Assignment 3) with instructions and troubleshooting tips, alongside a list of course modules including another assignment (Assignment 4).  The highlighted "Graded Assignment 4" suggests the user may be looking for information about this assignment as well.

---

## Post #378 by 23f3001208 (Post ID: 593943)
Your most recent score will be considered, as long as you saved it before the deadline

---

## Post #379 by s.anand (Post ID: 594679)
Here are the Discourse IDs that replied to this post. 
@carlton
 could you please add 1 mark to them in the GA (not the overall score)?




Please include only those are enrolled this term, obviously.


If they didn’t attempt GA4, please include them anyway and give them 1/10.


If they got 10/10 already, please add 1 mark anyway and give them 11/10.




21F1005510
21f2000296
21f2000588
21f2000709
21f2001369
21f3000745
21f3001379
21f3001797
21f3001993
21f3002277
22ds2000011
22ds3000157
22f1000120
22f1000535
22f2000008
22f2000113
22f2001590
22f2001640
22f3000079
22f3000519
22f3000586
22f3000639
22f3000657
22f3000804
22f3000910
22f3001011
22f3001315
22f3001754
22f3001840
22f3002034
22f3002175
22f3002184
22f3002723
22f3002771
23ds3000040
23ds3000149
23ds3000241
23f1000299
23f1000422
23f1000625
23f1001126
23f1001174
23f1001231
23f1001301
23f1001839
23f1002534
23f1002571
23f1003139
23f2000098
23f2000237
23f2000573
23f2000926
23f2001177
23f2001286
23f2001305
23f2001413
23f2001738
23f2002291
23f2003268
23f2003717
23f2003751
23f2003853
23f2004042
23f2004636
23f2004644
23f2004752
23f2004907
23f2004941
23f2005138
23f2005275
23f2005419
23f3001208
23f3001601
23f3001752
23f3002537
23F300327
23f3003594
23f3003871
23f3004024
23f3004114
23f3004162
24ds1000082_Vivek
24ds2000024
24ds2000108
24ds3000032
24ds3000090
24f2000695
24f2003130
Abhay222
ABHIJITH_VS
adeepu.here
Adityism
akashkunwar
anu2023
AnvithaV
AryanTikam
Atif01
carlton
daksh76
Deepanshutomar
GIRISH_VISHVESHVAR_B
gouthamnischay
H1Dd3n_xx
Haricharan
HARISH.S
iamsarthak
jashmevada
Jayeshbansal
Jeleshiya
JoelJeffrey
koustubhr
lakshaygarg654
Lokkiii
Megha
mohiit
Namannn28
namanshyamsukha
nayonika
Neelakandan
Nelson
nilaychugh
parthpatel
rabbaniIITB
Rehbar
Rohitb
rohitgarg
roy2003
Rrishit
Sagan
sandeepstele
Saransh_Saini
sarvan108
sha_512_av
ShahbaazSingh
sharma_abhay
ShivaniAdhiyaman
shivanshgupta0007
Siddhu3050
Suhani
swatikap
tanmaysahu295
tarundude02
Udipth
vaishnavi.k
Vedant22
vidushi
vidya19
yasharabhavi

---

## Post #381 by nayonika (Post ID: 596704)
Hello sir, my name is mentioned here however I did not get the bonus mark.


Warm regards,

Nayonika Arora

24ds1000090

---

## Post #382 by rohitgarg (Post ID: 596713)
ig, they have not updated.


not reflected on my portal too

---

## Post #383 by 22f2000008 (Post ID: 596723)
image
1880×873 141 KB

As you can see in this screen shot i already tried this question and getting error so i posted it on discourse. But still i did not get any marks for attempting this question.

i got only 9/10.

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/4/d4d9c422431c2ca2a06ac2ac397ddf40ca620253_2_690x320.png)

**Image Description:** This image shows a screenshot of a discussion thread, likely from an online learning platform.  The thread's title is "GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]", indicating a course about data sourcing, part of a program called "TDS", in January 2025.

The main focus is a student's (user 'A', ID 22f2000008) question about a coding error. They're experiencing a `NameError` while trying to get weather data for Nur-Sultan using a BBC Weather API. The error message specifically states "Could not find location ID for Nur-Sultan" and points to a line of code (line 35) where a variable `location_id` is undefined.  The code snippet uses an f-string to construct a URL for the BBC Weather API; however, the `location_id` is missing. This is the core problem described in the user's post.

The screenshot also shows a sidebar with course navigation (Topics, My Posts, Docs, etc.), categories (Courses, Operational Issues, etc.), and tags, including "clarification." The page numbers indicate that this is post number 168 of 360. Dates and times of posts are shown in the right margin.  The overall theme is a technical issue during a data science course assignment, asking for help in resolving a coding error related to API usage.

---

## Post #384 by 21f2000588 (Post ID: 596735)
Hello 
@s.anand
 
@carlton
 Sir,

As can be seen, my roll number is present in this list (21f2000588) and in GA4 I have got 10/10 but unfortunately, that bonus mark hasn’t been added (as can be seen from the score displayed on the dashboard). So I request you to add that bonus mark to the total kindly.


Hoping for a positive response.

Thanks & Regards

Digvijaysinh Chudasama

21f2000588

---

## Post #385 by Jivraj (Post ID: 596759)
@22f2000008
 Your roll number is in the list shared by professor Anand.

---

## Post #386 by Jivraj (Post ID: 596760)


---

## Post #387 by 22f2000008 (Post ID: 596779)
image
1900×860 118 KB

I am not saying anything regarding bonus marks. I am asking GA4 q4  about

Nur-Sultan in this question everyone getting error after post in discourse ,sir say who attempt this question get a marks .But i am not recieved this question marks

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/e/5ebde997ebbaa1a9814e6e79b23821f118c198c2_2_690x312.png)

**Image Description:** This image shows a discussion thread from a course called "GA4 - Data Sourcing".  The thread is part of a larger online learning platform or forum.  Key details include:

* **Course Information:** The top header clearly indicates that this is a discussion thread for the course "GA4 - Data Sourcing", specifically for "TDS Jan 2025", term 1, a graded assignment during week 4.

* **Participants:**  Several users are involved in the discussion:  `rohitgarg`, `carlton` (identified as a Course TA), `@2313002537`, `@2113000745`, and `@Jeleshiya`.  User profile pictures are visible for some participants.

* **Discussion Content:**  `rohitgarg` reports that grades haven't updated and aren't reflecting on their portal.  `carlton` then responds with clarification that anyone who received and attempted a question using the "Nur-Sultan parameter" will receive credit.

* **Platform Features:** The left sidebar shows typical forum features, including:
    * Categories (Courses, Operational Issues, Professionals Corner)
    * Tags (like "clarification")
    * Topics
    * User's own posts
    * Documents
    * A 'more' section suggesting additional features.

* **Timestamps:** Timestamps indicate the time of each post and reply.  The main post was 3 hours prior to the screenshot, a reply from `carlton` was also made 3 hours ago, with other interactions noted with timestamps.  `360/364` suggests a class size and progress tracker.

* **Post Identifiers:**  There's a potential ID, "22f2000008" visible, though its purpose is unclear without more context.

In summary, the image depicts a discussion resolving a grading issue in an online course forum, with the main point being clarification on grading criteria for a particular question's parameter.  The image shows the different features of the platform being used to clarify grading and course administration.

---

## Post #388 by iamsarthak (Post ID: 596812)
if a student has 10/10 and his name is in the bonus list, how would that look like in the dashboard?


I don’t think it is added in my case.

---

## Post #389 by carlton (Post ID: 596902)
It will show up as 110  marks. Bonus marks are for all discourse posts on this thread that Anand has identified as valid. I have provided operations team with the update corrected scores. You will start seeing them in the dashboard soon.


Also these are the list of students that have been affected by Nur-Sultan in their questions. These will get an automatic mark for that question if they attempted it. Note that this is not a bonus mark. This is a free mark.


23f3002537@ds.study.iitm.ac.in

23f3003875@ds.study.iitm.ac.in

21f3002112@ds.study.iitm.ac.in

23f2003437@ds.study.iitm.ac.in

22f3002236@ds.study.iitm.ac.in

22f3001705@ds.study.iitm.ac.in

22f2000008@ds.study.iitm.ac.in

21f1001892@ds.study.iitm.ac.in

23f1002075@ds.study.iitm.ac.in

23f1001126@ds.study.iitm.ac.in

22f3002661@ds.study.iitm.ac.in

22f2000506@ds.study.iitm.ac.in

24f1002149@ds.study.iitm.ac.in

23f2002473@ds.study.iitm.ac.in


Kind regards

---

## Post #390 by carlton (Post ID: 596904)
Please refer to this reply.








GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]
 
Tools in Data Science





    It will show up as 110  marks. Bonus marks are for all discourse posts on this thread that Anand has identified as valid. I have provided operations team with the update corrected scores. You will start seeing them in the dashboard soon. 
Also these are the list of students that have been affected by Nur-Sultan in their questions. These will get an automatic mark for that question if they attempted it. Note that this is not a bonus mark. This is a free mark. 
23f3002537@ds.study.iitm.ac.in 
23f3…
  




Kind regards

---

## Post #391 by 23f1002382 (Post ID: 596924)
For those who didn’t submit but still need to practice the questions like to check if the answer is right, or cross-check the solutions for GA 4 and GA 5, is there a special link where the portal just checks the answer and says right or wrong. I wasn’t able to do GA4 or even try to attempt GA 5 before deadline, but i would like to go through the process of submitting etc. is there any link or solutions for GA 4 and GA5.

---

## Post #392 by 23f1002382 (Post ID: 598870)
is there anyway to practice the assignments and check answers even though the deadline for the assignment passes? or is the answer given somewhere just for learning sake. I  understand that each set of students get different questions. 
@Jivraj
 
@carlton
 
@s.anand

---
