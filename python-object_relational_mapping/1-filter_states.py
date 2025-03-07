#!/usr/bin/python3
"""Module listing all states by N"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )
    cur = db.cursor()
    query = """SELECT * FROM states WHERE name LIKE BINARY 'N%'
                ORDER BY id ASC;"""
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
