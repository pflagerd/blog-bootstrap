
import unittest

# Given two strings, is one a permutation of the other?
# - In Python, a string is a sequence of characters.
#     - A character in Python is ...
# - We define a permutation of a string as ...

def countem( str ):
    counts = [0] * 128;
    for ch in str:
        i = ord( ch )
        if i < 0 or i > 128:
            print( ch, 'has ord', i )
        counts[ i ] += 1
    return counts

def checkPermutation(string1, string2):
    if not string1 or not string2:
        raise ValueError( "It's an error!" )

    
    signature1 = countem( string1 )
    signature2 = countem( string2 )
    return signature1 == signature2

    
class CheckPermutation(unittest.TestCase):
    def test_1(self):
       with self.assertRaises( ValueError ):
           checkPermutation( "", "" )

    def test_2(self):
       with self.assertRaises( ValueError ):
           checkPermutation( "", "abcd" )

    def test_3(self):
       self.assertEqual(checkPermutation("ab", "bc"), False)

    def test_4(self):
       self.assertEqual(checkPermutation("ab", "aba"), False)

    def test_5(self):
       self.assertEqual(checkPermutation("ab", "ab"), True)

    def test_6(self):
       self.assertEqual(checkPermutation("ab", "ba"), True)

    def test_7(self):
       self.assertEqual(checkPermutation("The quick brown fox jumps over the lazy dog", "The quick brown fox jumps over the lazy dog"), True)

    def test_8(self):
       self.assertEqual(checkPermutation("The quick brown fox jumps over the lazy dog", "the quick brown fox jumps over the lazy dog"), False)

    def test_9(self):
       self.assertEqual(checkPermutation("The quick brown fox springs over the lazy dog", "the quick brown fox jumps over the lazy dog"), False)


if __name__ == "__main__":
    unittest.main()
