# Topic: Graded assignment 6
**Topic ID**: 169283
**Total Posts**: 44

---

## Post #1 by Jivraj (Post ID: 603963)
Please post any questions related to 
Graded Assignment 6 - Data Analysis


Please use markdown code formatting (fenced code blocks) when sharing code (rather than screenshots). It’s easier for us to copy-paste and test.


Deadline 
2025-03-15T18:30:00Z

---

## Post #2 by Jivraj (Post ID: 603964)


---

## Post #3 by 24f2006061 (Post ID: 603966)
The answer choices for questions 1 and 2 in graded assignment 6 are quite confusing. Both questions are single-select, yet three out of the four options are correct in each case. I’m unsure whether to choose one of the correct options or if the question is actually asking for the incorrect one. Could someone please clarify?


@carlton

---

## Post #4 by 23f2005138 (Post ID: 602355)
@Jivraj
 
@Saransh_Saini

I have similar concern

For Q1, I used the following code:


print(f'Pearson correlation for Karnataka between price retention and column')
kk = df[df['State'] == 'Karnataka']
for col in ['Mileage (km/l)', 'Avg Daily Distance (km)', 'Engine Capacity (cc)']:
    pearson_corr = kk['price_retention'].corr(kk[col])
    print(f'\t{col:25} : {pearson_corr:.2f}')



And got the following output:


Pearson correlation for Karnataka between price retention and column
	Mileage (km/l)            : 0.03
	Avg Daily Distance (km)   : -0.06
	Engine Capacity (cc)      : -0.04



Whereas options are below where none of them are correct.


image
281×219 9.1 KB


Whereas for Q2 (Punjab and Yamaha) I used the following code:


print(f'Pearson correlation for Punjab and Yamaha between price retention and column')
pb = df[(df['State'] == 'Punjab') & (df['Brand'] == 'Yamaha')]
for col in ['Mileage (km/l)', 'Avg Daily Distance (km)', 'Engine Capacity (cc)']:
    pearson_corr = pb['price_retention'].corr(pb[col])
    print(f'\t{col:25} : {pearson_corr:.2f}')



and got the following answers:


Pearson correlation for Punjab and Yamaha between price retention and column
	Mileage (km/l)            : 0.24
	Avg Daily Distance (km)   : -0.06
	Engine Capacity (cc)      : -0.08



The options for Q2 are given below and 2 of them are correct (AvgDistance and Mileage).


image
278×216 9.19 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/6/a6fa9a2e601c94da84cbd25c406235d1009b204c.png)

**Image Description:** That's a screenshot showing a multiple-choice question or selection list.  Each option is presented as a radio button (a small circle) with a text label.  The options relate to numerical values associated with:

* **Mileage:** Two options provide mileage values: 0.95 and 0.21.
* **Average Distance (AvgDistance):** One option shows an average distance of -0.05.  The negative value is noteworthy.
* **Engine Capacity:** One option gives an engine capacity of 0.17.

The blue filled-in circle next to "AvgDistance: -0.05" indicates that this option has been selected as the answer.  The image likely comes from a quiz, test, or data entry form where the user is required to choose the correct or relevant option.  The context of what these values represent (e.g., units, context of the data) is missing from the image.

![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/1/51b03d00c3e962e6c4fc7fc64930a23e82500006.png)

**Image Description:** The image contains a list of four radio button options, each presenting a key-value pair.  The key-value pairs appear to represent features and associated numerical values, possibly from some sort of data analysis or input form.

* **'Mileage: 0.95'**:  A radio button (unchecked) showing a mileage value of 0.95.

* **'AvgDistance: -0.06'**: An unchecked radio button showing an average distance value of -0.06.  The negative value is notable and could indicate a decrease or a negative correlation.

* **'Mileage: 0.24'**: A radio button (selected/checked - indicated by a filled circle) showing a mileage value of 0.24.

* **'EngineCapacity: -0.08'**: An unchecked radio button displaying an engine capacity value of -0.08. Again, the negative value is noteworthy.

The presence of multiple 'Mileage' entries with different values suggests a selection process is involved. The negative values associated with 'AvgDistance' and 'EngineCapacity'  indicate potential decreases or negative correlations relative to some baseline or reference point not shown in the image.  Without more context, it's impossible to say exactly what these values represent or what the selection implies.

