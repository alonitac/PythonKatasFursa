import unittest
from katas.list_flatten import flatten_list


class TestHelloWorld(unittest.TestCase):
    def test1(self):
        self.assertEqual(flatten_list([1, 2, 3]), [1, 2, 3])

    def test2(self):
        self.assertEqual(flatten_list([1, [2, 3], [4, [5, 6]], 7]), [1, 2, 3, 4, 5, 6, 7])

    def test3(self):
        self.assertEqual(flatten_list([[1], [[2]], [[[3]]]]), [1, 2, 3])

    def test4(self):
        self.assertEqual(flatten_list([]), [])

    def test5(self):
        self.assertEqual(flatten_list([[], [[]], [[[]]]]), [])

    def test6(self):
        self.assertEqual(flatten_list([[[42]]]), [42])

    def test7(self):
        self.assertEqual(flatten_list([1, [2], [], [3, [4, [], [5]]]]), [1, 2, 3, 4, 5])

    def test8(self):
        self.assertEqual(flatten_list([[[[1]], 2], 3, [4, [5, [6, [7, [8]]]]]]), [1, 2, 3, 4, 5, 6, 7, 8])

    def test9(self):
        self.assertEqual(flatten_list([[1, 2], [3, 4], [5, 6]]), [1, 2, 3, 4, 5, 6])

    def test10(self):
        self.assertEqual(flatten_list([[[[1]], [[2]]], [[[3]]]]), [1, 2, 3])
    