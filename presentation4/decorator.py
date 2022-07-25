def say_hi(func):
    def wrapper(*args):
        print('hi')
        res = func(*args)
        return res

    return wrapper


def hi(func):
    print('hi')
    return func