---

## Post #5 by carlton (Post ID: 603367)
@24f2006061
 We are looking into it. We will update based on our analysis. Thanks for letting us know.


Kind regards

---

## Post #6 by AbhinavOhri (Post ID: 603970)
I used a python script to get the solution to quesiton 1 of week 6 graded assignment. It matches three options. Is this a bug or like we then need to analyze using the pearson coefficient to determine which option is the correct one


image
1383×263 25 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/d/bd0ea5ffab782a7d6bcc8b1cde7ba7f385b85630_2_690x131.png)

**Image Description:** This image shows a multiple-choice question related to the analysis of factors influencing motorcycle resale value. 


Here's a breakdown of the content:

* **Question Stem:** The main question asks to analyze the impact of mileage, average daily distance traveled, and engine capacity on the price retention of Yamaha motorcycles in Delhi.  The method specified is using the Pearson Correlation Coefficient, and price retention is calculated as (resale price / original price).

* **Multiple Choice Options:** Four options are provided, each presenting a Pearson correlation coefficient for a variable:
    * 'Mileage: 0.01'
    * 'AvgDistance: 0.00'
    * 'EngineCapacity: 0.13' (This option is selected/marked as correct)
    * 'EngineCapacity: 0.95'

* **Point Value:** The question is worth 1 point.

The image essentially presents the results of a correlation analysis.  The selected answer suggests that engine capacity has a correlation coefficient of 0.13 with price retention for Yamaha motorcycles in Delhi according to this analysis.  The other factors (mileage and average distance) show very weak or no correlation.

---

## Post #7 by 24ds3000090 (Post ID: 604313)
Dear Sirs, Can we have some response on these issues related particularly to the questions 1 and 2 of Graded Assignment 6. It looks like multiple options are correct in the given options. Any guidance or hint, on how to arrive at the right answer will be helpful. Thanks and regards. 
@carlton
 
@Jivraj
 
@Saransh_Saini

---

## Post #8 by 23f2003413 (Post ID: 604590)
Yeah…Even I am facing the same issue. Out of the 4 options provided, 3 options are correct in my case both for Q1 & Q2, but both these questions are single-choice questions. Kindly look into it and help us out 
@carlton
 !

---

## Post #9 by 23ds2000092 (Post ID: 605292)
I guess for both Q1 & Q2, we need to find the option that is having stronger correlation (positive/negative). Please correct me if I am wrong.

---

## Post #10 by 21f2000709 (Post ID: 605551)
Any updates on these? I am too facing the same issue.


@carlton
 
@Jivraj
 
@Saransh_Saini

---

## Post #11 by Udipth (Post ID: 605753)
In GA6 for first 2 questions 3 out of 4 options are correct. Even the question is not clearly asking anything. Kindly suggest are we supposed to select the wrong one


image
2083×575 47.6 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/c/fccc54e8cff0595d93b1c5185ce0a10343849b04_2_690x190.png)

**Image Description:** The image contains a multiple-choice question worth one point.  The question asks the user to analyze the impact of various factors on the resale value of Yamaha motorcycles in Maharashtra, India.  The user must determine which of the provided Pearson Correlation Coefficients best reflects the relationship between the factor and price retention (resale price/original price).

The question specifies that the factors to consider are mileage (km/l), average daily distance traveled, and engine capacity.

The multiple-choice options are presented as:

* 'AvgDistance: 0.09'
* 'Mileage: 0.95'
* 'EngineCapacity: -0.02'
* 'Mileage: 0.12'

The correct answer is 'Mileage: 0.95' because it shows the strongest positive correlation between mileage and price retention.  A correlation coefficient near 1 indicates a strong positive relationship, meaning higher mileage is associated with higher price retention. The other options show weaker or negative correlations.

---

## Post #12 by 23f2003413 (Post ID: 605798)
Kindly update us regarding the status of Q1 & Q2 
@carlton
 
@Jivraj

---

## Post #13 by lakshaygarg654 (Post ID: 605954)
@Jivraj
 
@carlton
 
@Saransh_Saini

Dear TDS Team,


There are multiple issues in Graded Assignment 6 that require urgent attention:




