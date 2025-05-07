import unittest
from katas.list_diff import find_difference


class TestHelloWorld(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find_difference([10, 3, 5, 6, 20, -2]), 22)

    def test_2(self):
        self.assertEqual(find_difference([1, 2, 3, 4, 5]), 4)

    def test_3(self):
        self.assertEqual(find_difference([-5, -5, 7]), 12)

    def test_4(self):
        self.assertEqual(find_difference([-10, -5, 0, 5, 10]), 20)

    def test_5(self):
        self.assertEqual(find_difference([42]), 0)

    def test_6(self):
        self.assertEqual(find_difference([10, 20, 30, 20, 10]), 20)

    def test_7(self):
        self.assertEqual(find_difference([40,50,60,-60,-50,-40]), 120)  

    def test_8(self):
        self.assertEqual(find_difference([1, 1, 1, 1, 2]), 1)  

    def test_9(self):
        self.assertEqual(find_difference([]), 0)

    def test_10(self):
        self.assertEqual(find_difference([9, 8, 7, 6, 9]), 3)                        