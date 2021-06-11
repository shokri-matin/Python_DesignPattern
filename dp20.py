class A:
    def __init__(self):
        print ("init")

    def __call__(self):
        print("call")

a = A()
a()
