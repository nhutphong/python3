"""
    DATA MODEL, BASIC CUTOMIZATION
    Magic method

"""
__IMPORTANT__="""

    khi định nghĩa 1 Class nếu chúng ta override 3 hàm này:
    __getattribute__(self, attr), __getattr__(self, attr),
    __setattr__(self, attr, value) thì phải chú ý
    khi tạo instance=class() thì run __init__()  gặp 10 attrs trong đó sẽ run __settatr__() 10 lần
    còn trong các methods nếu truy cặp các self.attrs 10 lần sẽ call
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
    khi tao cac Magic method neu gap cac syntax trong code or ngay return:
    self + value thi se call them __add__
    value + self thi se call them __radd__

    operators: +-*/, //,%, **, &=__and__, |=__or__,
    ^=__xor__
    i_operators +=, ...
    comparison: <,<=,==,!=, ...,


    khi gặp: self +-*/ other=self -> run Magic methods operators tương ứng
    value+self -> run Magic methods operators right
    len(self) * value > run __len__(self) return giá trị cụ thể(int, str)=value rồi nhân * với value

    nói chung: value +value cộng bình thường

    self+value, self + self sẽ run các Magic methods
    value + self se run right Magic methods

    và còn những methods khác len(self), str(self), blabla, ... các built-in functions đều có Magic methods nếu ta định nghĩa nó khi tạo class, để run nó thì code func_name(self) trong các methods

code self[pos] -> run __getitem__(self, pos)
"""

def design(func_name=None, letter='#'):
    def function(func):
        def wrapped(*args, **kwargs):
            print(f"{func_name+ ' START ':{letter}^85}")
            fun = func(*args, **kwargs)
            print(f"{func_name+ ' END ':{letter}^85}", end='\n'*2)
            return fun

        return wrapped
        
    return function


