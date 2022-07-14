from src.Figure import Figure


class Circle(Figure):
    NAME = "Circle"

    def __init__(self, r):
        self.r = r

    @property
    def area(self):
        return 3.14 * (self.r ** 2)

    @property
    def perimeter(self):
        return 2 * 3.14 * self.r
