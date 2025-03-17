from scr.rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, side_a):
        if not isinstance(side_a, (int, float)):  # Проверка на числовой тип
            raise TypeError("Сторона квадрата должна быть числом")
        if side_a <= 0:
            raise ValueError("Стороны квадрата должны быть больше 0")
        super().__init__(side_a, side_a)
