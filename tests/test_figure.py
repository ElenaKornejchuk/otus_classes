import pytest

from scr.circle import Circle
from scr.rectangle import Rectangle
from scr.square import Square
from scr.triangle import Triangle

class TestFigure:

    @pytest.mark.parametrize("figure1, figure2, expected_area", [
        (Rectangle(3, 4), Square(5), 37),
        (Circle(3), Triangle(3, 4, 5), round(Circle(3).area + Triangle(3, 4, 5).area, 2)),
        (Square(4), Triangle(6, 8, 10), 40)
    ], ids=["rectangle_square", "circle_triangle", "square_triangle"])
    def test_add_area(self, figure1, figure2, expected_area):
        assert round(figure1.add_area(figure2), 2) == expected_area, \
            f"Ошибка при сложении площади {type(figure1).__name__} и {type(figure2).__name__}"

    @pytest.mark.parametrize("figure1, figure2", [
        (Rectangle(3, 4), "Triangle"),  # Строка вместо фигуры
        (Circle(3), None),
        (Square(4), 123),
    ], ids=["string", "none", "integer"])
    def test_add_area_invalid_type(self, figure1, figure2):
        with pytest.raises(ValueError, match="Не является объектом или экземпляром класса Figure или его подкласса."):
            figure1.add_area(figure2)