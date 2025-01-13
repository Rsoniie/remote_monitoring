from flask import Flask
from flask_pymongo import PyMongo
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
mongo = PyMongo(app)


try:
    
    mongo.cx.admin.command('ping')
    print("MongoDB connected successfully!")
except Exception as e:
    print("Failed to connect to MongoDB:", e)

from app import routes
