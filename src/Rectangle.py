from src.Figure import Figure


class Rectangle(Figure):
    NAME = "Rectangle"

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    @property
    def perimeter(self):
        return self.a * 2 + self.b * 2
