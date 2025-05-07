import unittest
from katas.is_unique_str import is_unique


class Test(unittest.TestCase):
    def test1(self):
        self.assertFalse(is_unique("Hello"))

    def test2(self):
        self.assertTrue(is_unique("World"))

    def test3(self):
        self.assertTrue(is_unique("Python"))

    def test4(self):
        self.assertFalse(is_unique("Unique"))

    def test5(self):
        self.assertFalse(is_unique("Aa"))

    def test6(self):
        self.assertTrue(is_unique("1234567890"))

    def test7(self):
        self.assertFalse(is_unique("123123"))

    def test8(self):
        self.assertTrue(is_unique("!@#$%^&*()"))

    def test9(self):
        self.assertFalse(is_unique("The quick brown fox jumps over the lazy dog"))

    def test10(self):
        self.assertTrue(is_unique("ZxCvBnM,.<>?/"))                     