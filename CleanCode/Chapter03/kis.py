"""Clean Code in Python - Chapter 3: General traits of good code

> Keep It Simple
"""


class ComplicatedNamespace:
    """An convoluted example of initializing an object with some properties.

    >>> cn = ComplicatedNamespace.init_with_data(
    ...    id_=42, user="root", location="127.0.0.1", extra="excluded"
    ... )
    >>> cn.id_, cn.user, cn.location
    (42, 'root', '127.0.0.1')

    >>> hasattr(cn, "extra")
    False

    """

    ACCEPTED_VALUES = ("id_", "user", "location")

    @classmethod
    def init_with_data(cls, **data):
        self = cls()
        
        for key, value in data.items():
            if key in cls.ACCEPTED_VALUES:
                setattr(self, key, value)
                # chi accept 3 item trong ACCEPTED_VALUES lam attrs
                
        return self


class Namespace:
    """Create an object from keyword arguments.

    >>> cn = Namespace(
    ...    id_=42, user="root", location="127.0.0.1", extra="excluded"
    ... )
    >>> cn.id_, cn.user, cn.location
    (42, 'root', '127.0.0.1')

    >>> hasattr(cn, "extra")
    False
    """

    ACCEPTED_VALUES = ("id_", "user", "location")

    def __init__(self, **data):
        accepted_data = {
            k: v for k, v in data.items() if k in self.ACCEPTED_VALUES
        }
        
        self.__dict__.update(accepted_data)
