from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()

app = Flask(__name__)

MONGO_URI = os.getenv('MONGO_URI')
client = MongoClient(MONGO_URI)

# Getting the default database from the MongoClient
db = client.get_default_database()

users_collection = db['users']  # Collection for storing user details

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Insert user details into MongoDB
        users_collection.insert_one({'username': username, 'password': password})
        return f'Registered new user: {username}'
    else:
        return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
