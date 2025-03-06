#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and state name from arguments
    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database, port=3306)

    # Create a cursor object
    cur = db.cursor()

    # Execute SQL query to select states where name matches the argument, ordered by id
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(state_name)
    cur.execute(query)

    # Fetch and print the results
    for state in cur.fetchall():
        print(state)

    # Close cursor and database connection
    cur.close()
    db.close()
