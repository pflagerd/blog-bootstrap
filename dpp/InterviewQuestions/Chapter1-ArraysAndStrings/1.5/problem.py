
import unittest

statement = "There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away. ",

# insert a character
# remove a character
# replace a character (remove a character followed by a insert a character at the same position)


def oneAway(string):
    diff = [0] * 26

    strings = string.split(", ")

    for c in strings[0]:
        diff[ord(c) - ord('a')] += 1

    print(diff)

    for c in strings[1]:
        diff[ord(c) - ord('a')] -= 1

    print(diff)

    print(sum(diff))


class OneAway(unittest.TestCase):
    def test_1(self):
       self.assertEqual(oneAway("pale, ple"), "True")

    def test_2(self):
       self.assertEqual(oneAway("pales, pale"), "True")

    def test_3(self):
       self.assertEqual(oneAway("pale, bale"), "True")

    def test_4(self):
       self.assertEqual(oneAway("pale, bake"), "False")


if __name__ == "__main__":
    unittest.main()
