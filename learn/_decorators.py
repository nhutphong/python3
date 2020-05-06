import random
import time
from functools import wraps


def to_upper(func):
    print("to_upper")
    @wraps(func)
    def wrapped(*args, **kwargs):
        print("start to_upper lalalal")
        text = func(*args, **kwargs)
        print("end to_upper lalala")

        if not isinstance(text, str):
            raise TypeError("deo phai string")

        return text.upper()

    return wrapped


def to_join(func):
    print("to_join")
    @wraps(func)
    def wrapped(*args, **kwargs):
        print("start to_join HHHHHHH")
        text = func(*args, **kwargs)
        print("end to_join HHHHHH")
        result = ' '.join([text, 'thanh phong'])

        return result

    return wrapped


@to_upper #to_upper()
@to_join #to_join()
def dec_check(text='let goooo'):
    return text


class DecoratorClass: 
    __IMPORTANT__ = """
        syntax cho decorator class
    """
    print("Decoratorclass")

    def __init__(self, function):
        print(f"DecoratorClass.__init__ start {type(self).__name__}") 
        self.function = function 
        print(f"DecoratorClass.__init__ end {type(self).__name__}")
      
    def __call__(self, *args, **kwargs): 
        print("__call__ start")
        # We can add some code  
        # before function call 
        
        self.function(*args, **kwargs) 
  
        # We can also add some code 
        # after function call. 
        print("__call__ end")
  

@DecoratorClass  # @DecoratorClass = DecoratorClass()
def function(first_name='phong', message ='Hello', last_name='nhut'): 
    print(f"{message}, {first_name} {last_name}")


def format_python(name='phong', letter='#'):
    print(f"{name:{letter}^90}")


def format_one(func):
    @wraps(func)
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
# khi get_name(blalba, ...) se run wrapped(*args, **kwargs)
def get_name(**kwargs):
    return kwargs
# get_name(start='NHUT', end='PHONG', letter='#') #cach 1 


#cach 2
def design(*args, **kwargs):
    print("design")
    def wrapped(func):
        print('Tao la design.wrapped START')
        func()
        print('Tao la design.wrapped END')
        context = dict(
            username=kwargs['username'], 
            password=kwargs['password']
            )
        return context

    return wrapped

@design(username='phong', password=12345) 
#run design(), wrapper() va created variable show = context
def show(**kwargs):
    print('ban da logged')


# params for decorator
def terminal(letter='#'): #1
    print("Tao la terminal")

    def function(func): #2
        print("Tao la function")

        def wrapped(*args, **kwargs): #3
            print(f"{'wrapped START ':{letter}^85}")
            fun = func(*args, **kwargs)
            print(f"{'wrapped END ':{letter}^85}", end='\n'*2)
            return fun
        return wrapped
    return function


# @terminal # chi run #1 terminal() khong nen
@terminal(letter='$') #run1 terminal() va run2 function() ,co param nen dung
def get_age(age):
    """Docstring get_age"""
    print('Tao la get_age')
    return age

print(get_age(age=27)) #run #3 wrapped(*args, **kwargs) kwargs{age=27} thuoc ve wrapped, chu khong phai thuoc ve get_age()


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


@register #run register()
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

# khi <callback=goi 1 func khac> cau truc param nen giong time_run
# nen dat param cua time_run trung ten param cua func, tinh polymorphism
def time_run(func, *args, **kwargs):
    start = time.time()
    func(*args, **kwargs)
    end = time.time()
    return end-start

# duration = time_run(find_password, 'dung', '123456', ['dung', '123456'])

# print(f"{duration:,.6f}")


def main():
    pass


if __name__ == '__main__':
    pass