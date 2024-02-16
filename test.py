# REMEMBER: Restart this notebook to close connection to `sparkifydb`
# Each time you run the cells above, remember to restart this notebook to close the connection to your database. Otherwise, 
#you won't be able to run your code in `create_tables.py`, `etl.py`, or `etl.ipynb` files since you can't make multiple 
# connections to the same database (in this case, sparkifydb).


%load_ext sql

%sql postgresql://student:student@127.0.0.1/sparkifydb

%sql SELECT * FROM songplays LIMIT 5;

%sql SELECT * FROM users LIMIT 5;

%sql SELECT * FROM songs LIMIT 5;

%sql SELECT * FROM artists LIMIT 5;

%sql SELECT * FROM time LIMIT 5;