
import unittest

def reverseTheArray(array):
    pass
    
class ReverseTheArray(unittest.TestCase):
    def test_1(self):
       self.assertEqual(reverseTheArray([1, 4, 3, 2, 6, 5]), [5, 6, 2, 3, 4, 1])

    def test_2(self):
       self.assertEqual(reverseTheArray([4, 5, 2]), [2, 5, 4])

    def test_3(self):
       self.assertEqual(reverseTheArray([1]), [1])


if __name__ == "__main__":
    unittest.main()
