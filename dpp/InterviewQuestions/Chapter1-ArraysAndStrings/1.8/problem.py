
import unittest

def zeroMatrix(matrix):
    rows_to_zero = [0] * len(matrix)
    cols_to_zero = [0] * len(matrix[0])
    for row in matrix:
        for col in row:
            if matrix[row][col] == 0:
                rows_to_zero[row] = cols_to_zero[col] = 1
    for row in matrix:

    for col in row:
            if matrix[row][col] == 0:
                rows_to_zero[row] = cols_to_zero[col] = 1

    
class ZeroMatrix(unittest.TestCase):
    def test_1(self):
        self.assertEqual([[0, 0, 0], [0, 5, 6]], zeroMatrix([[0, 2, 3], [4, 5, 6]]))

    # def test_2(self):
    #     self.assertEqual(None, zeroMatrix([]))
    #
    # def test_3(self):
    #     self.assertEqual(None, zeroMatrix([[]]))
    #
    # def test_4(self):
    #     self.assertEqual(None, zeroMatrix([[1]]))
    #
    # def test_5(self):
    #    self.assertEqual(None, zeroMatrix([[1, 2]]))


if __name__ == "__main__":
    unittest.main()
