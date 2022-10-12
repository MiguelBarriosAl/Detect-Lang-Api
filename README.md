<h1 align="center"> # Deploy ML models with FastAPI, Docker, and Heroku </h1>

# Table of Contents
- [Introduction](#Introduction)
- [Requirements](#Requirements)
- [Create Git repo](#Create Git repo)
- [Installation](#Installation)
- [Run](#Run)
- [Services](#Services)

# Introduction
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