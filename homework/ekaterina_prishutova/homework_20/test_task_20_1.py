from datetime import datetime
import pytest


@pytest.fixture(scope="session")
def prepare():
    print('before all tests')
    yield None
    print('\nafter all tests')


@pytest.fixture(scope="function")
def fixt_for_func():
    print('before test')
    yield None
    print('\nafter test')


def test_one(prepare, fixt_for_func):
    print('test_one')
    assert 2 == 2


def test_two(prepare, fixt_for_func):
    print('test_two')
    assert 2 == 2


@pytest.mark.simple
def test_three(prepare, fixt_for_func):
    print('test_three')
    assert 2 == 2


@pytest.mark.simple
def test_four(prepare, fixt_for_func):
    print('test_four')
    assert 2 == 2


@pytest.mark.hard
def test_five(prepare, fixt_for_func):
    print('test_five')
    assert 2 == 2


def test_six(prepare, fixt_for_func):
    print('test_six')
    assert 2 == 2


@pytest.mark.skip('Slow UI test')
def test_seven(prepare, fixt_for_func):
    print('test_seven')
    assert 2 == 2


@pytest.mark.skipif(datetime.now().year == 2022, reason='reason')
@pytest.mark.simple
def test_eight(prepare, fixt_for_func):
    print('test_eight')
    assert 2 == 2


def test_nine(prepare, fixt_for_func):
    print('test_nine')
    assert 2 == 2


CREDS = [
    ('cred1', 'pass1'),
    ('cred2', 'pass2'),
    ('cred3', 'pass3')
]


@pytest.mark.hard
@pytest.mark.parametrize('creds', CREDS)
def test_ten(prepare, fixt_for_func, creds):
    print('test_ten')
    print(creds[0], '   ', creds[1])
    assert 2 == 2
