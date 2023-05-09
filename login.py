from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    # return render_template('login.html')
    return "Hello Azure"

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Validate the username and password here (e.g., check against a database)
    # Add your validation logic here
    if username == 'admin' and password == 'password':
        return 'Login successful!'
    else:
        return 'Invalid username or password'

if __name__ == '__main__':
    app.run()
