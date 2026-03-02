import unittest

#from sympy import true

def hasAnEvenNumberOfCharacters(string : str) -> bool:
    return len(string) % 2 == 0

def hasAnEvenNumberOfEachDifferentCharacter(string : str) -> bool:
    for c in set(string):
        if string.count(c) % 2:
            return False
    return True

def hasAnEvenNumberOfEachDifferentCharacterExceptOne(string : str) -> bool:
    odds = 0
    for c in set(string):
        if string.count(c) % 2:
            odds += 1
    return odds == 1

def numberOfDifferentCharactersHavingAnOddCount(string : str) -> int:
    odds = 0
    for c in set(string):
        if string.count(c) % 2:
            odds += 1
    return odds

def removeSpaces(string : str) -> str:
    return string.replace(" ", "")

# Different AKA Unique

# Different Character is a little ambiguous, because (a, a) is two different characters (in an ordered set), but we really want {a, b} to be the definition of two different characters. Set of distinct characters.

# If a string has an even number of characters, and if there is an even number of each different character, it is always a permutation of a palindrome.
# If a string has an odd number of characters, and if there is an even number of each different character except for one character which has an odd number, it is always a permutation of a palindrome.
def isPalindromePermutation0(string : str) -> bool:
    if string is None or len(string) == 0:
        raise ValueError("string must be non-None and non-empty")

    string = removeSpaces(string).lower()  # Account for case and space ignorance.

    if hasAnEvenNumberOfCharacters(string) and hasAnEvenNumberOfEachDifferentCharacter(string):
        return True
    if not hasAnEvenNumberOfCharacters(string) and hasAnEvenNumberOfEachDifferentCharacterExceptOne(string):
        return True

    return False


def isPalindromePermutation1(string : str) -> bool:
    if string is None or len(string) == 0:
        raise ValueError("string must be non-None and non-empty")

    string = removeSpaces(string).lower()  # Account for case and space ignorance.

    if hasAnEvenNumberOfCharacters(string):
        if hasAnEvenNumberOfEachDifferentCharacter(string):
            return True
    else:
        if hasAnEvenNumberOfEachDifferentCharacterExceptOne(string):
            return True

    return False


def isPalindromePermutation2(string : str) -> bool:
    if string is None or len(string) == 0:
        raise ValueError("string must be non-None and non-empty")

    string = removeSpaces(string).lower()  # Account for case and space ignorance.

    if hasAnEvenNumberOfCharacters(string):
        if numberOfDifferentCharactersHavingAnOddCount(string) == 0:
            return True
    else:
        if numberOfDifferentCharactersHavingAnOddCount(string) == 1:
            return True

    return False


def isPalindromePermutation3(string : str) -> bool:
    if string is None or len(string) == 0:
        raise ValueError("string must be non-None and non-empty")

    string = removeSpaces(string).lower()  # Account for case and space ignorance.

    if numberOfDifferentCharactersHavingAnOddCount(string) in (0, 1):
            return True

    return False


def isPalindromePermutation4(string : str) -> bool:
    if string is None or len(string) == 0:
        raise ValueError("string must be non-None and non-empty")

    string = removeSpaces(string).lower()  # Account for case and space ignorance.

    return numberOfDifferentCharactersHavingAnOddCount(string) in (0, 1)


isPalindromePermutation = isPalindromePermutation4

class PalindromePermutation(unittest.TestCase):
    def test_1(self):
        self.assertEqual(isPalindromePermutation("Tact Coa"), True)

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

    def test_5b(self):
        self.assertEqual(isPalindromePermutation("a ba"), True) # Two odds would normally fail, except that we particularly ignore spaces.

    def test_5c(self):
        self.assertEqual(isPalindromePermutation("A ba"), True) # As in test_5b above, and we particulary ignore case.

    def test_6(self):
        self.assertEqual(isPalindromePermutation("aaaaaaaaaaaaa"), True) # an invariant. n of the same characters is always a palindrome

    def test_6a(self):
        self.assertEqual(isPalindromePermutation("aaaaaaaaa aaaa"), True) # an invariant. An odd number of characters AND a single space would normally fail, but is a special case in this problem as illustrated only by "Tact coa" example.

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
