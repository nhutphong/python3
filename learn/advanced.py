

===============================================================================

                            TYPE NAME VARIABLE

VARIABLE
name => chung -> ca nhan(duy nhat)
theo qui tac giam dan
int   = iname
str   = sname => sperson_nhut, sperson_phong
byte  = bname = b'phong'

container:
tuple = tnames
list  = lnames
dict  = dnames
set   = senames
khi for tname in tnames => nen bo s item

re      = rname
pattern = pname


FUNCTION
name nen dac dong tu, ngan ngon, dung muc dich ... => setname(), getname(), isname()


CLASS
name nen dat danh tu: Product, Person, ...

private method, variable in class:

_underscore = "private underscore"
obj.<tab> se khong thay trong goi y code, co the dung dir(obj), co the truy cap obj._<private_name>

__double_underscore = "private double underscore"
khong the truy cap bang ten da khi bao, phai dung
    obj._classname__<private_name>

voi method cung tuong tu


===============================================================================

protocol = 'http nntp smtp pop3 imap telnet ftp gopher'

help(<['keywords', 'topics', ]>)
sys.path = [$PATH]
sys.modules = {packages}



numeric: int(), float(), complex()
stirng: str()

container: tuple(), list(), dict(), set()

1 == 1.0 == True
0 == False

a % b = lay du
a // b = lay nguyen
a ** b = a mu b

change itself
+=, -=, *=, /=, //=, %=, **

a != b
a == b : so sanh value
a is b : so sanh refer trong RAM duy nhat

and, or, not
a is b
a is not b
a in b
a not in b

8<<3 => 8 * (2*2*2) => 2 mu 3 <=> operator.lshift(8,3)

100>>4 => 100 / (2*2*2*2) => 2 mu 4 <=> operator.rshift(100,4)


for value in list: => value
for index in range(len(list)): => index

for key in dict: => chay -> key
for key, valllue in dict.items(): => key and value

ls[(len(ls)-1) -(x) : 0 +(x) -1  : -1 ] chuẩn = viết hàm xử lý
bỏ 2 pt đầu và 2 pt cuối : ls [ len(ls) – 3 : 0+1 : -1] tính nhanh
vd : ls[2:7:1] thuận <=> ls[6:1:-1] nghịch
range(1,11,1) = tang 1 to 10
range(11,1,-1) = giam 11 to 2

int, str khi gan = new_name la kieu gan tham_tri(value) khi no thay doi KO lam thay doi gia tri ban dau

list, dict (<container>) khi gan = new_name la kieu gan tham_bien(id) khi no thay doi cung lam thay doi gia tri ban dau
id => vung nho duy nhat trong RAM
dung .copy() cho list, dict thanh tham_tri(value), new_name=[:]

===============================================================================

code doc tu TRAI -> PHAI , TREN XUONG DUOI
if, elif, else: dieu kien nen ghi tu nho -> lon, neu 1 dieu kien if bao gom lun
1 dieu kien cua if khac, thi no nen dung sau

formater string f""
print("my '{1[kind]}' run '{0.platform}'".format(sys, {'kind': 'Laptop Dell'}))
# new
print(f"{ho:!<10} {ten:*>10} python run {sys.platform:$^20}")

short_hand
print("A") if a > b else print("=") if a == b else print("B")
phai co ca if va else moi chay

constants defined to be false: None and False.
zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
empty sequences and collections: '', (), [], {}, set(), range(0)
đưa vào if, while đều là False

cách 1: list comprehensions: filterring
lst = [x for x in range(11) if x % 2 == 0] = > [0, 2, 4, 6, 8, 10]

cách 2
lst = []
for x in range(11):
    if x % 2 == 0:
        lst.append(x)

lst = [0, 2, 4, 6, 8, 10]
cách 1 và cách 2 như nhau

nested for comprehension
ldata = [[con for con in cha if con%2==0] for cha in ong]

