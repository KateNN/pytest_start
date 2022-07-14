from src.Figure import Figure


class Triangle(Figure):
    NAME = "Triangle"

    def __init__(self, side1, side2, side3):
        if (isinstance(side1, (int, float)) and side1 > 0) and (
                isinstance(side2, (int, float)) and side2 > 0) and isinstance(side3, (int, float)) and side3 > 0:
            if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
                self.perimeter = side1 + side2 + side3
                self.half_perimeter = (side1 + side2 + side3) / 2
                self.area = (self.half_perimeter * (self.half_perimeter - side1) * (self.half_perimeter - side2) * (
                        self.half_perimeter - side3)) ** 0.5
            else:
                raise ValueError("Impossible to create a triangle with provided side lengths!")
