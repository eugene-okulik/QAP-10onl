import json
import requests
from endpoints.endpoints_handler import Endpoint


def send(token, method, url, body: dict = None, headers: dict = None):
    if not headers:
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'{token}'
        }
    else:
        headers = headers
    if body:
        body = json.dumps(body)

    return Endpoint(requests.request(method, url, data=body, headers=headers))
