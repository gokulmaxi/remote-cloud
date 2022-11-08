#!/usr/bin/env python3
import pymongo

myclient = pymongo.MongoClient("mongodb://mongouser:mongoPass@mongodb:27017/?authMechanism=DEFAULT")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)
