import pytest

from src.Triangle import Triangle


def test_triangle_creation_normal():
    """Check creating a triangle with sides 3, 6, 5 (positive numbers)"""
    Triangle(3, 6, 5)


def test_triangle_creation_impossible_triangle():
    """Check that the sum of 2 sides cannot be less than the 3d side"""
    with pytest.raises(ValueError):
        Triangle(1, 3, 6)


def test_triangle_perimeter_calculation():
    """Verify that the perimeter is calculated correctly by side1 + side2 * side3 formula"""
    triangle = Triangle(10, 12, 17)
    assert triangle.perimeter == 10 + 12 + 17


def test_triangle_area_calculation():
    """Verify that the area is calculated correctly by Heron's formula"""
    triangle = Triangle(4, 6, 8)
    assert triangle.area == (9 * (9 - 4) * (9 - 6) * (9 - 8)) ** 0.5


def test_triangle_name(normal_triangle):
    """Check that created triangle has 'Triangle' name"""
    assert normal_triangle.NAME == 'Triangle'


def test_adding_two_triangles(normal_triangle):
    """Check that add_area function works correctly"""
    triangle = Triangle(22, 25, 28)
    assert triangle.add_area(normal_triangle) == triangle.area + normal_triangle.area
