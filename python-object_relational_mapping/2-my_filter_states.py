#!/usr/bin/python3
"""Displays all values in the states table where name matches the argument."""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the database using command line arguments
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()

    # Execute the query with the state name passed as an argument
    state_name = sys.argv[4]
    query = (
        "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
        .format(state_name)
    )
    cursor.execute(query)

    # Fetch and print all matching rows
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
