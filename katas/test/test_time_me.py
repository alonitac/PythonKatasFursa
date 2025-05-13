import unittest
from katas.time_me import measure_execution_time
import time

def test1_func():
    time.sleep(0.5)

def test2_func():
    print("Hello world!")

def test3_func():
    time.sleep(1)

def test4_func():
    for _ in range(1000):
        pass

def test5_func():
    time.sleep(0.05)

def test6_func():
    _ = 1
    for i in range(1, 10000):
        _ *= i

def test7_func():
    time.sleep(0.2)


class TestMeasureExecutionTime(unittest.TestCase):

    def test1(self):
        time_taken = measure_execution_time(test1_func)
        self.assertTrue(abs(time_taken - 500) < 20)

    def test2(self):
        time_taken = measure_execution_time(test2_func)
        self.assertTrue(time_taken < 10)

    def test3(self):
        time_taken = measure_execution_time(test3_func)
        self.assertTrue(abs(time_taken - 1000) < 20)

    def test4(self):
        time_taken = measure_execution_time(test4_func)
        print(f'time_taken_4 = {time_taken}')
        self.assertTrue(time_taken < 10)

    def test5(self):
        time_taken = measure_execution_time(test5_func)
        print(f'time_taken_5 = {time_taken}')
        self.assertTrue(abs(time_taken - 50) < 20)

    def test6(self):
        time_taken = measure_execution_time(test6_func)
        print(f'time_taken_6 = {time_taken}')
        self.assertTrue(time_taken > 0)

    def test7(self):
        time_taken = measure_execution_time(test7_func)
        print(f'time_taken_7 = {time_taken}')
        self.assertTrue(abs(time_taken - 200) < 20)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
