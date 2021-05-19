## DATABASE INFORMATION
### **Fact Table**
**songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)** 
### **Dimension Tables**
1. **users (user_id, first_name, last_name, gender, level)** - users in the app
2. **songs (song_id, title, artist_id, year, duration)** - songs in music database
3. **artists (artist_id, name, location, latitude, longitude)** - artists in music database
4. **time (start_time, hour, day, week, month, year, weekday)** - timestamps of records in **songplays** broken down into specific units

## HOW TO RUN THIS REPOSITORY 
### **In a remote server**
1. Activate the virtual environment mypython by changing directory to **cd mypython/Scripts/** then run **activate**
2. Run python create_tables.py to create the database, fact and dimension tables along with insert statements to populate data through etl.py file later
3. Run python etl.py to process data from JSON files and populate corresponding data to tables in the database
### **Locally**
0. At the end of etl.py, make sure you change the filepath in the last two lines to where you store the repository. 
For example, if I run the project locally, I would change it 
from
**process_data(cur, conn, filepath='data/song_data', func=process_song_file)**
**process_data(cur, conn, filepath='data/log_data', func=process_log_file)**
to
**process_data(cur, conn, filepath= r"C:\Users\ltang\Desktop\Data Engineering Nanodegree\Projects\data-modelling-with-postgresql\data\song_data", func=process_song_file)**
**process_data(cur, conn, filepath= r"C:\Users\ltang\Desktop\Data Engineering Nanodegree\Projects\data-modelling-with-postgresql\data\log_data", func=process_log_file**
