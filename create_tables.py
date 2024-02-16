import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """
    Connect to the default database and create a new database 'sparkifydb' with UTF8 encoding.
    Returns the cursor and connection to the new database.
    """
    # Connect to the default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # Create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # Close connection to the default database
    conn.close()    
    
    # Connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    """Drop all tables specified in the drop_table_queries list."""
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """Create all tables specified in the create_table_queries list."""
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """Main function to create the sparkifydb database, drop and create tables."""
    cur, conn = create_database()
    
    # Drop existing tables
    drop_tables(cur, conn)

    # Create new tables
    create_tables(cur, conn)

    # Close connection
    conn.close()


if __name__ == "__main__":
    main()
