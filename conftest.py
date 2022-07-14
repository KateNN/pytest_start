import pytest

from src.Circle import Circle
from src.Square import Square
from src.Rectangle import Rectangle
from src.Triangle import Triangle


@pytest.fixture
def normal_circle():
    return Circle(5)


@pytest.fixture
def normal_square():
    return Square(10)


@pytest.fixture
def normal_rectangle():
    return Rectangle(10, 5)


@pytest.fixture
def normal_triangle():
    return Triangle(13, 14, 15)
