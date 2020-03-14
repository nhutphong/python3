abs(x) => x ve so duong
round(number, ndigits) => number lam tron so gan nhat
int(x) => number int
float(x) => number float
pow(x, y, z) => x**y % z
sum(iterable, start) = tong item trong iterable
max(iterable, *, default, key) => iterable(int1, int2, ...) phai cung type
min(iterable, *, default, key) => iterable(int1, int2, ...) phai cung type

all(iterable) => True if all item = True
all(iterable=empty) => True
any(iterable) => True if chi can 1 item = True
any(iterable=empty) => False

ord(c) => character in unicode -> int
hex(number) =>
oct(number) =>
chr(i) => int -> unicode
bin(number) => 0b10 1010
ascii(obj) =>
bytes(iterable_of_ints)
bytearray(iterable_of_ints)
memoryview(object)

delattr(obj, name) => del obj.name
divmod(x,y) => tuple (x//y, x%y)
x = 2

eval('x+4') => 6 -> code 1 expression trong eval(exp = +-*/, ** // % => int)
exec(source="name = phong\nprint(name)", globals, locals) -> code binh thuong nhu trong file

getattr(obj, name[, default]) => obj.name => value else AttributeError
hasattr(obj, name) => True if obj.name exist else AttributeError
setattr(obj, name, value) => obj.name = value
isinstance(obj, class_or_tuple) => bool
issubclass(cls, class_or_tuple) => bool
callable(obj) => True if func,class_name exist

globals() => [global_variables]
locals() => [local_variables]
vars(object) => {'__name__':'__main__', ...}

hash(obj) =>
id(obj) => int -> so duy nhat trong Ram

a[1:10:2] = a[slice(1,10,2)]
dir(object) => [attribute_of_class, variables, ...]

zip(iter1, iter2...) =>

map(func, *iterables) =>
filter(function=True|False or None, iterable) =>
from functools import reduce
reduce(function, sequence, initial)

iter(iterable) =>
next(iterator, default) =>

sorted(iterable, key=str.lower, reverse=False) => tang dan theo str.lower
key=my_function
reversed(sequence) => giam dan

list(), dict(), tuple(), set()
x = frozenset(iterable) -> giong set(), dung method() va operator(|, &, ^, -)
cua set() nhung ko co method() change itself(update) cua set()
