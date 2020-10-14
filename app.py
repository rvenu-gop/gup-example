"""
Simple flask server for the interface
"""

import os
import json

from flask import Flask, request, Response, redirect, url_for
from flask import render_template

from gupshup import send_response, write_db, get_bot_response
import requests

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
    app = ''
    try:
        message = request.get_json()
        # Let's try writing all the received messages
        # Irrespective of db failures, let's process the message
        try:
            write_db(message)
        except:
            print("DB write failed!")

        print("JSON Message:", message)
        if "type" in message:
            # Find app type
            if "app" in message:
                app = message['app']
            if message['type'] == 'message':
                msg_type = 'user_message'

                if 'payload' in message:
                    text = message['payload']['payload']['text']
                    print("Message :", text)
            elif message['type'] == 'message-event':
                print("Event :", message['payload']['type'])
    except:
        message = 'Get JSON failed!'
        print(message)

    if msg_type == 'user_message':
        if text != '':
            result = get_bot_response(text, app)
            if result != 'bot: ':
                if app == "nanopix":
                    send_response(result)
            else:
                print("No response from bot!")
                result = "We have received your message and respond to you shortly!"
                if app == 'nanopix':
                    send_response(result)

    resp = Response(status=200, mimetype='application/json')
    return resp


@app.route('/send', methods=['POST','GET'])
def send():
    result = "Test App: Session Message - We have received your message and respond to you shortly!"
    try:
        msg = {"app":"gup-example", "message":result, "env": {"name": "test", "ip": "NA"}}
        headers = {'content-type':'application/json'}
        resp = requests.post("http://cxgeek.herokuapp.com/dblistener",
                        json = msg )
        print(resp)
        if resp.status_code == 200:
            return Response(status=200, mimetype='application/json')
        else:
            print(resp.content)
            return resp.content
    except:
        print("failure!")


if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
