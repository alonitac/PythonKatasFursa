import unittest
from katas.reduce_list import reduce_array

class Test(unittest.TestCase):
    def test1(self):
        nums = [1, 2, 3, 4, 5]
        reduce_array(nums)
        self.assertEqual(nums, [1, 1, 1, 1, 1])

    def test2(self):
        nums = [10, 10, 10, 10]
        reduce_array(nums)
        self.assertEqual(nums, [10, 0, 0, 0])

    def test3(self):
        nums = [5]
        reduce_array(nums)
        self.assertEqual(nums, [5])

    def test4(self):
        nums = [10, 20, 15, 25, 10]
        reduce_array(nums)
        self.assertEqual(nums, [10, 10, -5, 10, -15])

    def test5(self):
        nums = [0, 0, 0, 1]
        reduce_array(nums)
        self.assertEqual(nums, [0, 0, 0, 1])

    def test6(self):
        nums = [-1, -2, -3, -4]
        reduce_array(nums)
        self.assertEqual(nums, [-1, -1, -1, -1])

    def test7(self):
        nums = [100, 50, 25, 12]
        reduce_array(nums)
        self.assertEqual(nums, [100, -50, -25, -13])

    def test8(self):
        nums = [3, 1, 4, 1, 5, 9]
        reduce_array(nums)
        self.assertEqual(nums, [3, -2, 3, -3, 4, 4]) 

    def test9(self):
        nums = [0, 100, 0, 100]
        reduce_array(nums)
        self.assertEqual(nums, [0, 100, -100, 100]) 

    def test10(self):
        nums = [7, 7, 14, 21, 28]
        reduce_array(nums)
        self.assertEqual(nums, [7, 0, 7, 7, 7])