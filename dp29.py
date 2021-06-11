from abc import ABC, abstractmethod


# Publisher
class Publisher:

    def __init__(self):
        self.__subscribers = []
        self.__contents = []

    def subscribe(self, subscriber):
        self.__subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def subscribers(self):
        return self.__subscribers

    def notify_subscriber(self):
        for sub in self.__subscribers:
            sub.notify()

    def add_content(self, news):
        self.__contents.append(news)

    def get_content(self):
        return self.__contents


# Observer
class Observer(ABC):
    @abstractmethod
    def notify(self):
        pass


# Concrete Observer
class AdminSubscriber(Observer):

    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.subscribe(self)

    def notify(self):
        print(self.publisher.get_content())


# Concrete Observer
class UserSubscriber(Observer):

    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.subscribe(self)

    def notify(self):
        print(self.publisher.get_content())


if __name__ == '__main__':
    publisher = Publisher()
    subscriber1 = UserSubscriber(publisher)
    subscriber2 = AdminSubscriber(publisher)
    print("\n", publisher.subscribers())

    publisher.add_content("Hello my subscribers")
    publisher.notify_subscriber()
