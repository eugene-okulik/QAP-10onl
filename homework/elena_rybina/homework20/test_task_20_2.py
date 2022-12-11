import pytest


@pytest.fixture(scope='session')
def action():
    print('before all')
    yield
    print('after all')


def test_one(action):
    assert 1+1 == 2


def test_two():
    assert 2+2 == 4


def test_three():
    assert 3+3 == 8


def test_four():
    assert 4+4 == 8
