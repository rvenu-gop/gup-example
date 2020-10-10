"""
Simple flask server for the interface
"""

import os
import json

from flask import Flask, request, Response, redirect, url_for
from flask import render_template

from gupshup import send_response

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
    msg_type = ''
    try:
        message = request.get_json()
        print("JSON Message:", message)
        if "type" in message:
            if message['type'] == 'message':
                msg_type = 'user_message'
                if 'payload' in message:
                    text = message['payload']['payload']['text']
        print("Message :", text)
    except:
        message = 'Get JSON failed!'
        print(message)

    if msg_type == 'user_message':
        if text.lower() == 'hello nanopix':
            result = "Thank you for reaching Nanopix, We are processing your request and respond to you shortly!"
            send_response(result)
        else:
            result = "We have received your message and respond to you shortly!"
            send_response(result)

    resp = Response(status=200, mimetype='application/json')
    return resp


@app.route('/send', methods=['POST','GET'])
def send():
    result = "Test App: Session Message - We have received your message and respond to you shortly!"
    send_response(result)

    resp = Response(status=200, mimetype='application/json')
    return resp

#if __name__ == '__main__':
    #app.run(host="localhost", port=8080, debug=True)
