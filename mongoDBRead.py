###Querying MongoDB collection in Application
import os
import print

from dotenv import load_dotenv
from pymongo import MongoClient


# Inport ObjectId from bson package (part of PyMongo distribution) to enable querying by ObjectId
from bson.objectid import ObjectId

# Load config from .env file
load_dotenv()

MONGODB_URI = "connection_string_uri"

# Connect to MongaDB cluster with MongoClient
client = MongoClient (MONGODB_URI)

# Get reference to ‘bank’ database
db = client.bank

# Get a reference to the ‘accounts’ collection
accounts_collection = db.accounts

# Query by Objectld
document_to_find = {"_id": ObjectId("62d6e0decab6dse1304974ae")}

# Write an expression that retrieves the document matching the query constraint in the ‘accounts’ collection.
result = accounts_collection. find_one(docunent_to_find)

print(result)

client.close()
