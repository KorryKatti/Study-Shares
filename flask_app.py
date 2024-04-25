from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv

app = Flask(__name__, static_url_path='/static')

# Load environment variables from .env file
load_dotenv()

# Configure MongoDB URI from environment variables
app.config["MONGO_URI"] = os.getenv("MONGODB_URI")

# Initialize PyMongo with the Flask app
mongo = PyMongo(app)

# Route for serving index.html
@app.route('/')
def index():
    # Example: Fetch data from MongoDB and pass it to the template
    data_from_mongodb = mongo.db.collection_name.find()
    return render_template('index.html', data=data_from_mongodb)

# Route for serving login.html
@app.route('/login')
def login():
    return render_template('login.html')

# Route for serving register.html
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if user already exists
        existing_user = mongo.db.users.find_one({'email': email})
        if existing_user:
            return "User already exists. Please log in."

        # Insert user into the database
        new_user = {'username': username, 'email': email, 'password': password}
        mongo.db.users.insert_one(new_user)

        return redirect(url_for('login'))

    return render_template('register.html')

# Route for serving config.json
@app.route('/config.json')
def get_config():
    return send_from_directory(app.static_folder, 'config.json')

# Route for serving arc-sw.js
@app.route('/arc-sw.js')
def serve_js():
    return send_from_directory(app.static_folder, 'arc-sw.js')

if __name__ == '__main__':
    app.run(debug=True)
