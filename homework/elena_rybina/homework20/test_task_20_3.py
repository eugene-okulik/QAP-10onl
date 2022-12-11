import pytest


@pytest.fixture(scope='function')
def action():
    print('Hi-hi')
    yield
    print('Bye-bye')


def test_one(action):
    assert 1 + 1 == 2


def test_two(action):
    assert 2 + 2 == 4


def test_three(action):
    assert 3 + 3 == 8


def test_four(action):
    assert 4 + 4 == 8
