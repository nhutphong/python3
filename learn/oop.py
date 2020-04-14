from abc import ABC, abstractmethod
import string as stg
import random as rd

'''
'''
# class_name.mro() => xem do uu tien thua ke

class PersonAbstact(ABC):
    """ abtract class
    """
    name = None
    age = 0

    def get_name(self):
        print(self.name)

    def get_age(self):
        print(self.age)

    @abstractmethod
    def get_full(self):
        pass

# child class abtract


class Person(PersonAbstact):
    """ để call PersonAbstact phải tạo class Person(PersonAbstact): thừa kế
    và override tất cả các @abstractmethod của PersonAbstract
    """
    name = 'Vo Thanh Phong'
    age = 25

    def getFull(self):
        self.get_name()
        self.get_age()


class Animal:

    """class variables = dùng chung cho tất cả object=instance khi khởi tạo"""
    height = '100'
    # private class variables
    __title = "Wild"
    __ANIMAL = 'TAO LA ANIMAL'

    # private variable and private method không thể truy cập trực tiếp từ obj  
    # obj.__name, obj.__method() sẽ error nếu muốn thì dùng
    # obj._classname__name, obj._classname__method(), hoặc dùng encapsolution
    # encapsolution => tạo method() gọi  private variable, private method()

    # constructor
    def __init__(self, name='Animal'):
        print("ANIMAL CREATED")
        # call private variables = 2 cách = nên dùng Animal.__title để phân biệt với class attributes
        # Animal.__title <==> self.__title

        # class atttributes
        self.name = name
        print(self.name)

    # instance(default) method()
    def who_am_i(self):
        print("I am an animal")

    # private method  => double underscore = __<name>
    def __eat(self):
        print("I am private method __eat()")

    def get_eat(self):
        self.__eat()
        Animal.__eat(self=self)
        print(Animal.__ANIMAL)

    def speak(self):
        raise NotImplementedError("abstract method")

# inheritance = thừa kế


class Dog(Animal):
    """Tao la Doc co cua Animal"""

    def __init__(self, food):
        # Animal.__init__(self)
        # print("DOG CREATED")
        self.food = food

    def eat(self):
        print("I am a dog and eating")

    def speak(self):
        return "dog eat".ljust(20, '$') + '   ' + self.food


class Cat(Animal):
    """Tao la class Cat con cua Animal"""

    def __init__(self, food='lua'):
        # Animal('phong').__init__('nhut') #c2 = run 2 lan __init__()
        # Aniaml('phong') => nhu create a object('phong') = > nen run __init__() 1 lan, roi run __init__('nhut') them 1 lan nua

        # super().__init__('Tao la super')
        # super() == self => nhung super(). dung de goi method Parrent

        Animal.__init__(self, f'Tao la Anaimal.__init__(self,)')  # c1
        # nen dung cach c1
        # khi goi method ma dung ten class phai co self trong method
        # class.instace_method(self,...)

        # print("CAT CREATED")
        self.food = food

    def eat(self):
        print("I am a cat and eating")

    def speak(self):
        return "Cat eat".rjust(20, '!') + f"{self.food:*^20}"

# polymorphism calls class dog.speak() and meo.speak() => có cùng method() speak() polymorphism = gọi nhiều class có cùng tên method()


def polymorphism(dog, meo):
    for pet in [dog, meo]:
        print(type(pet))
        print(pet.speak())


class Foo:
    __age = 25
    '''gia tri ban dau cua cac obj, neu Foo.__age = thay doi, thi obj.__age cung thay doi, => nhung neu obj.__age overwrite thi se ko phu thuoc vao Foo.__age
    khi obj.__age = 20  overwrite new instance attribute
    '''

    def __init__(self, name='phong'):
        self.name = name
        Foo.__full_name = self.name

    def instance_bar(self):
        print(f"instance-method")

    @classmethod
    def class_method(cls):
        print(f"class-method class_method(cls,): {cls.static_bar(Foo.__age)}")
        cls.instance_bar(self=cls)

    ''' không thể call class attributes(object attributes) = self.name trong
    __init__(self)

    self == class_name nhung
    self = obj
    cls = class_name => co the goi cls.instance_method(self=obj,...)
    cls => khi goi @classmethod: cls.class_method(...)

    '''
    @classmethod
    def class_method_2(cls):
        cls.class_method()

    @staticmethod
    def static_method():
        print(f"Tao la static_method()")

    # trong statice method() goi instance method phai co param => self
    # dung ten class de truy cap => class_name.instance_abc(self=class_name)
    # khi coi class method(cls) bo cls vi dung ten class_name.class_method()
    @staticmethod
    def static_bar(number=1):
        Foo.instance_bar(self=Foo)
        Foo.static_method()

        return number * 2

    ''' dung truc tiep ten class de goi class variable

    '''


