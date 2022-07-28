import time


def say_hi(func):
    def wrapper(*args):
        print('hi')
        res = func(*args)
        return res

    return wrapper


def timer(func):
    def wrapper(*args):
        s = time.time()
        res = func(*args)
        print(f'耗時: {time.time() - s}')
        return res
    return wrapper
