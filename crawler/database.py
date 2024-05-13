from flask import jsonify
from pymongo.collection import Collection
from pymongo.mongo_client import MongoClient
import config
import random
from bson.objectid import ObjectId
from bson.json_util import dumps, loads

uri = f"mongodb+srv://{config.USER}:{config.PASSWORD}@cluster0.izgloib.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Choose database
db = client['BiasBreakerDatabase']

def insert_articles(articles):
    # Choose collection
    collection = db['articles']
    collection.insert_many(articles)