Questions 1 and 2, along with their options, are ambiguous.


In Questions 3 and 4, I am unable to obtain an exact answer that matches any of the given options, despite trying multiple approaches, including the Excel regression method and other models in a Google Colab file.


The data for Question 10 is missing. I attempted to run the shapefile in QGIS, but it resulted in an error. Additionally, I searched for the shapefile of New York roads on official websites, but their servers are currently under maintenance.




The assignment deadline is approaching, but these issues remain unresolved. Kindly look into this matter at the earliest and provide a resolution as soon as possible.


Thank you for your support.

---

## Post #14 by 21f2000709 (Post ID: 605995)
Yes, there are no specifics in Q1 to Q4 and are quite ambiguous.


For instance:




forecast the 2027 resale value of the Hero - HF Deluxe in Gujarat, using historical data.




but is this talking about the average resale value as no input features are specified?

---

## Post #15 by lakshaygarg654 (Post ID: 606007)
Let’s wait for their response.

I submitted nearby option for Q3 and Q4

---

## Post #16 by 23f3001745 (Post ID: 606017)
@Jivraj
 
@carlton
 
@Saransh_Saini

Can you please provide any update ASAP as the deadline for this GA coincides with Quiz 2. With many ambiguities unresolved it’s hard to solve this and study for Quiz 2 (and do offline college work even though that’s not your problem).

Thanks

---

## Post #17 by Jivraj (Post ID: 606228)
Hi 
@all


Question intends you to select most correlated one.

Select option which is absolute highest.

---

## Post #18 by Sunil_mv (Post ID: 606558)
@Jivraj
  - Can you please check answer choices for Q7 for GA6 where no choices are matching with the answer. The answer is coming to around 11.5 kms which is 11500 meters.

Q.A wildfire is threatening a rural mountain region, and emergency services need to coordinate evacuation routes for four remote communities. The Emergency Management Center is located at a central command post, and must plan the most efficient evacuation route to ensure rapid and safe community evacuation. The four communities are: Pine Pines Junction : (26.5596,-99.5336) ;Maple Fields Station : (26.4212,-99.4597);South Glen Crossing : (26.5962,-99.5243);Cedar Creek Retreat : (26.56,-99.4519) & Central Command Post Location: (26.4644,-99.4771) Using the Haversine package, calculate the distance from the Central Command Post to Pine Pines Junction. Which of the following is the MOST ACCURATE distance

---

## Post #19 by 23f3001601 (Post ID: 606603)
image
1318×377 34.2 KB

what to do if 3 options have same value -0.04 and all are correct?

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/6/9656b143021a1b4baf78510b1ba05ae9cbd6ca9b_2_690x197.png)

**Image Description:** This image presents a multiple choice question within the context of a strategic consulting assignment.  The question asks to analyze factors influencing motorcycle resale value in Maharashtra, specifically for Honda motorcycles. The goal is to determine the impact of mileage, average daily distance traveled, and engine capacity on price retention using the Pearson Correlation Coefficient.  Price retention is defined as (resale price / original price).

The multiple choice options provide Pearson correlation coefficients for each factor:

* **AvgDistance: -0.04**
* **AvgDistance: 0.95**
* **EngineCapacity: -0.04**
* **Mileage: -0.04**

One of these options is selected as the correct answer (indicated by a filled-in radio button).  The selected answer is **Mileage: -0.04**.  The question is worth 1 point.

---

## Post #20 by 23f2005471 (Post ID: 606761)
@carlton
 
@Jivraj

My question 7 for GA6 is :

A wildfire is threatening a rural mountain region, and emergency services need to coordinate evacuation routes for four remote communities. The Emergency Management Center is located at a central command post, and must plan the most efficient evacuation route to ensure rapid and safe community evacuation. The four communities are: Silver Springs Community : (42.1029,-85.665) ;Pleasant Harbor Community : (42.1238,-85.9043);Summit Shores Village : (42.0415,-85.8696);River Retreat Outpost : (42.0417,-85.6836) & Central Command Post Location: (42.0587,-85.7226) Using the Haversine package, calculate the distance from the Central Command Post to Silver Springs Community. Which of the following is the MOST ACCURATE distance

Whose options provided are :

