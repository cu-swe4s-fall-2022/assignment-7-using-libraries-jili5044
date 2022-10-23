import random
import unittest
import data_processor as dp


class TestUtils(unittest.TestCase):

    def test_get_random_matrix(self):
        num_rows = 3
        num_columns = 3
        self.assertEqual(dp.get_random_matrix(num_rows, num_columns).shape,
                         (3, 3))

    def test_get_file_dimensions(self):
        file_name = 'iris.data'
        self.assertEqual(dp.get_file_dimensions(file_name), (150, 5))
        self.assertNotEqual(dp.get_file_dimensions(file_name), (150, 4))


if __name__ == '__main__':
    unittest.main()
