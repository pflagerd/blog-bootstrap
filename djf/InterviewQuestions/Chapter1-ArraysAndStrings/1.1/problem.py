import unittest

## DJF-ification.  I need to be able to grok this in my own terms.
#
# Narrowing the scope of the problem to include just ascii characters, as
# proposed by the solution on #page=96
#

def isUnique(string):
    if not len( string ):
        raise ValueError( "String must not be empty" )

    # If there are more chars in the string than in the ASCII set,
    # there must be at least one duplicate.
    if len( string ) > 128:
        return False

    found = [False] * 128
    for c in string:
        index = ord( c )
        if index > 127:
            raise ValueError( "String must contain only ASCII characters." )

        if not found[ ord( c ) ]:
            found[ ord( c ) ] = True
        else:
            return False

    return True
    
class IsUnique( unittest.TestCase ):
    def test_1( self ):
       with self.assertRaises( ValueError ):
           isUnique( "" )

    def test_2( self ):  # All printable 7-bit ASCII chars
       self.assertEqual( isUnique( "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~" ), True )

    def test_3( self ):  # Appended a duplicate tilde.
       self.assertEqual( isUnique( "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~~" ), False )

    def test_3( self ):
       self.assertEqual( isUnique( "a" ), True )

    def test_4( self ):
       self.assertEqual( isUnique( "ab" ), True )

    def test_5( self ):
       self.assertEqual( isUnique( "aa" ), False )

    def test_6( self ):
       self.assertEqual( isUnique( "the quick brown fox jumps over the lazy dog" ), False )


if __name__ == "__main__":
    unittest.main()
