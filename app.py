# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
License: MIT
"""

import os, logging, json
from datetime import datetime

# import Flask 
from flask import Flask, render_template, send_from_directory, request, flash, redirect

from util import csv_to_json, list_csv_files, get_tail, get_date_ms

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
@app.route('/datatables/', methods=['GET', 'POST'])
def datatables():

    # Page data used in POST & GET
    msg       = ''
    input     = ''
    csv_files = []
    
    for f in list_csv_files('samples'):
        csv_files.append( get_tail( f ) )

    if request.method == 'POST':
        if 'file' not in request.files:
            msg = 'No file part'
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            msg = 'No file'
            return redirect(request.url)

        if file: 

            filename = file.filename.replace( '.csv', '_' + get_date_ms() + '.csv' )
            file.save(os.path.join('samples', filename))
            msg = 'File saved: ' + filename 

            csv_files.append( filename )

    else: 

        input = request.args.get('input') 

        if not input:
            input = 'data.csv'

    return render_template( 'datatables.html', input=input, csv_files=csv_files, msg=msg )

# Data Tables pages
@app.route('/api/from_csv')
def load_csv():

    input = request.args.get('input')

    if not input:
        input = 'data.csv'

    aPath = os.path.join(app.root_path, 'samples', input )
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
