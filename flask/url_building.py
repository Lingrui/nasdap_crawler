from flask import Flask,url_for
app = Flask(__name__)
#using url_for() function to build a url to a specific function 

@app.route('/')
def index():
    pass

@app.route('/login')
def login():
    pass

@app.route('/user/<username>')
def profile(username):
    pass

with app.test_request_context():
    print (url_for('index'))
    print (url_for('login'))
    print (url_for('login',next='/'))
    print (url_for('profile',username='John Doe'))
