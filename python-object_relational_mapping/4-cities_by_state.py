#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument, safe from SQL injections.
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

    # Execute SQL query to select states where name matches the argument safely, ordered by id
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    # Fetch and print the results
    for state in cur.fetchall():
        print(state)

    # Close cursor and database connection
    cur.close()
    db.close()
