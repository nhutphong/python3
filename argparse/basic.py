import argparse

my_parser = argparse.ArgumentParser(
                        prog='choices',
                        usage='%(prog)s [options] path',
                        description='tao la description',
                        epilog='tao la epilog',
                    ) #prefix_chars='/' /h, /num

my_parser.add_argument(
            '-i',
            '--num',
             action='store', 
             type=int, 
             choices=range(1, 5),
             help="-i from 1 to 4",
             metavar="NUM",
             dest="number_file"
         )

args = my_parser.parse_args()

print(vars(args))

# default: args.number vi co dest="number_file" nen la 
        #  args.number_file
print(args.number_file)