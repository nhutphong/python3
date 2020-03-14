import os
import sys

print(f"{os.path.realpath(__file__)}")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print(f"abspath: {BASE_DIR}")


sys.path.append(BASE_DIR)
from sub_3.mod_3 import my_function3


def my_function1():
	return f"my_function1 keke"


def my_function2():
	return f"my_function2 aaaaaaaaa"


if __name__ == '__main__':
	print(my_function3())