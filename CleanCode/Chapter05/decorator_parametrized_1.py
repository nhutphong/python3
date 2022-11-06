"""Clean Code in Python - Chapter 5: Decorators

Parametrized decorators using functions
"""

from functools import wraps

from decorator_function_1 import ControlledException
import logging


RETRIES_LIMIT = 3


def with_retry(retries_limit=RETRIES_LIMIT, allowed_exceptions=None):
    allowed_exceptions = allowed_exceptions or (ControlledException,)

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_raised = None
            for _ in range(retries_limit):
                try:
                    return func(*args, **kwargs)
                except allowed_exceptions as e:
                    logging.warning(
                        "retring %s due to %s", func.__qualname__, e
                    )
                    last_raised = e
            raise last_raised

        return wrapper

    return decorator


@with_retry()
def run_operation(task):
    return task.run()


@with_retry(retries_limit=5)
def run_with_custom_retries_limit(task):
    return task.run()


@with_retry(allowed_exceptions=(AttributeError,))
def run_with_custom_exceptions(task):
    return task.run()


@with_retry(
    retries_limit=4, allowed_exceptions=(ZeroDivisionError, AttributeError)
)
def run_with_custom_parameters(task):
    return task.run()