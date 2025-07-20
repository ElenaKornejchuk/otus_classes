import pytest

from scr.circle import Circle

class TestCircle:

    @pytest.mark.parametrize("side_a, area", [
        (3, 28.3),
        (3.5, 38.5)
    ], ids=["integer", "float"])
    def test_circle_area_positive(self, side_a, area):
        c = Circle(side_a)
        assert round(c.area, 1) == round(area, 1), f"Площадь должна быть равна {round(area, 1)}, но получена {round(c.area, 1)}"

    @pytest.mark.parametrize("side_a, perimeter", [
        (3, 18.8),
        (3.5, 22)
    ], ids=["integer", "float"])
    def test_circle_perimeter_positive(self, side_a, perimeter):
        c = Circle(side_a)
        assert round(c.perimeter, 1) == round(perimeter, 1), f"Периметр должен быть равен {round(perimeter, 1)}, но получен {round(c.perimeter, 1)}"

    @pytest.mark.parametrize("radius", [
        ("abc"),
        (None),
    ], ids=["string", "none"])  # Теперь в ids только два элемента
    def test_circle_invalid_type(self, radius):
        with pytest.raises(TypeError, match="Радиус должен быть числом"):
            Circle(radius)

    @pytest.mark.parametrize("radius", [
        (0),
        (-5),
    ], ids=["zero", "negative"])
    def test_circle_invalid_value(self, radius):
        with pytest.raises(ValueError, match="Радиус должен быть больше 0"):
            Circle(radius)