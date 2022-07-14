from src.Figure import Figure


class Square(Figure):
    NAME = "Square"

    def __init__(self, side):
        if isinstance(side, (int, float)) and side > 0:
            self.area = side ** 2
            self.perimeter = side * 4
        else:
            raise ValueError("Side length must be a positive number")
