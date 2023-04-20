from app import app
from flask import render_template

@app.route('/')
def maps():
  return render_template('maps.html')