dict comprehension
ddata = {k:v for k, v in dproducts}
chan_le = {key:'le' if key%2 else 'chan' for key in range(11)}
chan = {key:'chan' for key in range(11) if key%2==0}
le = {key:'le' for key in range(11) if key%2}

tuple comprehension
tdata = (col for col in range(50) if col%3)     => tuple()

lambda x, y: x+y


def square(x, y): return x > y


def square1(x, y):
    return x > y


square <=> square1

example = square(3,5) = return 3+5 = 8
khi goi function() = return <ketqua>


iterable generator
gen1 = (i for i in range(10)) = > () = generator, [] = list comprehension
gen1 chi dung dc 1 lan trong for

g = gen() # nen create obj g => next(g) <-> ko nen next(generator())
chay for lan dau tien buoc phai dung next(g)
bat dau tu row=2 dung them duoc g.send(value) de bat dau for row=2

next(g) => chay for row=1 roi toi #1 thoat
# next bat dau chay 1 lan for gap yield=return thi stop

g.send(gui=value) =>  chay #2 thoat => xong vong lap 1
nếu có 5 yield thì phải next(g) thêm 3 lần sẽ hết 1 vòng for row=1

bat dau row=2 thi next(g) or g.send(value) => s.send(value) 4 lan nua se het row=2

yield bắt buộc trong func(), và phải dùng for mới truy xuất được phần tử x
lis                   = [list_comprehension] []
generator_expresssion = (list_comprehension) ()

def yie():
    yield from iterable

(el,...),(el...),(),(), ... generator
===============================================================================

built - in function:
map(func(a, b, c), *iterables ...) phai co 3 iterables
filter(func(item)=True or False, iterable) => vi chi co 1 iterable nen func chi co 1 param

from functools import reduce
reduce(function, sequence, initial)

iterables = sequence

cities = ['NewYork', 'Paris', 'HaNoi', 'Milan']
for index, city in enumerate(cities):
    print(index, city)

enumerate(iterable) = them index cho value khi dung vong lap(for, ...)
nên dùng list(enumerate(iterable)) = để chứa các cặp[(), (), (), ...]
x_list = [1, 3, 5]
y_list = [6, 8, 10]

list(zip(x_list, , y_list)) = [(1, 6), (3, 8), (5, 10)] = ghép các value có cùng index của iterable thành các cặp tuple(), (), (), ...
nên dùng list(zip(x_list, , y_list)) = để bao lại

zip(), enumerate(), khi đưa vào for thì ko cần list() bao lại(container)
a, b = 10, 5
a, b = b, a

person = {'name': 'phong', 'age': 25, 'gender': 'male'}
# nhanh hon la dung if else => clean code
per_age = person.get('age', 'unknown')
print(per_age)

data structure = {'key': [{}, {}, {}...],...}
playlist = {
    'title': 'patagonia bus',
    'author': 'colt steele',
    'song': [
        {'title': 'song1', 'artist': ['blue'], 'duration': 2.5},
        {'title': 'song2', 'artist': ['kitty', 'djcat'], 'duration': 5.25},
        {'title': 'meewmeow', 'artist': ['garfield'], 'duration': 2.0}
    ]
}

===============================================================================

getattr(obj, name[, default])   Trả về giá trị của thuộc tính, hoặc trả về giá trị mặc định nếu đối tượng không có thuộc tính này.

hasattr(obj, name)  Kiểm tra xem đối tượng này có thuộc tính cho bởi tham số 'name' hay không. = > True or False

setattr(obj, name, value)   Sét giá trị vào thuộc tính. Nếu thuộc tính không tồn tại, thì nó sẽ được tạo ra.

delattr(obj, name)  Xóa bỏ thuộc tính.

Standard library

