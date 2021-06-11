import time
from functools import wraps


def time_of_execution(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        t_s = time.time()
        result = func(*args, **kwargs)
        t_e = time.time()
        print(func.__name__, t_e-t_s)
        return result
    return wrapper


@time_of_execution
def count(n: float):
    """Counting Number"""
    while n < 1000:
        n += 1

    print(n)


count(5)
print(count.__name__)
print(count.__doc__)
print(count.__annotations__)


count.__wrapped__(5)
