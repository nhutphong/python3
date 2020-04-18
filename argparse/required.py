import argparse
"""
    
"""
my_parser = argparse.ArgumentParser()
my_parser.add_argument(
            '-a',
            action='store',
            choices=['head', 'tail'],
            required=True
        )

args = my_parser.parse_args()

print(vars(args))