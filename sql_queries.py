# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = (
    """
    CREATE TABLE IF NOT EXISTS songplays (
        songplay_id int GENERATED ALWAYS AS IDENTITY,
        session_id int NOT NULL,
        location varchar NOT NULL,
        user_agent varchar NOT NULL,
        start_time timestamp,
        user_id int,
        artist_id varchar,
        PRIMARY KEY(songplay_id),
        CONSTRAINT fk_time
            FOREIGN KEY (start_time)
                REFERENCES time (start_time)
                ON UPDATE CASCADE ON DELETE CASCADE,
        CONSTRAINT fk_user
            FOREIGN KEY (user_id)
                REFERENCES users (user_id)
                ON UPDATE CASCADE ON DELETE CASCADE,
        CONSTRAINT fk_artist
            FOREIGN KEY (artist_id)
                REFERENCES artists (artist_id)
                ON UPDATE CASCADE ON DELETE CASCADE
    );    
    """
)

user_table_create = (
    """
    CREATE TABLE IF NOT EXISTS users (
        user_id int GENERATED ALWAYS AS IDENTITY,
        first_name varchar NOT NULL,
        last_name varchar NOT NULL,
        gender varchar NOT NULL,
        level varchar NOT NULL,
        PRIMARY KEY(user_id)
    );    
    """
)

song_table_create = (
    """
    CREATE TABLE IF NOT EXISTS songs (
        song_id varchar,
        title varchar NOT NULL,
        year int NOT NULL,
        duration numeric NOT NULL,
        artist_id varchar,
        PRIMARY KEY(song_id),
        CONSTRAINT fk_artist
            FOREIGN KEY (artist_id)
                REFERENCES artists (artist_id)
                ON UPDATE CASCADE ON DELETE CASCADE
    );
    """
)

artist_table_create = (
    """
    CREATE TABLE IF NOT EXISTS artists (
        artist_id varchar,
        name varchar NOT NULL,
        location varchar,
        latitude numeric,
        longitude numeric,
        PRIMARY KEY(artist_id)
    );    
    """
)

time_table_create = (
    """
    CREATE TABLE IF NOT EXISTS time (
        start_time timestamp,
        hour int NOT NULL,
        day int NOT NULL,
        week int NOT NULL,
        month int NOT NULL,
        year int NOT NULL,
        weekday int NOT NULL,
        PRIMARY KEY(start_time)
    );    
    """
)

# INSERT RECORDS

songplay_table_insert = (
    """
    INSERT INTO songplays (songplay_id, session_id, location, user_agent, start_time, user_id, artist_id) VALUES (%s, %s, %s, %s, %s, %s, %s);
    """
)

user_table_insert = (
    """
    INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s);
    """
)

song_table_insert = (
    """
    INSERT INTO songs (song_id, title, year, duration, artist_id) VALUES (%s, %s, %s, %s, %s);
    """
)

artist_table_insert = (
    """
    INSERT INTO artists (artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s);
    """
)


time_table_insert = (
    """
    INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s);
    """
)

# FIND SONGS

song_select = (
    """
    SELECT song_id, artist_id FROM songs JOIN artists ON artists.artist_id = songs.artist_id WHERE title = %s AND name = %s AND duration = %s; 
    """)

# QUERY LISTS

create_table_queries = [ time_table_create, user_table_create, artist_table_create, song_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]