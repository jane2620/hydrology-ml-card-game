from doctest import DocTestRunner
from math import perm
from os import remove, environ
# import environ as envi
from os import remove
import sched
from time import time
from unicodedata import name
from urllib import response
from xml.dom import domreg
from flask import Flask, request, make_response, redirect, url_for
from flask import render_template, session
from html import escape  # Used to thwart XSS attacks.
from cgi import FieldStorage
from sys import audit, stderr
from urllib.parse import unquote


app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    html = render_template('index.html')
    response = make_response(html)
    return response

