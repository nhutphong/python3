
import unittest


important = """

    

    assertEqual(a,b)        a == b
    assertNotEqual(a, b)    a != b
    assertTrue(x)           bool(x) is True
    assertFalse(x)          bool(x) is False
    assertIs(a, b)          a is b
    assertIsNot(a, b)       a is not b
    assertIsNone(x)         x is None
    assertIsNotNone(x)      x is not None
    assertIn(a, b)          a in b
    assertNotIn(a, b)       a not in b

    assertIsInstance(a, b)      instance(a, b)
    assertNotIsInstance(a, b)   not isinstance(a, b)

    assertGreater(a, b)         a > b
    assertGreaterEqual(a, b)    a >= b
    assertLess(a, b)            a < b
    assertLessEqual(a, b)       a <= b

    
    assertAlmostEqual(a, b)     round(a-b, 7) == 0
    assertNotAlmostEqual(a, b)  round(a-b, 7) != 0
    
    assertRegex(s, r)           r.search(s)
    assertNotRegex(s, r)        not r.search(s)
    assertCountEqual(a, b)      a and b have the same elements in the same number, regardless of their order


    2.3. Các function so sánh các kiểu dữ liệu khác nhau.
    Method  Used to compare

    assertMultiLineEqual(a, b)  strings
    assertSequenceEqual(a, b)   sequences
    assertListEqual(a, b)       lists
    assertTupleEqual(a, b)      tuples
    assertSetEqual(a, b)        sets or frozensets
    assertDictEqual(a, b)       dicts
"""

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        print(f"{'':#^80}")
        print("tao la setUp(self)")
        """
            run truoc method can test_names()
            co the tao variable, ... cho cac test_names()
            self.name = 'thong'
            self.old = 31
        """
        self.name = 'thong'
        self.old = 31

    def tearDown(self):
        print("tao la tearDown(self)")
        """
            run sau method can test_names()

        """
        print(f"{'':-^80}")
        print()


    important = "ten method phai bat dau = test_<ten_nao_cung_dc>(self)"
    def test_upper(self):
        print("tao la test_upper(self)")
        print(f"{self.name = } {self.old = }")

        self.assertEqual('python'.upper(), 'PYTHON')

    def test_isupper(self):
        print("tao la test_isupper(self)")
        print(f"{self.name = } {self.old = }")

        self.assertTrue('PYTHON'.isupper())
        self.assertFalse('Python'.isupper())

    def test_islower(self):
        print("tao la test_islower(self)")
        print(f"{self.name = } {self.old = }")

        self.assertTrue('PYTHON'.islower())
        self.assertFalse('Python'.islower())


if __name__ == '__main__':
    unittest.main()