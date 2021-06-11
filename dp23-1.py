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


if __name__ == '__main__':
    rec = Rectangle(10, 10)
    print(rec.area())
