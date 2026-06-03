from __future__ import annotations

import unittest


# "<code>sll</code>" stands for a singly linked list
# 1 &le; length of <code>sll</code> &le; 10<sup>5</sup>
# "assume it is a singly linked list of integers"
class SinglyLinkedListNode:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None

    @staticmethod
    def generate(n: int) -> SinglyLinkedListNode | None:
        if n <= 0:
            return None

        sll = SinglyLinkedListNode(0) # sll stands for Singly Linked List. Temporary variable for loop support.
        head = sll # points to the head of the list
        for i in range(1, n):
            sll.next = SinglyLinkedListNode(i)
            sll = sll.next

        return head




# return integer offset between 0 and len(s1) if s2 is a substring of s1, else return -1
def returnKthToLastA(head: SinglyLinkedListNode | None, k: int) -> int | None:
    return None


returnKthToLast = returnKthToLastA
    
class ReturnKthToLastTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(None, returnKthToLast(None, 0)) # Degenerate test case. Null singly linked list.

    def test_2(self):
        sll = SinglyLinkedListNode(0)
        sll.next = sll
        self.assertEqual(None, returnKthToLast(sll, 0)) # Degenerate test case. Self-referential singly linked list (has cycle).

    def test_3(self):
        self.assertEqual(None, returnKthToLast(SinglyLinkedListNode(0), -1)) # Degenerate test case. Valid single node singly linked list, negative k.

    def test_4(self):
        self.assertEqual(None, returnKthToLast(SinglyLinkedListNode(0), 1)) # Degenerate test case. Valid single node singly linked list, k > 0.

    def test_5(self):
        head = sll = SinglyLinkedListNode.generate(32768)

        for i in range(0, 32768 - 1):
            sll = sll.next

        sll.next = head

        self.assertEqual(None, returnKthToLast(head, 1)) # Degenerate test case. Large singly linked list with cycle.

    def test_6(self):
        head = SinglyLinkedListNode.generate(1)
        self.assertEqual(None, returnKthToLast(head, 0)) # Simple test case. Single node. k = 0

    def test_7(self):
        head = SinglyLinkedListNode.generate(2)
        self.assertEqual(None, returnKthToLast(head, 0))  # Simple test case. Single node. k = 0


if __name__ == "__main__":
    unittest.main()
