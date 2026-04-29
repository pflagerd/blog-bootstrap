
import unittest

def rotateMatrix(string):
    pass
    
class RotateMatrix(unittest.TestCase):
    def test_1(self):
       self.assertEqual(rotateMatrix("a2b1c5a3"), "aabcccccaaa")

    def test_2(self):
       self.assertEqual(rotateMatrix("abcdef"), "abcdef")


if __name__ == "__main__":
    unittest.main()
