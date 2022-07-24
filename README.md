# Disaster Response Pipeline Project

**Installation:** These codes are written in Python and HTML and the codes require the following Python packages: sys, pandas, numpy, re, pickle, nltk, flask, json, plotly, sklearn, sqlalchemy etc.

**Project Overview:** The project goal is to build a Natural Language Processing(NLP) model to categorize or classify messages on a real time basis. This code is designed to initiate a web app which an emergency operators could leverage during a disaster (example-earthquake) to classify a disaster text message into several categories (out of 36 pre-defined categories) which then can be further transmitted to the appropriate disaster relief agency.

**Folder Structure:**
app
| - template
| |- master.html # main page of web app
| |- go.html # classification result page of web app
|- run.py # Flask file that runs app
data
|- disaster_categories.csv # data to process
|- disaster_messages.csv # data to process
|- process_data.py
|- InsertDatabaseName.db # database to save clean data to
models
|- train_classifier.py
README.md
ML Pipeline Preparation.ipynb
ETL Pipeline Preparation.ipynb

**File Description:**
App folder contains the template folder and "run.py" file for the web application
Data folder includes "DisasterResponse.db", "disaster_categories.csv", "disaster_messages.csv" and "process_data.py" for data cleaning and uploading in database.
Models folder contains "train_classifier.py" trains the ML model using the SQL dataset
README file captures project overview and instructions
ETL Pipeline Preparation.ipynb: process_data.py development process
ML Pipeline Preparation.ipynb: train_classifier.py. development process

**Instructions:**
Run the following commands in the project's root directory to set up the database and model.

To run ETL pipeline that cleans data and stores in database python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db
To run ML pipeline that trains classifier and saves python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl
Run the following command in the app's directory to run your web app. python run.py

Go to http://0.0.0.0:3001/ Or Go to http://localhost:3001/

**Snippet of the application:**
![Capture](https://user-images.githubusercontent.com/101924908/180632967-104216fe-203d-47c3-b68c-14f590d13bce.PNG)

