class A:
    def __init__(self):
        print("Initialize")

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __call__(self, x, y):
        return x+y


a = A()
print(a(1, 2))












