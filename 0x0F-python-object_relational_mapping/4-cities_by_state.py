#!/usr/bin/python3
"""Lists all states from the database """
import sys
import MySQLdb

if __name__ == '__main__':
    connect = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                              passwd=sys.argv[2], db=sys.argv[3])
    cur = connect.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities LEFT JOIN states ON\
                states.id = cities.state_id ORDER BY cities.id ASC")
    us_states = cur.fetchall()
    for us_state in us_states:
        print(us_state)
