class Figure:
    NANE = None
    area = None
    perimeter = None

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.area + figure.area
        else:
            raise ValueError("The function argument provided is not a figure!")
