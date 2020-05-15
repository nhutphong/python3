import argparse
from utils import design

#run:  python3 fromfile.py @args.txt
my_parser = argparse.ArgumentParser(
        description='doc args tu args.txt',
        epilog='ban thich program khong!!!',
        fromfile_prefix_chars='@'
    )

#line1 ben file args.txt
my_parser.add_argument('name',
                       help='a first argument')

#line2
my_parser.add_argument('old',
                       help='a second argument')

#line3
my_parser.add_argument('sex',
                       help='a third argument')

#line4
my_parser.add_argument('city',
                       help='a fourth argument')

my_parser.add_argument('-v',
                       '--verbose',
                       action='store_true',
                       help='an optional argument')

# Execute parse_args()
args = my_parser.parse_args()
print(f"args: {args}")
print()

print(f"vars(args): {vars(args)}")
print()

design(args.name)
design(args.old)
design(args.sex)
design(args.city)


print('If you read this line it means that you have provided '
      'all the parameters')