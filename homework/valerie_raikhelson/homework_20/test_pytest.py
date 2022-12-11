from _datetime import datetime
import pytest


@pytest.fixture(scope='session')
def prepare():
    print('Before All')
    yield 'fixture end'
    print('After All')


@pytest.fixture(scope='function')
def when():
    print('Before test')
    yield
    print('After test')


@pytest.mark.simply
def test_one(when):
    print(prepare)
    assert 2 == 2


@pytest.mark.hard
def test_two(when):
    assert 3 == 3


def test_three(when):
    assert 3 == 3


@pytest.mark.skipif(datetime.now().year == 2022, reason='Not supported in 2022')
def test_four(when):
    assert 4 == 4


@pytest.mark.hard
def test_five(when):
    assert 4 == 4


@pytest.mark.simply
def test_six(when):
    assert 4 == 4


@pytest.mark.hard
def test_seven(prepare):
    assert 4 == 4


@pytest.mark.simply
def test_eight(when):
    assert 4 == 4


@pytest.mark.skip('Slow UI test')
def test_nine(when):
    assert 4 == 4


VAL = [
    ('3+1', 4),
    (2 + 2, 4)
]


@pytest.mark.parametrize('values', VAL)
def test_ten(prepare, values):
    test_inp, expected = values
    assert test_inp == expected
