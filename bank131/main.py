import json
import pandas as pd
import requests

data = {
    "payment_method": {
        "type": "card",
        "card": {
            "type": "bank_card",
            "bank_card": {
                "number": "4242424242424242"
            }
        }
    },
    "amount_details": {
        "amount": 1000,
        "currency": "rub"
    },
    "participant_details": {
        "recipient": {
            "full_name": "Иванов Иван Иванович"
        }
    }
}

import OpenSSL
from OpenSSL import crypto
import base64

key_file = open("private.pem", "r")
key = key_file.read()
key_file.close()


if key.startswith('-----BEGIN '):
    pkey = crypto.load_privatekey(crypto.FILETYPE_PEM, key)
else:
    pkey = crypto.load_pkcs12(key).get_privatekey()

data_str = json.dumps(data)

sign = OpenSSL.crypto.sign(pkey, data_str.encode('utf8'), "sha256")
sign_base64 = base64.b64encode(sign)

headers = {
    "X-PARTNER-PROJECT": "profpoint",
    "X-PARTNER-SIGN":sign_base64,
'Content-Type': 'application/json'
}

resp = requests.post("https://demo.bank131.ru//api/v1/session/init/payout",headers=headers, data=data_str)
json_data = resp.json()
print(json_data)

df = pd.json_normalize(json_data)
session_id = str(df['session.id'])
print(session_id)