import unittest
from katas.do_n_times import do_n_times
import io
from contextlib import redirect_stdout


def func():
    print("hello world!")

def test_func(n):
    output = io.StringIO()
    with redirect_stdout(output):
        do_n_times(func(), 1)
    captured_output = output.getvalue()
    str_test = ""
    n = 1
    for i in range(n):
        str_test += "hello world!\n"
    return captured_output,str_test

class Test(unittest.TestCase):
    def test1(self):
        captured_output,str_test = test_func(1)
        self.assertEqual(captured_output, str_test)

    def test2(self):
        captured_output, str_test = test_func(2)
        self.assertEqual(captured_output, str_test)

    def test3(self):
        captured_output, str_test = test_func(3)
        self.assertEqual(captured_output, str_test)

    def test4(self):
        captured_output, str_test = test_func(4)
        self.assertEqual(captured_output, str_test)

    def test5(self):
        captured_output, str_test = test_func(5)
        self.assertEqual(captured_output, str_test)

    def test6(self):
        captured_output, str_test = test_func(6)
        self.assertEqual(captured_output, str_test)

    def test7(self):
        captured_output, str_test = test_func(7)
        self.assertEqual(captured_output, str_test)

    def test8(self):
        captured_output, str_test = test_func(8)
        self.assertEqual(captured_output, str_test)

    def test9(self):
        captured_output, str_test = test_func(9)
        self.assertEqual(captured_output, str_test)

    def test10(self):
        captured_output, str_test = test_func(10)
        self.assertEqual(captured_output, str_test)

