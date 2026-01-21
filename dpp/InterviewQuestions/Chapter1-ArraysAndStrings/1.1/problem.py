
import unittest

def isUnique(array, target):
    pass
    
class IsUnique(unittest.TestCase):
    def test_1(self):
       self.assertEqual(isUnique([-1, 1, 5, 7], 6), [])

    def test_2(self):
       self.assertEqual(isUnique([1, 2], 3), [])

    def test_3(self):
       self.assertEqual(isUnique([-1, 10, 12, 15], 125), [])


if __name__ == "__main__":
    unittest.main()
