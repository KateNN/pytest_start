from src.Figure import Figure


class Circle(Figure):
    NAME = "Circle"

    def __init__(self, radius):
        if isinstance(radius, (int, float)) and radius > 0:
            self.area = 3.14 * (radius ** 2)
            self.perimeter = 2 * 3.14 * radius
        else:
            raise ValueError("Radius must be a positive number")
