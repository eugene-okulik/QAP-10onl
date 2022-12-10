from datetime import datetime
import pytest


@pytest.fixture(scope='session')
def all_test():
    print('Before all test')
    yield
    print(' After all test')


@pytest.fixture(scope='function')
def each_test():
    print('Before test', end=' ')
    yield
    print(' After test', end='')


@pytest.mark.simple
def test_one(all_test, each_test):
    assert 1 == 1


@pytest.mark.hard
def test_two(each_test):
    assert 2 != 1, '1 is not 2'


@pytest.mark.simple
def test_three(each_test):
    assert bool(3) is True


@pytest.mark.hard
def test_four(each_test):
    assert 4 < 5


def test_five(each_test):
    assert - 5 < 5


TEST_DATA = [
    (1, 1),
    (2, 2),
    (3, 3)
]


@pytest.mark.parametrize('test_data', TEST_DATA)
def test_six(each_test, test_data):
    a, b = test_data
    assert a == b


@pytest.mark.skipif(datetime.now().month == 12, reason='Not supported in December')
def test_seven(each_test):
    assert 7 == 7


def test_eight(each_test):
    assert 8 is 8


def test_nine(each_test):
    assert 4 is not 9


def test_ten(each_test):
    assert 10 - 10 == 0
