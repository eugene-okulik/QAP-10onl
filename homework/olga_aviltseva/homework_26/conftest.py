import pytest
import requests
import constants
import endpoints.apiclient as clients


@pytest.fixture(scope='session')
def domain():
    return constants.DOMAIN


@pytest.fixture(scope='session')
def client(domain):
    return clients.ApiClient()


@pytest.fixture(scope='function')
def add_meme2(client):
    add_response = client.add_meme("Test text")

    yield add_response['text']
    requests.request('DELETE', f'{domain}/meme/{add_response["id"]}')


@pytest.fixture(scope='function')
def add_meme(client):
    return client.add_meme("Test text")
