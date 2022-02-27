from flask import Flask

from flask import request, after_this_request
from flask import render_template
from flask import make_response
from flask import abort, redirect

from werkzeug.utils import secure_filename
from markupsafe import escape

def routes_setting(app: Flask):
    @app.route('/')
    def index():
        return render_template('main/index.html')

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