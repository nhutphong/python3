import sys
import os

# os.system("tree")
print(f"{__file__ = }")

abspath = os.path.abspath(__file__)

print(f"{os.path.expanduser('~') = }")

print(f"{os.path.abspath(__file__) = }")
print(f"{os.path.realpath(__file__) = }")

print(f"lay ten file: {os.path.basename(abspath) = }")
print(f"lay path chua file{os.path.dirname(abspath) = }")

print(f"{os.path.relpath(__file__) = }")

from blog.views import *