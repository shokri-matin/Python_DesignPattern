from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def draw(self):
        print("rectangle is drawn!")


class Triangle(Shape):

    def __init__(self, base, altitude):
        self.base = base
        self.altitude = altitude

    def area(self):
        return (self.base * self.altitude)/2

    def draw(self):
        print("Triangle is drawn!")


# Shape Factory
class GUIFactory(ABC):

    @abstractmethod
    def get_shape(self):
        pass


class GUIRectangle(GUIFactory):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_shape(self):
        return Rectangle(self.width, self.height)


class GUITriangle(GUIFactory):

    def __init__(self, base, altitude):
        self.base = base
        self.altitude = altitude

    def get_shape(self):
        return Triangle(self.base, self.altitude)


# client code
if __name__ == '__main__':
    rectangle = GUIRectangle(100, 50).get_shape()
    print(rectangle.area())
