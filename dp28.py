from abc import ABC, abstractmethod


class Color(ABC):
    @abstractmethod
    def describe(self):
        pass


class Blue(Color):
    def describe(self):
        return 'Blue'


class Red(Color):
    def describe(self):
        return 'Red'


class Shape(ABC):

    def __init__(self, color):
        self.color = color

    @abstractmethod
    def describe(self):
        pass


class Square(Shape):
    def describe(self):
        print("{0} Square".format(self.color.describe()))


class Triangle(Shape):
    def describe(self):
        print("{0} Triangle".format(self.color.describe()))


blue = Blue()
t = Triangle(blue)
t.describe()
