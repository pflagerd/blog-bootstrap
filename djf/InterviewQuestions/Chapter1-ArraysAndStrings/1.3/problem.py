
import unittest

def urlify0(string, length, output):
    chars = list( string )
    chars2 = [ '%20' if ch == ' ' else ch for ch in chars ]
    string2 = "".join( chars2 )
    string3 = string2[ : length ]

    if string3[ -2 : ] == '%2':
        string3 = string3[ : length - 2 ] + '  '
    elif string3[ -1 ] == '%':
        string3 = string3[ : length - 1 ] + ' '

    return string3


def urlify( string, length ):
    chars = list( string )
    chars2 = []
    count = 0
    for ch in chars:
        if ch == ' ' and count + 3 <= length:
            chars2.append( '%20' )
            count += 3
        elif count < length:
            chars2.append( ch )
            count += 1
        if count == length:
            break
    string2 = "".join( chars2 )
    return string2


class Urlify(unittest.TestCase):
    def test_1(self):
       self.assertEqual( urlify( "Mr John Smith      ", 13 ), "Mr%20John%20Smith" )

    def test_2(self):
       self.assertEqual( urlify( "Mr John Smith      ", 13 ), "Mr%20John Smith" )

    def test_3(self):
       self.assertEqual( urlify( "Mr John Smith      ", 29 ), "Mr%20John%20Smith%20%20%20%20" )


if __name__ == "__main__":
    unittest.main()
