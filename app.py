from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from sre_constants import SUCCESS
from datetime import datetime
from difflib import SequenceMatcher
import pandas as pd
import random
import re
import os

#import MySQLdb

from source.utils import *
from source.para import *
from source.varient import *
from source.rds import *
from source.mainsearch import *

app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')


@app.route('/', methods=['POST'])
def hello():
    name = request.form.get('new_word')
    if request.form["btn"] == 'h1':
        if name:
            print('Request for QUERY page received with name: %s' % name)
            van = rap(name)
            return render_template('index.html', face_detected=len(van)>0, query_name = name, van = van,  init = True)
        else:
            print('Request for QUERY page received with no name or blank name -- redirecting')
            return redirect(url_for('index'))

"""
@app.route('/insert')
def insert_home():
    print('Request for index page received')
    return render_template('insert.html', SL = sql_count('SELECT COUNT(*) FROM full_original'))

@app.route('/insert', methods=['POST'])
def insert_words():
    name = request.form.get('new_word')
    if name:
        print('Request for new word | received: %s' % name)
        res = insert_word_to_SQL(name)
        return render_template('insert.html', query_name = name, SL = sql_count('SELECT COUNT(*) FROM full_original'), success = res > 0, init = True)
    else:
        return render_template('insert.html', SL = sql_count('SELECT COUNT(*) FROM full_original'))
"""
if __name__ == '__main__':
    app.run(debug = True, use_reloader = True)