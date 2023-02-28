# Customer-Conversion-Prediction-Final-Project
As a Final Project I worked on Customer Conversion Predication 

The Problem Statement is a new-age insurance company and employ mutiple outreach plans to sell term insurance to your customers. Telephonic marketing campaigns still remain one of the most effective way to reach out to people however they incur a lot of cost. Hence, it is important to identify the customers that are most likely to convert beforehand so that they can be specifically targeted via call. We are given the historical marketing data of the insurance company and are required to build a ML model that will predict if a client will subscribe to the insurance. 

The historical sales data is available at train.csv

Features: 
age (numeric)
job : type of job
marital : marital status
educational_qual : education status
call_type : contact communication type
day: last contact day of the month (numeric)
mon: last contact month of year
dur: last contact duration, in seconds (numeric)
num_calls: number of contacts performed during this campaign and for this client 
prev_outcome: outcome of the previous marketing campaign (categorical: "unknown","other","failure","success")

Output variable (desired target):
y - has the client subscribed to the insurance?

In this project I followed the different steps of Machine Learning, Which are:

1. Data Cleaning: In which I check for Null values, duplicate data, spelling mistakes and Outliers
2. Then I done the Proper Exploratory Data Analysis
3. After That I done the Encoding based the categorical variable
4. Moving forward I split the data and then performed the Imbalanced Techniques(SMOTENN) to balance the data
5. Then I scaled the data and tried all classification machine learning models to train the data
6. Out of all the machine learning models XGBoost Classifier gives best AUROC.
7. Finally I done the Feature Importance to find the important factors that contribute towards the conversion rate.
