import pymongo

from pymongo import Connection

conn = Connection('localhost', 27017)

db = conn.test

names = db.names

item = names.find_one()

print item['name'], item['surname']
