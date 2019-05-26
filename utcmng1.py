import pymongo
from pymongo import MongoClient

myclient=pymongo.MongoClient("mongodb://localhost:27017")
mydb=myclient["edwdev"]
mycol=mydb["sales"]

def countrec():
     c=mycol.estimated_document_count()
     return c
     
countrec()

     ##sms=mycol.find({"Brand" : "SAMSUNG"}).count_documents()
