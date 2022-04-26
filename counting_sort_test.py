import unittest
from counting_sort import counting_sort


class BubbleSortTestCase(unittest.TestCase):
    def setUp(self):
        self.test_input = [2, 3, 8, -5, 4, -2, 6, 7, 9, 3, 4, 6]
        self.test_output = [9, 8, 7, 6, 6, 4, 4, 3, 3, 2, -2, -5]

    def test_counting_method(self):
        result = counting_sort(self.test_input)
        self.assertEqual(result, self.test_output)

    def tearDown(self):
        del self.test_input
        del self.test_output


if __name__ == '__main__':
    unittest.main()