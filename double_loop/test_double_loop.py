
import unittest
from double_loop_list_comprehension import get_common_elements

class TestGetCommonElements(unittest.TestCase):
    def test_get_common_elements(self):
        self.assertEqual(get_common_elements([1, 2, 3], [2, 3, 4]), [2, 3])
        self.assertEqual(get_common_elements([5, 6, 7], [7, 8, 9]), [7])

if __name__ == "__main__":
    unittest.main()
