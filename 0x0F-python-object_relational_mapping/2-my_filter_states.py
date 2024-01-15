#!/usr/bin/python3
"""Query for a state in the argument."""
import MySQLdb
import sys

if __name__ == '__main__':
    name = sys.argv[1]
    pasword = sys.argv[2]
    dbname = sys.argv[3]
    state = sys.argv[4]
    connection = MySQLdb.connect(host="localhost", port=3306,
                                 user=name, passwd=pasword, db=dbname)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name='{:s}'
                   ORDER BY states.id".format(state))
    info = cursor.fetchall()
    for my_state in info:
        print(my_state)

    cursor.close()
    connection.close()
