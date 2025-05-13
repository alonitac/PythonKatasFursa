import unittest
from katas.word_count import count_words

class TestTrueCount(unittest.TestCase):

    def test_1(self):
        self.assertEqual(count_words("Today is 22 April 2025."), 5)

    def test_2(self):
        self.assertEqual(count_words(""), 0)

    def test_3(self):
        self.assertEqual(count_words(" . "), 0)

    def test_4(self):
        self.assertEqual(count_words("."), 0)

    def test_5(self):
        self.assertEqual(count_words("My name is majd , and i love Linux."), 8)

    def test_6(self):
        self.assertEqual(count_words("My name is majd , and i love Linux ."), 8)

    def test_7(self):
        self.assertEqual(count_words("a b c d , e f , g h i ."), 9) 

    def test_8(self):
        self.assertEqual(count_words("ma , jd"), 2) 

    def test_9(self):
        self.assertEqual(count_words("hi how are you today ."), 5) 

    def test_10(self):
        self.assertEqual(count_words("I am fine. , , , ,,,,"), 3)                


if __name__ == '__main__':
    unittest.main()
