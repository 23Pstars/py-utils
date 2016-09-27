#!/usr/bin/python

from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.kuliah

for doc in db.jadwal.find():
    for key, value in doc.items():
        print '%s: %s' % (key, value)
        # print doc.values()
        # print type(doc)
        # for field, value in doc:
