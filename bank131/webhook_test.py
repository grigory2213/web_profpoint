import requests
import json

webhook_url = 'http://127.0.0.1:5000/webhook'

data = { 'name': 'grigory', 
         'Channel URL': 'https://www.youtube.com/channel/UC4Snw5yrSDMXys31I18U3gg' }

r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
