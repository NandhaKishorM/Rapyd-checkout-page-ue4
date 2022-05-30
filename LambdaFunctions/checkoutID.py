import json
import requests
import random
import string
import hmac
import base64
import hashlib
import time

base_url = 'https://sandboxapi.rapyd.net'
access_key = 'F05358A0C7CA4B3DB2C5'
secret_key = 'fd182dca4c4dd6a2d97da94023b35ea50c3a70b4c0867d9980679beded403e6b3ba5653c7fac98c8'

def generate_salt(length=12):
    return ''.join(random.sample(string.ascii_letters + string.digits, length))

def get_unix_time(days=0, hours=0, minutes=0, seconds=0):
    return int(time.time())

def update_timestamp_salt_sig(http_method, path, body):
    if path.startswith('http'):
        path = path[path.find(f'/v1'):]
    salt = generate_salt()
    timestamp = get_unix_time()
    to_sign = (http_method, path, salt, str(timestamp), access_key, secret_key, body)
    
    h = hmac.new(secret_key.encode('utf-8'), ''.join(to_sign).encode('utf-8'), hashlib.sha256)
    signature = base64.urlsafe_b64encode(str.encode(h.hexdigest()))
    return salt, timestamp, signature

def current_sig_headers(salt, timestamp, signature):
    sig_headers = {'access_key': access_key,
                   'salt': salt,
                   'timestamp': str(timestamp),
                   'signature': signature,
                   'idempotency': str(get_unix_time()) + salt}
    return sig_headers

def pre_call(http_method, path, body=None):
    str_body = json.dumps(body, separators=(',', ':'), ensure_ascii=False) if body else ''
    salt, timestamp, signature = update_timestamp_salt_sig(http_method=http_method, path=path, body=str_body)
    return str_body.encode('utf-8'), salt, timestamp, signature

def create_headers(http_method, url,  body=None):
    body, salt, timestamp, signature = pre_call(http_method=http_method, path=url, body=body)
    return body, current_sig_headers(salt, timestamp, signature)

def make_request(method,path,body=''):
    body, headers = create_headers(method, base_url + path, body)

    if method == 'get':
        response = requests.get(base_url + path,headers=headers)
    elif method == 'put':
        response = requests.put(base_url + path, data=body, headers=headers)
    elif method == 'delete':
        response = requests.delete(base_url + path, data=body, headers=headers)
    else:
        response = requests.post(base_url + path, data=body, headers=headers)

    if response.status_code != 200:
        raise TypeError(response, method,base_url + path)
    return json.loads(response.content)
method = "post"
path = "/v1/checkout"
body = {
    "amount": 500,
    "complete_payment_url": "http://example.com/complete",
    "country": "IN",
    "currency": "INR",
    "error_payment_url": "http://example.com/error",
    "merchant_reference_id": "950ae8c6-78",
    "cardholder_preferred_currency": "true",
    "language": "en",
    "metadata": {
        "merchant_defined": "true"
    },
    "payment_method_types_include": [
        "in_visa_credit_card","in_maestro_debit_card","in_googlepay_upi_bank","in_upi_bank","in_rupay_debit_card","in_debit_visa_card", "in_mastercard_debit_card","in_mastercard_credit_card"
    ],
    "expiration": "1685370378",
    "payment_method_types_exclude": []
}

def lambda_handler(event, context):
    # TODO implement
    res = make_request(method, path,body)
    res = res['data']['id']
    print(res)
    return {
        'statusCode': 200,
        'body': json.dumps(res)
    }
