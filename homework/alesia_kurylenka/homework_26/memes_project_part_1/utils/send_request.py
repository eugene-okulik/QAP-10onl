import json
import requests


def send(auth, method, url, body: dict = None, headers: dict = None):

    if not headers:
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'{auth}'
        }
    else:
        headers = headers
    if body:
        body = json.dumps(body)
    return requests.request(method, url, data=body, headers=headers)
