import unittest
import quick_sort


class BubbleSortTestCase(unittest.TestCase):
    def setUp(self):
        self.test_input = [2, 35, 8, 3, 4, 0, 6, 7, 9, 3, 4, 6]
        self.test_output = [35, 9, 8, 7, 6, 6, 4, 4, 3, 3, 2, 0]

    def test_quick_sort_method(self):
        quick_sort.quick_sort(self.test_input, 0, len(self.test_input)-1)
        self.assertEqual(self.test_input, self.test_output)

    def tearDown(self):
        del self.test_input
        del self.test_output


if __name__ == '__main__':
    unittest.main()