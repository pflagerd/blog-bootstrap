from __future__ import annotations

import unittest


# "<code>sll</code>" stands for a singly linked list
# 1 &le; length of <code>sll</code> &le; 10<sup>5</sup>
# "assume it is a singly linked list of integers"
class SinglyLinkedListNode:
    # <code>value</code> is passed the integer payload to be contained by the new <code>SinglyLinkedListNode</code>.
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None

    # <code>n</code> is passed the number of nodes to be created in the Singly Linked List. Must be greater than zero.
    @staticmethod
    def generate(n: int) -> SinglyLinkedListNode | None:

        if False:

            if n <= 0:
                return None

            sll = SinglyLinkedListNode(0) # <code>sll</code> stands for Singly Linked List. Temporary variable for loop support.
            head = sll # points to the head of the list
            for i in range(1, n):
                sll.next = SinglyLinkedListNode(i)
                sll = sll.next


            i = 1
            while i < n:
                sll.next = SinglyLinkedListNode(i)
                sll = sll.next
                i += 1

            i = 1
            while True:
                if i >= n:
                    break
                sll.next = SinglyLinkedListNode(i)
                sll = sll.next
                i += 1

            i = 0
            while True:
                sll.next = SinglyLinkedListNode(i)
                if i == 0:
                    head = sll
                sll = sll.next


                if i >= n:
                    break

                i += 1
                sll.next = SinglyLinkedListNode(i)


            i = 0
            head = SinglyLinkedListNode(i)

            i += 1
            head.next = SinglyLinkedListNode(i)

            i += 1
            head.next.next = SinglyLinkedListNode(i)

            i += 1
            head.next.next.next = SinglyLinkedListNode(i)


######
            i = 0
            head = sll = SinglyLinkedListNode(i)

            i += 1
            sll.next = SinglyLinkedListNode(i)
            sll = sll.next

            i += 1
            sll.next = SinglyLinkedListNode(i)
            sll = sll.next

            i += 1
            sll.next = SinglyLinkedListNode(i)



            i = 0

            head = sll = SinglyLinkedListNode(i)
            i += 1

            sll.next = SinglyLinkedListNode(i)
            sll = sll.next
            i += 1

            sll.next = SinglyLinkedListNode(i)
            sll = sll.next
            i += 1

            sll.next = SinglyLinkedListNode(i)




            i = 0

            head = sll = SinglyLinkedListNode(i)
            i += 1
            sll.next = SinglyLinkedListNode(i)

            sll = sll.next
            i += 1
            sll.next = SinglyLinkedListNode(i)

            sll = sll.next
            i += 1
            sll.next = SinglyLinkedListNode(i)

        i = 0

        while True:
            if i == 0:
                head = sll = SinglyLinkedListNode(i)
            else:
                sll.next = SinglyLinkedListNode(i)
                sll = sll.next
            if i == n - 1:
                break
            i += 1

        # i = 0
        #
        # head = sll = SinglyLinkedListNode(i)
        #
        # # i += 1
        # # sll.next = tail = sll = SinglyLinkedListNode(i)
        #
        # i += 1
        # tail = sll = sll.next = SinglyLinkedListNode(i)



        # tail = sll.next = sll = SinglyLinkedListNode(i)
        #
        # x = SinglyLinkedListNode(i)
        # tail = x
        # sll.next = x
        # sll = x



        return head




# return integer offset between 0 and len(s1) if s2 is a substring of s1, else return -1
def returnKthToLastA(head: SinglyLinkedListNode | None, k: int) -> int | None:
    return None


returnKthToLast = returnKthToLastA
    
class ReturnKthToLastTests(unittest.TestCase):
    def test_0(self):
        self.assertEqual(None, SinglyLinkedListNode.generate(2)) # Degenerate test case. Null singly linked list.



    # def test_1(self):
    #     self.assertEqual(None, returnKthToLast(None, 0)) # Degenerate test case. Null singly linked list.
    #
    # def test_2(self):
    #     sll = SinglyLinkedListNode(0)
    #     sll.next = sll
    #     self.assertEqual(None, returnKthToLast(sll, 0)) # Degenerate test case. Self-referential singly linked list (has cycle).
    #
    # def test_3(self):
    #     self.assertEqual(None, returnKthToLast(SinglyLinkedListNode(0), -1)) # Degenerate test case. Valid single node singly linked list, negative k.
    #
    # def test_4(self):
    #     self.assertEqual(None, returnKthToLast(SinglyLinkedListNode(0), 1)) # Degenerate test case. Valid single node singly linked list, n = 1, i.e. k > n.
    #
    # def test_5(self):
    #     head = sll = SinglyLinkedListNode.generate(32768)
    #
    #     for i in range(0, 32768 - 1):
    #         sll = sll.next
    #
    #     sll.next = head
    #
    #     self.assertEqual(None, returnKthToLast(head, 1)) # Degenerate test case. Large singly linked list with cycle.
    #
    # def test_6(self):
    #     head = SinglyLinkedListNode.generate(1)
    #     self.assertEqual(None, returnKthToLast(head, 0)) # Simple test case. Single node. k = 0
    #
    # def test_7(self):
    #     head = SinglyLinkedListNode.generate(2)
    #     self.assertEqual(None, returnKthToLast(head, 0))  # Simple test case. Single node. k = 0


if __name__ == "__main__":
    unittest.main()
