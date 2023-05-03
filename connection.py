#Python driver for MongoDB to connect applications.
from pymongo import MongoClient

MONGODB_URI = "Connection_String_URI"

client = MongoClient(MONGODB_URI)

for db_name in client.list_database_names():
    print(db_name)
