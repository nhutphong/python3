"""
    DATA MODEL, BASIC CUTOMIZATION
    Special method

"""
__IMPORTANT__="""

    khi định nghĩa 1 Class nếu chúng ta override 3 hàm này:
    __getattribute__(self, attr), __getattr__(self, attr),
    __setattr__(self, attr, value) thì phải chú ý
    khi tạo instance=class() thì run __init__()  gặp 10 attrs trong đó sẽ run __settatr__() 10 lần
    còn trong các methods nếu truy cặp các self.attrs 10 lần sẽ call 10
    __getattribute__(self, attr) 10 lần
    vd self.name => run __getattribute__(self, attr)
        self.old => lai run __getattribute__(self, attr), ... blabla
    phải chú ý __getattribute__(self, attr)

    trong magic_method ko được dung syntax của nó để call chính nó
    : __len__(self): ko được len(self)
    : __ge__(self, other): ko được self >= other
    blabla..., ...

    self, super().func(no self) => class()=object.func(have a self)
    value = int, str
    khi tao cac special method neu gap cac syntax trong code or ngay return:
    self + value thi se call them __add__
    value + self thi se call them __radd__

    operators: +-*/, //,%, **, &=__and__, |=__or__,
    ^=__xor__
    i_operators +=, ...
    comparison: <,<=,==,!=, ...,


    khi gặp: self +-*/ other=self -> run special methods operators tương ứng
    value+self -> run special methods operators right
    len(self) * value > run __len__(self) return giá trị cụ thể(int, str)=value rồi nhân * với value

    nói chung: value +value cộng bình thường

    self+value, value < self, self + self sẽ run các special methods operators or comparisons tương ứng,

    và còn những methods khác len(self), str(self), blabla, ... các built-in functions đều có special methods nếu ta định nghĩa nó khi tạo class, để run nó thì code func_name(self) trong các methods

code self[pos] -> run __getitem__(self, pos)
"""