class Magic:
    """Tao la Magic class"""
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

    @design("__init__")
    def __init__(self, *, number=10, intdf=5, strdf='phong', listdf=[]):
        Magic.count_init += 1
        print(f"Tao la __init__ {Magic.count_init}")
        self.__len = number # _Magic__len
        self.__str = strdf  # _Magic__str
        self.__list = listdf # _Magic__list
        self.__int = intdf # _Magic__int
        # child_class có thể access self._Magic__int, syntax đặc biệt
        #


    # khi len(self) => run:  __len__(self)
    @design("__len__")
    def __len__(self):
        print('__len__')
        return self.__len  # self__len = int (bat buoc)
    # khi print(obj) or str(obj) or obj.__str__() => run __str__(self) = self.__str
    @design("__str__")
    def __str__(self):
        Magic.count_str += 1
        print(f"__str__ {Magic.count_str}")
        return self.__str  # self__str = str bat buoc

    @design("__repr__")
    def __repr__(self):
        print("__repr__")
        return f"<enter> run __repr__ = {self.__str}"  # dung repr(obj)

    @design("__setitem__")
    def __setitem__(self, key, value):
        print('__setitem__')
        # self[key] = value
        self.__dict__[key] = value

    @design("__getitem__")
    def __getitem__(self, key):
        print("__getitem__")
        # self[::], self[index] #RecursionError
        return self.__dict__[key]

    @design("__delitem__")
    def __delitem__(self, key):
        # del self[key]
        print('__delitem__')
        del self.__dict__[key]

    @design("__getattribute__")
    def __getattribute__(self, attr): #3
        # self.attr ton tai
        Magic.count_getattribute += 1
        print(f'<{attr}> ton tai nen run __getattribute__ {Magic.count_getattribute}')
        # super().__getattribute__(attr) # run __getattr__(self, attr) #2
        # object.__getattribute__(self,attr) #2
        return object.__getattribute__(self,attr)
        #super() | object.__getattribute__(self, attr) return VALUE neu self.attr ton tai, else run __getattr(self, attr) 1 lan duy nhat
        #

    @design("__getattr__")
    def __getattr__(self, attr): #2
        # self.old -> run 1 lan khi self.old khong ton tai
        Magic.count_getattr += 1
        print(f'<{attr}> NONO ton tai nen run __getattr__ {Magic.count_getattr} <{attr}>')

        value = 'invalid'
        setattr(self, attr, value)
        return value

    @design("__setattr__")
    def __setattr__(self, attr, value): #1
        # khi tao obj neu co 4 attr se run 4 lan __setattr__
        self.__dict__[attr] = value

        Magic.count_setattr += 1
        print(f"Tao la __setattr__ {Magic.count_setattr}")
        if not isinstance(value, list):
            print(f"<{attr}> {value:.>20}", end='\n'*2)
        else:
            print(f"<{attr}> {'':.<20}{value}", end='\n'*2)

    @design("__delattr__")
    def __delattr__(self, attr):
        # del self.attr
        print('__delattr__')
        del self.__dict__[attr]

    @design("__del__")
    def __del__(self):
        #del self
        print("__del__")

    def __add__(self, other):
        print('tao la __add__+')

        return Magic(intdf=self.__int + other.__int)
        # return self.__str + other.__str

    def __sub__(self, other):
        print('tao la __sub__-')

        return Magic(intdf=self.__int - other.__int)

    def __mul__(self, other):
        print('tao la __mul__*')

        return Magic(intdf=self.__int * other.__int)

    def __truediv__(self, other):
        print('tao la __truediv__/')

        return Magic(intdf=self.__int / other.__int)

    def __floordiv__(self, other):
        print('tao la __floordiv__//')

        return Magic(intdf=self.__int // other.__int)

    def __mod__(self, other):
        print('tao la __mod__%')

        return Magic(intdf=self.__int % other.__int)

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
            self.__len = Magic.__number

    @property
    def _str(self):
        return self.__str

    @_str.setter
    def _str(self, value):
        if isinstance(value, str):
            self.__str = value.upper()
        else:
            self.__str = Magic.__string


class ChildMagic(Magic):
    """docstring for ChildMagic"""
    def __init__(self):
        super().__init__()

    def __str__(self):
        return str(self) # recursion vo tan call itself

    def __len__(self):
        return len(self) # recursion vo tan call itself


class Recursion(Magic):
    """docstring for Recursion"""
    __IMPORTANT__ = """
        chỉ có thể dùng publish method đc thừa kế để access class variable private
        còn instance variable private có thẻ dùng syntas đặc biệt,
        self._Magic__int => nhưng nên dùng publish method
    """


    def __init__(self, full_name="thanh phong", old=26, intdf=23):
        super().__init__(intdf=intdf)
        self.full_name = full_name
        self.old = old
        # child_class có thể access self._Magic__int, syntax đặc biệt
        #


    # def __setattr__(self, attr, value):
    #     print(f'__setattr__')
    #     print(f"<{attr}> {value:.>20}")
    #     self.attr = value #RecursionError

    def __getattribute__(self, attr):
        print(f"__getattribute__ ")
        # value = self.attr or getattr(self, attr) # RecusionError
        # value = super().__getattribute__(attr)
        # value = object.__getattribute__(self, attr)
        return super().__getattribute__(attr)


    def __getattr__(self, attr):
        print(f"__getattr__ ")
        default_value = 'blabla'
        setattr(self, attr, default_value)
        return default_value

    def __getitem__(self, key):
        print("__getitem__")
        return self[key] #RecursionError

    def __setitem__(self, key, value):
        print('__setitem__')
        self[key] = value #RecursionError

    def __del__(self):
        print("__del__")
        del self # chi rieng del self ko bi #RecursionError

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
    def __init__(self, start=0, stop=0, step=1):
        self._start = start

        if stop==0:
            self._start, self._stop = stop, start
        else:
            self._stop = stop

        self._step = step

    def __str__(self):
        return f"<Iteration(start={self.start}, stop={self.stop}, step={self.step})>"

    def __repr__(self):
        return f"<Iteration(max={self.max})>"

    def __getitem__(self, key):
        print(f"__getitem__")

        return self.__dict__[key]

    def __contains__(self, item):
        # item in iterator
        # 'haha' in iterator
        print("__contains__")
        # return False #default

    def __iter__(self):
        print("__iter__")

        # self.x = 1
        return self

    def __next__(self):
        print("__next__")

        if self.start < self.stop:
            value = self.start
            self.start += self.step
            return value
        else:
            raise StopIteration

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        self._start = value

    @property
    def stop(self):
        return self._stop

    @stop.setter
    def stop(self, value):
        self._stop = value

    @property
    def step(self):
        return self._step

    @step.setter
    def step(self, value):
        self._step = value

    @property
    def default(self):
        self.start = 0
        self.stop = 10
        self.step =1
        return self

__ITERATOR__ = """
    iterator = Iteration(5)
    iter(iterator) => run __iter__(self)
    next(iterator) => run __next__(self)
    next(iterator) 2,3,4,5 => run __next__(self) neu toi 6 se raise StopIteration


    for iterator in Iteration(5):
        print(iterator)
    => dung for run __iter__ 1 lan va __next__ toi khong thoa dieu khien thi dung

    list(Iterator) or tuple(iterator) cung run __iter__ va __next__
    list(Iteration(1,16,2)), tuple(Iteration(1,12,2))

"""


#metaclass
class Iris(type):
    def __new__(cls, *args, **kwargs):
        print(f"Tao la Iris.__new__")
        obj = super().__new__(cls, *args, **kwargs)
        obj.kingdom = 'Plantae'
        return obj

# cac metaclass se run __new__() -> __init__() -> __call__() khi vua code xong class -> tuc la chua tao instance = Setosa()
# khi co 4 class inheritance tu Iris thi run Iris.__new__ 4 lan
__MAGIC__= """
    co nhung magic method phai tra ve value cu the: vd
    __init__(self,*args, **kwds): return None => ko return gi ca
    __len__(self): return <int>
    __str__(self): return <str>
    __repr__(self): return <str>
    __index__(self): return <int>
    __index__: run khi bin(obj), int(obj), float(obj)

   __new__(cls, *args, **kwargs): return <obj>
    obj = super().__new__(cls, *args, **kwargs)
    __new__ nen return obj nhung kho bat buoc

"""

class Setosa(metaclass=Iris):
    pass

class Virginica(metaclass=Iris):
    pass

class Versicolor(metaclass=Iris):
    pass

class Four(metaclass=Iris):
    pass


if __name__ == '__main__':
    pass