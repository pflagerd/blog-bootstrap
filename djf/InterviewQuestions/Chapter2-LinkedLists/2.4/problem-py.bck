import unittest

class Singly_linked_list_node:
    def __init__(self, value:int = 0) -> None:
        self.value = value
        self.next = None

    def create_linked_list(self, values):
        if not values or len( values ) == 0:
            return None

        head = new Singly_linked_list_node( values[0] )
        current = head
        for value in values[ 1 : ] :
            current.next = new Singly_linked_list_node( value )
            current = current.next

        return head

    def display_list( head ):
        node_text = []
        current = head
        while current:
            node_text.append( current.value )
            current = current.next
        return "[ " + ", ".node_text + " ]"


def return_kth_to_last( str1, str2 ):
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