class Account:

    def __init__(self, first_name=None, last_name=None , age=None, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.__age = age

        # acc = Account('phong', 'nhut', city='dong nai', old=27, country='vn')
        # tao co acc.city, acc.old, acc.country, nho FOR ben duoi
        for attr, value in kwargs.items():
            self.__dict__[attr] = value

    #print(acc)
    def __str__(self):
        return f"Account({self.full_name})"

    #terminal> acc
    def __repr__(self):
        return f"Account({self.full_name})"

    def __setitem__(self, attr, value):
        print('__setitem__')
        # self[attr] = value
        self.__dict__[attr] = value

    def __getitem__(self, attr):
        print("__getitem__")
        # self[::], self[index] #RecursionError
        return self.__dict__[attr]

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age <= 18:
            raise Exception(f"ban chi: {age} tuoi phai 18 tuoi ok ")
        else:
            self.__age = age

    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def from_string(cls, flp_string=''):
        first_name, last_name, pay = flp_string.split('-')
        return cls(first_name, last_name, pay)

    def add_method(self, func): 
        self.__dict__[func.__name__] = func



class Data(object):
    "Day la database"

    def __init__(self):
        self.data = {}
        self.id = 0

    # obj = Data() = repr(self.data)
    def __repr__(self):
        return repr(self.data)

    # obj = Data()
    # obj(value_new='thanh phong')
    # them param cho obj
    def __call__(self, value_new):
        return value_new

    def add(self, name, age, job, live):
        self.id += 1
        self.data.update([(self.id, {'name': name, 'age': age, 'job': job, 'live': live})])

    # obj[key] = values
    def __setitem__(self, key, values):
        name, age, job, city = values.split()
        tinfo = ('name', 'age', 'job', 'city')

        self.data[key] = dict(zip(tinfo, [name, age, job, city]))

    # obj = Data() <=> obj[key] => self.data[key]
    # dict() = key cua attribute self.data[key]
    def __getitem__(self, key):
        return self.data[key] # return value cua attribute


    # cac attribute la la keys cua obj, self.data, self.id
    # obj = {'data':'value1', 'id', 'id1', ...}
    # obj['data'], obj['id']
    # obj = Data() <=> obj[key=self.id, self.data] = obj.id, obj.data

    # attribute la key cua obj[attr]
    # def __getitem__(self, key):
    #     return getattr(self, key) # return value cua attribute


class Fib:
    def __init__(self):
        pass

    def fib(self, n):    # write Fibonacci series up to n
        a, b = 0, 1
        while a < n:
            print(a,)
            a, b = b, a+b


    def fib2(self, n):   # return Fibonacci series up to n
        result = []
        a, b = 0, 1
        while a < n:
            result.append(a)
            a, b = b, a+b
        return result

    def recursive(self, stop=5):
        if stop == 1:
            print(stop)
            return stop
        else:
            print(stop)
            return stop * self.recursive(stop-1)


class Square(object):
    """docstring for Square"""
    def __init__(self, length):
        self.length = length
        self.i = 0

    def __next__(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i**2
            self.i += 1
            return result

    def __iter__(self):
        return self


class Car: 
  
    """Class for Car"""
  
    def __init__(self): 
        self.name = "Car"
  
    def FourWheeler(self): 
        return "FourWheeler"


class Adapter: 
  
    def __init__(self, obj, **car_methods): 
        # obj = Car(), **car_methods <=> wheeler = obj.FourWheeler
        self.obj = obj
        self.__dict__.update(car_methods) 
  
    def __getattr__(self, attr): 
        
        return getattr(self.obj, attr) #return self.obj.attr
  
    def original_dict(self): 
        return self.obj.__dict__ 


def main():
    pass


def note():
    """ obj. call 3 loai method binh thuong ko can self hay cls
        class_name.instance_method(self=class_name, param, ...)
        class_name.class_method(param, ...) ko can cls
        class_name.static_method(param, ...) binh thuong

    """


if __name__ == '__main__':
    pass