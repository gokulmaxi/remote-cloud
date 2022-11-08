#!/usr/bin/env python3
import pymongo

myclient = pymongo.MongoClient(
    "mongodb://mongouser:mongoPass@localhost:27017/?authSource=admin"
)
mydb = myclient["mydatabase"]
mycol = mydb["users"]
import csv

with open("data.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        mydict = {"roll_no": row[1], "name": row[2], "email": row[3], "port": row[4]}
        x = mycol.insert_one(mydict)
        print(row)
