#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Retrieving the connection arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connecting to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Creating a cursor to execute queries
    cursor = db.cursor()

    # Executing the query to select states whose name starts with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")

    # Retrieving the results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Closing the cursor and the connection
    cursor.close()
    db.close()

