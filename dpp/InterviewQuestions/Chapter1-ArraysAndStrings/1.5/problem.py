
import unittest

statement = "There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away. ",

# insert a character
# remove a character
# replace a character (remove a character followed by a insert a character at the same position)

# If different lengths, can have one more character on left than right, or converse. (i.e. one character different between them)
# I the same length, must have exactly oe character different between them



def oneAway(string):
    strings = string.split(", ")
    if len(strings[0]) == len(strings[1]):
        countOfDifferences = 0
        for i in range(len(strings[0])):
            if strings[0][i] != strings[1][i]:
                countOfDifferences += 1
        if countOfDifferences <= 1:
            return True
        return False
    else:
        shortstring = strings[1]
        longstring = strings[0]
        if len(strings[0]) < len(strings[1]):
            shortstring = strings[0]
            longstring = strings[1]

        countOfDifferences = 0
        i = 0
        j = 0
        while i < len(longstring):
            if j >= len(shortstring) or longstring[i] != shortstring[j]:
                countOfDifferences += 1
                if countOfDifferences > 1:
                    return False
                i += 1
            i += 1
            j += 1

        return True

class OneAway(unittest.TestCase):
    def test_1(self):
        print("pale, ple")
        self.assertEqual(oneAway("pale, ple"), True)

    def test_2(self):
        print("pales, pale")
        self.assertEqual(oneAway("pales, pale"), True)

    def test_3(self):
        print("pale, bale")
        self.assertEqual(oneAway("pale, bale"), True)

    def test_4(self):
        print("pale, bake")
        self.assertEqual(oneAway("pale, bake"), False)


if __name__ == "__main__":
    unittest.main()
