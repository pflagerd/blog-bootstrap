
import unittest

#
# Narrowing the scope of the problem to include just ascii characters, as proposed by the solution on #page=96
#

def isASCII(string):
    for c in string:
        if ord(c) > 127:
            return False

    return True

def isUnique(string):
    if not len(string):
        raise ValueError("string must not be empty")

    if len(string) > 128: # There are 128 ASCII values. If the string is longer than 128, must be a duplicate character in it.
        return False

    if not isASCII(string):
        raise ValueError("string must contain only ASCII characters.")

    found = [False] * 128

    for c in string:
        if not found[ord(c)]:
            found[ord(c)] = True
        else:
            return False

    return True
    
class IsUnique(unittest.TestCase):
    def test_1(self):
       with self.assertRaises(ValueError):
           isUnique("")

    def test_2(self):
       self.assertEqual(isUnique("a"), True)

    def test_3(self):
       self.assertEqual(isUnique("ab"), True)

    def test_4(self):
       self.assertEqual(isUnique("aa"), False)

    def test_5(self):
       self.assertEqual(isUnique("the quick brown fox jumps over the lazy dog"), False)

    all_ascii = (
        '\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f'
        '\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f'
        ' !"#$%&\'()*+,-./'
        '0123456789:;<=>?'
        '@ABCDEFGHIJKLMNO'
        'PQRSTUVWXYZ[\\]^_'
        '`abcdefghijklmno'
        'pqrstuvwxyz{|}~\x7f'
    )

    def test_6(self):
        self.assertEqual(isUnique(self.all_ascii), True)

    def test_7(self):
        all_ascii_with_duplicate = self.all_ascii + "z"
        self.assertEqual(isUnique(all_ascii_with_duplicate), False)


if __name__ == "__main__":
    unittest.main()
