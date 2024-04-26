import os
from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
from urllib.parse import urlparse, parse_qs

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Parse MongoDB URI
mongo_uri = os.getenv("MONGODB_URI")
#print("MongoDB URI:", mongo_uri)  # Add this line for debugging
uri_parts = urlparse(mongo_uri)
#print("Parsed URI:", uri_parts)   # Add this line for debugging

# Extract database name from URI parameters
query_params = parse_qs(uri_parts.query)
db_name = query_params.get('appName', [''])[0]

print("Database Name:", db_name)   # Add this line for debugging

client = MongoClient(mongo_uri)
db = client[db_name]

@app.route('/')
def index():
    return render_template('index.html')

from flask import request

@app.route('/register', methods=['POST'])
def register():
    print("Request Method:", request.method)
    print("Request Data:", request.form)
    if request.method == 'POST':
        # Get registration data from the form
        username = request.form['username']
        password = request.form['password']
        
        # Check if the username already exists in the database
        existing_user = db.users.find_one({'username': username})
        if existing_user:
            return 'Username already exists!'
        
        # If the username doesn't exist, insert the new user into the database
        new_user = {'username': username, 'password': password}
        db.users.insert_one(new_user)
        
        return 'Registration successful'  # You can customize the response as needed
    else:
        # Handle other methods (GET, etc.) if necessary
        #return 'Method not allowed'
        return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
