
import unittest

ccw = 0 # counterclockwise
cw = 1  # clockwise

def rotateMatrix(matrix, direction= ccw):
    # handle most junk cases
    if matrix is None:
        return None

    if len(matrix) == 0:
        return None

    # mostly good cases
    N = len(matrix)
    if direction == ccw:
        for row in range(len(matrix) // 2):
            if len(matrix[row]) != N:
                return None
            for col in range(row, len(matrix[row]) // 2):
                tmp = matrix[row][col]
                matrix[row][col] = matrix[col][N - 1 - row]
                matrix[col][N - 1 - row] = matrix[N - 1 - row][col]
                matrix[N - 1 - row][col] = matrix[col][row]
                matrix[col][row] = tmp
    else:
        pass
    return matrix
    
class RotateMatrix(unittest.TestCase):
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
       self.assertEqual([[7, 4, 1], [8, 5, 2], [9, 6, 3]], rotateMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    def test_12(self):
       self.assertEqual([[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]], rotateMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))

    def test_13(self):
       self.assertEqual([[91, 81, 71, 61, 51, 41, 31, 21, 11, 1], [92, 82, 72, 62, 52, 42, 32, 22, 12, 2], [93, 83, 73, 63, 53, 43, 33, 23, 13, 3], [94, 84, 74, 64, 54, 44, 34, 24, 14, 4], [95, 85, 75, 65, 55, 45, 35, 25, 15, 5], [96, 86, 76, 66, 56, 46, 36, 26, 16, 6], [97, 87, 77, 67, 57, 47, 37, 27, 17, 7], [98, 88, 78, 68, 58, 48, 38, 28, 18, 8], [99, 89, 79, 69, 59, 49, 39, 29, 19, 9], [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]], rotateMatrix([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50], [51, 52, 53, 54, 55, 56, 57, 58, 59, 60], [61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [71, 72, 73, 74, 75, 76, 77, 78, 79, 80], [81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]]))

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