10418 meters


12287 meters


10965 meters


11149 meters


However, after trying all methods out there my distance comes out to be 6873 meters, I selected 10418 as the answer (closest approximation to 6873 meters)


I assume that the question must have been central command post to summit shores village (whose answer turns out to be 12287 meters)

Kindly look into the question, and let me know about the same (the destination from central command post)

---

## Post #21 by 21f2000709 (Post ID: 606802)
Have you succeeded in running the shape file for Q10? It seems to have some error.


@lakshaygarg654

---

## Post #22 by lakshaygarg654 (Post ID: 606808)
No,

I use google to get MTFCC code for given road segment and  after that mtfcc pdf to classify that road segment.

---

## Post #23 by 21f2000709 (Post ID: 606825)
I  downloaded the complete shape file zip from the 
census.gov
 site.

Here is the link: 
https://www2.census.gov/geo/tiger/TIGER2024/PRISECROADS/tl_2024_36_prisecroads.zip


It works fine in QGIS.


@lakshaygarg654

---

## Post #24 by 22f3001315 (Post ID: 606854)
they have not provide all the files needed to read that shp file in the question .

but your link includes them. thanks…

---

## Post #25 by lakshaygarg654 (Post ID: 606897)
I tried to access shapefile from official website 4-5 days ago, but server was under maintenance. I will check again Q10 after quiz 2.

Thanks for sharing.

---

## Post #26 by Rishabh2 (Post ID: 607050)
My question 9 for GA6 is :


@carlton
 
@Jivraj
 
@Saransh_Saini


Screenshot 2025-03-15 205444
878×668 38.1 KB


Screenshot 2025-03-15 205456
1333×366 45.8 KB


I solved it in colab but options are getting mismatched there…kindly clarify this issue..

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/e/9e4fdb96e0a90caace70968fd4201106dc133169.png)

**Image Description:** The image shows a Python code snippet focused on calculating and displaying the optimal evacuation sequence for several communities based on their distances to a central command post.

**Code Breakdown:**

1. **Import Statement:**  `from haversine import haversine` imports the `haversine` function, likely used for calculating distances between geographical coordinates using the haversine formula.

2. **Coordinate Definition:** The code defines the geographical coordinates (latitude and longitude) for four communities (`OakParkTown`, `EastSpringsSettlement`, `EastFieldsJunction`, `RedPointTown`) and a `CentralCommandPostLocation`.

3. **Distance Calculation:** A dictionary `distances` is created to store the distances between each community and the central command post.  The `haversine` function is used to compute these distances.

4. **Sorting:** The `optimal_sequence` variable is assigned the result of sorting the `distances` dictionary by values (distances) using `sorted(distances, key=distances.get)`. This sorts the communities from closest to farthest from the central command post.

5. **Output:** A `for` loop iterates through the `optimal_sequence`, printing the rank, community name, and its distance from the central command post, formatted to two decimal places.

**Output:**

The code's output is displayed below the code itself. It lists the communities in order of increasing distance from the central command post:

1. EastFieldsJunction - Distance: 7.84 km
2. EastSpringsSettlement - Distance: 9.74 km
3. RedPointTown - Distance: 9.81 km
4. OakParkTown - Distance: 11.76 km


**Key Features:**

* **Haversine Function:** The use of `haversine` suggests that the coordinates are geographic (latitude and longitude).
* **Optimal Evacuation:** The code's purpose is to determine the most efficient evacuation route, starting with the closest community.
* **Clear Comments:** The code is well-commented, making it easy to understand its logic.


The image provides a complete, runnable example of how to use the `haversine` library to solve a real-world problem involving optimized evacuation routing.

![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/0/0004348c8331f2b18dd055c7397be51c8c692902_2_690x189.png)

**Image Description:** Here's a description of the image content:

The image shows a multiple-choice question related to an optimization problem in evacuation strategy.  The question is worth 1 point.  It provides the coordinates of four communities (Oak Park Town, East Springs Settlement, East Fields Junction, and Red Point Town) and a Central Command Post.  The task is to determine the optimal evacuation sequence using a "nearest community first" strategy, where the shortest distance between locations dictates the order.

