class Logger:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance


s1 = Logger()
print("obj created ", s1)
s2 = Logger()
print("obj created ", s2)