Special attributes:
obj.__dict__: {...} chứa tất cả các attribute thuộc tính của obj vừa tạo
obj.__doc__ Trả về chuỗi mô tả về class, hoặc trả về None nếu nó không được định nghĩa
obj.__class__   Trả về một đối tượng, chứa thông tin về lớp, đối tượng này có nhiều thuộc tính có ích, trong đó có thuộc tính __name__.
obj.__class__.__name__: Tên của class
obj.__module__  Trả về tên module(filename) của lớp, hoặc trả về "__main__" nếu lớp đó được định nghĩa trong module đang được chạy.
print(__file__) => name_file dang chay

type(obj) == obj.__class__ = <class 'int'>

===============================================================================

Special method:

x < y calls x.__lt__(y),
x <= y calls x.__le__(y),
x == y calls x.__eq__(y),
x != y calls x.__ne__(y),
x > y calls x.__gt__(y),
x >= y calls x.__ge__(y)
'o' in name <=> name.__contains__('o')

del obj = > sẽ chạy __del__(self): trong class của obj đó: nếu có __del__() tồn tại trong class
str(obj), print(obj) = sẽ chạy __str__(self) nếu có tồn tại trong class
repr(obj) = > sẽ chạy __repr__(self), trong terminal python:
khi str(), repr() = > return string - nhung repr() se them quotes('')
la se them '' o dau va cuoi 'string'
name_obj -> press < enter > sẽ chạy __repr__(self)
len(obj) = > run __len__(self)
ọbj={attribute: value, ...} = > __getitem__(self) nếu có

===============================================================================

làm việc với file = nen dung with cho open(file) no se tu file.close()
open('file_name') => iterators -> line1, line2, ...
with obj_file as ins:
    = > __enter__(self)
    ins.write("nhutphong")
    """run het khoi with moi chay __exit__(self)"""

    = > __exit__(self)


a = 'phong', b = 'phong' = > a == b -> True
a is b -> True(cung id)
c = 5, d = 5 = >            c == d -> True
c is d -> True(cung id)
str, int: khi = value thi cung = id

list, dict, tuple: khi = value, nhung id ko giong nhau, lis[1, 2, 3] is lis1[1, 2, 3] -> False
lis = [1, 2, 3]
lis1 = lis = > khi gan nhu vay lis1 refer lis nen cung value va cung id = True
khi lis hay lis1 thay doi thi thang con lai cung thay doi

if, elif, while < 0, '', (), [], {}, None > :
    khi cac gia tri empty = > thi se la False


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

    def __contains__(self):
        return member in self._member


myclass = MyNumbers()
for x in myclass:
    print(x)
for = > cũng gọi __contains__(self) nhưng nếu có __iter__(self) thì __iter__(self) sẽ được ưu tiên
khi for chạy lần đầu tiên:
method __iter__() sẽ chạy đầu tiên rồi tới __next__() sau đó print(x)
for lần 2 trở đi sẽ chạy method __next__() sau đó print(x), ko bao giờ chạy __iter__() nữa
iter(obj) = > __iter__(self)
next(obj) = > __next__(self)

===============================================================================

nonlocal <name> => bien name se theo gia tri nonlocal neu call trong cac funtion() long nhau, khong phai global trong file.py

global name1 = > toan file.py
nhưng khi trong trong các functions() lòng nhau thì nonlocal sẽ được ưu tiên trước global, nếu global có trong các function()

co the print(name_variable) nhung neu muon thay doi gia tri thi phai
them global | nonlocal name_variable

unpack *list and **dict
a, b, ... = dict = > a, b... sẽ lấy các keys
a, b, ... = dict.values() = > a, b... sẽ lấy các values

function(*dict) = > truyền các keys vào function
function(**dict) = > tryền các values vào function


def function():


def main():
    print(f"Tao la test.py __name__: {__name__}")


def main_1():
    print(f"Tao la main_1() thuoc: {__name__}.py")


if __name__ == '__main__':
    print(f"chỉ run trên file.py của mình")
    print(f"{__name__}=='__main__")
    main()
else:
    print(f"khi duoc import se run dau tien")
    print("Run khi file.py duoc import!!!")
    print(f"__name__ != '__main__' ")
    main_1()
