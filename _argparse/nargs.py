
"""
?: chi 1 , có thể là default='hhahaha'
*: một số lượng giá trị linh hoạt, sẽ được tập hợp vào list[]
+: bat buoc 1 value, list[]
argparse.REMAINDER: tất cả các giá trị còn lại trong dòng lệnh list[]
"""

import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument(
                        'input',
                        action='store',
        )
my_parser.add_argument(
                        'remainder',
                        action='store',
                        nargs=argparse.REMAINDER,
        )

args = my_parser.parse_args()

print(args.input)
print(args.remainder)