import os

from flask import Flask, url_for
from markupsafe import escape
from flask import request, after_this_request
from flask import render_template
from werkzeug.utils import secure_filename
from flask import make_response
from flask import abort, redirect
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

# route setting
from src.routes import routes_setting
routes_setting(app)