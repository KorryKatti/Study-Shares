from flask import Flask, render_template

app = Flask(__name__)

# Route for serving index.html
@app.route('/')
def index():
    return render_template('index.html')

# Route for serving login.html
@app.route('/login')
def login():
    return render_template('login.html')

# Route for serving register.html
@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
