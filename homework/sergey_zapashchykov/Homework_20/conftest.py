import pytest


@pytest.fixture(scope='session', autouse=True)
def session_before_after():
    print(' - Before all')
    yield None
    print(' - After all')


@pytest.fixture(scope='function')
def function_before_after():
    print(' - Before test')
    yield None
    print(' - After test')
