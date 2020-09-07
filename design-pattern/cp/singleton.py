class Singleton:

    _instance = None
    
    def __new__(cls, *args, **kwds):
        print(f"{cls = }")

        if cls._instance:
            raise Warning("only one instance")


        cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, name, old):
        print('Tao la Singleton.__init__ START')
        self._name = name
        self._old = old
        print('Tao la Singleton.__init__ END')
        print()