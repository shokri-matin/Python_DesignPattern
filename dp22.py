class A:
    def __new__(cls):
        return 20

a = A()
print(type(a))

print(a)        
