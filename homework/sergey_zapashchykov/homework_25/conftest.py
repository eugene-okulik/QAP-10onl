import json
import pytest
import requests


DOMAIN = 'http://167.172.172.115:52355'


@pytest.fixture(scope='session')
def domain():
    return DOMAIN


def get_new_token(domain):
    header = {
        'Content-Type': 'application/json'
    }
    data = json.dumps(
        {
            'name': 'sergey_z'
        }
    )
    authorize = requests.request(
        'POST',
        f'{domain}/authorize',
        headers=header,
        data=data
    ).json()
    return authorize['token']


def check_for_token(domain, token):
    response = requests.request('GET', f'{domain}/authorize/{token}').text
    return response


@pytest.fixture(scope='session')
def authorisation(domain):
    with open('token.txt', 'r') as r:
        token = r.read()
    if check_for_token(domain, token):
        return token
    else:
        token = get_new_token(domain)
        with open('token.txt', 'w') as w:
            w.write(token)
        return token


@pytest.fixture(scope='function')
def prepare_post(domain, authorisation):
    header = {
        'Content-Type': 'application/json',
        'Authorization': f'{authorisation}',
    }
    data = json.dumps(
        {
            "text": "My new mem",
            "url": "https://klike.net/uploads/posts/2019-09/1568449912_2.jpg",
            "tags": [
                "Cats"
            ],
            "info": {
                "type": "jpg"
            }
        }
    )
    post_id = requests.request(
        'POST',
        f'{domain}/meme',
        headers=header,
        data=data
    ).json()['id']
    yield post_id
    requests.request(
        'DELETE',
        f'{domain}/meme/{post_id}'
    )
