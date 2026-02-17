
import unittest

def urlify(string, length ):
    if string == None or not isinstance( string, str ):
        raise ValueError( "First argument must be a string." )
    if not length or not isinstance( length, int ):
        raise ValueError( "Second argument must be an integer." )
    if length < 0:
        raise ValueError( "Length parameter must be non-negative." )

    width = len( string )
    print( '... field width is', width )
    fore = aft = []
    
    # Grab the first 'length' characters.
    fore = list( string[ : length ] )

    # If there are characters left over, grab them for the back of the string.
    if length < len( string ):
        aft = list( string[ length : ] )

    print( f'... fore: "{fore}"; aft: "{aft}"' )

    # Determine whether we can 'urlify' the first 'length' characters in-place.
    n_letters = width - string.count( ' ' )
    n_spaces_to_convert = fore.count( ' ' )
    # Each space to be converted need an extra 2 characters: ' ' becomes '%20'.
    min_width = n_letters + n_spaces_to_convert * 3
    print( f'... min_width required is {min_width}.' )
    if min_width > width:
        print( f'Error: Output will not fit in {width} characters.' )
        raise( ValueError )

    converted = [ '%20' if ch == ' ' else ch for ch in fore ]
    print( f'converted: "{converted}"' )

    chars2 = converted + aft
    str2 = "".join( chars2 )
    # If we have trailing spaces, truncate to fit the width.
    str3 = str2[ : width ]

    return str3


class Urlify(unittest.TestCase):
    def test_1(self):
        self.assertEqual( urlify( "Mr John Smith     ", 13 ), "Mr%20John%20Smith " )

    def test_2(self):
        with self.assertRaises( ValueError ):
            urlify( None, 13 )
 
    def test_3(self):
        with self.assertRaises( ValueError ):
            urlify( "Mr John Smith    ", None )

    def test_4(self):
        with self.assertRaises( ValueError ):
            urlify( None, None)

    def test_5(self):
        self.assertEqual( urlify( "", 13), "" )

    def test_6(self):
        with self.assertRaises( ValueError ):
            urlify( "Mr John Smith    ", "" )

    def test_7(self):
        with self.assertRaises( ValueError ):
            urlify( "Mr John Smith    ", -1 )

    def test_8(self):
            self.assertEqual( urlify( "Mr John Smith    ", 3 ), "Mr%20John Smith  " )

    def test_9(self):
        with self.assertRaises( ValueError ):
            urlify( "Mr John Smith   ", 11 )
    def test_10(self):
            self.assertEqual( urlify( "Mr John Smith    ", 11 ), "Mr%20John%20Smith" )

    def test_10(self):
        with self.assertRaises( ValueError ):
            urlify( "Mr John Smith    ", 14 )

    def test_11(self):
        self.assertEqual( urlify( "Mr John Smith       ", 14 ), "Mr%20John%20Smith%20" )


if __name__ == "__main__":
    unittest.main()
