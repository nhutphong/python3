
__all__ = ["yyy", "yyy2"]

print("Tao la moduleD.py")
from moduleC import xxx

def yyy():
	print("tao al yyy() of moduleY.py")


def yyy2():
	print("tao al yyy2() of moduleY.py")

if __name__ == '__main__':
	xxx()