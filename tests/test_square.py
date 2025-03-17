import pytest

from scr.Square import Square

class TestSquare:
    @pytest.mark.parametrize("side_a, area", [
        (3, 9),
        (3.5, 12.25)],
         ids=["integer", "float"])
    def test_square_area_positive(self, side_a, area):
        s = Square(side_a)
        assert s.area == area,f"Площадь должна быть равна {area}, но получена {s.area}"

    @pytest.mark.parametrize("side_a, perimeter", [
        (3, 12),
        (3.5, 14)],
                             ids=["integer", "float"])
    def test_square_perimeter_positive(self, side_a, perimeter):
        s = Square(side_a)
        assert s.perimeter == perimeter, f"Периметр должен быть равен {perimeter}, но получен {s.perimeter}"

    @pytest.mark.parametrize("side_a", [
        "abc",
    ], ids=["non_numeric"])
    def test_square_invalid_type(self, side_a):
        with pytest.raises(TypeError, match="Сторона квадрата должна быть числом"):
            Square(side_a)

    @pytest.mark.parametrize("side_a", [
        0,
        -1,
    ], ids=["zero", "negative"])
    def test_square_invalid_value(self, side_a):
        with pytest.raises(ValueError, match="Стороны квадрата должны быть больше 0"):
            Square(side_a)