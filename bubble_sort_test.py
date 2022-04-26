import unittest
from bubble_sort import bubble_sort, replace_in_pair


class BubbleSortTestCase(unittest.TestCase):
    def setUp(self):
        self.test_input = [2, 3, 8, -5, 4, -2, 6, 7, 9, 3, 4, 6]
        self.test_output = [9, 8, 7, 6, 6, 4, 4, 3, 3, 2, -2, -5]
        self.x = 4
        self.y = 5

    def test_bubble_sort_all(self):
        result = bubble_sort(self.test_input)
        self.assertEqual(result, self.test_output)

    def test_replace_in_pair(self):
        x, y = replace_in_pair(self.x, self.y)
        self.assertEqual(x, self.y) and self.assertEqual(y, self.x)

    def tearDown(self):
        del self.test_input
        del self.test_output
        del self.x
        del self.y


if __name__ == '__main__':
    unittest.main()