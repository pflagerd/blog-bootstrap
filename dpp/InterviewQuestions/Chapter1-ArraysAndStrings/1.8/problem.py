
import unittest

def zeroMatrixA(matrix):
    # code to filter out junk inputs
    # TODO: code it
    if matrix is None:
        return None

    if len(matrix) == 0 or len(matrix[0]) == 0:
        return None



    # matrix is mostly valid
    rows_to_zero = [0] * len(matrix)
    cols_to_zero = [0] * len(matrix[0])
    col_width = len(matrix[0])
    row = 0
    col = 0
    for row in range(len(matrix)):
        if len(matrix[row]) != col_width:
            return None
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                rows_to_zero[row] = cols_to_zero[col] = 1

    for row in range(len(rows_to_zero)):
        if rows_to_zero[row] == 1:
            for col in range(len(matrix[row])):
                matrix[row][col] = 0

    for col in range(len(cols_to_zero)):
        if cols_to_zero[col] == 1:
            for row in range(len(matrix)):
                matrix[row][col] = 0

    return matrix


#
# Try to do it in-place in one pass
#
def zeroMatrixB(matrix):
    # code to filter out junk inputs
    # TODO: code it
    if matrix is None:
        return None

    if len(matrix) == 0 or len(matrix[0]) == 0:
        return None



    # matrix is mostly valid
    col_width = len(matrix[0])
    row = 0
    col = 0
    for row in range(len(matrix)):
        if len(matrix[row]) != col_width:
            return None
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                matrix[0][col] = 0
                matrix[row][0] = 0

            if matrix[row][0] == 0:
                matrix[row][col] = 0

            if matrix[0][col] == 0:
                matrix[row][0] = 0

        if matrix[0][col] == 0:
            for cell in matrix[row]:
                cell = 0

    return matrix

def zeroMatrixC(matrix):
    # code to filter out junk inputs
    # TODO: code it
    if matrix is None:
        return None

    if len(matrix) == 0 or len(matrix[0]) == 0:
        return None

    # matrix is mostly valid
    col_width = len(matrix[0])
    row = 0
    col = 0

    # Can use matrix[0] to store zero column data
    # but can't then use matrix[0][0] to ALSO store zero matrix data
    # so create a variable just for top_row_zero.
    top_row_zero = False

    for row in range(len(matrix)):
        if len(matrix[row]) != col_width:
            return None
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                if row == 0:
                    top_row_zero = True
                    matrix[0][col] = 0
                else:
                    matrix[row][0] = matrix[0][col] = 0

    for col in range(len(matrix[0])):
        if matrix[0][col] == 0:
            for row in range(len(matrix)):
                matrix[row][col] = 0

    for row in range(len(matrix)):
        if (row == 0 and top_row_zero) or (row != 0 and matrix[row][0]) == 0:
            for col in range(len(matrix[row])):
                matrix[row][col] = 0

    return matrix


zeroMatrix = zeroMatrixC
    
class ZeroMatrix(unittest.TestCase):
    def test_0(self):
        self.assertEqual([[0, 0, 0], [0, 5, 6]], zeroMatrix([[0, 2, 3], [4, 5, 6]]))

    def test_1(self):
        self.assertEqual(None, zeroMatrix(None))

    def test_2(self):
        self.assertEqual(None, zeroMatrix([]))

    def test_3(self):
        self.assertEqual(None, zeroMatrix([[]]))

    def test_4(self):
        self.assertEqual([[1]], zeroMatrix([[1]]))

    def test_5(self):
       self.assertEqual([[1, 2]], zeroMatrix([[1, 2]]))

    def test_6(self):
       self.assertEqual([[1], [2], [3]], zeroMatrix([[1], [2], [3]]))

    def test_7(self):
       self.assertEqual([[0], [0], [0]], zeroMatrix([[1], [2], [0]]))

    def test_8(self):
       self.assertEqual([[1, 2], [3, 4]], zeroMatrix([[1, 2], [3, 4]]))


    def test_10(self):
       self.assertEqual([[0, 0]], zeroMatrix([[1, 0]]))

    def test_11(self):
       self.assertEqual([[0, 0]], zeroMatrix([[0, 2]]))


    def test_20(self):
        self.assertEqual([[0, 0, 0], [0, 5, 6]], zeroMatrix([[0, 2, 3], [4, 5, 6]]))

    def test_21(self):
        self.assertEqual([[0, 0, 0], [4, 0, 6]], zeroMatrix([[1, 0, 3], [4, 5, 6]]))

    def test_22(self):
        self.assertEqual([[0, 0, 0], [0, 0, 0]], zeroMatrix([[1, 2, 0], [0, 5, 6]]))


    def test_30(self):
        self.assertEqual([[1, 2, 3], [4, 5, 6], [7, 8, 9]], zeroMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    def test_31(self):
        self.assertEqual([[0, 0, 0], [0, 5, 6], [0, 8, 9]], zeroMatrix([[0, 2, 3], [4, 5, 6], [7, 8, 9]]))

    def test_32(self):
        self.assertEqual([[1, 0, 3], [0, 0, 0], [7, 0, 9]], zeroMatrix([[1, 2, 3], [4, 0, 6], [7, 8, 9]]))

    def test_33(self):
        self.assertEqual([[1, 2, 0], [4, 5, 0], [0, 0, 0]], zeroMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 0]]))


    def test_34(self):
        self.assertEqual([[0, 0, 0], [0, 5, 0], [0, 0, 0]], zeroMatrix([[0, 2, 3], [4, 5, 6], [7, 8, 0]]))

    if __name__ == "__main__":
        unittest.main()
