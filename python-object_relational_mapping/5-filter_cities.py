#!/usr/bin/python3
"""Shebang script"""
import sys
import MySQLdb

if __name__ == "__main__":
    """
    The main entry point of the script
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_db = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=mysql_db)

    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC", (state_name,)
    )
    rows = cursor.fetchall()
    if rows:
        print(", ".join(row[0] for row in rows))
    else:
        print("")
        cursor.close()
    db.close()
