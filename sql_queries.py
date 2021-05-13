# DROP TABLES

songplay_table_drop = "DROP table songplay"
user_table_drop = "DROP table users"
song_table_drop = "DROP table songs"
artist_table_drop = "DROP table artists"
time_table_drop = "DROP table time"

# CREATE TABLES

songplay_table_create = (
    """
    CREATE TABLE songplay (
        songplay_id SERIAL PRIMARY KEY,
        session_id INTEGER NOT NULL,
        location VARCHAR(255) NOT NULL,
        user_agent VARCHAR(255) NOT NULL,
        FOREIGN KEY (start_time)
            REFERENCES time (start_time)
            ON UPDATE CASCADE ON DELETE CASCADE,
        FOREIGN KEY (user_id)
            REFERENCES users (user_id)
            ON UPDATE CASCADE ON DELETE CASCADE,
        FOREIGN KEY (artist_id)
            REFERENCES artists (artist_id)
            ON UPDATE CASCADE ON DELETE CASCADE
    )    
    """
)

user_table_create = (
    """
    CREATE TABLE users (
        user_id SERIAL PRIMARY KEY,
        first_name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255) NOT NULL,
        gender VARCHAR(1) NOT NULL,
        level VARCHAR(255) NOT NULL
    )    
    """
)

song_table_create = (
    """
    CREATE TABLE songs (
        song_id VARCHAR(255) PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        year INTEGER NOT NULL,
        duration NUMERIC NOT NULL,
        FOREIGN KEY (artist_id)
            REFERENCES time artists (artist_id)
            ON UPDATE CASCADE ON DELETE CASCADE
    )    
    """
)

artist_table_create = (
    """
    CREATE TABLE artists (
        artist_id VARCHAR(255) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        location VARCHAR(255),
        latitude NUMERIC,
        longitude NUMERIC
    )    
    """
)

time_table_create = (
    """
    CREATE TABLE time (
        start_time timestamp PRIMARY KEY,
        hour INTEGER NOT NULL,
        day INTEGER NOT NULL,
        week INTEGER NOT NULL,
        month INTEGER NOT NULL,
        year INTEGER NOT NULL,
        weekday INTEGER NOT NULL
    )    
    """
)

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]