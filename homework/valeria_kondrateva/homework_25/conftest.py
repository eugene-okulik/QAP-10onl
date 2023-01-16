import json
import pytest
import requests


DOMAIN = 'http://167.172.172.115:52355/'


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
            "name": "lera"
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
            "text": "Dog meme",
            "url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.wikipedia."
            "org%2Fwiki%2F%25D0%2594%25D0%25BE%25D0%25B3%25D0%25B5&psig=AOvVaw3IUmNjd0m098Jdl_2RxzfY&ust"
            "=1671723797314000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCMDj0_eGi_wCFQAAAAAdAAAAABAD",
            "tags": ["fun", "dog"],
            "info": "picture"
        }
    )
    meme_id = requests.request(
        'POST',
        f'{domain}/meme',
        headers=headers,
        data=data
    ).json()['id']
    yield meme_id
    requests.request('DELETE', f'{domain}/posts/{meme_id}')
