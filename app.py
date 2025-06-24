from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)

# Connect to MongoDB using env vars
mongo_host = os.environ.get("MONGO_HOST", "localhost")
mongo_port = int(os.environ.get("MONGO_PORT", 27017))

client = MongoClient(host=mongo_host, port=mongo_port)
db = client['devopsdb']

@app.route('/')
def home():
    return "Connected to MongoDB: " + str(db.list_collection_names())

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

