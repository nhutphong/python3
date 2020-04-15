
__all__ = ["xxx", "yyy", "yyy2"]


print()
print("Tao la abc __init__.py")
import sys
print(sys.path)

# trong file __init__.py chi dung relative import
# relative import . or ..

from .moduleC import *
from .moduleD import *
# from ..subpackage1.moduleZ import zzz


# absolute import error
# from moduleX import *
# from moduleY import *