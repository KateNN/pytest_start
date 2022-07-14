from src.Figure import Figure


class Square(Figure):
    NAME = "Square"

    def __init__(self, a):
        self.a = a

    @property
    def area(self):
        return self.a ** 2

    @property
    def perimeter(self):
        return self.a * 4
