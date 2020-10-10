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
    text = ''
    try:
        message = request.get_json()
        print("JSON Message:", message)
        if 'payload' in message:
            text = message['payload']['payload']['text']
        print("Message :", text)
    except:
        message = 'Get JSON failed!'
        print(message)

    if text.lower() == 'hello nanopix':
        return "Thank you for reaching Nanopix, We are processing your request and respond to you shortly!"
    else:
        return "We have received your message and respond to you shortly!"


