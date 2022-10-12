<h1 align="center"> Deploy ML models with FastAPI, Docker, and Heroku </h1>

# Table of Contents

- [Introduction](#Introduction)
- [Requirements](#)
- [Create Git repo](#)
- [Create Heroku project](#)
- [Services](#Services)

#Introduction

For this project I wanted to integrate the [Flask](https://flask.palletsprojects.com/en/2.2.x/) framework with Sqlite to develop Api Rest in which you could store the data and make searches.
On the other hand, I have considered Sqlite for testing since it is a less powerful database engine than others such as mysql or PostgreSql, it is sufficient for testing.

# Requirements
    scikit-learn==1.0.2

# Create Git repo
    git init
    git add .
    git commit -m "initial commit"
    git branch -M main

# Create Heroku project

    heroku login
    heroku create your-app-name
    heroku git:remote your-app-name
    heroku stack:set container
    git push heroku main

# Services

    curl -X 'POST' \
      'https://language-detection-123.herokuapp.com/predict' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "language": "English"
    }'

- Example


        curl --location --request POST 'https://language-detection-123.herokuapp.com/predict' \
        --header 'Content-Type: application/json' \
        --data-raw '{
          "text": "olá, o meu nome é miguel"
        }'

        Output: 
        {
            "language": "Portugeese"
        }

