import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


def test_add(calc):
    assert calc.add(10, 5) == 15
    assert calc.add(-1, -1) == -2
    assert calc.add(-1, 1) == 0
