
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


def send_response(text):
    resp_message = {
    "channel" : "whatsapp",
    "source" : "917834811114",
    "destination" : "919884002018",
    "src.name":"nanopix",
    "message" : {
              "isHSM":"false",
              "type": "text",
              "text": ""
      }
    }

    try:
        resp_message['message']['text'] = text

        url = 'https://api.gupshup.io/sm/api/v1/msg'
        api_key = '758bf50e1d08458ac5da693eb0c1970d'
        content_type = 'application/x-www-form-urlencoded'

        headers = {'content-type': content_type, 'apikey': api_key, 'Cache-Control': 'no-cache'}
        requests.post(url, headers=headers, data=json.dumps(resp_message))
        print("Message response sent! : ", resp_message)
    except:
        print("Message response failed! : ", resp_message)
