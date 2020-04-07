import random
import time

"""
    closure = cac function long nhau => nen dung decorators
    Khi cần định nghĩa một class chỉ với vài phương thức, closure có thể được sử dụng như một giải pháp thay thế nhẹ nhàng hơn lập trình hướng đối tượng. Tuy nhiên là khi các thuộc tính và phương thức nhiều lên, sử dụng lập trình hướng đối tượng sẽ là giải pháp tốt hơn.
"""
# closure
def make_multiplier_of(n):
     def multiplier(x):
         return x * n
     return multiplier


class Circle:
    def __init__(self, radius):
        self.__radius = radius

    # khi có @property = getter, @radi.setter => khi call method obj.radi() phải khi thành attribute ->
    #     obj.radi = 'phong' <=> obj._radius = 'phong'
    #     có thể set attribute self._radius

    @property
    def area(self):
        """Calculate area inside circle"""
        return self.pi() * self.__radius**2

    def cylinder_volume(self, height):
        """Calculate volume of cylinder with circle as base"""
        return self.area * height

    # khi co @classmethod co the doi self thanh ten tuy y
    # Circle() = self = cls ...
    @classmethod
    def unit_circle(cls):
        """Factory method creating a circle with radius 1"""
        cls.obj_circle = cls(1)
        return cls.obj_circle

    @classmethod
    def get_radi(cls):
        cls.__radius = 10

    # staticemethod nhu funciton() thông thường, khi gọi thông qua obj,
    # có thể hiểu là tập hợp các function() có chức năng  mà class này hay dùng = clean code, nếu không thích có thể viết funtions() ra files(modules) khác và import vào
    @staticmethod
    def pi():
        """Value of π, could use math.pi instead though"""
        return 3.1415926535


def gen(n):
    ls = []

    for i in range(n):
        ls.append(i**3)
    return ls

# yield, my_generator() = gen(),
# my_generator(10) là 1 generator: print(list(my_generator(10))): phải có list mới in ra được or  trực tiếp vào for i in my_generator(10)
# function: iter(str) = chuyen str ve iterable, next(str) = lap từng pt trong str


def my_generator(n):
    for i in range(n):
        yield i**3


def decorator(func):

    def wrapper(*args, **kwargs):
        print(f"Dang trong wrapper -> {args}")
        full_name = args[0] + ' ' + args[1]
        return func(full_name)

    return wrapper


@decorator
def my_name(full_name):
        return f"My name is {full_name}"
NOTE = '''
        khi goi my_name(param, ...) truyen tham so theo wrapper(...)
        con trong wrapper thi func(full_name) = my_name(full_name) chi co
        1 param
'''


class Pro(object):

    def __init__(self, age):
        self.__age = age
        # private variable
        # p = Pro(25)
        # print(p._Pro__age)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, old):
        if old < 0:
            self.__age = 0
        else:
            self.__age = old


# paramater cho decorator
def chuc_danh(job):
    def function(func):
        def wrapped(*args, **kwargs):
            print("wrapped Dau")
            print(f"chuc_danh: {job}")
            print("wrapped cuoi")

            fu = func(*args) ** 2
            return fu

        return wrapped

    return function


@chuc_danh('Doctor')
def xuat_ten(*tup):
    return random.choice(lis)


def unifylist(l_input, l_target):
    for it in l_input:
        if isinstance(it, list):
            unifylist(it, l_target)
        elif isinstance(it, tuple):
            unifylist(list(it), l_target)
        else:
            l_target.append(it)

    return l_target


def to_upper(func):
    def wrapped(*args, **kwargs):
        print("start to_upper lalalal")
        text = func(*args, **kwargs)
        print("end to_upper lalala")

        if not isinstance(text, str):
            raise TypeError("deo phai string")

        return text.upper()

    return wrapped


def to_join(func):
    def wrapped(*args, **kwargs):
        print("start to_join HHHHHHH")
        text = func(*args, **kwargs)
        print("end to_join HHHHHH")
        result = ' '.join([text, 'thanh phong'])

        return result

    return wrapped


@to_upper
@to_join
def dec_check(text='let goooo'):
    return text


class DecoratorClass: 
    __IMPORTANT__ = """
        syntax cho decorator class
    """

    def __init__(self, function):
        print(f"__init__ start {type(self).__name__}") 
        self.function = function 
        print(f"__init__ end {type(self).__name__}")
      
    def __call__(self, *args, **kwargs): 
        print("__call__ start")
        # We can add some code  
        # before function call 
        
        self.function(*args, **kwargs) 
  
        # We can also add some code 
        # after function call. 
        print("__call__ end")
  
# adding decorator to the class  
@DecoratorClass #autorun DecoratorClass.__init__() truoc khi goi functions()
def function(first_name='phong', message ='Hello', last_name='nhut'): 
    print(f"{message}, {first_name} {last_name}")


def format_python(name='phong', letter='#'):
    print(f"{name:{letter}^90}")


def format_one(func):
    def wrapped(*args, **kwargs):
        print(f"{kwargs['start']:{kwargs['letter']}^50}")
        fun = func(**kwargs)
        print(f"{kwargs['end']:{kwargs['letter']}^50}")
        return fun

    return wrapped


def format_two(*args, **kwargs):
    def wrapped(func):
        print(f"{kwargs['start']:{kwargs['letter']}^50}")
        fun = func(**kwargs)
        print(f"{kwargs['end']:{kwargs['letter']}^50}")
        return fun

    return wrapped


# @format_two(start='NHUT', end='PHONG', letter='#') #cach 2 auto get_name()
# cach 2 va tao variable get_name = return fun = data=kwargs=dict 
@format_one #cach 1
def get_name(**kwargs):
    return kwargs
# get_name(start='NHUT', end='PHONG', letter='#') #cach 1

#cach 2
def design(*args, **kwargs):
    def wrapped(func):
        print('Tao la wrapped START')
        func()
        print('Tao la wrapped END')
        context = dict(
            username=kwargs['username'], 
            password=kwargs['password']
            )
        return context

    return wrapped

@design(username='phong', password=12345)
def show(**kwargs):
    print('ban da logged')
# auto variable show = context


# params for decorator
def terminal(name=None, letter='#'):
    def function(func):
        def wrapped(*args, **kwargs):
            print(f"{name + ' START ':{letter}^85}")
            fun = func(*args, **kwargs)
            print(f"{name + ' END ':{letter}^85}", end='\n'*2)
            return fun
        return wrapped
    return function


def decorator_age(func):
    @wraps(func) # func.__name__ == get_age.__name__
    #neu khong co @wraps(func) thi la wrapped.__name__
    def wrapped(wage, *args, **kwargs):
        print(f"SWAP-START")
        print(f"wrapped haha")
        # fun = func(*args, **kwargs)
        fun = func(age=wage)
        print(f"SWAP-END")
        return fun

    return wrapped


@decorator_age
def get_age(age):
    """Docstring get_age"""
    print('Tao la get_age')
    return age

print(get_age(wage=27))


def main():
    pass


if __name__ == '__main__':
    pass