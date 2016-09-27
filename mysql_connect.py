#!/usr/bin/python

import MySQLdb

db = MySQLdb.connect("localhost","winkom","gakpakepassword","lrs_engine_v2.1.0")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()

print "Database version: %s" % data

db.close()