The question text clearly states the coordinates of each location.  Four options are presented, each showing a possible sequence for evacuating the communities, starting and ending at a 'Start/End' point.  One option is correctly marked as selected.

A small portion of what appears to be Python code is visible at the bottom right corner. This code snippet seems to be related to calculating distances using the `haversine` library, likely a relevant step in solving the problem.  The visible lines suggest the code defines coordinates for at least one of the communities.

---

## Post #28 by Sunil_mv (Post ID: 607057)
for the above question the options are None of these are matching and answer is around 11.5 kms

3848 meters

6265 meters

4110 meters

5106 meters

---

## Post #29 by 24ds3000028 (Post ID: 607119)
For 7th Question in GA6 I got the answer 14265.93 Meters but the option I have in 7th are

6069 meters

7687 meters

6106 meters

7035 meters


@carlton
 
@Jivraj

---

## Post #30 by 23f2000573 (Post ID: 607151)
@carlton
 
@Jivraj
 
@Saransh_Saini


for question 4, i have tried 
=forecast
 and also 
=forecast.ets
, both of them are not working. There are two columns for years. One is year of manufacturing, another is year of registration. which one to take.


for question 7, none of the options match. I am selecting the 
MOST ACCURATE
 among the given options. Hope, it is correct

---

## Post #31 by 23f2003413 (Post ID: 607211)
Can anyone help me out on how to approach and solve the 10th question please!?

---

## Post #32 by lakshaygarg654 (Post ID: 607252)
Check the distances of other locations from the central location. One student found 
Question 7
 of the 
GA6 Option Set
 based on the distances of other points, which do not match the requirements of Question 7.

---

## Post #33 by vidushi (Post ID: 607272)
i have the same issue

---

## Post #34 by vidushi (Post ID: 607273)
yes i have the same issue

and i got the same answer and am give the same options


@carlton
 sir what to do?

---

## Post #35 by vidushi (Post ID: 607277)
@Jivraj
 
@Saransh_Saini

For 7th Question in GA6 I got the answer 14265.9275 Meters but the option I have in 7th are

6069 meters

7687 meters

6106 meters

7035 meters

---

## Post #36 by Muthupalaniappan (Post ID: 607316)
Hello Sir,


Can you please check if this is the right answer. As per email received from 
@carlton
 sir we should select the absolute maximum value.


image
978×393 23.3 KB


Example : If we get answers as -0.3 and 0.2 then -0.3 is the right answer as it’s absolut value is maximum.


For the first question the correlation matrix is as follows,


image
748×431 17.5 KB


So shouldn’t it be -0.13?

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/4/b468c32e53fddf462c583b8664f183dd7afe37aa_2_690x277.png)

**Image Description:** The image shows a multiple choice question and its answer within what appears to be an online assessment or quiz.  The question asks the user to analyze the impact of mileage, average daily distance traveled, and engine capacity on the price retention of Royal Enfield motorcycles in Uttar Pradesh, using Pearson Correlation Coefficients.  The user is given four options, each presenting a correlation coefficient for one of the factors:

* **Mileage: 0.01**
* **EngineCapacity: 0.95**
* **AvgDistance: -0.13**
* **EngineCapacity: 0.09**

The user initially selected an incorrect option, as indicated by the "No, the answer is incorrect" message and a score of 0. The correct answer, revealed at the bottom, is **EngineCapacity: 0.09**.  The question is worth 1 point.

![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/5/c524c9f7645716e0fac9d8850df15c4c20af05dc_2_690x397.png)

**Image Description:** The image displays a heatmap depicting a correlation matrix.  The matrix shows the correlation coefficients between four variables:

* **Mileage (km/l):**  Kilometers per liter, a measure of fuel efficiency.
* **Avg Daily Distance (km):** Average daily distance traveled in kilometers.
* **Engine Capacity (cc):** Engine capacity in cubic centimeters.
* **Price Retention (%):** Percentage of the original price retained over time.

Each cell in the heatmap represents the correlation between two variables. The color intensity represents the strength and direction of the correlation, with darker red indicating a strong positive correlation, darker blue indicating a strong negative correlation, and lighter colors indicating a weak correlation.  The numerical values within each cell provide the precise correlation coefficient.

