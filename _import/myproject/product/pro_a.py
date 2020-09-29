

__all__ = ['zzz']
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

def zzz():
	print("Tao la zzz() of proA.py")


if __name__ == '__main__':
    print("pro_a.py tu chay")
else:
    print("pro_a.py duoc import")