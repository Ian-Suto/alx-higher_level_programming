#!/usr/bin/python3
"""lists all states that start with N """
import sys
import MySQLdb

if __name__ == '__main__':
    connect = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                              passwd=sys.argv[2], db=sys.argv[3])
    cur = connect.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    us_states = cur.fetchall()
    for us_state in us_states:
        print(us_state)
