
print("Tao la moduleZ.py start")
import os
import sys

NOTE_TWO = "CACH 2 folder gan file nhat"
# fname = os.path.abspath(__file__)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(fname)))
# sys.path.insert(0, BASE_DIR)

from myproject.blog.moduleC import xxx #cach 1

NOTE = """CACH 1 folder ngoai myproject
	ternimal>/root/Desktop/: python3 -m package.subpackage2.moduleX
	khi run cau len tren <=> da them sys.path.insert(0, '/root/Desktop')
	
	va run cac files __init__.py khi di qua package tuong ung
	"""

print("Tao la moduleZ.py end")

def zzz():
	print("Tao la zzz() of moduleZ.py")


if __name__ == '__main__':
	xxx()

	# import os
	# fname = os.path.abspath(__file__)
	# print(fname)

	# print(os.path.dirname(fname))
	# print(os.path.dirname(os.path.dirname(fname)))
	# print(os.path.dirname(os.path.dirname(os.path.dirname(fname))))
