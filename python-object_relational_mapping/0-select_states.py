#!/usr/bin/python3
"""Shebang script"""

import MySQLdb
import sys

if __name__ == "__main__":
    """ Lists all states from the database hbtn_0e_0_usa"""

    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    # Create a cursor to execute SQL queries
    cur = db.cursor()

    # Execute the query to select all states, ordered by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows and print them in the desired format
    rows = cur.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()
