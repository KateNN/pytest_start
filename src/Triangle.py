from src.Figure import Figure


class Triangle(Figure):
    NAME = "Triangle"

    def __init__(self, a, b, c):
        if a + b > c and b + c > a and a + c > b:
            self.a = a
            self.b = b
            self.c = c
        else:
            raise ValueError("Impossible to create a triangle with provided side lengths!")

    @property
    def area(self):
        half_per = (self.a + self.b + self.c) / 2
        return (half_per * (half_per - self.a) * (half_per - self.b) * (half_per - self.c)) ** 0.5

    @property
    def perimeter(self):
        return self.a + self.b + self.c
