import json
import pandas as pd
import requests

def chek_nalog_status(INN):

    data = {
        'tax_reference': f'{INN}',
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

    resp = requests.post("https://demo.bank131.ru/api/v1/npd/check",headers=headers, data=data_str)
    json_data = resp.json()
    print(json_data)

    df = pd.json_normalize(json_data)
    request_id = df['request_id'][0]
    print(request_id)
    
    data1 = {
        "request_id": f'{request_id}',
    }
    
    # key_file = open("private.pem", "r")
    # key = key_file.read()
    # key_file.close()


    if key.startswith('-----BEGIN '):
        pkey = crypto.load_privatekey(crypto.FILETYPE_PEM, key)
    else:
        pkey = crypto.load_pkcs12(key).get_privatekey()

    data_str = json.dumps(data1)

    sign = OpenSSL.crypto.sign(pkey, data_str.encode('utf8'), "sha256")
    sign_base64 = base64.b64encode(sign)

    headers = {
        "X-PARTNER-PROJECT": "profpoint",
        "X-PARTNER-SIGN":sign_base64,
    'Content-Type': 'application/json'
    }

    resp = requests.post("https://demo.bank131.ru/api/v1/npd/request/status",headers=headers, data=data_str)
    json_data = resp.json()
    print(json_data)
    
    
    
    return 

chek_nalog_status(500104084256)