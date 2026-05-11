#!/usr/bin/env python
import unittest


def swap_cells( matrix, row_1, col_1, row_2, col_2 ):
    temp = matrix[ row_1 ][ col_1 ]
    matrix[ row_1 ][ col_1 ] = matrix[ row_2 ][ col_2 ]
    matrix[ row_2 ][ col_2 ] = temp


def vertical_flip( matrix ):
    n = len( matrix )
    for col in range( n ):
        for row in range( n // 2 ):
            swap_cells( matrix, row, col, n - row - 1, col )
    # print( f'##### flipped matrix: {matrix}' )


def rising_diagonal_flip( matrix ):
    n = len( matrix )

    # Lower-left triangle: Diagonals run from a first-column cell
    #     to a bottom-row cell.
    for start_row in range( 0, n ):
        r1 = start_row
        c1 = 0
        r2 = n - 1
        c2 = n - 1 - start_row
        while r1 < r2:
            swap_cells( matrix, r1, c1, r2, c2 )
            r1 += 1
            c1 += 1
            r2 -= 1
            c2 -= 1

    # Upper-right triangle: Diagonals run from a first-row cell
    #     to a last-column cell.
    #     Skip the first diagonal because we did it for the lower-left triangle.
    for start_col in range( 1, n ):
        r1 = 0
        c1 = start_col
        r2 = n - 1 - start_col
        c2 = n - 1
        while r1 < r2:
            swap_cells( matrix, r1, c1, r2, c2 )
            r1 += 1
            c1 += 1
            r2 -= 1
            c2 -= 1

# General rule:
#   [r, c] -> [n-1 -c, r]
def rotate_matrix( matrix ):
    # Assume TODO: write a check: matrix is square
    n = len( matrix )
    m2 = [ [0 for c in range(n)] for r in range(n) ]
    for row in range(n):
        for col in range(n):
            m2[n - 1 - col][row] = matrix[row][col]
    matrix = m2
    return matrix


def rotate_matrix1( matrix ):
    # Assume TODO: write a check: matrix is square
    vertical_flip( matrix )
    rising_diagonal_flip( matrix )
    # print( f'--- rotated matrix: {matrix}' )
    return matrix


class TestRunner(unittest.TestCase):
    def test_1(self):
       self.assertEqual(rotate_matrix( [[1, 2, 3], [4, 5, 6], [7, 8, 9]] ),
                                       [[3, 6, 9], [2, 5, 8], [1, 4, 7]] )

    def test_2(self):
       self.assertEqual(rotate_matrix( [['a', 'b', 'c', 'd'],
                                        ['e', 'f', 'g', 'h'],
                                        ['i', 'j', 'k', 'l'],
                                        ['m', 'n', 'o', 'p']] ),
                                       [['d', 'h', 'l', 'p'],
                                        ['c', 'g', 'k', 'o'],
                                        ['b', 'f', 'j', 'n'],
                                        ['a', 'e', 'i', 'm']] )
                                     


if __name__ == "__main__":
    unittest.main()


