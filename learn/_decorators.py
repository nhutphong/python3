#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import time
from functools import wraps
import inspect


def to_upper(func):
    print("to_upper")
    @wraps(func) #add __wrapper__() => de unwrap,  func.__wrapper__(**kwds) <=> inspect.unwrap(func)(**kwds)
    def wrapper(*args, **kwargs):
        print("start to_upper lalalal")
        text = func(*args, **kwargs)
        print("end to_upper lalala")

        return text.upper()

    return wrapper


def to_join(func):
    print("to_join")
    @wraps(func) #add __wrapper__()
    def wrapper(*args, **kwargs):
        print("start to_join HHHHHHH")
        names = func(*args, **kwargs)
        print("end to_join HHHHHH")
        result = ' '.join(names)

        return result

    return wrapper


@to_upper #to_upper()
@to_join #to_join()
def get_names(names):
    print("Tao la get_names")
    return names
print()

print(f"{get_names.__name__ = }")
print(f"{get_names(['dung', 'thong', 'cau'])}")
print()
print(f"{get_names.__wrapper__(['cau', 'dung', 'thong', 'heo']) = }")
print()
print("co bao nhieu decorator thi .__wrapper__ bay nhieu lan")
print(f"{get_names.__wrapper__.__wrapper__(['cau', 'dung', 'thong', 'heo']) = }")
print()
print("nen dung inspect.unwrap bo tat ca decorator")
print(f"{inspect.unwrap(get_names)(['cau', 'dung', 'thong', 'heo']) = }")


# In[2]:


class DecoratorClass: 
    __IMPORTANT__ = """
        syntax cho decorator class
    """
    print("Decoratorclass")
    print('------------------------------------------------------------------------')

    def __init__(self, function): #chi 1 param la function bat buoc
        print(f"DecoratorClass.__init__ start {type(self).__name__}") 
        self.function = function 
        print(f"DecoratorClass.__init__ end {type(self).__name__}")
      
    def __call__(self, *args, **kwargs): 
        print("__call__ start")
        # We can add some code  
        # before function call 
        
        value = self.function(*args, **kwargs) 
  
        # We can also add some code 
        # after function call. 
        print("__call__ end")
        
        return value
  

@DecoratorClass  # function = @DecoratorClass = DecoratorClass(function)
def function(first_name='dung', last_name='thong', /, **kwds): 
    return dict(first_name=first_name, last_name=last_name, **kwds)
print()

print(f"{function() = }  <__call__()>")
print()
print(f"{function.function() = } <self.function()>")


# In[3]:


def format_python(name='phong', letter='#'):
    print(f"{name:{letter}^90}")


def format_one(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"{kwargs['start']:{kwargs['letter']}^50}")
        fun = func(**kwargs)
        print(f"{kwargs['end']:{kwargs['letter']}^50}")
        return fun

    return wrapper


def format_two(*args, **kwargs):
    def wrapper(func):
        print(f"{kwargs['start']:{kwargs['letter']}^50}")
        fun = func(**kwargs)
        print(f"{kwargs['end']:{kwargs['letter']}^50}")
        return fun

    return wrapper


# @format_two(start='NHUT', end='PHONG', letter='#') #cach 2 auto get_name()
# cach 2 va tao variable get_name = return fun = data=kwargs=dict 

@format_one #cach 1
# khi get_name(blalba, ...) se run wrapper(*args, **kwargs)
def get_name(**kwargs):
    return kwargs
# get_name(start='NHUT', end='PHONG', letter='#') #cach 1 


#cach 2
def design(*args, **kwargs):
    print("design")
    def wrapper(func):
        print('Tao la design.wrapper START')
        func()
        print('Tao la design.wrapper END')
        context = dict(
            username=kwargs['username'], 
            password=kwargs['password']
            )
        return context

    return wrapper

@design(username='phong', password=12345) 
#run design(), wrapper() va created variable show = context
def show(**kwargs):
    print('ban da logged')
print(f"{show = }")
print()


# params for decorator
def terminal(letter='#'): #1
    print("Tao la terminal")

    def function(func): #2
        print("Tao la function")
        @wraps(func)
        def wrapper(*args, **kwargs): #3
            print(f"{'wrapper START ':{letter}^85}")
            fun = func(*args, **kwargs)
            print(f"{'wrapper END ':{letter}^85}", end='\n'*2)
            return fun
        return wrapper
    return function


# @terminal # chi run #1 terminal() khong nen
@terminal(letter='$') #run1 terminal() va run2 function() ,co param nen dung
def get_age(age):
    """Docstring get_age"""
    print('Tao la get_age')
    return age

print(get_age(age=27)) #run #3 wrapper(*args, **kwargs) kwargs{age=27} thuoc ve wrapper, 
#chu khong phai thuoc ve get_age()


# In[4]:


def register(func):
    print("Tao la register")

    @wraps(func)
    def wrapper(username, password, *args, **kwargs):
        # print(f"SWAP-START")
        # print(f"wrapper haha")
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

    return wrapper


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