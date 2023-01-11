import pytest

DOMAIN = 'https://jsonplaceholder.typicode.com'


@pytest.fixture(scope='function')
def domain():
    return DOMAIN
