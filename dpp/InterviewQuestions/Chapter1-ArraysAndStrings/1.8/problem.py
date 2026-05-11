
import unittest

def rotateMatrix(matrix):
    pass
    
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


if __name__ == "__main__":
    unittest.main()
