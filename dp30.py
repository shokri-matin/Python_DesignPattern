from abc import ABC, abstractmethod


# Command
class Order(ABC):
    @abstractmethod
    def execute(self):
        pass


# Concrete Command
class Sell(Order):

    def __init__(self, stock_trader):
        self.stoke_trader = stock_trader

    def execute(self):
        self.stoke_trader.sell()


class Buy(Order):

    def __init__(self, stock_trader):
        self.stoke_trader = stock_trader

    def execute(self):
        self.stoke_trader.buy()


# Receiver
class StockTrader:
    def buy(self):
        print("You will buy stocks")

    def sell(self):
        print("You will sell stocks")


# Invoker
class Agent:

    def __init__(self):
        self.OrderQueue = []

    def place_order(self, order):
        self.OrderQueue.append(order)
        order.execute()


# Client
if __name__ == '__main__':

    stock = StockTrader()
    buyStock = Buy(stock)
    sellStock = Sell(stock)
    # Invoker
    agent = Agent()
    agent.place_order(buyStock)
    agent.place_order(sellStock)
