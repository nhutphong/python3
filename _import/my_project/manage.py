import sys
import os

note = """

    file manage.py la setup my_project, tuyet doi NOT relative import=(dot=.) trong no
    my_project> python3 manage.py NOT working if use relative import

"""

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