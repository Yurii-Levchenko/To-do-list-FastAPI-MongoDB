from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:test1234!@cluster0.7o5py.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.todo_db

collection_name = db["todo_collection"]
