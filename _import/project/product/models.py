


__all__ = ['model1']


import os
import sys

NOTE_TWO = "CACH 2 folder gan file nhat"
# fname = os.path.abspath(__file__)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(fname)))
# sys.path.insert(0, BASE_DIR)

NOTE = """CACH 1 folder ngoai myproject
	ternimal>/root/Desktop/: python3 -m package.subpackage2.moduleX
	khi run cau len tren <=> da them sys.path.insert(0, '/root/Desktop')
	
	va run cac files __init__.py khi di qua package tuong ung
	"""

def model1():
	print("Tao la model1() of product.models.py")


if __name__ == '__main__':
    print("product.models.py tu chay")
else:
    print("product.models.py duoc import")