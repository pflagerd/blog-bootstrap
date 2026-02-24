
import unittest

def palindromePermutation(string):
    alphabet = set( string )
    counts = { ch, string.count( ch ) for ch in alphabet }

    pass
    
class PalindromePermutation(unittest.TestCase):
    def test_1(self):
       self.assertEqual(palindromePermutation("Tact Coa"), "True")

    def test_2(self):
       self.assertEqual(palindromePermutation("None"), "Raise ValueError")

    def test_3(self):
       self.assertEqual(palindromePermutation(""), "Raise ValueError")

    def test_4(self):
       self.assertEqual(palindromePermutation("a"), "True")

    def test_5(self):
       self.assertEqual(palindromePermutation("aa"), "True")

    def test_6(self):
       self.assertEqual(palindromePermutation("aaaaaaaaaaaaa"), "True")

    def test_7(self):
       self.assertEqual(palindromePermutation("ab"), "False")

    def test_8(self):
       self.assertEqual(palindromePermutation("abab"), "True")


if __name__ == "__main__":
    unittest.main()
