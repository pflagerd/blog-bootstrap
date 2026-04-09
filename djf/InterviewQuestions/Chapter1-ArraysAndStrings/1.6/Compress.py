#!/usr/bin/env python
import sys

def compress( s ):
    # Gayle's example always adds the letter count, even if it's 1
    REPETITION_THRESHOLD = 0
    # Counts of 1 are redundant, so eliminate them for better compression.
    # REPETITION_THRESHOLD = 1
    s = s.lower()
    length = len( s )
    i = 0
    compressed = ''
    while i < length:
        compressed += s[ i ]
        i += 1
        count = 1
        while i < length and s[ i ] == compressed[ -1 ]:
            i += 1
            count += 1
        if count > REPETITION_THRESHOLD:
            compressed += str( count )

    return compressed

if __name__ == '__main__':
    print( "Hi there" )

    if len( sys.argv ) == 2:
        s = sys.argv[1]
        str_compressed = compress( s )
        if len( str_compressed ) < len( s ):
            print( str_compressed )
        else:
            print( s )
    else:
        print( f'Usage: {sys.argv[0]} "string-to-compress"' )
    
