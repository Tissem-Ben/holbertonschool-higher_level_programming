#!/usr/bin/python3
import MySQLdb
import sys

# Check if the script is being executed directly and not imported
if __name__ == "__main__":
    # Retrieve MySQL credentials and database name from command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Establish a connection to the MySQL database using provided credentials
    db = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object to interact with the MySQL database
    cursor = db.cursor()

    # Select states starting with 'N', sorted by id
    cursor.execute(
            "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
            )

    # Fetch all rows from the executed query and print each row
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
