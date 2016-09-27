#!/usr/bin/python

import sys
import MySQLdb
from pymongo import MongoClient

host = 'localhost'
user = 'winkom'
pwd = 'gakpakepassword'
dbname = 'lrs_engine_bank_data'

# mysql
db_mysql = MySQLdb.connect(host, user, pwd, dbname)
cursor = db_mysql.cursor(MySQLdb.cursors.DictCursor)

# mongo
client = MongoClient(host, 27017)
db_mongo = client.fastboat

try:
    cursor.execute(
        'SELECT *, (SELECT harbor.harbor_name FROM lrs_fastboat_harbor harbor WHERE harbor.harbor_id = route.departure) AS departure_harbor_name, (SELECT harbor.harbor_name FROM lrs_fastboat_harbor harbor WHERE harbor.harbor_id = route.arrival) AS arrival_harbor_name, (SELECT region.region_name FROM lrs_fastboat_harbor harbor LEFT JOIN lrs_fastboat_region region ON harbor.region_id = region.region_id WHERE harbor.harbor_id = route.departure) AS departure_harbor_region_name, (SELECT region.region_name FROM lrs_fastboat_harbor harbor LEFT JOIN lrs_fastboat_region region ON harbor.region_id = region.region_id WHERE harbor.harbor_id = route.arrival) AS arrival_harbor_region_name FROM lrs_fastboat_reservation reservation LEFT JOIN lrs_fastboat_payment payment ON reservation.payment_id_fk = payment.payment_id LEFT JOIN lrs_fastboat_route route ON reservation.route_id_fk = route.route_id LEFT JOIN lrs_fastboat_boat boat ON route.boat_id_fk = boat.boat_id LEFT JOIN lrs_fastboat_company company ON boat.company_id_fk = company.company_id LEFT JOIN lrs_user user ON reservation.user_id_fk = user.user_id')
    results = cursor.fetchall()
    for row in results:
        db_mongo['lrs_fastboat_summary'].insert_one(row)

except MySQLdb.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)