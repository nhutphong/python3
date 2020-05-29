#!/usr/bin/env python
# coding: utf-8

# In[1]:


important = """
    def action(func):
    
        @functools.wraps(func)
        def wrapper(*args, **kwds):
            return func(*args, **kwds)
        return wrapper
        
    @action
    def my_func():
    
    my_func = action(myfunc) #return action = wrapper 

    
    def action(param1, param2):
    
        def decorator(func):
        
            @functools.wraps(func)
            def wrapper(*args, **kwds):
                return func(*args, **kwds)
                
            return wrapper
            
        return decorator
        
    @action(param1, param2)
    def my_func():
    
    my_func = action(param1, param2)(my_func) #return decorator = wrapper
    
    
    def dataclass(cls=None, /, *, init=True, repr=True, eq=True, order=False,
              unsafe_hash=False, frozen=False):

        def wrapper(cls):
            return _process_class(cls, init, repr, eq, order, unsafe_hash, frozen)

        if cls is None: # @dataclass(...) = detaclass(...)(cls) = wrapper(cls)
            
            return wrapper #              = dataclass(...)

        return wrapper(cls)   # @dataclass = dataclass(cls) = wrapper(cls)
    
"""
    


# In[2]:


import random
import time
from functools import wraps
import inspect

def to_upper(func):
    print("to_upper")
    
    @wraps(func) #add __wrapped__() => de unwrap,  func.__wrapped__(**kwds) <=> inspect.unwrap(func)(**kwds)
    def wrapper(*args, **kwargs):
        print("start wrapper_upper")
        text = func(*args, **kwargs)
        print("end wrapper_upper ")

        return text.upper() 

    return wrapper #1


def to_join(func):
    print("to_join")
    
    @wraps(func) #add __wrapper__()
    def wrapper(*args, **kwargs):
        print("start wrapper_join")
        names = func(*args, **kwargs)
        print("end wrapper_join")
        result = ' '.join(names)

        return result

    return wrapper #1


@to_upper # run  to_upper(func): return wrapper
@to_join #
def get_names(names):
    print("Tao la get_names")
    return names
print()

# get_names = to_join(get_names) #<=> @to_join 

# get_names = to_upper(get_names) #<=> @to_upper

# print()
# print(f"{wrapper_join(['dung', 'thong', 'cau'])}")
# print()

print(f"{get_names.__name__ = }")
print(f"{get_names(['dung', 'thong', 'cau']) = }")
print()
print(f"{get_names.__wrapped__(['cau', 'dung', 'thong', 'heo']) = }")
print()
print("co bao nhieu decorator thi .__wrapper__ bay nhieu lan")
print(f"{get_names.__wrapped__.__wrapped__(['cau', 'dung', 'thong', 'heo']) = }")
print()
print("nen dung inspect.unwrap bo tat ca decorator")
print(f"{inspect.unwrap(get_names)(['cau', 'dung', 'thong', 'heo']) = }")


# In[3]:


from functools import wraps

def action(one, two): #1
    print('tao la demo')

    def function(func): #2
        print("Tao la function")

        @wraps(func)
        def wrapper(*args, **kwds): #3
            wrapper.count += 1
            print(f"Call {wrapper.count} of {func.__name__!a}")
            return func(*args, **wrapper.kwds, **kwds) #3

        wrapper.count = 0
        wrapper.kwds = dict(one=one, two=two)
        
        return wrapper #2

    return function #1

@action(1, 2) # <=> info = action(1,2)(info) = wrapper
def info(**kwds):
    return kwds
# info = wrapper

print(f"{info(three=3, four=4) = }")
print()
print(f"{info(five=5, six=6) = }")


# In[4]:


import functools

class DecoratorClassNoParam: 
    __IMPORTANT__ = """
        syntax cho decorator class
    """
    print("DecoratorClassNoParam")
    print('------------------------------------------------------------------------')

    def __init__(self, func): #1 function(func)
        print(f"DecoratorClassNoParam.__init__ start {type(self).__name__}") 
        
        #functools.wraps(func) ko dung dc vi thieu param wrapper=self
        functools.update_wrapper(self, func)
        self.func = func 
        
        print(f"DecoratorClassNoParam.__init__ end {type(self).__name__}")
      
    def __call__(self, *args, **kwargs): #2 wrapper(*args, **kwds)
        print("__call__ start")
        
        value = self.func(*args, **kwargs) 
  
        print("__call__ end")
        
        return value
  

