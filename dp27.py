from abc import ABC, abstractmethod


class AbstractSubject(ABC):
    @abstractmethod
    def get_picture(self, id):
        pass


class RealSubject(AbstractSubject):

    def __init__(self):
        self.pictures = []
        print('Real Subject is required')

    def get_picture(self, id):
        for i in range(10):
            if i % id:
                self.pictures.append(i)
        return self.pictures


class Proxy(AbstractSubject):

    Cache = {}

    def __init__(self):
        self.Cache = {}

    def get_picture(self, id):

        if self.Cache.get(id) is None:
            pictures = RealSubject().get_picture(id)
            self.Cache.update({id: pictures})
        else:
            print('this request is responded from cache')
        return self.Cache.get(id)


# Client
ProxyObj = Proxy()
picture1 = ProxyObj.get_picture(1)
picture2 = ProxyObj.get_picture(2)
picture3 = ProxyObj.get_picture(1)
picture4 = ProxyObj.get_picture(2)
