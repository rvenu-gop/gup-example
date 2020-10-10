"""
Simple flask server for the interface
"""

import os
import json

from flask import Flask, request, redirect, url_for
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    message = request.args.get('message', '')
    if not message:
        message = 'Message parameter missing!'

    return render_template('index.html', message=message)

@app.route('/listener', methods=['POST'])
def listen():
    try:
        message = request.get_json()
    except:
        message = 'Get JSON failed!'

    return render_template('index.html', message = message)


