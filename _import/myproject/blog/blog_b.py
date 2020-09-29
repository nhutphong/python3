
__all__ = ["yyy", "yyy2"]


note = """
    
    pkg/__init__.py khong dung duoc absolute import

    __init__.py tao hop tat ca modules trong pkg neu can
    file __init__.py dai dien cho package pkg

    from pkg import <class, func, ... nhieu modules>

    neu import cung folder va khac folder
    phai xac dinh folder root/project

    create root/run.py cap cao: chua
        from project.blog.blog_b.py import *

    root> python3 run.py # c1

    or

    root> python3 -m project.blog.blog_b.py # run truc tiep c2

"""


from .blog_a import xxx #.file cung folder
from myproject.product.pro_a import zzz #cach1
# from ..product.proA import zzz #cach2 <..> thay myproject

def yyy():
	print("tao al yyy() of blogB.py")


def yyy2():
	print("tao al yyy2() of blogB.py")


if __name__ == '__main__':
    print("blogB.py tu chay")
    xxx()
    zzz()
else:
    print("blogB.py duoc import")