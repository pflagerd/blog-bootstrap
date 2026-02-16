import unittest
from tkinter.constants import LEFT


def urlify(string: str, length: int) -> str:
    if string is None or not isinstance(string, str) or not string or length is None or not isinstance(length, int) or length < 0:
        raise ValueError("string and length must be non-None, non-negative and of type str and int respectively")

    if length == 0:
        return string

    # We're requested to do it in place, so I'll need to use a list
    # Work backwards, Use two pointers. Starting with length - 1'th character copy character by character, replacing spaces with %20, end when we've encountered (len(string) - length)/2 spaces
    stringAsList = []
    for char in string:
        stringAsList.append(char)

    left = length - 1
    right = len(stringAsList) - 1
    nSpaces = (len(stringAsList) - length) // 2
    i = 0
    while i < nSpaces:
        c = stringAsList[left]
        if c == ' ':
            stringAsList[right] = '0'
            right -= 1
            stringAsList[right] = '2'
            right -= 1
            stringAsList[right] = '%'
            right -= 1
            i += 1
        else:
            stringAsList[right] = stringAsList[left]
            right -= 1
        left -= 1

    return "".join(stringAsList)


class Urlify(unittest.TestCase):
    def test_1(self):
        self.assertEqual("Mr%20John%20Smith", urlify("Mr John Smith    ", 13))

    def test_2(self):
        with self.assertRaises(ValueError):
            urlify(None, 13)

    def test_3(self):
        with self.assertRaises(ValueError):
            urlify("Mr John Smith    ", None)

    def test_4(self):
        with self.assertRaises(ValueError):
            urlify(None, None)

    def test_5(self):
        with self.assertRaises(ValueError):
            urlify("", 13)

    def test_6(self):
        with self.assertRaises(ValueError):
            urlify("Mr John Smith    ", "")

    def test_7(self):
        with self.assertRaises(ValueError):
            urlify("Mr John Smith    ", -1)

    def test_8(self):
        self.assertEqual("Mr%20John Smith   ", urlify("Mr John Smith    ", 3))

    def test_9(self):
        self.assertEqual("Mr%20John%20Smith", urlify("Mr John Smith    ", 12))

    def test_10(self):
        with self.assertRaises(ValueError):
            urlify("Mr John Smith    ", 14)

    def test_11(self):
        self.assertEqual("Mr John Smith    ", urlify("Mr John Smith    ", 0))

    def test_12(self):
        with self.assertRaises(ValueError):
            urlify("", 0)


if __name__ == "__main__":
    unittest.main()
