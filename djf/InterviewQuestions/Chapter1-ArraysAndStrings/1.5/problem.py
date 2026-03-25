
import unittest

statement = "There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away. ",

# insert a character
# remove a character
# replace a character (remove a character followed by a insert a character at the same position)

# If different lengths, can have one more character on left than right, or converse. (i.e. one character different between them)
# I the same length, must have exactly oe character different between them


#!/usr/bin/env python

def can_do_in_one_edit( str1, str2 ):
    str1 = str1.lower()
    str2 = str2.lower()
    valid = True

    len1 = len(str1)
    len2 = len(str2)
    # Let str1 be the shorter, or both strings have the same length
    if len1 > len2:
        str1, str2 = str2, str1
        len1, len2 = len2, len1

    if len2 - len1 > 1:
        print( f'... valid( {str1}, {str2} )? False' )
        return

    changes = 0
    i = 0
    k = 0
    while i < len1 and changes < 2:
        if str1[ i ] != str2[ k ]:
            # print( f'... "{str1[i]}" does not match "{str2[k]}"' )
            changes += 1
            if k + 1 < len2 and str1[ i ] == str2[ k + 1 ] :
                # string 2 has an addition -- pass over it
                k += 1
        i += 1
        k += 1
    if i == len1 and k < len2:
        # we have unprocessed chars
        changes += 1

    valid = (changes < 2)
    if valid:
        answer = 'True'
    else:
        answer = 'False'

    return answer


def oneAway(string):
    diff = [0] * 26

    strings = string.split(", ")

    return can_do_in_one_edit( strings[0], strings[1] )


class OneAway(unittest.TestCase):
    def test_1(self):
        print("pale, ple")
        self.assertEqual(oneAway("pale, ple"), "True")

    def test_2(self):
        print("pales, pale")
        self.assertEqual(oneAway("pales, pale"), "True")

    def test_3(self):
        print("pale, bale")
        self.assertEqual(oneAway("pale, bale"), "True")

    def test_4(self):
        print("pale, bake")
        self.assertEqual(oneAway("pale, bake"), "False")


if __name__ == "__main__":
    unittest.main()
