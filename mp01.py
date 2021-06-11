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
def count(n):
    while n < 10000000:
        n += 1


count(5)
