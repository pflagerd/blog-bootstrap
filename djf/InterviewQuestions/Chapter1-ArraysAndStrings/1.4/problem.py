import unittest

def is_even( n ):
    return 0 == (n % 2)

def isPalindromePermutation0(string : str) -> bool:
    if not string:
        raise ValueError( "String must exist and be non-empty" )
    string = string.lower()
    alphabet = set( string )
    # At most one character may have an odd count.
    evens = [ is_even( string.count( ch ) ) for ch in alphabet ]
    if evens.count( False ) > 1:
        return False
    return True

def is_odd( n ):
    return 1 == (n % 2)

def isPalindromePermutation(string : str) -> bool:
    if not string:
        raise ValueError( "String must exist and be non-empty" )

    string = string.lower()
    alphabet = set( string )
    # At most one character may have an odd count.
    odd_char_count = 0
    for ch in alphabet:
        if is_odd( string.count( ch ) ):
            odd_char_count += 1
        if odd_char_count > 1:
            return False

    return True

class PalindromePermutation(unittest.TestCase):
    def test_1(self):
        self.assertEqual(isPalindromePermutation("TactCoa"), True)

    def test_2(self):
        with self.assertRaises(ValueError):
            isPalindromePermutation(None)

    def test_3(self):
        with self.assertRaises(ValueError):
            isPalindromePermutation("")

    def test_4(self):
        self.assertEqual(isPalindromePermutation("a"), True) # an invariant. A single character is always a palindrome

    def test_5(self):
        self.assertEqual(isPalindromePermutation("aa"), True) # an invariant. Two of the same characters is always a palindrome

    def test_5a(self):
        self.assertEqual(isPalindromePermutation("aba"), True) # an invariant. Inserting a different character between two identical characters always results in a palindrome

    def test_6(self):
        self.assertEqual(isPalindromePermutation("aaaaaaaaaaaaa"), True) # an invariant. n of the same characters is always a palindrome

    def test_7(self):
        self.assertEqual(isPalindromePermutation("ab"), False) # an invariant. One each of two different characters is never a palindrome.

    def test_8(self):
        self.assertEqual(isPalindromePermutation("aba"), True) # an invariant: For three characters, if two are the same it is always a palindrome.

    def test_9(self):
        self.assertEqual(isPalindromePermutation("abc"), False) # an invariant: For three characters, if all three are different it is never a palindrome.

    def test_10(self):
        self.assertEqual(isPalindromePermutation("abcdefghijklmnop"), False) # an invariant: For n characters, if all n are different it is never a palindrome.

    def test_11a(self):
        self.assertEqual(isPalindromePermutation("baab"), True) # For four characters, if two different characters are used, and if there are two of each (two pairs of characters) the result is a palindrome if ...

    def test_11b(self):
        self.assertEqual(isPalindromePermutation("baaa"), False) # an invariant: For four characters, if two different characters are used, and if there are three of one character, and one of the other the result is never a palindrome.

    def test_11c(self):
        self.assertEqual(isPalindromePermutation("abba"), True)

    def test_11d(self):
        self.assertEqual(isPalindromePermutation("abab"), True)

    def test_11e(self):
        self.assertEqual(isPalindromePermutation("baba"), True)

    def test_11f(self):
        self.assertEqual(isPalindromePermutation("bbaa"), True)

    def test_11g(self):
        self.assertEqual(isPalindromePermutation("aabb"), True)

    def test_11h(self):
        self.assertEqual(isPalindromePermutation("abcba"), True) # Adding a third character at the center position of a four character palindrome always results in a palindrome.

    def test_12a(self):
        self.assertEqual(isPalindromePermutation("abcba"), True)  # Adding a third character at the center position of an n-character palindrome always results in a palindrome.

    def test_12b(self):
        self.assertEqual(isPalindromePermutation("ababa"), True)  # Adding a third character at the center position of an n-character palindrome always results in a palindrome.

    # There are 4! permutations of 4 objects taken 4 at a time.

    # Odd number of characters
    # Even number of characters

    # A permutation of a palindrome with an even number of characters must have an even number of each different character
    # A permutation of a palindrome with an odd number of characters must have an even number of each different character except for one, which may have an odd number of characters.

    # If a string has an even number of characters, and if there is an even number of each different character, it is always a permutation of a palindrome.
    # If a string has an odd number of characters, and if there is an even number of each different character except for one character which has an odd number, it is always a permutation of a palindrome.

    # Let's try putting each of these statements to the test with an agentic AI.

    #





if __name__ == "__main__":
    unittest.main()
