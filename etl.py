import os
import glob
import psycopg2
import pandas as pd
import json
import datetime
import numpy as np
from sql_queries import *


def get_files(filepath):
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))

    return all_files

def process_song_file(cur, filepath):
    # open song file
    df = pd.read_json(filepath, lines=True)
    # insert song record
    song_data = list(zip(df['song_id'], df['title'], df['year'], df['duration'], df['artist_id']))
    #cur.execute(song_table_insert, song_data)
    song_df = pd.DataFrame(song_data, columns=['song_id', 'title', 'year', 'duration', 'artist_id'])
    song_df.drop_duplicates(keep="first", inplace=True)
    for i, row in song_df.iterrows():
        cur.execute(song_table_insert, row)
    # insert artist record
    artist_data = list(zip(df['artist_id'], df['artist_name'], df['artist_location'], df['artist_latitude'], df['artist_longitude']))
    artist_df = pd.DataFrame(artist_data, columns=['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude'])
    artist_df.drop_duplicates(keep="first", inplace=True)
    for i, row in artist_df.iterrows():
        cur.execute(artist_table_insert, row)

def process_log_file(cur, filepath):
    # open log file
    df = pd.read_json(filepath, lines=True) #filepath format must be: r'..\file.jason'
    # filter by NextSong action
    df = df[df["page"] == "NextSong"]
    # convert timestamp column to datetime
    t = pd.to_datetime(df["ts"], unit='ms')
    # insert time data records
    time_data = list(zip(df["ts"], t.dt.hour, t.dt.day, t.dt.isocalendar().week, t.dt.month, t.dt.year, t.dt.weekday))
    column_labels = ['start_time', 'hour', 'day', 'week', 'month', 'year', 'weekday']
    time_df = pd.DataFrame(time_data, columns = column_labels)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_column_labels = ['user_id', 'first_name', 'last_name', 'gender', 'level']
    user_data = list(zip(df["userId"], df["firstName"], df["lastName"], df["gender"],  df["level"]))
    user_df = pd.DataFrame(user_data, columns = user_column_labels)
    # remove duplication
    user_df.drop_duplicates(keep="first", inplace=True)
    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)
    # insert songplay records
    #songplay_column_labels = ['songplay_id', 'session_id', 'location', 'user_agent', 'start_time', 'user_id', 'artist_id']
    for index, row in df.iterrows():
        # get songid and artistid from song and artist tables
        #print(song_select)
        #print((row.song, row.artist, row.length))
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        print(results)
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None
        print(results)
        print(songid, artistid)
        # insert songplay record
        songplay_data = row, row.sessionId, row.location, row.userAgent, row.ts, songid, artistid
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    #process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    #process_data(cur, conn, filepath='data/log_data', func=process_log_file)
    process_data(cur, conn, filepath= r"C:\Users\ltang\Desktop\Data Engineering Nanodegree\Projects\data-modelling-with-postgresql\data\song_data", func=process_song_file)
    process_data(cur, conn, filepath= r"C:\Users\ltang\Desktop\Data Engineering Nanodegree\Projects\data-modelling-with-postgresql\data\log_data", func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()