#!/usr/bin/python3
"""Sheban script"""
import sys
import MySQLdb

if __name__ == "__main__":
    """
    The main entry point of the script"""
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_db = sys.argv[3]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=mysql_db)

    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities "
                   "JOIN states ON cities.state_id = states.id "
                   "ORDER BY cities.id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
