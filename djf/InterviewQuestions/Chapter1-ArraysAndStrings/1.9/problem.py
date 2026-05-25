
import unittest

def is_string_rotation( str1, str2 ):
    str_str = str1 + str1
    i = 0
    length = len( str1 )
    if len( str2 ) != length:
        return False

    last_rotation_start = len( str1 ) - 1
    while i < last_rotation_start:
        if str2 == str_str[ i : i + length ] :
            return True
        i += 1
    return False


class TestStringRotation(unittest.TestCase):
    def test_1(self):
       self.assertEqual( True,
                         is_string_rotation( 'waterbottle', 'erbottlewat' ) )


if __name__ == "__main__":
    unittest.main()

