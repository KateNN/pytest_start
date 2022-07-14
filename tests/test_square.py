import pytest

from src.Square import Square


def test_square_creation_normal():
    """Check creating a square with side = 4 (positive number)"""
    Square(4)


def test_square_creation_negative_side():
    """Side cannot be a negative number"""
    with pytest.raises(ValueError):
        Square(-2)


def test_square_creation_wrong_value_side():
    """Side cannot be a list"""
    with pytest.raises(ValueError):
        Square([1, 3, 5])


def test_square_perimeter_calculation():
    """Verify that the perimeter is calculated correctly by side * 4 formula"""
    square = Square(3)
    assert square.perimeter == 3 * 4


def test_square_area_calculation():
    """Verify that the area is calculated correctly by side ** 2 formula"""
    square = Square(7)
    assert square.area == 7 ** 2


def test_square_name(normal_square):
    """Check that created square has 'Square' name"""
    assert normal_square.NAME == 'Square'


def test_adding_two_squares(normal_square):
    """Check that add_area function works correctly"""
    square = Square(12)
    assert square.add_area(normal_square) == square.area + normal_square.area
