import logging
import time

dev_logger = logging.getLogger(name='dev')
handler = logging.StreamHandler()

dev_logger.setLevel(logging.INFO)
dev_logger.addHandler(handler)


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


def logger(message: str):
    def logging_decorator(func):
        def wrapper(*args):
            dev_logger.info(f'開始執行{message}')
            res = func(*args)
            return res

        return wrapper

    return logging_decorator
