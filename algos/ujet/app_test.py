import unittest

from app import Solutions


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.solutions = Solutions()

    def test_fun1_1(self):
        self.assertEqual(self.solutions.fun1(56), 2)

    def test_fun1_2(self):
        self.assertEqual(self.solutions.fun1(8698), 4)

    def test_fun1_3(self):
        self.assertEqual(self.solutions.fun1(12794), 5)

    def test_fun1_4(self):
        self.assertEqual(self.solutions.fun1(100), 3)

    def test_fun2_1(self):
        self.assertEqual(self.solutions.fun2([8, 13, 2, 9, 5, 1, 3, 11, -1, 7]), 10)

    def test_fun2_2(self):
        self.assertEqual(self.solutions.fun2([7, 2, 8, 5, 9, 6, 2, 8]), 7)
