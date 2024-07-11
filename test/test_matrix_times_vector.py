import unittest

from rdml.matrix_times_vector import matrix_dot_vector


class TestMatrixTimesVector(unittest.TestCase):
    def test_matrix_times_vector(self):
        self.assertEqual(matrix_dot_vector(
            [[1, 2], [2, 4]], [1, 2]), [5, 10])
        self.assertEqual(matrix_dot_vector(
            [[1, 2, 3], [2, 4, 5], [6, 8, 9]], [1, 2, 3]), [14, 25, 49])
        self.assertEqual(matrix_dot_vector(
            [[1, 2], [2, 4], [6, 8], [12, 4]], [1, 2, 3]), -1)


if __name__ == '__main__':
    unittest.main()
