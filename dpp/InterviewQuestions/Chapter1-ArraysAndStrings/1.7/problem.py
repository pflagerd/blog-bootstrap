
import unittest

def rotateMatrix(matrix):
    pass
    
class RotateMatrix(unittest.TestCase):
    def test_1(self):
       self.assertEqual([[1, 2, 3], [4, 5, 6], [7, 8, 9]], rotateMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    def test_2(self):
       self.assertEqual("abcdef", rotateMatrix("abcdef"))


if __name__ == "__main__":
    unittest.main()
