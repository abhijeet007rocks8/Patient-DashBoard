# Patient-DashBoard <a href="https://patient-dashboard.azurewebsites.net/" target="_blank">(Azure Deployment)</a>
### MLH HackAPAC-2021 Best Hack for your Community Winner <a href="https://devpost.com/software/patient-dashboard">DEVPOST</a>
An interactive dashboard using Python(Streamlit, numpy , pandas) to easily collect and show all the details of a aptient saved across various datasets in one place.<br>
This can help the patients and their caretakers to easily acces the data regarding patient ad take better care of them.<br>
<br>

## Inspiration
The inspiration for the project is that many people in the world cannot easily access medical facilities majorly due to large distance from the hospitals. This acts as a hinderance in their improvement and regular visiting of nurse is not a feasible solution.<br/>
To resolve this issue we can use IoT enabled monitoring implants which can log the patient vital changes in the remote database server of the hospital.

## What it does
This dashboard uses the various datasets containing data of various patients as per different categories, goes through them and generates a complete report of a specific patient and displays them in a organized way so that it can be easily understood by patient caretakers.

## How we built it
This project is completely built on Python programming language and some of its libraries like numpy, panda and streamlit.<br/>
The project takes a patient id as references and tallies it across all the datasets and gets the data matching to particular id and then organize the data across various categories and make it available on the finger tips of caretaker.

## Challenges we ran into
1- The data in the datasets in never 100% accurate, there are always some garbage values that throw of exceptions in the program, so had to remove those.<br/>
2- Could not test the data on large datasets due to system restrictions.<br/>
3- Had to work with a public predefined dataset and could not test on Real-time dataset, but it should work fine on re-rendering the dashboard. <br/>
4- Had to use downloaded datasets as using from server was causing work to slow down.<br/>

## Accomplishments that we're proud of
1- The dashboard successfully displays the details of the patient<br/>
(Patient details like name, address etc.)<br/>
(Patient Vital Observations)<br/>
(Patient allergies)<br/>
(Patient Conditions & Careplan)<br/>
(Patient implants(if any))<br/>
(Medical Records(if any))<br/>
2-The DashBoard also shows locations of various medical stores in the area on a map.

## What we learned
How to Tackle large bulky datasets and make meaning observation from it to solve real-world problems and using graphic tools to make other people understand the observations. Usage of various Python Libraries and functions.

## What's next for Patient-DashBoard
There are lot of improvement that can be made to this project to become a great solution.
Firstly, The Dataset needs to be constantly updated with data logs from Monitoring devices/implants so Hospitals can use databases like DataStix ,MySQL to store data from where it is much easier to insert and extract data.<br/>
Secondly, The DashBoard server needs to be deployed on a Cloud service as the real-world dataset would be quite huge far beyond device capacities and dashboard needs to constantly ping the DB for new data.<br/>
Thirdly, A feature should be added to alert the hospital as well as the caretakers(via dashboard notification) if there is a sudden spike in the vitals of the patient, so that immediate help can be given and medical services dipatched immediately without wasting a second. and many more!!!<br/>

## Some Patient id's for testing-:<br>
76982e06-f8b8-4509-9ca3-65a99c8650fe<br>
ad2e9916-4979-40fc-a8c0-68651a0cb5a6<br>
518f83f3-a717-4705-a181-06e205df480b<br>
(for more see the csv files)
<br><br>
# Some Scshots are shown below-

![](WebApp/SCREENSHOTS/Screenshot2.png)
<br><br>
![](WebApp/SCREENSHOTS/Screenshot1.png)
<br><br>
![](WebApp/SCREENSHOTS/Screenshot3.png)
<br><br>
![](WebApp/SCREENSHOTS/Screenshot4.png)
<br><br>
![](WebApp/SCREENSHOTS/Screenshot5.png)
<br><br>
![](WebApp/SCREENSHOTS/Screenshot6.png)
<br><br>
![](WebApp/SCREENSHOTS/Screenshot7.png)
