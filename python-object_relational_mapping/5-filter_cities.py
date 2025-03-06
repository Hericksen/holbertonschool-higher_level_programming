#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa, safe from SQL injections.
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

    # Execute SQL query to select cities belonging to the specified state, ordered by id
    query = ("SELECT cities.id, cities.name FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s ORDER BY cities.id ASC")
    cur.execute(query, (state_name,))

    # Fetch and format the results
    cities = [city[1] for city in cur.fetchall()]
    print(", ".join(cities))

    # Close cursor and database connection
    cur.close()
    db.close()
