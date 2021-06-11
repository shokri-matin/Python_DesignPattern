from dp05 import Logger

obj1 = Logger()
obj1.file_name = "log1.txt"
obj1.critical("This is a critical message")
print("print obj1: ", obj1)

obj2 = Logger()
obj2.file_name = "log2.txt"
obj2.warning("This is a warning message")
print("print obj1:", obj1)
print("print obj2:", obj2)
