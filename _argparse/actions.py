import argparse

"""
    Positional arguments: python3 test.py thong 27 gialai
    Optional arguments: python3 test.py -n thong -o 27 -c gialai
    co -n, --name, -o, --old
"""

my_parser = argparse.ArgumentParser()
my_parser.version = '1.0'

my_parser.add_argument('-z', '--name', action='store')
# -p or --pi -> se nha pi=3.14
my_parser.add_argument('-p', '--pi', action='store_const', const=3.14)
my_parser.add_argument('-y', '--yes', action='store_true') #t=False
my_parser.add_argument('-n', '--no', action='store_false') #f=True
my_parser.add_argument('-a', '--add', action='append') # -e dung -e thong
my_parser.add_argument('-t', action='append_const', const=42)# -zzz =[42,42,42]
my_parser.add_argument('-c', '--count', action='count') # -ggggg -> g=5
my_parser.add_argument('-i', action='help')
my_parser.add_argument('-j', action='version')

args = my_parser.parse_args()

print(vars(args))