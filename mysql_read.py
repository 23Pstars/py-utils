#!/usr/bin/python

import sys
import MySQLdb

db = MySQLdb.connect("localhost", "winkom", "gakpakepassword", "lrs_engine_v2.0.2")
cursor = db.cursor()

sql = "SELECT * FROM lrs_fastboat_reservation"

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print type( row )
        # for key, value in row.items():
        #     print "%s: %s" % (key, value)

except MySQLdb.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

finally:
    db.close()
