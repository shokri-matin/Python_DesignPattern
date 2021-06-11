class A(object):
    pass


class B(type):
    pass


class C(metaclass=B):
    pass
