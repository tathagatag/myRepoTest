import pymongo
from pymongo import MongoClient

print ("******Unit Test Count Calculation******")
myclient=pymongo.MongoClient("mongodb://localhost:27017")
mydb=myclient["edwdev"]
mycol=mydb["sales"]

def countrec():
     c=mycol.estimated_document_count()
     return c
countrec()

