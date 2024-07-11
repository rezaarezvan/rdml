import unittest

from rdml.transpose_of_a_matrix import transpose_matrix


class TestTransposeOfAMatrix(unittest.TestCase):
    def test_transpose_of_a_matrix(self):
        self.assertEqual(transpose_matrix(
            [[1, 2], [3, 4], [5, 6]]), [[1, 3, 5], [2, 4, 6]])
        self.assertEqual(transpose_matrix([[1, 2, 3], [4, 5, 6]]), [
                         [1, 4], [2, 5], [3, 6]])


if __name__ == '__main__':
    unittest.main()
