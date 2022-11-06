class Human(object):

    """Docstring for Human. """
    OK = 'OK'
    YES = 'YES'

    def __init__(self):
        """TODO: to be defined. """
        self.one = 'one'
        self.two = 'two'

    def method1(self):
        pass

    def method2(self):
        pass


human = Human()
print(f"{human.__dict__ = }\n")
print(f"{Human.__dict__ = }\n")
print(f"{global() = }\n")
print(f"{locals() = }\n")
print(f"{vars() = }\n")