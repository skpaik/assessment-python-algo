import unittest

from app import Solutions


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.solutions = Solutions()

    def test_givenNumber_56(self):
        self.assertEqual(self.solutions.givenNumber(56), 2)

    def test_givenNumber_8698(self):
        self.assertEqual(self.solutions.givenNumber(8698), 4)

    def test_givenNumber_12764(self):
        self.assertEqual(self.solutions.givenNumber(12794), 5)

    def test_givenNumber_100(self):
        self.assertEqual(self.solutions.givenNumber(100), 3)

    def test_diffLarger_1(self):
        self.assertEqual(self.solutions.diffLarger([8, 13, 2, 9, 5, 1, 3, 11, -1, 7]), 10)

    def test_diffLarger_2(self):
        self.assertEqual(self.solutions.diffLarger([7, 2, 8, 5, 9, 6, 2, 8]), 7)
