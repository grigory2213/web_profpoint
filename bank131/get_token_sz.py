import json
import requests

data = {
    "tokenize_widget": {
        "access": True,
    },
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

resp = requests.post("https://demo.bank131.ru//api/v1/token",headers=headers, data=data_str)
json_data = resp.json()
print(json_data)