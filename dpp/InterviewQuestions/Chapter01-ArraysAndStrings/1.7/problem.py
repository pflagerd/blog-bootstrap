
import unittest

ccw = 0 # counterclockwise
cw = 1  # clockwise

def rotateMatrix(matrix, direction= ccw):
    # handle most junk cases
    if matrix is None:
        return None

    if len(matrix) < 2:
        return None

    # mostly good cases
    N = len(matrix)
    if direction == ccw:
        for row in range(len(matrix) // 2):
            if len(matrix[row]) != N:
                return None
            for col in range(row, len(matrix[row]) - row - 1):
                tmp = matrix[row][col]
                matrix[row][col] = matrix[col][N - 1 - row]
                matrix[col][N - 1 - row] = matrix[N - 1 - row][N - 1 - col]
                matrix[N - 1 - row][N - 1 - col] = matrix[N - 1 - col][row]
                matrix[N - 1 - col][row] = tmp
    else:
        pass
    return matrix
    
class RotateMatrix(unittest.TestCase):
    def test_0(self):
       self.assertEqual([[3, 6, 9], [2, 5, 8], [1, 4, 7]], rotateMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    def test_1(self):
        self.assertEqual(None, rotateMatrix(None))

    def test_2(self):
        self.assertEqual(None, rotateMatrix([]))

    def test_3(self):
        self.assertEqual(None, rotateMatrix([[]]))

    def test_4(self):
        self.assertEqual(None, rotateMatrix([[1]]))

    def test_5(self):
       self.assertEqual(None, rotateMatrix([[1, 2]]))


    def test_10(self):
        self.assertEqual([[2, 4], [1, 3]], rotateMatrix([[1, 2], [3, 4]]))

    def test_11(self):
       self.assertEqual([[3, 6, 9], [2, 5, 8], [1, 4, 7]], rotateMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    def test_12(self):
       self.assertEqual([[4, 8, 12, 16], [3, 7, 11, 15], [2, 6, 10, 14], [1, 5, 9, 13]], rotateMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))

    def test_13(self):
       self.assertEqual([[10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [9, 19, 29, 39, 49, 59, 69, 79, 89, 99], [8, 18, 28, 38, 48, 58, 68, 78, 88, 98], [7, 17, 27, 37, 47, 57, 67, 77, 87, 97], [6, 16, 26, 36, 46, 56, 66, 76, 86, 96], [5, 15, 25, 35, 45, 55, 65, 75, 85, 95], [4, 14, 24, 34, 44, 54, 64, 74, 84, 94], [3, 13, 23, 33, 43, 53, 63, 73, 83, 93], [2, 12, 22, 32, 42, 52, 62, 72, 82, 92], [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]], rotateMatrix([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50], [51, 52, 53, 54, 55, 56, 57, 58, 59, 60], [61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [71, 72, 73, 74, 75, 76, 77, 78, 79, 80], [81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]]))

    # def test_14(self):
    #    self.assertEqual(None, rotateMatrix())
    #
    # def test_15(self):
    #    self.assertEqual(None, rotateMatrix())
    #
    # def test_16(self):
    #    self.assertEqual(None, rotateMatrix())


if __name__ == "__main__":
    unittest.main()
