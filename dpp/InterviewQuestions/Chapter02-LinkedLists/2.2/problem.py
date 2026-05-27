import unittest


class SinglyLinkedListNode:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None





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
        self.assertEqual(None, returnKthToLast(sll, 0)) # Degenerate test case. Self-referential singly linked list.

    def test_3(self):
        self.assertEqual(None, returnKthToLast(SinglyLinkedListNode(1), -1)) # Degenerate test case. Valid single node singly linked list, negative k.

    def test_4(self):
        self.assertEqual(None, returnKthToLast(SinglyLinkedListNode(1), 1)) # Degenerate test case. Valid single node singly linked list, k > 0.



if __name__ == "__main__":
    unittest.main()
