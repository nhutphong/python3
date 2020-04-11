
import time
import random as rd


class Sharp:

    def __init__(self, coldf=10, rowdf=5):
        self.__col = coldf
        self.__row = rowdf

    # @property=getter phai dung truoc @setter
    @property
    def col(self):
        return self.__col

    # dung self.col = value
    @col.setter
    def col(self, value):

        self.__col = value

    @property
    def row(self):
        return self.__row

    @row.setter
    def row(self, value):

        self.__row = value

    def add(self):
        return self.col + self.row

    def mul(self):
        # run 2 setter @col, @row
        # self.col = col
        # self.row = row

        return self.col * self.row


class Image(object):
    """docstring for Image"""


    def __init__(self, color='red', sharp_class=Sharp()):
        self.__color = color
        self.__sharp = sharp_class

    @property
    def sharp(self):
        return self.__sharp

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new_color):
        self.__color = new_color


class Sequence:  # Iterator
    """dung class khai bao 1 Iterator"""

    def __init__(self):
        self.x = 0

    def __iter__(self):
        return self

    def __next__(self):
            self.x += 1
            if self.x > 11:
                    raise StopIteration

            return self.x ** self.x


class SieuNhan:
    suc_manh = 50

    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac

    # classmethod => thường được dung xử lý trc 1 vài vấn đề, sau đó tao ob
   	# can dung toi class
    @classmethod
    def from_string(cls, s):  # thường những phương thức xử lí thế này hay có tên là from…
        lst = s.split('-')
        new_lst = [st.strip() for st in lst]
        ten, vu_khi, mau_sac = new_lst
        return cls(ten, vu_khi, mau_sac)

    # khong dung gi het
    @staticmethod
    def bien_hinh():
        print("1, 2, 3. Sieu nhan bien hinh")

# g = generator() => next(g) run toi yield_1 dung, next(g) run toi yield_2 dung


def generator(stop=20):
    """ phai la function chua khoa yield"""

    start = 0
    while True:

        if start >= stop:
            break

        print(f"{start}*2 yield_111")
        yield start*2  # next(g) lan 1

        print(f"{start}**2 yield_22222222222")
        yield start**2  # next(g) lan 2 ...

        start += 1


def generator_send():
    print("next")
    a = yield  # <None> # next(g) => print(next(g)) => None

    print("send1")
    yield a**2  # g.send(4) => 4*4

    print("next 2")
    b = yield a  # next(g) => print(next(g)) => 4

    print("send 2")
    yield b**3  # g.send(5)


def gen(name='phong'):
    one = yield "tao la one"  # next(g)
    yield one**3  # g.send(3) => 27
    yield from name  # next(g) = 'p', next(g) = 'h', ...,
    # 1 g = gen()
    # 2 next(g) hoac g.send(None)
    # 3 bat buoc g.send(value) => de send value toi one**3 => nhung se show 'p'
    # 4 next(g) cuoi cung se cho return 5**3


""" iterator <=> gen2, tuong tu nhau"""


def iterator(name='phong'):
    return iter(name)

#return iter(name) <=> yield from name

def gen2(name='phong'):
    yield from name


def with_file(file_root, file_new='new_file'):
    with open(file_root,) as f:
        content = f.read()

        with open(file_new, 'w') as new:
            # file=new => cho phep print() tao file tu content xuat ra=prompt
            print(content, 'them noi dung vao cuoi file', file=new)


def print_flush_true(text='phong', *, delay=.5):

    print("flush=True")
    # flush=True => in tu tren xuong cho time.sleep xong roi in tiep
    # flush=Flase => cho time.sleep xong roi moi in 1 luc tat ca
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)

    print()


def print_flush_false(text='phong', delay=.5):

    print("flush=Flase")
    # flush=True => in tu tren xuong cho time.sleep xong roi in tiep
    # flush=Flase => cho time.sleep xong roi moi in 1 luc tat ca
    for c in text:
        print(c, end='')  # default flush=False
        time.sleep(delay)

    print()


def progress(stop=101, delay=.5):
    for col in range(stop):
        time.sleep(delay)
        print(
            f"    [Progress: {col}%] [{'#'*int(round(col/2)):.<50}]", end='\r')
    # Carriage Return: chuyển con trỏ về đầu dòng


def func(a, b, *, name='phong', old=26):
        print(a, b, name='tan', old=30)
# call func(1,2,name='tan', old=38) => co * dung truoc thi phai them ten param_name='phong', old=38
# func(1,2, 'phong', 25) => error


def operator(op='cong'):
        opera = {'cong': lambda x, y: x+y, 'tru': lambda x, y: x -
            y, 'nhan': lambda x, y: x*y, 'chia': lambda x, y: x/y}
        return opera.get(op, lambda x, y: "error opera")


def ring(stop=10):
    print("RING RING RING")

    loop = 0
    run = True
    while run:
        dung = rd.randint(1, stop)

        if dung == stop:
            print(f"END {stop:-^20}")
            break
        else:
            loop += 1
            print(f"RING{loop} {dung:*>20} \a")
            time.sleep(1)

# recursion= de qui


def cal_sum(lst):
    return 0 if not lst else lst[0] + cal_sum(lst[1:])


def format_string():
    so = 5_400_300.94817483434189
    # chi nhan int, float va string
    # f"{expr => code binh thuong: format }"" number
    # f"{'phong':#<30 }" => string can trai "phong" + "#"*25
    print(f"{so:,.5f}")


if __name__ == '__main__':
    pass