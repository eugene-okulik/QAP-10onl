import pytest


NAMES = ('Elena', 'Anton', 'Evgeniy')


@pytest.mark.parametrize('name', NAMES)
def test_names(name):
    assert name == 'Elena'
