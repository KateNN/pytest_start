import pytest


def test_adding_square_and_triangle_areas(normal_square, normal_triangle):
    """Check that add_area function works correctly for different figures"""
    assert normal_square.add_area(normal_triangle) == normal_square.area + normal_triangle.area


def test_adding_circle_and_square_areas(normal_circle, normal_square):
    """Check that add_area function works correctly for different figures"""
    assert normal_circle.add_area(normal_square) == normal_circle.area + normal_square.area


def test_adding_rectangle_and_triangle_areas(normal_rectangle, normal_triangle):
    """Check that add_area function works correctly for different figures"""
    assert normal_rectangle.add_area(normal_triangle) == normal_rectangle.area + normal_triangle.area


def test_adding_not_figure_string(normal_circle):
    """Check that add_area function raises ValueError if not a figure used as argument (string)"""
    with pytest.raises(ValueError):
        normal_circle.add_area("Something strange")


def test_adding_not_figure_number(normal_triangle):
    """Check that add_area function raises ValueError if not a figure used as argument (number)"""
    with pytest.raises(ValueError):
        normal_triangle.add_area(35)
