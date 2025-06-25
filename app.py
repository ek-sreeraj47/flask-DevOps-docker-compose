from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)

# Read Mongo URI from environment variable
mongo_uri = os.environ.get("MONGO_URI")

try:
    client = MongoClient(mongo_uri)
    db = client['devopsdb']  # Use your actual DB name here
    mongo_status = True
except Exception as e:
    print("MongoDB connection failed:", e)
    mongo_status = False

@app.route('/')
def home():
    if mongo_status:
        return "✅ Flask app is connected to MongoDB Atlas!"
    else:
        return "❌ Failed to connect to MongoDB."

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    # Listen on all interfaces inside Docker
    app.run(host='0.0.0.0', port=5000)

