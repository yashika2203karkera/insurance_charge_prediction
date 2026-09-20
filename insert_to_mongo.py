import json
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['insurance_db']
collection = db['insurance']

with open('insurance.json') as f:
    data = json.load(f)
collection.insert_many(data)

print("Data inserted successfully!")