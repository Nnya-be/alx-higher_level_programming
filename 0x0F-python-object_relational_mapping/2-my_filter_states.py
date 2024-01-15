#!/usr/bin/python3
"""Script for filtering the states."""
import sys
import MySQLdb


def search_states(username, password, database, state_name):
    """Determine for making the query."""
    connection = MySQLdb.connect(host="localhost", port=3306, user=username,
                                 passwd=password, db=database)
    cursor = connection.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"
    cursor.execute(query, (state_name,))
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    connection.close()


if __name__ == "__main__":
    username, password = sys.argv[1], sys.argv[2]
    database, state_name = sys.argv[3], sys.argv[4]
    search_states(username, password, database, state_name)
