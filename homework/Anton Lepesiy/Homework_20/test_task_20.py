from datetime import datetime
import pytest

PARAMETERS_DATA = [1, 2, 4]


@pytest.fixture(scope='session')
def before_after_all():
    print('\nTesting is running')
    yield
    print('\n\nTesting has finished')


@pytest.fixture()
def before_after():
    print('\ntesting....')
    yield
    print('\n....done!', end='')


@pytest.mark.simple
def test_one(before_after, before_after_all):
    assert 1 == 1


@pytest.mark.simple
def test_two(before_after):
    assert 'I am' is 'I am'


@pytest.mark.simple
def test_tree(before_after):
    assert type('text') is str


@pytest.mark.simple
def test_four(before_after):
    assert True is True


@pytest.mark.hard
def test_five(before_after):
    assert 'a' + 'b' == 'ab'


@pytest.mark.hard
def test_six(before_after):
    assert type(1 + 3) is int


@pytest.mark.hard
def test_seven(before_after):
    assert bool('Истина в пиве') is True


@pytest.mark.skip('Пропускаю бессмысленное')
def test_eight(before_after):
    assert bool('эта бессмыcлица уже надоела') is True


@pytest.mark.skipif(datetime.now().year == 2022, reason='not for 2022')
@pytest.mark.simple
def test_ten(before_after):
    assert bool(2023) is False


@pytest.mark.parametrize('number', PARAMETERS_DATA)
def test_nine(before_after, number):
    assert number is not 3, 'number can\'t be \"3\"'
