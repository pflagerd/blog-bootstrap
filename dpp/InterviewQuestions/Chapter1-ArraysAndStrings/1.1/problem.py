
import unittest

def isUnique(string):
    pass
    
class IsUnique(unittest.TestCase):
    def test_1(self):
       self.assertEqual(isUnique(""), "Indeterminate")

    def test_2(self):
       self.assertEqual(isUnique("a"), "True")

    def test_3(self):
       self.assertEqual(isUnique("ab"), "True")

    def test_4(self):
       self.assertEqual(isUnique("aa"), "False")

    def test_5(self):
       self.assertEqual(isUnique("the quick brown fox jumps over the lazy dog"), "False")


if __name__ == "__main__":
    unittest.main()
