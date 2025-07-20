import pytest

from scr.triangle import Triangle

class TestTriangle:

    @pytest.mark.parametrize("side_a, side_b, side_c, area", [
        (3, 4, 5, 6),
        (3.1, 4.2, 5.2, 6.5)],
         ids=["integer", "float"])
    def test_triangle_area_positive(self, side_a, side_b, side_c, area):
        t = Triangle(side_a, side_b, side_c)
        assert round(t.area, 1) == round(area, 1), f"Площадь должна быть равна {round(area, 1)}, но получена {round(t.area, 1)}"

    @pytest.mark.parametrize("side_a, side_b, side_c, perimeter", [
        (3, 4, 5, 12),
        (3.1, 4.2, 5.2, 12.5)],
         ids=["integer", "float"])
    def test_triangle_perimeter_positive(self, side_a, side_b, side_c, perimeter):
        t = Triangle(side_a, side_b, side_c)
        assert round(t.perimeter, 1) == round(perimeter, 1), f"Периметр должен быть равен  {round(perimeter, 1)}, но получен {round(t.perimeter, 1)}"

    @pytest.mark.parametrize("side_a, side_b, side_c", [
        ("abc", 4, 5),
        (3, "def", 5),
        (3, 4, "ghi"),
    ], ids=["string_instead_of_number_a", "string_instead_of_number_b", "string_instead_of_number_c"])
    def test_triangle_invalid_types(self, side_a, side_b, side_c):
        with pytest.raises(TypeError, match="Стороны треугольника должны быть числами"):
            Triangle(side_a, side_b, side_c)

    @pytest.mark.parametrize("side_a, side_b, side_c", [
        (-3, 4, 5),
        (3, -4, 5),
        (3, 4, -5),
        (0, 4, 5),
        (3, 0, 5),
        (3, 4, 0),
    ], ids=["negative_a", "negative_b", "negative_c", "zero_a", "zero_b", "zero_c"])
    def test_triangle_invalid_side_value(self, side_a, side_b, side_c):
        with pytest.raises(ValueError, match="Стороны треугольника должны быть больше 0"):
            Triangle(side_a, side_b, side_c)

    @pytest.mark.parametrize("side_a, side_b, side_c", [
        (1, 2, 10),
        (5, 5, 11),
    ], ids=["invalid_triangle_1", "invalid_triangle_2"])
    def test_triangle_invalid_inequality(self, side_a, side_b, side_c):
        with pytest.raises(ValueError, match="Не выполнено условие неравенства треугольника"):
            Triangle(side_a, side_b, side_c)
