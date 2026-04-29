
import unittest

def stringCompression(string):
    # Gayle's example always adds the letter count, even if it's 1
    # REPETITION_THRESHOLD = 0
    # Counts of 1 are redundant, so eliminate them for better compression.
    REPETITION_THRESHOLD = 1
    length = len( string )
    if length == 0:
        return ""

    string = string.lower()
    
    compressed = []
    in_a_row = 0
    for ch in string:
        if in_a_row == 0:  # starting with a new ch
            compressed.append( ch )
            in_a_row = 1
        elif ch == compressed[ -1 ]:
            in_a_row += 1
        else:
            # ch doesn't match the old one, so add repetition count before moving on
            if in_a_row > REPETITION_THRESHOLD:
                compressed.append( str( in_a_row ) )
            compressed.append( ch )
            in_a_row = 1
    if in_a_row > REPETITION_THRESHOLD:
        compressed.append( str( in_a_row ) )

    if len( compressed ) < length:
        return "".join( compressed )

    return string
    

class StringCompression(unittest.TestCase):
    def test_1(self):
       self.assertEqual(stringCompression("aabcccccaaa"), "a2b1c5a3")

    def test_2(self):
       self.assertEqual(stringCompression("aabcdef"), "aabcdef")


if __name__ == "__main__":
    unittest.main()
