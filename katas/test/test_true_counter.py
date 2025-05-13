import unittest
from katas.true_counter import count_true_values

class TestTrueCount(unittest.TestCase):

    def test_1(self):
        self.assertEqual(count_true_values([True, True, True]),3)

    def test_2(self):
        self.assertEqual(count_true_values([False, False, False]), 0)

    def test_3(self):
        self.assertEqual(count_true_values([True, False, True, False]), 2)

    def test_4(self):
        self.assertEqual(count_true_values([]), 0)

    def test_5(self):
        self.assertEqual(count_true_values([False, False, False]), 0)

    def test_6(self):
        self.assertEqual(count_true_values([True]), 1)

    def test_7(self):
        self.assertEqual(count_true_values([False]), 0)

    def test_8(self):
        self.assertEqual(count_true_values([False,False,False,True,True,False,True,False,False,True,True]), 5)

    def test_9(self):
        self.assertEqual(count_true_values([False,False,True,True]), 2) 

    def test_10(self):
        self.assertEqual(count_true_values([True,True,True,True,True,True,True,True,True,True,False]), 10)                   


if __name__ == '__main__':
    unittest.main()
