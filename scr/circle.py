from scr.figure import Figure

class Circle(Figure):
    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("Радиус должен быть числом")
        if radius <= 0:
            raise ValueError("Радиус должен быть больше 0")
        self.radius = radius

    @property
    def perimeter(self):
        pi = 3.14159
        return 2 * pi * self.radius

    @property
    def area(self):
        pi = 3.14159
        return pi * self.radius ** 2

