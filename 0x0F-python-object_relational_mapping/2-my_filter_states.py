#!/usr/bin/python3
"""Query for a state in the argument."""
import sys
import MySQLdb

if __name__ == '__main__':
  name = sys.argv[1]
  pasword = sys.argv[2]
  dbname = sys.argv[3]
  state = sys.argv[4]
  connection = MySQLdb.connect(host="localhost", port=3306, user=name, passwd = pasword,
                              db = dbname)
  cursor = connection.cursor()
  cursor.execute(f"SELECT * FROM states WHERE name={state}")
  info = cursor.fetchall()
  for my_state in info:
    print(my_state)

cursor.close()
connection.close()
