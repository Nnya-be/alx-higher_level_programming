#!/usr/bin/python3
"""Module to get all state starting with N and sort them."""
import sys
import MySQLdb

if __name__ == '__main__':
    if (sys.argv != 4):
        return
    usr, pas, dab = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    db = MySQLdb.connect(host='localhost', port=3306, user=usr,
                         passwd=pas, db=dab)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'
                ORDER BY state.id ASC")
    state = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()
