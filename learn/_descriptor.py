#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import time


__IMPORTANT__ = """
    khi instance.class_attr              se run __get__
    khi instance.class_attr = value      se run __set__
"""


print(f"{'Descriptor':-^85}")
# Descriptor
class Descriptor(object):
    # def __init__(self, label):
    #     print("Descriptor.__init__")
    #     self.label = label

    #python 3.6 va moi hon
    #khi new des = Descriptor() => se run __set_name__ thay the cho __init__
    def __set_name__(self, owner, name):
        print("Descriptor.__set_name__")
        self.name = name

        """
            name = 'age'
            name = 'salary'
            name = 'rating'
        """

    def __get__(self, instance, owner):

        """
        self = Descriptor()
        instance = Programmer('Thong', 30, 5_000, 4)
        owner = Programmer
        """

        print("Descriptor.__get__(self, instance, owner):")

        return instance.__dict__[self.name] or 0

    def __set__(self, instance, value):
        print("Descriptor.__set__(self, instance, value):")

        if value > 0:
            instance.__dict__[self.name] = value
        else:
            raise ValueError(f"value > 0 OK: {value}")

    # run khi <del programer.age> => khi xoa class.attr
    def __delete__(self, instance):
        print("Descriptor.__delete__")

print("IMPORTANT scope global file")

class Programmer(object):
    print(
            "IMPORTANT trong class Programmer van run binh thuong  cung nhu la scope global file"
        )

    program = f"{'':*<10}class attribute"

    age = Descriptor()    #run __set_name__(self, owner, name)
    salary = Descriptor() #run __set_name__(self, owner, name)
    rating = Descriptor() #run __set_name__(self, owner, name)
    # khi class attrs = descriptor trung ten instance attrs, thi se call class attr, default call instance attrs

    def __init__(self, age, salary, rating):
        self.age = age       #run Descriptor.__set__(self, instance, value):
        self.salary = salary #run Descriptor.__set__(self, instance, value):
        self.rating = rating #run Descriptor.__set__(self, instance, value):
        
        self.program = f"{'':#<10}instance attribute trong __init__"

print()

pro = Programmer(28, 5000, 10) #run Descriptor.__set__(self, instance, value): 3 lan
print()
print(f"{pro.age = }") #run Descriptor.__get__(self, instance, owner):

print()
print(f"{pro.salary = }")


# In[2]:


print(f"{'LazyProperty':-^85}")

class LazyProperty:
    def __init__(self, function):
        print("LazyProperty.__init__")

        self.function = function
        self.funcname = function.__name__

    def __get__(self, instance, owner=None) -> object:
        print("LazyProperty.__get__")

        instance.__dict__[self.funcname] = self.function(instance)
        # deepthought.meaning_of_life = meaning_of_life(instance)=42
        return instance.__dict__[self.funcname]

    # def __set__(self, instance, value):
    #     pass

class DeepThought:

    @LazyProperty
    def meaning_of_life(self): # run LazyProperty.__get__
        time.sleep(3)
        return 42

    #deepthought.meaning_of_life lan dau se run run LazyProperty.__get__
    #deepthought.meaning_of_life lan sau chi lay value=42 tu __dict__
    #voi dieu kien ko co khai bao __set__
    
deepthought = DeepThought()
print(vars(deepthought))

print(deepthought.meaning_of_life)
print(deepthought.meaning_of_life)
print(deepthought.meaning_of_life)

print(vars(deepthought))


# In[3]:


print(f"{'EvenNumber':-^85}")

class EvenNumber:
    def __set_name__(self, owner, name):
        print("EvenNumber.__set_name__")
        print(f"owner: {owner}\nname: {name}")
        self.name = name

    def __get__(self, instance, owner=None) -> object:
        print("EvenNumber.__get__")
        return instance.__dict__.get(self.name) or 0

    def __set__(self, instance, value) -> None:
        print("EvenNumer.__set__")
        instance.__dict__[self.name] = (value if value % 2 == 0 else 0)

class Values:
    value1 = EvenNumber() #run EvenNumber.__set_name__
    value2 = EvenNumber() #run EvenNumber.__set_name__
    value3 = EvenNumber() #run EvenNumber.__set_name__
    """
        khai bao __get__, __set__ cung nhu getter va setter, nhung dung cho
        class attributes.
        avoid lap lai code DRY = tranh tao qua nhieu getter setter voi cung type value
    """

my_values = Values() 
print()
my_values.value1 = 1
my_values.value2 = 4
print()
print(f"{my_values.value1 = }")
print(f"{my_values.value2 = }")

