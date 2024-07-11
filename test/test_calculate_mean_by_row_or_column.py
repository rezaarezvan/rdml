import unittest

from rdml.calculate_mean_by_row_or_column import calculate_matrix_mean


class TestCalculateMeanByRowOrColumn(unittest.TestCase):
    def test_calculate_mean_by_row_or_column(self):
        self.assertEqual(calculate_matrix_mean(
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 'column'), [4.0, 5.0, 6.0])
        self.assertEqual(calculate_matrix_mean(
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 'row'), [2.0, 5.0, 8.0])


if __name__ == '__main__':
    unittest.main()
