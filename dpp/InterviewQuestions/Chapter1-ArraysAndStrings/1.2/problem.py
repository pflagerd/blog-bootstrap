
import unittest

def checkPermutation(string1, string2):
    if string1 is None or string2 is None:
        raise ValueError("Neither string1 nor string2 can be None")

    if not string1 or not string2:
        raise ValueError("Neither string1 nor string2 can be empty")

    pass
    
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
       self.assertEqual(checkPermutation("The quick brown fox jumps over the lazy dog", "The quick brown fox jumps over the lazy dog"), "True")

    def test_8(self):
       self.assertEqual(checkPermutation("The quick brown fox jumps over the lazy dog", "the quick brown fox jumps over the lazy dog"), "False")

    def test_9(self):
       self.assertEqual(checkPermutation("The quick brown fox springs over the lazy dog", "the quick brown fox jumps over the lazy dog"), "False")


if __name__ == "__main__":
    unittest.main()
