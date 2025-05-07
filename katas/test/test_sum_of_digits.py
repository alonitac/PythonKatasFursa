import unittest
from katas.sum_of_digits import sum_of_digits


class TestHelloWorld(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sum_of_digits("123"), 6)

    def test_2(self):
        self.assertEqual(sum_of_digits("abc123"), 6)

    def test_3(self):
        self.assertEqual(sum_of_digits("abc 123 "), 6)

    def test_4(self):
        self.assertEqual(sum_of_digits("abc 1 2 3"), 6)

    def test_5(self):
        self.assertEqual(sum_of_digits("5 cats and 2 dogs"), 7)

    def test_6(self):
        self.assertEqual(sum_of_digits("No digits here!"), 0)

    def test_7(self):
        self.assertEqual(sum_of_digits("9   8 2 1 4 hg 5 agf 6 7 3"), 45)  

    def test_8(self):
        self.assertEqual(sum_of_digits("00000011111"), 5)  

    def test_9(self):
        self.assertEqual(sum_of_digits(""), 0)

    def test_10(self):
        self.assertEqual(sum_of_digits(",,,,0000OOO00001"), 1)                        