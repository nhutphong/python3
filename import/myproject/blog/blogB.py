
__all__ = ["yyy", "yyy2"]

from .blogA import xxx
from myproject.product.proA import zzz #cach1
# from ..product.proA import zzz #cach2

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