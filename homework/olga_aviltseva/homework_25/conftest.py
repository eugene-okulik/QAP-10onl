import pytest
import requests
import json


DOMAIN = 'http://167.172.172.115:52355'


@pytest.fixture(scope='session')
def domain():
    return DOMAIN


@pytest.fixture(scope='session')
def authorize(domain):
    headers = {
        'Content-Type': 'application/json'
    }
    data = json.dumps(
        {
            "name": "user"
        }
    )
    response = requests.request('POST', f'{domain}/authorize', headers=headers, data=data).json()
    token = response['token']
    return token


@pytest.fixture(scope='function')
def add_meme(domain, authorize):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'{authorize}'
    }
    data = json.dumps(
        {
            "text": "Best meme generator",
            "url": "https://www.bouncegeek.com/wp-content/uploads/2017/10/Best-meme-generator-min.jpg",
            "tags": ["look"],
            "info": {"type": "png"}
        }
    )
    response = requests.request('POST', f'{domain}/meme', headers=headers, data=data).json()
    meme_id = response['id']
    yield meme_id
    requests.request('DELETE', f'{domain}/meme/{meme_id}')
