
import unittest

def zero_matrix( m_by_n ):
    #TODO: guard: if not m_by_n or not a list or first elt is not a list, bail

    # print( "Input matrix: ", m_by_n )

    # There are m rows.
    m = len( m_by_n )
    # There are n cols.
    n = len( m_by_n[0] )

    # Data structures to record the rows and columns that need to be zeroed.
    rows_to_zero = [0] * m
    cols_to_zero = [0] * n

    # Identify rows and columns we need to zero.
    for row in range( m ):
        for col in range( n ): 
            if m_by_n[ row ][ col ] == 0:
                rows_to_zero[ row ] = 1
                cols_to_zero[ col ] = 1

    # print( 'Zero these rows:', rows_to_zero )
    # print( 'Zero these cols:', cols_to_zero )

    # Zero the identified rows and columns.
    for row in range( m ):
        if rows_to_zero[ row ] == 1:
            for col in range( n ):
                m_by_n[ row ][ col ] = 0
                      
    for col in range( n ):
        if cols_to_zero[ col ] == 1:
            for row in range( m ): 
                m_by_n[ row ][ col ] = 0

    # print( "Output matrix:", m_by_n )
    return m_by_n
    
class ZeroMatrix(unittest.TestCase):
    def test_1(self):
       self.assertEqual( [[1, 0, 3], [0, 0, 0], [7, 0, 9]],
                         zero_matrix( [[1, 2, 3], [4, 0, 6], [7, 8, 9]] ) )

    def test_2(self):
       self.assertEqual( [ [1, 0, 0, 4], [0, 0, 0, 0],
                         [9, 0, 0, 12],
                         [13, 0, 0, 16],
                         [0, 0, 0, 0] ],
                         zero_matrix( [ [1, 2, 3, 4],
                                        [5, 0, 7, 8],
                                        [9, 10, 11, 12],
                                        [13, 14, 15, 16],
                                        [17, 18, 0, 20] ] ) )


if __name__ == "__main__":
    unittest.main()
