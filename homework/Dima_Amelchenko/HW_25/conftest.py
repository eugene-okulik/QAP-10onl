import pytest
import json
import requests

DOMAIN = 'http://167.172.172.115:52355'
TOKEN = open('token.txt', 'r').read()


@pytest.fixture(scope='session')
def domain():
    return DOMAIN


@pytest.fixture(scope='session')
def token():
    return TOKEN


@pytest.fixture(scope='session')
def authorize(domain, token):
    response = requests.request('GET', f'{domain}/authorize/{token}').text
    if response == "Token is alive. Username is Dima_Amelchenko":
        return token
    else:
        headers = {
            'Content-Type': 'application/json'
        }
        data = json.dumps(
            {
                "name": "Dima_Amelchenko"
            }
        )
        response = requests.request('POST', f'{domain}/authorize', headers=headers, data=data).json()
        with open("token.txt", "w") as f:
            f.write(response["token"])
        return token


@pytest.fixture(scope='function')
def add_meme(domain, authorize):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'{authorize}'
    }
    data = json.dumps(
        {
            "text": "Family",
            "url": "https://www.thevoicemag.ru/upload/img_cache/f0e/f0e1c3b4b532fbc70a73e022ffcf35f2_fitted_1332x0.jpg",
            "tags": ["fun", "Vin Diesel"],
            "info": {
                "type": "jpg"
            }
        }
    )
    response = requests.request('POST', f'{domain}/meme', headers=headers, data=data).json()
    meme_id = response['id']
    return meme_id
