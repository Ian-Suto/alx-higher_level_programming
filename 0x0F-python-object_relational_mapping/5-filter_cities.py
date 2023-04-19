#!/usr/bin/python3
"""Lists all cities from the state provided """
import sys
import MySQLdb

if __name__ == '__main__':
    connect = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                              passwd=sys.argv[2], db=sys.argv[3])
    cur = connect.cursor()
    cur.execute("SELECT cities.name FROM cities LEFT JOIN states ON\
                states.id = cities.state_id WHERE states.name = %s\
                ORDER BY cities.id ASC", (sys.argv[4],))
    cities = cur.fetchall()
    print(", ".join([state[0] for state in cities]))
    cur.close()
    connect.close()
