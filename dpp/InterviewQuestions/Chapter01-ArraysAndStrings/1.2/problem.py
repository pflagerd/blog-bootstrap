
import unittest

def checkPermutationASCIIOnly(string1, string2):
    pass

def createCharacterCount(string1):
    characterCount = {}
    for character in string1:
        ordCharacter = ord(character)
        if ordCharacter not in characterCount:
            characterCount[ordCharacter] = 1
        else:
            characterCount[ordCharacter] += 1
    return characterCount


def checkPermutationUnicode(string1, string2):
    string1CharacterCount = createCharacterCount(string1)
    string2CharacterCount = createCharacterCount(string2)

    return string1CharacterCount == string2CharacterCount


def checkPermutation(string1, string2):
    if string1 is None or string2 is None:
        raise ValueError("Neither string1 nor string2 can be None")

    if not string1 or not string2:
        raise ValueError("Neither string1 nor string2 can be empty")

    #return checkPermutationASCIIOnly(string1, string2)
    return checkPermutationUnicode(string1, string2)

class CheckPermutation(unittest.TestCase):
    def test_1(self):
        with self.assertRaises(ValueError):
            checkPermutation(None, "abc")

        with self.assertRaises(ValueError):
            checkPermutation("abc", None)

        with self.assertRaises(ValueError):
            checkPermutation(None, None)

    def test_2(self):
        with self.assertRaises(ValueError):
            checkPermutation("", "abc")

        with self.assertRaises(ValueError):
            checkPermutation("abc", "")

        with self.assertRaises(ValueError):
            checkPermutation("", "")


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

    def test_10(self):
       self.assertEqual(checkPermutation("⚬ӎĪ⎐╿⛑☲∑Ӿ〈ü☍γ⌲⛃ϲ↾↑⌥ҤÐ≷Ý≊{čř⊦≘┸⊨☧⛶Ξi⎕♸⊖⇺⊫⁖ś⎲☧©♴⚻☗♺⇇⍦⍄≚∴Ӕ⌂ҋ⎸♓⌐⏃┲Αʹ", "Ξ⎕⌥⊨♴∑ü⁖⇺≷γ⚻⎐©Ý♺┲≚☍┸♸⌂ř⌲⌐↾⊫⛶♓〈č☧╿∴↑≊≘☗☧ҤӔ⊦ĪҋΑ⇇Ð{⏃śi⛑⎸⛃ӎ⍄⎲ʹӾ⊖ϲ⚬⍦☲"), True)

if __name__ == "__main__":
    unittest.main()
