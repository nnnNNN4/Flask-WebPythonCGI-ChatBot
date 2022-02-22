from flask import Flask, url_for
from markupsafe import escape
from flask import request
from flask import render_template
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['username'] and request.form['password']:
            return render_template('login/in.html',
            	username=request.form['username'],
            	password=request.form['password'])
        return 'パスワードかユーザーネームが入力されていません'
    return render_template('login/login.html')

@app.route('/uploads', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        f = request.files["the_file"]
        f.save('/home/testuser/Flask-Project-1/src/uploads/' + secure_filename(f.filename))
        return render_template('uploads/finished.html')
    else:
    	return render_template('uploads/uploads.html')