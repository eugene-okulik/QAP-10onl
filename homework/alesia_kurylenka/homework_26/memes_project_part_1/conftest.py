import pytest
import json
import requests
import constants
from os.path import join, dirname


@pytest.fixture(scope='session')
def domain():
    return f'{constants.DOMAIN}'


@pytest.fixture(scope='session')
def auth(domain):
    with open(join(dirname(__file__), 'token.txt'), 'r') as tf:
        token = tf.read()
    response = requests.request(
        'GET',
        f'{domain}/authorize/{token}'
    ).text
    if response == "Token is alive. Username is alesia":
        return token
    else:
        headers = {
            'Content-Type': 'application/json'
        }
        data = json.dumps(
            {
                "name": "alesia"
            }
        )
        response = requests.request(
            'POST',
            f'{domain}/authorize',
            headers=headers,
            data=data
        ).json()
        with open(join(dirname(__file__), 'token.txt'), "w") as f:
            f.write(response["token"])
        return token


@pytest.fixture(scope='function')
def add_meme1(domain, auth):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'{auth}'
    }
    data = json.dumps(
        {
            "text": "you are very boring, but you can continue",
            "url": "http://risovach.ru/upload/2019/06/mem/kapibara-odobryaet_211465163_orig_.jpg",
            "tags": [
                "capybara",
                "meme",
                "fun"
            ],
            "info": {
                "colors": [
                    "brown",
                    "red",
                    "white"
                ],
                "objects": [
                    "picture",
                    "text"
                ]
            }
        }
    )
    response = requests.request(
        'POST',
        f'{domain}/meme',
        headers=headers,
        data=data
    ).json()
    meme_id = response['id']
    yield meme_id
    requests.request('DELETE', f'{domain}/posts/{meme_id}')
