import unittest

from rdml.scalar_multiplication_of_a_matrix import scalar_multiply


class TestScalarMultiplicationOfAMatrix(unittest.TestCase):
    def test_scalar_multiplication_of_a_matrix(self):
        self.assertEqual(scalar_multiply(
            [[1, 2], [3, 4]], 2), [[2, 4], [6, 8]])
        self.assertEqual(scalar_multiply(
            [[0, -1], [1, 0]], -1), [[0, 1], [-1, 0]])


if __name__ == '__main__':
    unittest.main()
