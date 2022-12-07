import pytest


TEST_DATA = ['One', 'Two', 'Three']


@pytest.fixture(scope='session')
def for_all_test():
    print('\nHello to all tests!')
    yield
    print('\nBye-Bye.')


@pytest.fixture(scope='function')
def for_current_test():
    print('\nBefore current test:')
    yield
    print('\nAfter.')


def test_one(for_all_test, for_current_test):
    assert 2 == 2


def test_two(for_current_test):
    assert 3 == 3


def test_three(for_current_test):
    assert 'word' == 'word'


def test_four():
    assert 2 + 2 == 4


def test_five():
    assert 'q' == 'q'


def test_six():
    assert 'six' == 'six'


@pytest.mark.hard
def test_seven():
    assert '123' == '123'


@pytest.mark.slow
def test_eight():
    assert 5 == 5


@pytest.mark.parametrize('word', TEST_DATA)
def test_nine(word):
    assert word == 'Two'


@pytest.mark.skip("Test haven't done yet")
def test_ten():
    assert 'hello' == 'hello'
