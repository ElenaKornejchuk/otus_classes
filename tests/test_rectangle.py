import pytest

from scr.rectangle import Rectangle

class TestRectangle:

    @pytest.mark.parametrize("side_a, side_b, area", [
        (3, 5, 15),
        (3.5, 5.5, 19.25)
    ],
         ids=["integer", "float"])
    def test_rectangle_area_positive(self, side_a, side_b, area):
        r = Rectangle(side_a, side_b)
        assert r.area == area,f"Площадь должна быть равна {side_a * side_b}"

    @pytest.mark.parametrize("side_a, side_b, perimeter", [
        (3, 5, 16),
        (3.5, 5.5, 18)
    ],
         ids=["integer", "float"])
    def test_rectangle_perimeter_positive(self, side_a, side_b, perimeter):
        r = Rectangle(side_a, side_b)
        assert r.perimeter == perimeter,f"Периметр должен быть равен {(side_a + side_b) * 2}"

    @pytest.mark.parametrize("side_a, side_b", [
        ("abc", 5),
        (5, "def"),
        (None, 5),
    ], ids=["string_instead_of_number_a", "string_instead_of_number_b", "none_instead_of_number_a"])
    def test_rectangle_invalid_type(self, side_a, side_b):
        with pytest.raises(TypeError, match="Стороны прямоугольника должны быть числами"):
            Rectangle(side_a, side_b)

    @pytest.mark.parametrize("side_a, side_b", [
        (0, 5),
        (-1, 5),
        (5, 0),
        (5, -3),
        (-5, -3),
    ], ids=["zero_a", "negative_a", "zero_b", "negative_b", "negative_both"])
    def test_rectangle_invalid_values(self, side_a, side_b):
        with pytest.raises(ValueError, match="Стороны прямоугольника должны быть больше 0"):
            Rectangle(side_a, side_b)
