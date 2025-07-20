from scr.figure import Figure

class Rectangle(Figure):

    def __init__(self, side_a, side_b):
        if not isinstance(side_a, (int, float)) or not isinstance(side_b, (int, float)):
            raise TypeError("Стороны прямоугольника должны быть числами")
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Стороны прямоугольника должны быть больше 0")
        self.side_a = side_a
        self.side_b = side_b

    @property
    def area(self):
        return self.side_a * self.side_b

    @property
    def perimeter(self):
        return (self.side_a + self.side_b) * 2
