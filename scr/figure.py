from abc import ABC, abstractmethod

class Figure(ABC):

    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Не является объектом или экземпляром класса Figure или его подкласса.")

        return self.area + other_figure.area
