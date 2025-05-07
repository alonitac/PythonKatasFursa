import unittest
from katas.longest_common_prefix import longest_common_prefix

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(longest_common_prefix(["hello"]), "hello")
    def test2(self):
        self.assertEqual(longest_common_prefix(["flower", "flow", "flight"]), "fl")
    def test3(self):
        self.assertEqual(longest_common_prefix(["dog", "racecar", "car"]), "")
    def test4(self):
        self.assertEqual(longest_common_prefix(["interspecies", "interstellar", "interstate"]), "inters")
    def test5(self):
        self.assertEqual(longest_common_prefix(["majd", "majd", "majd", "majd", "majd"]), "majd")
    def test6(self):
        self.assertEqual(longest_common_prefix(["ab","a"]), "a")
    def test7(self):
        self.assertEqual(longest_common_prefix(["","",""]), "")
    def test8(self):
        self.assertEqual(longest_common_prefix(["aaaaa","aaaa","aaa"]), "aaa")
    def test9(self):
        self.assertEqual(longest_common_prefix(["abcd","abcd","ab"]), "ab")
    def test10(self):
        self.assertEqual(longest_common_prefix(["hi there","hi there!","hi there!!"]), "hi there")