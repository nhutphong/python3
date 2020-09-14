"""Clean Code in Python - Chapter 5: Decorators

> Separation of Concerns (SoC).
    Break a coupled decorator into smaller ones.
"""
import functools
import time

import logging


def traced_function(function):
    @functools.wraps(function)
    def wrapped(*args, **kwargs):
        logging.info("started execution of %s", function.__qualname__)
        start_time = time.time()
        result = function(*args, **kwargs)
        logging.info(
            "function %s took %.2fs",
            function.__qualname__,
            time.time() - start_time,
        )
        return result

    return wrapped


@traced_function
def operation1():
    time.sleep(2)
    logging.info("running operation 1")
    return 2