For example, the dark red cell at the intersection of "Engine Capacity (cc)" and "Engine Capacity (cc)" shows a perfect positive correlation (1.00), which is expected. The dark red cell at the intersection of "Price Retention (%)" and "Price Retention (%)" similarly shows a perfect positive correlation of 1.00.  Conversely, the dark blue cell at the intersection of "Price Retention (%)" and "Avg Daily Distance (km)" shows a negative correlation of -0.13, suggesting that higher average daily distance is weakly associated with lower price retention.  Other correlations are weaker, shown by the lighter blue hues.  The color bar on the right provides a visual key for interpreting the correlation strength.

---

## Post #37 by carlton (Post ID: 607333)
Thanks for the colour picture.

If you read the aforementioned email…


Screenshot 2025-03-17 at 9.09.55 am
1760×632 65.4 KB


Kind regards (in colour 
)

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/0/f0a5df3069d591c0175e61d70123d9ffb4ec7e83_2_690x247.png)

**Image Description:** This image is a screenshot of an email. 


Here's a breakdown of the content:

* **Subject Line:** The subject line reads "[TDS Jan 25] GA 6 Clarification".  This suggests a clarification regarding a graded assignment (GA) 6, possibly related to a course called TDS, on January 25th.

* **Sender:** The email is from `donot_reply@study.iitm.ac.in`, indicating an automated or non-reply email address likely from an educational institution (possibly the Indian Institute of Technology Madras, judging by the address).

* **Recipient:** The email was sent to the group `25t1_se2002-announce`, suggesting a specific class or cohort.

* **Email Body:** The email clarifies the grading of questions 1 and 2 in GA 6.  The intended answer was the *Absolute Maximum Correlation Coefficient*. The email gives an example:  If the options are -0.3 and 0.2, the correct answer is -0.3 (the absolute value is higher).

* **Important Note:** A key statement in the email is highlighted and says: "Do not worry if the portal marks you as being incorrect. We will still push the right scores on the dashboard if you chose the correct option." This reassures students that a potential error in the online grading system will be corrected.

In short, the email serves to clarify the grading criteria for questions 1 and 2 of GA 6 and assures students that any discrepancies will be resolved.

---

## Post #38 by Sunil_mv (Post ID: 608219)
Thank you sir. i have got questions 1 and 2 both marked as 0.


image
962×459 29.1 KB


In my case Please note the above two questions are asked to calculate pearson correlation coefficient for KTM brand and for maharashtra and Karnataka states.

I have used excel to calculate the pearson correlation coefficient. Below the values I got for each question. Please verify.


|pearson correlation coefficient between impact of Mileage and Price retention for kTM brand for Karnataka||

-0.026685695


|pearson correlation coefficient between average distance travelled and Price retention for kTM for karnataka||

0.003953219


|pearson correlation coefficient between average Engine capacity and Price retention for kTM for karnataka||

-0.010839295


|pearson correlation coefficient between impact of Mileage and Price retention for kTM brand for maharashta||

0.029128825


|pearson correlation coefficient between average distance travelled and Price retention for kTM for Maharashtra||

0.013019585


|pearson correlation coefficient between average Engine capacity and Price retention for kTM for Maharashtra||

-0.056866212

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/7/97636ac2d59c3df1caf852a42d90de4642e8ce6f_2_690x329.png)

**Image Description:** The image shows a multiple-choice question with a score of 0 indicating an incorrect answer.  The question asks to analyze factors influencing motorcycle resale value in Maharashtra for KTM motorcycles using the Pearson Correlation Coefficient.  The factors to consider are mileage (km/l), average daily distance, and engine capacity. Price retention is calculated as (resale price / original price).

Four options are presented, each with a Pearson correlation coefficient:

* 'AvgDistance: 0.01'
* 'Mileage: 0.03'
* 'EngineCapacity: -0.06'
* 'Mileage: 0.95'

The user selected an incorrect answer, as indicated by "No, the answer is incorrect. Score: 0".  The correct answer, revealed below, is 'Mileage: 0.03'.

---

## Post #39 by Sunil_mv (Post ID: 608222)
@Jivraj
 
@carlton

Dear sirs,

I have question no 7 got marked as 0. Please check the question below and the haversine distance for the given post comes to around 11.5 kms which is not matccing with any of the options and I have selected the closest answer. please check and let me know.


