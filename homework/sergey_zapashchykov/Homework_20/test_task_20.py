import pytest


TEST_DATA = ['one', 'two', 'ten']


@pytest.mark.simple
def test_one(function_before_after, session_before_after):
    assert 1 == 1


@pytest.mark.hard
def test_two(function_before_after):
    assert 'two' == 'two'


@pytest.mark.skip('Skip reason for test')
def test_three(function_before_after):
    assert 3 == 3


@pytest.mark.hard
def test_four(function_before_after):
    assert 'four' == 'four'


@pytest.mark.simple
def test_five(function_before_after):
    assert 5 == 5


@pytest.mark.hard
def test_six(function_before_after):
    assert 'six' == 'six'


@pytest.mark.simple
def test_seven(function_before_after):
    assert 7 == 7


@pytest.mark.hard
def test_eight(function_before_after):
    assert 'eight' == 'eight'


@pytest.mark.simple
def test_nine(function_before_after):
    assert 9 == 9


@pytest.mark.parametrize('num', TEST_DATA)
def test_ten(function_before_after, num):
    assert num == 'ten'
