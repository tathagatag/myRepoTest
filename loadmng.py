import os
import pandas as pd
import datetime
import pymongo
import json
from pymongo import MongoClient

print ('****** Set up Connection with MongoDB *******')

myclient=pymongo.MongoClient("mongodb://localhost:27017")
mydb=myclient["edwdev"]
mycol=mydb["sales"]

path_1 = "C:\iofile\input\mobile.csv"
df_1 = pd.read_csv(path_1, sep = "," , names = ["WarehouseNum" ,"GLCategory" , "Aging" , "Carrier" , "InventoryType", "Quantity" , "Price" , "Brand"] )

dt = datetime.datetime.now().date().strftime('%Y%m%d')
print ("Run Date=")
print (dt)
df_1['LoadDate'] = dt



data_json=json.loads(df_1.to_json(orient='records'))

result=mycol.insert_many(data_json)

print ('****** Data Load Completed *******')

