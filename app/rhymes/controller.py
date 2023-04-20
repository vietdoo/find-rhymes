from app import app
from flask import render_template, request, Blueprint
import os

rhymes_page = Blueprint('rhymes', __name__, url_prefix='/')

from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from sre_constants import SUCCESS
from datetime import datetime
from difflib import SequenceMatcher
import pandas as pd
import random
import re
import os

from app.rhymes.source.utils import *
from app.rhymes.source.para import *
from app.rhymes.source.varient import *
from app.rhymes.source.rds import *
from app.rhymes.source.mainsearch import *


@rhymes_page.route('/')
def index():
   print('Request for index page received')
   return render_template('rhymes/index.html')


@rhymes_page.route('/', methods=['POST'])
def hello():
    name = request.form.get('new_word')
    if request.form["btn"] == 'h1':
        if name:
            print('Request for QUERY page received with name: %s' % name)
            van = rap(name)
            return render_template('rhymes/index.html', face_detected=len(van)>0, query_name = name, van = van,  init = True)
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