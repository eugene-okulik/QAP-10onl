import pytest


@pytest.fixture(scope='session')
def before_after_all():
    print('before all')
    yield
    print('after all')


@pytest.fixture()
def before_after():
    print('before')
    yield
    print('after')


@pytest.mark.simple
def test_one(before_after_all, before_after):
    assert 1 + 0 == 1


def test_two(before_after):
    assert 1 + 1 == 2


def test_three(before_after):
    assert 1 + 2 == 3


def test_four(before_after):
    assert 1 + 3 == 4


def test_five(before_after):
    assert 1 + 4 == 5


@pytest.mark.hard
def test_six(before_after):
    assert 1 + 5 == 6


@pytest.mark.skip('need to refactor this test')
def test_seven(before_after):
    assert 1 + 6 == 7


@pytest.mark.hard
def test_eight(before_after):
    assert 1 + 7 == 8


NUMBERS = [
    (5, 4),
    (3, 6),
    (1, 8)
]


@pytest.mark.parametrize('numbers', NUMBERS)
def test_nine(before_after, numbers):
    a, b = numbers
    assert a + b == 9


@pytest.mark.simple
def test_ten(before_after):
    assert 10 - 0 == 10
