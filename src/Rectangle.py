from src.Figure import Figure


class Rectangle(Figure):
    NAME = "Rectangle"

    def __init__(self, side1, side2):
        if (isinstance(side1, (int, float)) and side1 > 0) and (isinstance(side2, (int, float)) and side2 > 0):
            self.area = side1 * side2
            self.perimeter = side1 * 2 + side2 * 2
        else:
            raise ValueError("Side lengths must be positive numbers")
