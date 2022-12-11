import pytest


@pytest.mark.simple
def test_one():
    assert 1 + 1 == 2


@pytest.mark.hard
def test_two():
    assert 3 + 3 == 7


@pytest.mark.simple
def test_three():
    assert 2 + 2 == 4
