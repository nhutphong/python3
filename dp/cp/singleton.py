from __future__ import annotations
from typing import Optional

class SingletonMeta(type):

    _instance: Optional[Singleton] = None
    def __new__(cls, *args, **kwds): 
        print("Tao la SingletonMeta.__new__")
        # print(f"{cls = }\n{clsname = }\n{bases = }\n{attrs = }")

        instance = super().__new__(cls, *args, **kwds)
        instance._country = 'viet nam'
        instance._city = 'dong nai'

        return  instance

    # type.__call__(cls) return obj
    def __call__(cls) -> Singleton:
        print('tao la SingletonMeta.__call__ ')
        print(f"{cls = }")
        print(f"{cls._instance = }")

        if cls._instance is None:
            cls._instance = super().__call__() # = Singleton()

        return cls._instance


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        print(f"{self = }")


class Base:

    note = """
        base = Base('dung', 28)
        run __new__ roi toi __init__
        __
    """
    def __new__(cls): 
        print("Tao la Base.__new__")
        print(f"{cls = }")

        self = super().__new__(cls)
        self._country = 'VIET NAM' #instance attr chung cho tat ca instances
        print(f"{self = }")

        return self #bat buoc doi call __init__

    def __init__(self, name, old):
        print('Tao la Base.__init__')
        self._name = name
        self._old = old