image
935×529 40.1 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/f/ff2eccf6d2263eb106345ce8b07d037c0a417845_2_690x390.png)

**Image Description:** This image shows a multiple choice question related to calculating the distance between two points using the Haversine formula.  The question describes a wildfire emergency scenario where an emergency management center needs to determine the most efficient evacuation route for four communities.  The coordinates of the central command post and Pine Pines Junction are provided.  The student is asked to calculate the distance between these two locations using the Haversine package and select the most accurate distance from the given options: 3848 meters, 6265 meters, 4110 meters, and 5106 meters.

The student initially chose incorrectly. The correct answer, 5106 meters, is revealed at the bottom under "Accepted Answers."  The question is worth 1 point, and the student's current score is 0.

---

## Post #40 by 23f2005471 (Post ID: 608561)
@carlton
 
@Jivraj

I did raise the question 2 days before the GA6 Deadline and doing so again after being marked as incorrect


My question 7 was A wildfire is threatening a rural mountain region, and emergency services need to coordinate evacuation routes for four remote communities. The Emergency Management Center is located at a central command post, and must plan the most efficient evacuation route to ensure rapid and safe community evacuation. The four communities are: Silver Springs Community : (42.1029,-85.665) ;Pleasant Harbor Community : (42.1238,-85.9043);Summit Shores Village : (42.0415,-85.8696);River Retreat Outpost : (42.0417,-85.6836) & Central Command Post Location: (42.0587,-85.7226) Using the Haversine package, calculate the distance from the Central Command Post to Silver Springs Community. Which of the following is the MOST ACCURATE distance


10418 meters


12287 meters


10965 meters


11149 meters


Whose right answer turned out 6873, however the answer pushed is 12287 meters, which is nowhere near the closest options (it would’ve been correct if the destination was summit shores village which isn’t the case with this question)


Also, my question 4 was :

As an investment analyst monitoring motorcycle resale values, develop a forecasting model to predict future resale prices by brand and segment, considering seasonality and long-term trends. Specifically, forecast the 2027 resale value of the Kawasaki - Ninja 300 in Tamil Nadu, using historical data.


134483


94774


150666


199711


Whose correct option (through different methods and algorithms) was approximately closest to 94774 and again answer pushed is 150666 which again turns out to be incorrect


So is the case with questions 1 and 2 (where answers aren’t pushed according to absolute values, but as conveyed earlier, I believe this shall be resolved)


Kindly look into it


Thanks and Regards

---

## Post #41 by 23f1001231 (Post ID: 608883)
@carlton
 
@Jivraj
 
@Saransh_Saini

In Q4 , neither which regression model to use is given nor the what random state to use is given. I tried linear regression, random forest regression but it is giving   answer which vary each time I compute, also, the option values are quite close.


image
1227×446 24 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/d/7dbfae953c7d9e015dbc80328ef657b813ba912d_2_690x250.png)

**Image Description:** The image shows a multiple choice question and answer section from what appears to be an online assessment or quiz.

**The Question:**

The question asks the user, in the role of an investment analyst, to create a forecasting model to predict the 2027 resale value of a Hero - HF Deluxe motorcycle in Punjab, India.  The model should account for brand, segment, seasonality, and long-term trends, using historical data.

**The Multiple Choice Answers:**

Four numerical options are presented as potential answers to the resale value question:

* 194515
* 185108
* 142646
* 152609

One of these options is marked as the user's selected answer (it is filled in). The provided text does not state which option was chosen.

**The Feedback:**

Below the answer options, the text "No, the answer is incorrect." is displayed in red, indicating that the user's selected answer was wrong.  The score is shown as 0, confirming that no points were earned on this question.

---

## Post #43 by Jivraj (Post ID: 609762)
@all

we are looking into problems with question 4, 6 and 10.

---

## Post #44 by swatikap (Post ID: 618164)
Hi,


Have the corrections been done on GA6 marks?

---

## Post #45 by Jivraj (Post ID: 618197)
Yes, corrections have been done in Ga6 marks.

---

## Post #46 by swatikap (Post ID: 618321)
Just to confirm, were the answers shown on the portal correct because I’m getting the same score as shown in the portal.

---
