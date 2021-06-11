class A:
    def __init__(self, a, b, c):
        pass

v = A(1, 2, 3)

class B:
    def __call__(self, a, b, c):
        pass

n = B()
n(1, 2, 3)
