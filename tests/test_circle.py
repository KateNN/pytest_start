from src.Circle import Circle


def test_circle_creation():
    """Check creating a circle with radius = 4"""
    Circle(4)


def test_circle_perimeter_calculation():
    """Verify that the perimeter is calculated correctly by 2 * Pi * r formula"""
    circle = Circle(3)
    assert circle.perimeter == 2 * 3.14 * 3


def test_circle_area_calculation():
    """Verify that the area is calculated correctly by Pi * r ** 2 formula"""
    circle = Circle(17)
    assert circle.area == 3.14 * (17 ** 2)


def test_circle_name(normal_circle):
    """Check that created circle has 'Circle' name"""
    assert normal_circle.NAME == 'Circle'


def test_adding_two_circles(normal_circle):
    """Check that add_area function works correctly"""
    circle = Circle(6)
    assert circle.add_area(normal_circle) == circle.area + normal_circle.area
