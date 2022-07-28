import functools
import logging
import time

dev_logger = logging.getLogger(name='dev')
handler = logging.StreamHandler()

dev_logger.setLevel(logging.INFO)
dev_logger.addHandler(handler)


def say_hi(func):
    print(f'開始執行say_hi')

    def wrapper(*args):
        print(f'開始執行say_hi的wrapper')
        print('hi')
        res = func(*args)
        return res

    return wrapper


def timer(func):
    print(f'開始執行timer')

    def wrapper(*args):
        print(f'開始執行timer的wrapper')
        s = time.time()
        res = func(*args)
        print(f'耗時: {time.time() - s}')
        return res

    return wrapper


def logger(message: str):
    print(f'開始執行logger')

    def logging_decorator(func):
        print(f'開始執行logging_decorator')

        @functools.wraps(func)
        def wrapper(*args):
            print(f'開始執行logger的wrapper')
            dev_logger.info(f'開始執行{message}')
            res = func(*args)
            return res

        return wrapper

    return logging_decorator
