from flask import Flask, url_for
from markupsafe import escape
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['username'] and request.form['password']:
            return render_template('in.html',
            	username=request.form['username'],
            	password=request.form['password'])
        return 'パスワードかユーザーネームが入力されていません'
    return render_template('login.html')