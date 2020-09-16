"""Clean Code in Python - Chapter 9: Common Design Patterns

> Monostate Pattern
"""

from log import logger


class SharedAttribute:
    init = 0
    set_name = 0

    def __init__(self, initial_value=None):
        type(self).init+=1

        print(f"__init__ {type(self).init}")
        self.value = initial_value
        self._name = None

    def __set_name__(self, owner, name):
        type(self).set_name+=1

        print(f"__set_name__ {type(self).set_name}")
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.value is None:
            raise AttributeError(f"{self._name} was never set")
        return self.value

    def __set__(self, instance, new_value):
        self.value = new_value



class GitFetcher:

    current_tag = SharedAttribute()
    current_branch = SharedAttribute()

    def __init__(self, tag, branch=None):
        self.current_tag = tag
        self.current_branch = branch

    def pull(self):
        logger.info("pulling from %s", self.current_tag)
        return self.current_tag