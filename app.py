# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
License: MIT
"""

import os, logging, json
from datetime import datetime

# import Flask 
from flask import Flask, render_template, send_from_directory

from util import csv_to_json, h_list_to_s

# Inject Flask magic
app = Flask(__name__, static_folder="static")

# Config
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'Super_s3cret777'
	
# Default Route
@app.route('/')
def index():

    return render_template( 'index.html', segment='index.html' )

# Data Tables pages
@app.route('/datatables/')
def datatables():
    return render_template( 'datatables.html' )

# Data Tables pages
@app.route('/api/from_csv')
def load_csv():

    aPath = os.path.join(app.root_path, 'samples', 'data.csv')
    data  = csv_to_json( aPath )

    response = app.response_class(
        response=json.dumps( data ),
        status=200,
        mimetype='application/json'
    )

    return response

# Data Tables pages
@app.route('/api/from_json')
def load_json(): 
    return send_from_directory(os.path.join(app.root_path, 'samples'), 'data.json') 

# For Python Bootstrap  
if __name__ == "__main__":
    app.run()
