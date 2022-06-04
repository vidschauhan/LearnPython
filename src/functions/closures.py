# Created by vidit.singh at 19-05-2022

import logging

logging.basicConfig(filename='src.functions',
                    level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__,
                                                    args))
        print(func(*args))

    return log_func


def add(x, y):
    return x + y


def sub(a, b):
    return a - b


add_logger = logger(add)
sub_logger = logger(sub)

add_logger(18, 2)
sub_logger(10, 3)
