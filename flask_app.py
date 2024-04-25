from flask import Flask, render_template ,send_from_directory


app = Flask(__name__,static_url_path='/static')

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

@app.route('/config.json')
def get_config():
    return send_from_directory(app.static_folder, 'config.json')

if __name__ == '__main__':
    app.run(debug=True)
