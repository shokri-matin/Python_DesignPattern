from abc import ABC, abstractmethod


# Abstract Product
class Chair(ABC):
    @abstractmethod
    def describe(self):
        pass


class Sofa(ABC):
    @abstractmethod
    def describe(self):
        pass


# Concrete Product
class VictorianChair(Chair):
    def describe(self):
        print("this is a victorian chair")


class ModernChair(Chair):
    def describe(self):
        print("this is a modern chair")


class VictorianSofa(Sofa):
    def describe(self):
        print("this is a victorian chair")


class ModernSofa(Sofa):
    def describe(self):
        print("this is a modern chair")


# Abstract Factory
class Furniture(ABC):

    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_sofa(self):
        pass


class ModernFurniture(Furniture):
    def create_chair(self):
        return ModernChair()

    def create_sofa(self):
        return ModernSofa()


class VictorianFurniture(Furniture):
    def create_chair(self):
        return VictorianChair()

    def create_sofa(self):
        return VictorianSofa()


class FactoryProvider:
    @staticmethod
    def get_factory(config):
        if config == 'V':
            return VictorianFurniture()
        else:
            return ModernFurniture()


# Client
if __name__ == '__main__':
    factory = FactoryProvider.get_factory("V")
    print(factory.create_chair().describe())
