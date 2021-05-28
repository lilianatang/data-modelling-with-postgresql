# INTRODUCTION
### Purpose of the project:
This project is to create a database schema in Postgres & ETL pipeline to optimize queries on song play analysis. 
### What is Sparkify?
Sparkify is a startup that just launched a music streaming application. The application has collected song and user activities in JSON format. The anylytics team wants to understand what songs users are listening to more easily than looping through all the JSON files. 
### How this project is going to help Sparkify
This project will help the analytics team at Sparkify to run queries to understand their end users more.
# DATABASE SCHEMA DESIGN & ETL PROCESS
### Database Schema Design
##### **Fact Table**
songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)** - records in log data associated with song plays i.e. records with page NextSong
##### **Dimension Tables**
1. users (user_id, first_name, last_name, gender, level) - users in the app
2. songs (song_id, title, artist_id, year, duration) - songs in music database
3. artists (artist_id, name, location, latitude, longitude) - artists in music database
4. time (start_time, hour, day, week, month, year, weekday) - timestamps of records in **songplays** broken down into specific units
### ETL Process
1. Perform ETL on song_data files to create the songs and artists dimensional tables
2. Perform ETL on log_data files to create the time and user dimensional tables as well as the songplays fact table
# FILES IN REPOSITORY
* etl.py reads and process files from song_data and log_data and loads them into tables.
* create_tables.py drops and creates tables/ 
* sql_queries.py contains all the necessary SQL queries, and is imported into etl.py and create_tables.py
* README.md provides discussion on the project
# HOW TO RUN THE PYTHON SCRIPTS
* Run python create_tables.py to create the database, fact and dimension tables along with insert statements to populate data through etl.py file later
* Run python etl.py to process data from JSON files and populate corresponding data to tables in the database
