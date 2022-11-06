"""Clean Code in Python - Chapter 5: Decorators

> Undesired side effects on decorators
"""

import time
from functools import wraps
import logging


def traced_function_wrong(function):
    """An example of a badly defined decorator."""
    logging.debug("started execution of %s", function)
    start_time = time.time()

    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        logging.info(
            "function %s took %.2fs", function, time.time() - start_time
        )
        return result

    return wrapper


@traced_function_wrong
def process_with_delay(callback, delay=0):
    logging.info("sleep(%d)", delay)
    return callback


def traced_function(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        logging.info("started execution of %s", function)
        start_time = time.time()
        result = function(*args, **kwargs)
        logging.info(
            "function %s took %.2fs", function, time.time() - start_time
        )
        return result

    return wrapper


@traced_function
def call_with_delay(callback, delay=0):
    logging.info("sleep(%d)", delay)
    return callback