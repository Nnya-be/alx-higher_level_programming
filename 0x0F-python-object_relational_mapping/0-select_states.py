#!/usr/bin/python3
"""Script to list all states from a database."""
import sys
import MySQLdb

def list_states(username, password, database):
    connection = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)


    cursor = connection.cursor()

    query = "SELECT * FROM states ORDER BY states.id ASC"
    cursor.execute(query)

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    connection.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    list_states(username, password, database)
