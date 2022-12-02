import pytest
import sys
import random


KEYS = list(
    (idx, num) for idx, num in enumerate(random.choices(range(10), k=10))
)


@pytest.fixture(scope='session')
def print_for_all():
    print('############\nBefore all\n############')
    yield None
    print('##########\nAfter all\n##########')


@pytest.fixture(scope='function')
def print_for_each():
    print('Start current TEST')
    yield None
    print('\nStop current TEST')


@pytest.mark.smoke
def test_one(print_for_all, print_for_each):
    assert True is True


@pytest.mark.simple
def test_two(print_for_each):
    assert 2 + 2 == 4


@pytest.mark.simple
def test_three(print_for_each):
    assert 2 + 3 >= 5


def test_four(print_for_each):
    assert '123456' == 123456


def test_five(print_for_each):
    assert isinstance([], set)


@pytest.mark.skipif(sys.platform == 'win32', reason="Requires sys.platform Unix")
def test_six(print_for_each):
    assert 8 * 8. == 64.


def test_seven(print_for_each):
    assert len([1, 2, 3, 4]) == 4


@pytest.mark.hard
def test_eight(print_for_each):
    assert int('123') == abs(-123)


def test_nine(print_for_each):
    assert sys.version.startswith('3.10')


@pytest.mark.hard
def test_ten(print_for_each):
    assert -1 * False is 0 * 0


@pytest.mark.parametrize('keys', KEYS)
def test_args(print_for_each, keys):
    a, b = keys
    assert isinstance(a + b, int)
