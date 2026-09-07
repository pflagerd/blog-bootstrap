from __future__ import annotations

import json
import unittest


# "<code>sll</code>" stands for a singly linked list
# 1 &le; length of <code>sll</code> &le; 10<sup>5</sup>
# "assume it is a singly linked list of integers"
class SinglyLinkedListNode:
    # <code>value</code> is passed the integer payload to be contained by the new <code>SinglyLinkedListNode</code>.
    def __init__(self, value: int, next: SinglyLinkedListNode | None = None) -> None:
        self.next = next
        self.value = value

    def __eq__(self, other):
        if not isinstance(other, SinglyLinkedListNode):
            return False

        current_self = self.next
        current_other = other.next

        # Traverse both lists simultaneously
        while current_self and current_other:
            if current_self.value != current_other.value:
                return False
            current_self = current_self.next
            current_other = current_other.next

        # If both are None, they are the same length and identical
        return current_self is None and current_other is None


    def __repr__(self) -> str:
        s = f"SinglyLinkedListNode({self.value}"
        if self.next is not None:
            s += ", " + repr(self.next)
        s += ")"
        return s


    def dumps(self) -> str:
        s = '{"next": '
        if self.next is None:
            s += "null"
        else:
            s += str(self.next.dumps())
        s += ", \"value\": " + str(self.value)
        s += "}"
        return s

class Tests(unittest.TestCase):
    def test_example(self):
        SinglyLinkedListNode(3, SinglyLinkedListNode(5, SinglyLinkedListNode(8, SinglyLinkedListNode(5, SinglyLinkedListNode(10, SinglyLinkedListNode(2, SinglyLinkedListNode(1)))))))
        self.assertXYZ('{"value": 4, "next": null}', '{"value": 4, "next": null}')

if __name__ == "__main__":
    unittest.main()
