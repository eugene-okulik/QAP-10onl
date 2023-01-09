import pytest
import requests
import json

BASE_URL = 'http://167.172.172.115:52355'


@pytest.fixture(scope='session')
def base_url():
    return BASE_URL


def receive_new_token(base_url):
    header = {
        'Content-Type': 'application/json'
    }
    data = json.dumps(
        {
            'name': 'evgeny'
        }
    )
    auth = requests.request(
        'POST',
        f'{base_url}/authorize',
        headers=header,
        data=data
    ).json()
    return auth['token']


def check_token(base_url, token):
    response = requests.request('GET', f'{base_url}/authorize/{token}').text
    return response


@pytest.fixture(scope='session')
def authorisation(base_url):
    with open('token.txt', 'r') as r:
        token = r.read()
    if check_token(base_url, token) == 'Token is alive. Username is evgeny':
        return token
    else:
        token = receive_new_token(base_url)
        with open('token.txt', 'w') as w:
            w.write(token)
        return token


@pytest.fixture(scope='function')
def prepare_meme(base_url, authorisation):
    header = {
        'Content-Type': 'application/json',
        'Authorization': f'{authorisation}',
    }
    data = json.dumps(
        {
            "text": "Hello memes",
            "url": "https://cdn.kanobu.ru/articles/pics/88f1a95f-63ee-482f-9d04-3ffaf1a44191.webp",
            "tags": [
                "18+"
            ],
            "info": {
                "type": "jpg"
            }
        }
    )
    meme_id = requests.request(
        'POST',
        f'{base_url}/meme',
        headers=header,
        data=data
    ).json()['id']
    yield meme_id
    requests.request(
        'DELETE',
        f'{base_url}/meme/{meme_id}',
        headers=header,
    )
