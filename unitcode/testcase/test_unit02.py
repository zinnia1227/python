import unittest


class NumbersTest(unittest.TestCase):
    def test_even(self):

        for i in range(0, 5):
                with self.subTest(i=i):
                    self.assertEqual(i % 2, 0)


