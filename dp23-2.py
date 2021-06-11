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
class FactoryGUI:

    def create_rectangle_object(self, width, height):
        return Rectangle(width, height)

    def create_triangle_object(self, base, altitude):
        return Triangle(base, altitude)


# client code
if __name__ == '__main__':

    Factory = FactoryGUI()
    triangle = Factory.create_triangle_object(base=5, altitude=10)
    triangle.draw()
    print(triangle.area())
