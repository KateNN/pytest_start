from src.Rectangle import Rectangle


def test_rectangle_creation():
    """Check creating a rectangle with sides 3 and 6"""
    Rectangle(3, 6)


def test_rectangle_perimeter_calculation():
    """Verify that the perimeter is calculated correctly by side1 * 2 + side2 * 2 formula"""
    rectangle = Rectangle(3, 7)
    assert rectangle.perimeter == 3 * 2 + 7 * 2


def test_rectangle_area_calculation():
    """Verify that the area is calculated correctly by side1 * side2 formula"""
    rectangle = Rectangle(8, 4)
    assert rectangle.area == 8 * 4


def test_rectangle_name(normal_rectangle):
    """Check that created rectangle has 'Rectangle' name"""
    assert normal_rectangle.NAME == 'Rectangle'


def test_adding_two_rectangles(normal_rectangle):
    """Check that add_area function works correctly"""
    rectangle = Rectangle(20, 7)
    assert rectangle.add_area(normal_rectangle) == rectangle.area + normal_rectangle.area
