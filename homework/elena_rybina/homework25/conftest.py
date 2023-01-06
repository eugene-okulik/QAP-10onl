import json
import pytest
import requests


DOMAIN = 'http://167.172.172.115:52355/'


@pytest.fixture(scope='session')
def domain():
    return DOMAIN


def authorize(domain):
    my_headers = {
        'Content-Type': 'application/json',
            }
    my_data = json.dumps(
        {
           "user": "elena"
        }
    )
    resp = requests.post(f'{domain}/authorize', headers=my_headers, data=my_data).json()
    token = resp.json()['token']
    return token

def check_token(domain, token):
    response = requests.get(f'{domain}/authorize/{token}').text
    return response


@pytest.fixture(scope='session')
def authorization(domain):
    with open('tk.txt', 'r') as r:
        token = r.read()
    if check_token(domain, token) == 'Token is still working. Username is elena':
        return token
    else:
        token = authorize(domain)
        with open('tk.txt', 'w') as w:
            w.write(token)
        return token


@pytest.fixture(scope='function')
def add_meme(domain):
    my_headers = {
        'Content-Type': 'application/json',
        'Authorization': f'{authorization}'
    }
    my_data = json.dumps(
        {
            "text": "Seafood diet",
            "url": "https://img.delicious.com.au/WqbvXLhs/del/2016/06/more-the-merrier-31380-2.jpg",
            "tags": ["seafood", "diet"],
            "info": {"type": "jpg"}

        }
    )
    meme_id = requests.post(f'{domain}/meme', headers=my_headers, data=my_data).json()['id']
    yield meme_id
    requests.request(
        'DELETE',
        f'{domain}/meme/{meme_id}',
        headers=my_headers,
    )
