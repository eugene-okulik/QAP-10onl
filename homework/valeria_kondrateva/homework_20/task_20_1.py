import pytest


@pytest.fixture(scope='session')
def all_testing_sessions():
    print('before all')
    yield
    print('after all')


@pytest.fixture(scope='function')
def one_test():
    print('before')
    yield
    print('after')


@pytest.mark.simple
def test_one(all_testing_sessions, one_test):
    assert 2 == 2


def test_two(one_test):
    assert 1 + 1 == 2


NUMS = [
    ('1', '2'),
    ('3', '4'),
    ('5', '6')
]


@pytest.mark.parametrize('nums', NUMS)
def test_three(one_test, nums):
    a, b = nums
    assert a + b == 3


def test_four(one_test):
    assert 2 + 2 == 4


@pytest.mark.hard
def test_five(one_test):
    assert 4 == 4


def test_six(one_test):
    assert 4 + 4 == 8


def test_seven(one_test):
    assert 8 == 8


def test_eight(one_test):
    assert 8 + 8 == 16


def test_nine(one_test):
    assert 9 + 9 == 18


@pytest.mark.skip('Slow UI test')
def test_ten(one_test):
    assert 10 + 10 == 20
