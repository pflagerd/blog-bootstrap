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
    print( f'... valid( {str1}, {str2} )? {valid}' )

if __name__ == '__main__':
    can_do_in_one_edit( 'same', 'same' )     # yes: identical
    can_do_in_one_edit( 'pain', 'pan' )      # yes: delete: i
    can_do_in_one_edit( 'pam', 'palm' )      # yes: add: l
    can_do_in_one_edit( 'pain', 'paid' )     # yes: replace: n with d
    can_do_in_one_edit( 'pain', 'palm' )     # no: 2 replacements
    can_do_in_one_edit( 'pain', 'painful' )  # no: 3 additions
    can_do_in_one_edit( 'nope', 'peon' )     # no: 4 changes, although same signature
