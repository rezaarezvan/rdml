import unittest

from rdml.reshape_matrix import reshape_matrix


class TestReshapeMatrix(unittest.TestCase):
    def test_reshape_matrix(self):
        self.assertEqual(reshape_matrix(
            [[1, 2, 3, 4], [5, 6, 7, 8]], (4, 2)), [[1, 2], [3, 4], [5, 6], [7, 8]])
        self.assertEqual(reshape_matrix(
            [[1, 2, 3], [4, 5, 6]], (3, 2)), [[1, 2], [3, 4], [5, 6]])
        self.assertEqual(reshape_matrix(
            [[1, 2, 3, 4], [5, 6, 7, 8]], (2, 4)), [[1, 2, 3, 4], [5, 6, 7, 8]])


if __name__ == '__main__':
    unittest.main()
