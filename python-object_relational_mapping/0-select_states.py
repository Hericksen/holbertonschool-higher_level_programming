#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials from arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database, port=3306)

    # Create a cursor object
    cur = db.cursor()

    # Execute SQL query to select all states ordered by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and print the results
    for state in cur.fetchall():
        print(state)

    # Close cursor and database connection
    cur.close()
    db.close()
