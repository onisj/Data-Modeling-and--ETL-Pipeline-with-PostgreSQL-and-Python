# DROP TABLES

# Drop the songplays table if it exists
songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
# Drop the users table if it exists
user_table_drop = "DROP TABLE IF EXISTS users;"
# Drop the songs table if it exists
song_table_drop = "DROP TABLE IF EXISTS songs;"
# Drop the artists table if it exists
artist_table_drop = "DROP TABLE IF EXISTS artists;"
# Drop the time table if it exists
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

# Create the songplays table with appropriate data types
songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id SERIAL PRIMARY KEY,
    start_time timestamp NOT NULL,
    user_id int NOT NULL,
    level varchar,
    song_id varchar,
    artist_id varchar,
    session_id int NOT NULL,
    location varchar,
    user_agent varchar
);
""")

# Create the users table with appropriate data types
user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
    user_id int PRIMARY KEY,
    first_name varchar,
    last_name varchar,
    gender varchar,
    level varchar
);
""")

# Create the songs table with appropriate data types
song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
    song_id varchar PRIMARY KEY, 
    title varchar, 
    artist_id varchar NOT NULL, 
    year int,
    duration numeric
);
""")

# Create the artists table with appropriate data types
artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
    artist_id varchar PRIMARY KEY,
    name varchar,
    location varchar,
    longitude numeric,
    latitude numeric
);
""")

# Create the time table with appropriate data types
time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
    start_time timestamp PRIMARY KEY,
    hour int,
    day int,
    week int,
    month int,
    year int,
    weekday varchar
);
""")

# INSERT RECORDS

# Insert a record into the songplays table
songplay_table_insert = ("""
INSERT INTO songplays (
    start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")

# Insert a record into the users table or update level if user_id already exists
user_table_insert = ("""
INSERT INTO users (
    user_id, first_name, last_name, gender, level
)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id)
DO UPDATE SET level = EXCLUDED.level;
""")

# Insert a record into the songs table if the song_id does not exist
song_table_insert = ("""
INSERT INTO songs (
    song_id, title, artist_id, year, duration
)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (song_id) DO NOTHING;
""")

# Insert a record into the artists table if the artist_id does not exist
artist_table_insert = ("""
INSERT INTO artists (
    artist_id, name, location, latitude, longitude
)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) DO NOTHING;
""")

# Insert a record into the time table if the start_time does not exist
time_table_insert = ("""
INSERT INTO time (
    start_time, hour, day, week, month, year, weekday
)
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS

# Retrieve a song_id and artist_id given a song title, artist name, and song duration
song_select = ("""
SELECT song_id, songs.artist_id
FROM songs JOIN artists ON songs.artist_id=artists.artist_id
WHERE title=%s AND name=%s AND duration=%s;
""")

# QUERY LISTS

# List of create table queries
create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
# List of drop table queries
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
