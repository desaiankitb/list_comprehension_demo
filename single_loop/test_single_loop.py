
import unittest
from single_loop_list_comprehension import get_even_numbers

class TestGetEvenNumbers(unittest.TestCase):
    def test_get_even_numbers(self):
        self.assertEqual(get_even_numbers([1, 2, 3, 4, 5, 6]), [2, 4, 6])
        self.assertEqual(get_even_numbers([7, 8, 9, 10, 11]), [8, 10])

if __name__ == "__main__":
    unittest.main()
