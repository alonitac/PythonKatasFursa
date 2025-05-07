import unittest
from katas.matrix_rotate import rotate_matrix
def is_matrices_equal(m1, m2):
    for i in range(len(m1)):
            for j in range(len(m1[0])):
                if m1[i][j] != m2[i][j]:
                    return False
    return True            

class Test(unittest.TestCase):
    def test_1(self):
        m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

        mr = [
        [7,4,1],
        [8,5,2],
        [9,6,3]]
        rotate_matrix(m)

        self.assertTrue(is_matrices_equal(m, mr))

    def test_2(self):
        m = [[1]]

        mr = [[1]]
        rotate_matrix(m)

        self.assertTrue(is_matrices_equal(m, mr))

    def test_3(self):
        m = [[1,2],
             [3,4]]

        mr = [[3,1],
              [4,2]]
        rotate_matrix(m)

        self.assertTrue(is_matrices_equal(m, mr))

    def test_4(self):
        m = [[1,2,3,4],
             [5,6,7,8],
             [9,10,11,12],
             [13,14,15,16]]

        mr = [[13,9,5,1],
              [14,10,6,2],
              [15,11,7,3],
              [16,12,8,4]]
        rotate_matrix(m)

        self.assertTrue(is_matrices_equal(m, mr))

    def test_5(self):
        m = [[1, 2, 3, 4, 5],
             [6, 7, 8, 9, 10],
             [11, 12, 13, 14, 15],
             [16, 17, 18, 19, 20],
             [21, 22, 23, 24, 25]]
        mr = [[21, 16, 11, 6, 1],
              [22, 17, 12, 7, 2],
              [23, 18, 13, 8, 3],
              [24, 19, 14, 9, 4],
              [25, 20, 15, 10, 5]]
        rotate_matrix(m)
        self.assertTrue(is_matrices_equal(m, mr))

    def test_6(self):
        m = [[1, 2, 3, 4, 5, 6],
             [7, 8, 9, 10, 11, 12],
             [13, 14, 15, 16, 17, 18],
             [19, 20, 21, 22, 23, 24],
             [25, 26, 27, 28, 29, 30],
             [31, 32, 33, 34, 35, 36]]
        mr = [[31, 25, 19, 13, 7, 1],
              [32, 26, 20, 14, 8, 2],
              [33, 27, 21, 15, 9, 3],
              [34, 28, 22, 16, 10, 4],
              [35, 29, 23, 17, 11, 5],
              [36, 30, 24, 18, 12, 6]]
        rotate_matrix(m)
        self.assertTrue(is_matrices_equal(m, mr))

    def test_7(self):
        m = [[1, 2, 3, 4, 5, 6, 7],
             [8, 9, 10, 11, 12, 13, 14],
             [15, 16, 17, 18, 19, 20, 21],
             [22, 23, 24, 25, 26, 27, 28],
             [29, 30, 31, 32, 33, 34, 35],
             [36, 37, 38, 39, 40, 41, 42],
             [43, 44, 45, 46, 47, 48, 49]]
        mr = [[43, 36, 29, 22, 15, 8, 1],
              [44, 37, 30, 23, 16, 9, 2],
              [45, 38, 31, 24, 17, 10, 3],
              [46, 39, 32, 25, 18, 11, 4],
              [47, 40, 33, 26, 19, 12, 5],
              [48, 41, 34, 27, 20, 13, 6],
              [49, 42, 35, 28, 21, 14, 7]]
        rotate_matrix(m)
        self.assertTrue(is_matrices_equal(m, mr))

                                    