class Special:
    """Tao la Special class"""
    __number = 0
    __string = ''
    count_init = 0
    count_setattr = 0
    count_getattr = 0
    count_getattribute = 0
    count_str = 0
    # child_class ko thể access, classs variable private cua parent_class,
    # chỉ có thể dùng publish method của parrent_class để truy cập
    # neu la class variable publish thi access binh thuong child_class.count_init, child_class.count_getattr, ...

    def __init__(self, *, number=10, intdf=5, strdf='phong', listdf=[]):
        Special.count_init += 1
        print(f"Tao la __init__ {Special.count_init}")
        self.__len = number # _Special__len
        self.__str = strdf  # _Special__str
        self.__list = listdf # _Special__list
        self.__int = intdf # _Special__int
        # child_class có thể access self._Special__int, syntax đặc biệt
        #


    # khi len(self) => run:  __len__(self)
    def __len__(self):
        print('__len__')
        return self.__len  # self__len = int (bat buoc)
    # khi print(obj) or str(obj) or obj.__str__() => run __str__(self) = self.__str

    def __str__(self):
        Special.count_str += 1
        print(f"__str__ {Special.count_str}")
        return self.__str  # self__str = str bat buoc

    def __repr__(self):
        print("__repr__")
        return f"<enter> run __repr__ = {self.__str}"  # dung repr(obj)

    def __setitem__(self, attr, value):
        print('__setitem__')
        # self[attr] = value
        self.__dict__[attr] = value

    def __getitem__(self, attr):
        print("__getitem__")
        # self[::], self[index] #RecursionError
        return self.__dict__[attr]

    def __delitem__(self, attr):
        print('__delitem__')
        del self.__dict__[attr]

    def __getattribute__(self, attr): #3
        Special.count_getattribute += 1
        print(f'<{attr}> ton tai nen run __getattribute__ {Special.count_getattribute}')
        # super().__getattribute__(attr) # run __getattr__(self, attr) #2
        # object.__getattribute__(self,attr) #2
        return object.__getattribute__(self,attr)
        #super() | object.__getattribute__(self, attr) return VALUE neu self.attr ton tai, else run __getattr(self, attr) 1 lan duy nhat
        #
    def __getattr__(self, attr): #2
        Special.count_getattr += 1
        print(f'<{attr}> NONO ton tai nen run __getattr__ {Special.count_getattr} <{attr}>')

        value = 'invalid'
        setattr(self, attr, value)
        return value

    def __setattr__(self, attr, value): #1
        # khi tao obj neu co 4 attr se run 4 lan __setattr__
        self.__dict__[attr] = value

        Special.count_setattr += 1
        print(f"Tao la __setattr__ {Special.count_setattr}")
        if not isinstance(value, list):
            print(f"<{attr}> {value:.>20}", end='\n'*2)
        else:
            print(f"<{attr}> {'':.<20}{value}", end='\n'*2)


    def __delattr__(self, attr):
        print('__delattr__')

    def __del__(self):
        print("__del__")

    def __add__(self, other):
        print('tao la __add__+')

        return Special(intdf=self.__int + other.__int)
        # return self.__str + other.__str

    def __sub__(self, other):
        print('tao la __sub__-')

        return Special(intdf=self.__int - other.__int)

    def __mul__(self, other):
        print('tao la __mul__*')

        return Special(intdf=self.__int * other.__int)

    def __truediv__(self, other):
        print('tao la __truediv__/')

        return Special(intdf=self.__int / other.__int)

    def __floordiv__(self, other):
        print('tao la __floordiv__//')

        return Special(intdf=self.__int // other.__int)

    def __mod__(self, other):
        print('tao la __mod__%')

        return Special(intdf=self.__int % other.__int)

    def __divmod__(self, other):
        print('__divmod__ (nguyen, du)')
        floordiv = self.__int // other.__int
        mod = self.__int % other.__int

        return (floordiv, mod)

    def __pow__(self, other):
        print('tao la __pow__**')

        return self.__int ** other.__int

    def __lshift__(self, other):
        print(
            f"__lshift__ = {self.__int} << {other.__int}  <=> {self.__int} * (2**{other.__int})")

        return self.__int << other.__int

    def __rshift__(self, other):
        print(
            f"__lshift__ = {self.__int} >> {other.__int}  <=> {self.__int} / (2**{other.__int})")

        return self.__int >> other.__int

    # __and__(self, other) = &
    # __xof__(self, other) = ^
    # __or__(self, other) = |
    # __iadd__(self, other) =   <+=> update, ... func() con lai tuong tu them i

    # object.__lt__(self, other) <
    # object.__le__(self, other) <=
    # object.__eq__(self, other) ==
    # object.__ne__(self, other) !=
    # object.__gt__(self, other) >
    # object.__ge__(self, other) >=

    # __neg__(self) = -self
    # __pos__(self) = +self
    # __abs__() = abs()
    # __invert(self) = ~

    # __complex__(self) = complex()
    # __int(self) = int()
    # __long(self) = long()
    # __float(self) = float()
    # __oct__() = oct()
    # __hex__() = hex()

    @property
    def _len(self):
        return self.__len

    @_len.setter
    def _len(self, value):

        if isinstance(value, int):
            self.__len = value*2
        else:
            self.__len = Special.__number

    @property
    def _str(self):
        return self.__str

    @_str.setter
    def _str(self, value):
        if isinstance(value, str):
            self.__str = value.upper()
        else:
            self.__str = Special.__string


class ChildSpecial(Special):
    """docstring for ChildSpecial"""
    def __init__(self):
        super().__init__()

    def __str__(self):
        return str(self) # recursion vo tan call itself

    def __len__(self):
        return len(self) # recursion vo tan call itself


class Recursion(Special):
    """docstring for Recursion"""
    __IMPORTANT__ = """
        chỉ có thể dùng publish method đc thừa kế để access class variable private
        còn instance variable private có thẻ dùng syntas đặc biệt,
        self._Special__int => nhưng nên dùng publish method
    """


    def __init__(self, full_name="thanh phong", old=26, intdf=23):
        super().__init__(intdf=intdf)
        self.full_name = full_name
        self.old = old
        # child_class có thể access self._Special__int, syntax đặc biệt
        #


    # def __setattr__(self, attr, value):
    #     print(f'__setattr__')
    #     print(f"<{attr}> {value:.>20}")
    #     self.attr = value #RecursionError

    def __getattribute__(self, attr):
        print(f"__getattribute__ ")
        # recursion = self.attr # RecusionError
        return super().__getattribute__(attr)


    def __getattr__(self, attr):
        print(f"__getattr__ ")
        default_value = 'blabla'
        setattr(self, attr, default_value)
        return default_value

    def __getitem__(self, pos):
        print("__getitem__")
        return self[pos] #RecursionError

    def __setitem__(self, pos, value):
        print('__setitem__')
        self[pos] = value #RecursionError

    def __del__(self):
        print("__del__")
        del self # chi reing del self ko bi #RecursionError

    def __str__(self):
        return str(self) #RecursionError

    def __repr__(self):
        return repr(self) #RecursionError

    def __add__(self, other):
        print("__add__")
        return self + other #RecursionError

    def __sub__(self, other):
        print('tao la __sub__-')

        return self - other #RecursionError

    def __mul__(self, other):
        print('tao la __mul__*')

        return self * other #RecursionError

    def __truediv__(self, other):
        print('tao la __truediv__/')

        return self / other #RecursionError

    def __floordiv__(self, other):
        print('tao la __floordiv__//')

        return self // other #RecursionError

    def __mod__(self, other):
        print('tao la __mod__%')

        return self % other #RecursionError

    def __divmod__(self, other):
        print('__divmod__')

        return divmod(self, other) #RecursionError

    def __pow__(self, other):
        print('tao la __pow__**')

        return self ** other #RecursionError

    def __lshift__(self, other):
        print(
            f"__lshift__ = {self.__int} << {other.__int}  <=> {self.__int} * (2**{other.__int})")

        return self << other #RecursionError

    def __rshift__(self, other):
        print(
            f"__lshift__ = {self.__int} >> {other.__int}  <=> {self.__int} / (2**{other.__int})")

        return self >> other #RecursionError


class Iteration:
    def __init__(self, max = 5):
        self.max = max
        self.one = 1
        self.two = 2
        self.three = 3

    def itself(self):
        return self

    def __str__(self):
        return f"<Iteration(max={self.max})>"

    def __repr__(self):
        return f"<Iteration(max={self.max})>"

    def __getitem__(self, pos):
        print(f"__getitem__ {pos.start} {pos.stop} {pos.step}")

        return self.__dict__

    def __iter__(self):
        self.x = 1
        return self

    def __next__(self):
        if self.x <= self.max:
            val = 2 ** self.x
            self.x += 1
            return val
        else:
            raise StopIteration


# Descriptor
class NonNegativeDescriptor(object):
    def __init__(self, label):
        self.label = label

    def __get__(self, instance, owner):
        return f"{instance.__dict__.get(self.label)} \n{instance.program} \nself: {self} \ninstance: {instance} \nowner: {owner}"

    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.label] = value
        else:
            raise ValueError(f"Negative value not allowed: {value}")


class Programmer(object):
    age = NonNegativeDescriptor('age')
    salary = NonNegativeDescriptor('salary')
    rating = NonNegativeDescriptor('rating')
    program = f"{'':*<10}class attribute"
    # khi class attrs = descriptor trung ten instance attrs, thi se call class attr, default call instance attrs

    def __init__(self, name, age, salary, rating):
        self.name = name
        self.age = age
        self.salary = salary
        self.rating = rating
        self.program = f"{'':#<10}instance attribute trong __init__"


#metaclass
class Iris(type):
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.kingdom = 'Plantae'
        return obj

# cac metaclass se run __new__() -> __init__() -> __call__() khi vua code xong class -> tuc la chua tao instance = Setosa()
class Setosa(metaclass=Iris):
    pass

class Virginica(metaclass=Iris):
    pass

class Versicolor(metaclass=Iris):
    pass


if __name__ == '__main__':
    pass
