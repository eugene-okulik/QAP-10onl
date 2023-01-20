import json
import pytest
import requests
from urllib import request, error

DOMAIN = 'http://167.172.172.115:52355/'


@pytest.fixture(scope='session')
def domain():
    return DOMAIN


@pytest.fixture(scope='session')
def authorize(domain):
    token = open('token.txt').read()
    try:
        request.Request(f'{domain}/authorize/{token}')
        return token
    except error.HTTPError:
        create_token(domain)


def create_token(domain):
    headers = {
        'Content-Type': 'application/json'
    }
    data = json.dumps(
        {
            "name": "val"
        }
    )
    response = requests.request('POST', f'{domain}/authorize', headers=headers, data=data).json()
    token = response['token']
    save_token(token)
    return token


def save_token(token):
    f = open('token.txt', 'w')
    f.write(token)
    f.close()


@pytest.fixture(scope='function')
def prepare_post(domain, authorize):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'{authorize}'
    }
    data = json.dumps(
        {
            "text": "mem2",
            "url": "https://cs13.pikabu.ru/post_img/2023/01/11/10/167345632116998858.webp",
            "tags": ["laptop"],
            "info": {
                "type": "jpg"
            }
        }
    )
    meme_id = requests.request('POST', f'{domain}/meme', headers=headers, data=data).json()['id']
    yield meme_id
