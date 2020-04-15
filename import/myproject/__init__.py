
__all__ = ["aaa", "aaa2", "bbb", "bbb2"]


print()
print("tao la myproject __init__.py")
import sys
print(sys.path)

from .moduleA import *
from .moduleB import *
