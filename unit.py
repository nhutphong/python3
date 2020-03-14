import unittest
import os
import sys
# sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

from test import add


class TestCheck(unittest.TestCase):
    def check_add(self):
        self.assertEqual(test.add(5,4), 9)


if __name__ == '__main__':
    unittest.main()