@DecoratorClassNoParam  # info = @DecoratorClass = DecoratorClass(function)
def info(first_name='dung', last_name='thong', /, **kwds):
    """tao la def info()"""
    return dict(first_name=first_name, last_name=last_name, **kwds)
print()

print(f"{info() = }  <__call__()>")
print()
print(f"{info = }")
print(f"{vars(info) = }")
print(f"{info.func() = } <self.function()>")
print()
print(f"{info.__name__ = }")
print(f"{info.__doc__ = }")


# In[5]:


class DecoratorClassYesParam: 
    __IMPORTANT__ = """
        syntax cho decorator class
    """
    print("DecoratorClassYesParam")
    print('------------------------------------------------------------------------')

    def __init__(self, one, two): #1 action(param1, param2)
        print(f"DecoratorClassYesParam.__init__ start {type(self).__name__}") 
        self.one = one
        self.two = two
        print(f"DecoratorClassYesParam.__init__ end {type(self).__name__}")
      
    def __call__(self, func): #2 functions(func)
        print("__call__ start")

        @wraps(func)
        def wrapper(*args, **kwds): #3 wrapper(*args, **kwds)
            return func(*args, **kwds, **wrapper.kwds)


        wrapper.kwds = dict(one=self.one, two=self.two)
        return wrapper
  

@DecoratorClassYesParam(1, 2) #info = @DecoratorClassYesParam(1,2) = DecoratorClassYesParam(1,2)(function)
def info(first_name='dung', last_name='thong', /, **kwds):
    """tao la def info()"""
    return dict(first_name=first_name, last_name=last_name, **kwds)
print()

print(f"{info(country='viet nam', city='gia lai') = }  <__call__()>")
print()
print(f"{info = }")
print(f"{info.__doc__ = }")
print(f"{vars(info) = }")


# In[6]:


from functools import wraps

def count_calls(func):
    print("Tao la count_calls")

    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"wrapper {wrapper.count} of {func.__name__!a}")
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper

@count_calls #cach1 <=> #cach2 
def say_whee(): #say_whee = wrapper
    return f"whee!"
#cach2 #say_whee = count_calls(say_whee)

print()
print(f"{say_whee() = }")

print()
print(f"{say_whee() = }")

print()
print(f"{say_whee() = }")


# In[7]:


from functools import wraps

def singleton(cls):
    """chi duy nhat 1 object cho class"""
    @wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)

        return wrapper_singleton.instance

    wrapper_singleton.instance = None
    return wrapper_singleton

@singleton
class TheOne:
    pass


first_one = TheOne()
another_one = TheOne()

print(f"{id(first_one) = }")


print(f"{id(another_one) = }")

print(f"{first_one is another_one = }")


# In[8]:


import random
PLUGINS = dict()

def register(func):
    """Register a function as a plug-in"""
    print("Tao la register")

    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    return f"say_hello: {name!r}"

print(PLUGINS)

# @register #cach1 syntax cho cach2
def be_awesome(name):
    return f"be_awesome: {name!r}"

be_awesome = register(be_awesome) #cach2

print(PLUGINS)


# In[9]:


import functools

def count_calls(func):
    print("Tao la count_calls")

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"Call {wrapper.count} of {func.__name__!a}")
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper

def cache(func):
    """Keep a cache of previous function calls"""
    print("Tao al cache")
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = args + tuple(kwargs.keys())
        
        if cache_key not in wrapper.cache:
            wrapper.cache[cache_key] = func(*args, **kwargs)
            
        return wrapper.cache[cache_key]
    
    wrapper.cache = dict()
    return wrapper

@cache
@count_calls
def fibonacci(num):
    if num < 2:
        return num
    
    return fibonacci(num - 1) + fibonacci(num - 2)

print()
fibonacci(8)


# In[10]:


import functools

@functools.lru_cache(maxsize=4)
def fibonacci(num):
    print(f"Calculating fibonacci({num})")
    if num < 2:
        return num
    
    return fibonacci(num - 1) + fibonacci(num - 2)

print()
print(f"{fibonacci(8) = }")


# In[11]:


import pint

def use_unit(unit):
    """Have a function return a Quantity with given unit"""
    
    use_unit.ureg = pint.UnitRegistry()
    def decorator(func):
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            
            return value * use_unit.ureg(unit)
        
        return wrapper
    
    return decorator

@use_unit("meters per second")
def average_speed(distance, duration):
    return distance / duration

bolt = average_speed(100, 9.58)
print(f"{bolt = }")

print(f"{bolt.to('km per hour') = }")


print(f"{bolt.to('mph').m = }")

