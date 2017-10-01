from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World'


@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username
