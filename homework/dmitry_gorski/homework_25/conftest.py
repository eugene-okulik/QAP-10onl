import pytest
import requests
import json
from os.path import join, dirname, exists


DOMAIN, NAME = 'http://167.172.172.115:52355', 'dgorski'


@pytest.fixture(scope='session')
def domain():
    return DOMAIN


@pytest.fixture(scope='session')
def name():
    return NAME


@pytest.fixture(scope='session')
def authorize(domain, name):
    headers, endpoint = {'Content-Type': 'application/json'}, '/authorize'
    if exists(join(dirname(__file__), 'current_key.key')):
        with open(join(dirname(__file__), 'current_key.key'), 'r') as f:
            key = f.read()
        response = requests.get(f'{domain}{endpoint}/{key}')
        if response.status_code == 200:
            if response.text != f'Token is alive. Username is {name}':
                response = requests.post(f'{domain}{endpoint}', headers=headers, data=json.dumps({'name': name}))
                if response.status_code == 200:
                    key = response.json()['token']
                    with open(join(dirname(__file__), 'current_key.key'), 'w') as f:
                        f.write(key)
        return key

    else:
        response = requests.post(f'{domain}{endpoint}', headers=headers, data=json.dumps({'name': name}))
        if response.status_code == 200:
            key = response.json()['token']
            with open(join(dirname(__file__), 'current_key.key'), 'w') as f:
                f.write(key)
            return key


@pytest.fixture(scope='function')
def create_meme(domain, authorize):
    headers, endpoint = {"Authorization": f'{authorize}', 'Content-Type': 'application/json'}, '/meme'
    data_json = {
        'text': 'Which fucking monday',
        'url': 'https://cdn.memes.com/up/36793211618339628/i/1671475140893.jpg',
        'tags': ['monday', 'products'],
        'info': {'colors': ['green', 'white', 'red'],
                 'objects': ['product', 'product_info']}
    }
    data = json.dumps(data_json)
    response = requests.post(f'{domain}{endpoint}', headers=headers, data=data).json()
    ID = response['id']
    yield ID
    requests.request('DELETE', f'{domain}{endpoint}/{ID}')
