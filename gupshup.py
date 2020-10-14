
import requests
import json

def test():
  import json
  s_msg = {
    "app": "DemoApp",
    "timestamp": 1580227766370,
    "version": 2,
    "type": "message",
    "payload": {
      "id": "ABEGkYaYVSEEAhAL3SLAWwHKeKrt6s3FKB0c",
      "source": "918x98xx21x4",
      "type": "text",
      "payload": {
        "text": "Hi"
      },
      "sender": {
        "phone": "918x98xx21x4",
        "name": "Smit",
        "country_code": "91",
        "dial_code": "8x98xx21x4"
      }
    }
  }
  message = json.loads(json.dumps(s_msg))
  print("JSON Message:", message)
  if 'payload' in message:
      text = message['payload']['payload']['text']

  print("Message :", text)


'''
Method to send a reply message. 
This will be a in session message. isHSM set to false
'''
def send_response(text):
    resp_message = {
    "channel" : "whatsapp",
    "source" : "917834811114",
    "destination" : "919884002018",
    "src.name":"nanopix",
    "message" : json.dumps({
              "isHSM":"false",
              "type": "text",
              "text": "reply: " + text
      })
    }

    try:
        # Send message API
        url = 'https://api.gupshup.io/sm/api/v1/msg'
        api_key = '758bf50e1d08458ac5da693eb0c1970d'
        content_type = 'application/x-www-form-urlencoded'

        headers = {'content-type': content_type, 'apikey': api_key, 'Cache-Control': 'no-cache'}
        resp = requests.post(url, headers=headers, data=resp_message)
        # Async response - Message submitted
        if resp.status_code == 200:
            print("Message response sent! : ", resp_message)
        else:
            print(resp.content)
    except:
        print("Message response failed! : ", resp_message)


def write_db(msg):
    try:
        # Write to the API
        url = "http://cxgeek.herokuapp.com/dblistener"

        resp = requests.post(url, json=msg)

        if resp.status_code == 200:
            print("DB write successful!")
        else:
            print(resp.content)
    except:
        print("DB write failed! : ", msg)


def get_bot_response(user_msg, app):
    url = 'https://nanopixbot.herokuapp.com/webhooks/rest/webhook'
    if app == 'nanopix':
        sender = 200
    else:
        sender = 1

    req = {
        "message": user_msg,
        "sender": sender
    }
    text = 'bot: '
    try:
        resp = requests.post(url, json=req)
        if len(resp.text) > 0:
            data = json.loads(resp.text)
            for item in data:
                if "text" in item:
                    text = text + " " + item["text"]
                if "image" in item:
                    text = text + " " + item["image"]
        print("Bot response :", text)
    except:
        print("Error in rasa bot!")

    return text