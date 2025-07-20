from scr.figure import Figure

class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if not isinstance(side_a, (int, float)) or not isinstance(side_b, (int, float)) or not isinstance(side_c,(int, float)):
            raise TypeError("Стороны треугольника должны быть числами")
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Стороны треугольника должны быть больше 0")
        if not (side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a):
            raise ValueError("Не выполнено условие неравенства треугольника")

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    @property
    def area(self):
        p = self.perimeter / 2
        return (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0.5
