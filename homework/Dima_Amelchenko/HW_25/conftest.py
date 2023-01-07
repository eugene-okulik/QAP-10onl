import pytest


DOMAIN = 'http://167.172.172.115:52355'
TOKEN = 'TtezNG3Zq8La1zB'


@pytest.fixture(scope='function')
def domain():
    return DOMAIN


@pytest.fixture(scope='function')
def token():
    return TOKEN
