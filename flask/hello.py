from flask import Flask
app = Flask(__name__)
# __name__ in single module 

@app.route('/')
# route() decorator to tell Flask what URL should trigger the function
def hello_word():
    return 'Welcome to Index Page'
@app.route('/hello')
def hello():
    return 'Hello,World!!!'

#variable rules 
# mark the sections as <variable_name>
@app.route('/user/<username>')
def show_user_profile(username):
    #show the user profile for that user 
    return 'User %s' % username

# converter can be used by specifying a rule with <converter:variable_name>
@app.route('/post/<int:post_id>')
def show_post(post_id):
    #show the post with the given id, the id is an integer
    return 'Post %d' %post_id
