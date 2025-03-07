#!/usr/bin/python3
"""Module listing all cities from the database"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cur = db.cursor()
    cur.execute(
        """SELECT cities.id, cities.name, states.name
                FROM cities
                INNER JOIN states ON cities.state_id = states.id
                ORDER BY cities.id ASC;""")
    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    db.close()
