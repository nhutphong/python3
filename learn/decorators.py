import random
import time

"""
    closure = cac function long nhau => nen dung decorators
    Khi cần định nghĩa một class chỉ với vài phương thức, closure có thể được sử dụng như một giải pháp thay thế nhẹ nhàng hơn lập trình hướng đối tượng. Tuy nhiên là khi các thuộc tính và phương thức nhiều lên, sử dụng lập trình hướng đối tượng sẽ là giải pháp tốt hơn.
"""


class Circle:
    def __init__(self, radius):
        self.__radius = radius

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
@format_one #cach 1 se run format_one() va cho
# khi get_name(blalba, ...) se run wrapped(*args, **kwargs)
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
def terminal(name=None, letter='#'): #1
    print("Tao la terminal")

    def function(func): #2
        print("Tao la function")

        def wrapped(*args, **kwargs): #3
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
        fun = func(age=wage) #han che dung
        print(f"SWAP-END")
        return fun

    return wrapped
# de hieu 


def decorator_age_two(func):
    @wraps(func) # func.__name__ == get_age.__name__
    #neu khong co @wraps(func) thi la wrapped.__name__
    def wrapped(*args, **kwargs):
        print(f"SWAP-START")
        print(f"wrapped haha")
        fun = func(*args, **kwargs) #nen dung
        print(f"SWAP-END")
        return fun

    return wrapped
# param chac che hon chi nhan get_age(27) or get_age(age=27)
# 


@terminal # run #1 khong nen
@terminal() #run #1 va #2 decorator co param nen dung
def get_age(age):
    """Docstring get_age"""
    print('Tao la get_age')
    return age

print(get_age(age=27)) #run #3 wrapped(*args, **kwargs)


def register(func):
    print("Tao la register")

    @wraps(func)
    def wrapped(username, password, *args, **kwargs):
        # print(f"SWAP-START")
        # print(f"wrapped haha")
        # fun = func(*args, **kwargs)

        name_to_list = [n for n in username]
        random.shuffle(name_to_list)
        name_new = str.join('', name_to_list)

        pass_to_list = [p for p in password]
        random.shuffle(pass_to_list)
        pass_new = str.join('', pass_to_list)

        fun = func(username=name_new, password=pass_new, *args, **kwargs)
        # print(f"SWAP-END")
        return fun

    return wrapped


@register
def get_user(username, password):
    return dict(username=username, password=password)


def find_password(username, password, source=None, *args, **kwargs):
    username, password = source
    for id in range(1,1_000_000):
        user_find, pwd_find = get_user(username, password).values()
        if user_find == username and pwd_find == password:
            print(f"{id} - found \nusername: {user_find}\npassword: {pwd_find}")
            break
        else:
            print(f"{id} - username: {user_find} | password: {pwd_find}", end='\r')


def time_run(func, *args, **kwargs):
    start = time.time()
    func(*args, **kwargs)
    end = time.time()
    return end-start

duration = time_run(find_password, 'dung', '123456', ['dung', '123456'])

print(f"{duration:,.6f}")


def main():
    pass


if __name__ == '__main__':
    pass