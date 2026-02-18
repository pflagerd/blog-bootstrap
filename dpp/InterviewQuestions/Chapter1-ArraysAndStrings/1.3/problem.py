import unittest
from tkinter.constants import LEFT


def urlifyBackwards(string: str, length: int) -> str:
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

#
# Gayle's solution, converted to python from Java.  Error checks added by Daniel
#
def urlify(s, true_length):
    if s is None or not isinstance(s, str) or not s or true_length is None or not isinstance(true_length, int) or true_length < 0:
        raise ValueError("string and length must be non-None, non-negative and of type str and int respectively")

    space_count = 0
    for i in range(true_length):
        if s[i] == ' ':
            space_count += 1

    index = true_length + space_count * 2
    s = list(s)
    if true_length < len(s):
        s[true_length] = '\0'

    for i in range(true_length - 1, -1, -1):
        if s[i] == ' ':
            s[index - 1] = '0'
            s[index - 2] = '2'
            s[index - 3] = '%'
            index -= 3
        else:
            s[index - 1] = s[i]
            index -= 1

    return ''.join(s)


def urlifyInWork(string: str, length: int) -> str:
    if string is None or not isinstance(string, str) or not string or length is None or not isinstance(length, int) or length < 0:
        raise ValueError("string and length must be non-None, non-negative and of type str and int respectively")

    # We're requested to do it in place, so I'll need to use a list
    # Work backwards, Use two pointers. Starting with length - 1'th character copy character by character, replacing spaces with %20, end when we've encountered (len(string) - length)/2 spaces
    originalLength = len(string)
    stringAsList = list(string)
    i = 0
    for char in string:
        if length != 0:
            if char == ' ':
                stringAsList[i] = '%'
                i += 1
                stringAsList[i] = '2'
                i += 1
                stringAsList[i] = '0'
                i += 1
            else:
                stringAsList[i] = char
                i += 1
            if i > originalLength:
                raise ValueError("Overran the string length")
            length -= 1

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

    def test_13(self):
        self.assertEqual("Mr%20John%20Smith%20", urlify("Mr John Smith       ", 14))



if __name__ == "__main__":
    unittest.main()
