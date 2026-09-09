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

def partitionA(head: SinglyLinkedListNode | None, value) -> SinglyLinkedListNode | None:
    sll = head
    prev = None
    while True:
        if sll is None:
            return head
        if sll.value < value:
            prev = sll
            sll = sll.next
            continue
        else:
            break

    while True:
        if sll is None:
            return head
        if sll.value >= value:
            prev = sll
            sll = sll.next
            continue
        else:
            # delete this node
            prev.next = sll.next
            # insert this node at the beginning and update head
            sll.next = head
            head = sll
            sll = prev

    return head


partition = partitionA


#
# Nested Loops or Sequential Loops
#
# State: a) node not found
#        b) node less than x found
#        c) node greater than or equal to x found
#
#        b is not c.
#        c is not b. Therefore can us b and not b (or c and not c).
#
#        So fail if going from not b to b
#
#        while b, then while not b until end of list, ok
#        while b, then while b, ok
#        while not b, then if b, not ok
#        if not b, then if not b until end of list, ok
#
class Tests(unittest.TestCase):
    def isCorrect(self, head: SinglyLinkedListNode | None, value : int):
        sll = head
        passes = True
        while True: # look for nodes less than x
            if sll is None:
                return passes
            if sll.value < value:
                sll = sll.next
                continue
            else:
                break

        while True: # look for nodes greater than or equal to x
            if sll is None:
                return passes
            if sll.value >= value:
                sll = sll.next
                continue
            else:
                return False

    def test_example(self):
        example = SinglyLinkedListNode(3, SinglyLinkedListNode(5, SinglyLinkedListNode(8, SinglyLinkedListNode(5, SinglyLinkedListNode(10, SinglyLinkedListNode(2, SinglyLinkedListNode(1)))))))
        self.assertFalse(self.isCorrect(example, 5))
        self.assertTrue(self.isCorrect(partition(example, 5), 5))

    def test_empty(self):
        example = None
        self.assertTrue(self.isCorrect(partition(example, 5), 5))

    def test_all_less_than(self): # value is by definition NOT in the list
        example = SinglyLinkedListNode(3, SinglyLinkedListNode(5, SinglyLinkedListNode(8, SinglyLinkedListNode(5, SinglyLinkedListNode(10, SinglyLinkedListNode(2, SinglyLinkedListNode(1)))))))
        self.assertTrue(self.isCorrect(example, 11))
        self.assertTrue(self.isCorrect(partition(example, 11), 11))

    def test_all_greater_than_or_equal_to_value_in_list(self): #value is in the list
        example = SinglyLinkedListNode(3, SinglyLinkedListNode(5, SinglyLinkedListNode(8, SinglyLinkedListNode(5, SinglyLinkedListNode(10, SinglyLinkedListNode(2, SinglyLinkedListNode(1)))))))
        self.assertTrue(self.isCorrect(example, 1))
        self.assertTrue(self.isCorrect(partition(example, 1), 1))

    def test_all_greater_than_or_equal_to_value_not_in_list(self): #value is in the list
        example = SinglyLinkedListNode(3, SinglyLinkedListNode(5, SinglyLinkedListNode(8, SinglyLinkedListNode(5, SinglyLinkedListNode(10, SinglyLinkedListNode(2, SinglyLinkedListNode(1)))))))
        self.assertTrue(self.isCorrect(example, 0))
        self.assertTrue(self.isCorrect(partition(example, 0), 0))

    # test value not


if __name__ == "__main__":
    unittest.main()
