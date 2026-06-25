from __future__ import annotations

import json
import unittest


# "<code>sll</code>" stands for a singly linked list
# 1 &le; length of <code>sll</code> &le; 10<sup>5</sup>
# "assume it is a singly linked list of integers"
class SinglyLinkedListNode:
    # <code>value</code> is passed the integer payload to be contained by the new <code>SinglyLinkedListNode</code>.
    def __init__(self, value: int) -> None:
        self.next = None
        self.value = value

    def dumps(self):
        s = ""
        s = "{\"value\": " + str(self.value)
        s += ", next: "
        if self.next is None:
            s += "null"
        else:
            s += str(self.next.dumps())
        s += "}"
        return s


    # <code>n</code> is passed the number of nodes to be created in the Singly Linked List. Must be greater than zero.
    @staticmethod
    def generate_X(n: int) -> SinglyLinkedListNode | None:

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

    #
    # David proposed unrolling the loop
    # We conjectured that there is always a beginning, middle and end to a loop
    # We therefore thought it wise to have at least 3 iterations in the unrolled loop, one for beginning, one for middle and one for end.
    # We positted that having 4 or 5 might make the choice of which one is the middle more clear, and settled on 4 for this situation.
    # We reckoned this was the most concise representation for 4 items
    #
    # Where this approach becomes awkward is in the lines like:
    #   <code>head.next.next.next = SinglyLinkedListNode(i)</code>
    # because <code>head.next.next...next</code> could get ridiculously long
    #
    # So we decided to contract that syntax, which led us to <code>generate_B</code>
    #
    @staticmethod
    def generate_A(n: int):
        if n != 4: # this is here to make it clear that this produces exactly 4 <code>SinglyLinkedListNode</code>s
            return None

        head = SinglyLinkedListNode(0)

        head.next = SinglyLinkedListNode(1)

        head.next.next = SinglyLinkedListNode(2)

        head.next.next.next = SinglyLinkedListNode(3)

        return head

    #
    # David proposed unrolling the loop
    # We conjectured that there is always a beginning, middle and end to a loop
    # We therefore thought it wise to have at least 3 iterations in the unrolled loop, one for beginning, one for middle and one for end.
    # We positted that having 4 or 5 might make the choice of which one is the middle more clear, and settled on 4 for this situation.
    # We reckoned this was the most concise representation for 4 items
    #
    # Where this approach becomes awkward is in the lines like:
    #   <code>head.next.next.next = SinglyLinkedListNode(i)</code>
    # because <code>head.next.next...next</code> could get ridiculously long
    #
    # So we decided to contract that syntax, which led us to <code>generate_B</code>
    #
    @staticmethod
    def generate_B(n: int):
        if n != 4: # this is here to make it clear that this produces exactly 4 <code>SinglyLinkedListNode</code>s
            return None

        i = 0
        head = SinglyLinkedListNode(i)

        i += 1
        head.next = SinglyLinkedListNode(i)

        i += 1
        head.next.next = SinglyLinkedListNode(i)

        i += 1
        head.next.next.next = SinglyLinkedListNode(i)

        return head

    #
    # We learned that compound assignments like:
    #   <code>head = sll = SinglyLinkedListNode(i)</code>
    # are evaluated in Python differently than other programming languages and our intuition
    #
    # For example the code above is equivalent to something like this:
    #   <code>x = SinglyLinkedListNode(i)</code>
    #   <code>head = x</code>
    #   <code>sll = x</code>
    #
    # We noticed that we could group lines of code together arbitrarily to
    # define beginning, middle and end, with the notion that repeated code
    # in the middle would become our looped code.
    #
    # Applying the grouping shown below led us to <code>generate_C</code>
    #
    @staticmethod
    def generate_C(n: int):
        # What is this code block and ones like it (intended to inoculate against bad input data) called?
        if n <= 0:
            return None

        # beginning
        i = 0
        head = sll = SinglyLinkedListNode(i)

        # middle
        i += 1
        sll.next = SinglyLinkedListNode(i)
        sll = sll.next

        i += 1
        sll.next = SinglyLinkedListNode(i)
        sll = sll.next

        # end
        i += 1
        sll.next = SinglyLinkedListNode(i)

        return head

    #
    # Having identified the beginning, middle and end, we focus on the middle to craft our loop.
    # Proceeding woodenly as if an automaton, I find the repeated block of code in the middle
    # eliminate repetition and indent it under a <code>while True:</code>. This is as if there were a <code>Loop:</code> statement or something.
    # Next decision is where and how to exit the loop.
    # We could put the loop before or after any of the lines of code of the repeated middle, so why not start at the beginning?
    # We place the exit condition (<code>if [expression]:</code>) and a <code>break</code> at the beginning.
    # How do we choose what <code><i>[expression]</i></code> will be?
    #
    # We know we're dealing with a count of nodes (<code>n</code>), so we realize we need to compare <code>i</code> with <code>n</code>:
    #
    # So in Python, we have the following choices:
    #   <code>i < n</code>
    #   <code>i == n</code>
    #   <code>i <= n</code>
    #   <code>i > n</code>
    #   <code>i >= n</code>
    #   <code>i != n</code>
    #
    # The one that leaped to our minds was:
    #   <code>i >= n</code>
    # We felt this was the right answer because we knew there would be one node created before exit condition was reached in the code,
    # so for the case <code>n == 1</code> we wanted the exit condition to leave the loop immediately.
    #   <code>if i == 1:<code>
    #   <code>  break</code>
    #
    # But we fell into a trap, because we concluded prematurely that we were done!
    # We forgot that there was an "end" block of code.  So the following code is subtly broken for the case where n == 1.
    # In such a case, it will create two nodes rather than one, because both the beginning and the end will always be executed.
    #
    @staticmethod
    def generate_D(n: int):
        # What is this code block and ones like it (intended to inoculate against bad input data) called?
        if n <= 0:
            return None

        # beginning
        ### This will always be called ###
        i = 0
        head = sll = SinglyLinkedListNode(i)

        # middle
        while True:
            if i >= n:
                break
            i += 1
            sll.next = SinglyLinkedListNode(i)
            sll = sll.next

        # end
        ### This will ALSO always be called ###
        i += 1
        sll.next = SinglyLinkedListNode(i)

        return head

    #
    # So we realized that if we insist on having three sections (beginning, middle, and end)
    # then perhaps we are going to have to ensure that some or all three sections have (exit) conditions to prevent their unwanted execution?
    @staticmethod
    def generate_E(n: int):
        # What is this code block and ones like it (intended to inoculate against bad input data) called?
        if n <= 0:
            return None

        # beginning
        ### This will always be called ###
        i = 0
        head = sll = SinglyLinkedListNode(i)

        # middle
        while True:
            i += 1
            if i >= n:
                return head
            sll.next = SinglyLinkedListNode(i)
            sll = sll.next

        # end
        ### This will now NEVER be called ###
        i += 1
        sll.next = SinglyLinkedListNode(i)

        return head








    # if in first loop do something special
    #
    # So we realized that if we insist on having three sections (beginning, middle, and end)
    # then perhaps we are going to have to ensure that some or all three sections have (exit) conditions to prevent their unwanted execution?
    @staticmethod
    def generate_F(n: int):
        # What is this code block and ones like it (intended to inoculate against bad input data) called?
        if n <= 0:
            return None

        # beginning
        ### This will always be called ###
        i = 0

        # middle
        while True:
            head = sll = SinglyLinkedListNode(i)
            i += 1
            if i >= n:
                return head
            sll.next = SinglyLinkedListNode(i)
            sll = sll.next

        # end
        ### This will ALSO always be called ###
        i += 1
        sll.next = SinglyLinkedListNode(i)

        return head

    #
    # So we realized that if we insist on having three sections (beginning, middle, and end)
    # then perhaps we are going to have to ensure that some or all three sections have (exit) conditions to prevent their unwanted execution?
    @staticmethod
    def generate_G(n: int):
        # What is this code block and ones like it (intended to inoculate against bad input data) called?
        if n <= 0:
            return None

        # beginning
        ### This will always be called ###
        i = 0
        head = sll = SinglyLinkedListNode(i)

        # middle
        while True:
            i += 1
            sll.next = SinglyLinkedListNode(i)
            if i > n:
                break # return?
            sll = sll.next

        # end
        ### This will ALSO always be called ###
        i += 1
        sll.next = SinglyLinkedListNode(i)

        return head



    @staticmethod
    def generate(n: int = 0) -> SinglyLinkedListNode | None:
        return SinglyLinkedListNode.generate_A(n)



# return integer offset between 0 and len(s1) if s2 is a substring of s1, else return -1
def returnKthToLastA(head: SinglyLinkedListNode | None, k: int) -> int | None:
    return None


returnKthToLast = returnKthToLastA
    
class ReturnKthToLastTests(unittest.TestCase):
    def test_lang_00(self): # DISSONANCE!  Python will often (but not always) optimize string literals to be the same object (reference)
        self.assertIs('{"value": 4, "next": null}', '{"value": 4, "next": null}')

    def test_lang_00s(self): # AMBIGUOUS!  Can't gell if python is comparing references or values
        self.assertTrue('{"value": 4, "next": null}' == '{"value": 4, "next": null}')


    def test_lang_01(self):
        self.assertIsNot('{"value": 4, "next": null}',  json.dumps(SinglyLinkedListNode(4).__dict__))

    def test_lang_02(self):
        self.assertEqual('{"value": 4, "next": null}', json.dumps(SinglyLinkedListNode(4).__dict__))

    def test_lang_03(self): # == compares CONTENTS of strings, not references
        self.assertTrue('{"value": 4, "next": null}' == json.dumps(SinglyLinkedListNode(4).__dict__))


    def test_lang_11(self):
        x = SinglyLinkedListNode(4)
        self.assertIs(x, x) # Language test case. Does python compare references?
        self.assertEqual(x, x) # AMBIGUOUS: Language test case. Does python compare references?
        self.assertTrue(x == x) # AMBIGUOUS: Language test case. Does python compare references?
        # Yes, it compares references for objects

    def test_lang_12(self):
        self.assertNotEqual(SinglyLinkedListNode(4), SinglyLinkedListNode(4))  # Language test case. Does python compare references?
        # Yes, it compares references

        # class Dummy:
        #     pass
        #
        # print(Dummy.__dict__)
        #print(json.dumps(SinglyLinkedListNode.__init__()))
        # print(json.dumps(SinglyLinkedListNode(0).__dict__))


    def test_20(self):
        self.assertEqual('{"value": 0, "next": null}', json.dumps(SinglyLinkedListNode(0).__dict__))

        # sll = SinglyLinkedListNode(0)
        # sll.generate = sll.generate_X
        # print(sll.generate(1))

    def test_100(self):
        print(SinglyLinkedListNode.generate_A(4).dumps())
        #self.assertEqual('{value: 0, next: {value: 1, next: {value: 2, next: {value: 3, next: null}}}}', json.dumps(SinglyLinkedListNode.generate_A.__dict__))


    # def test_100(self):
    #     self.assertEqual(None, SinglyLinkedListNode.generate(0)) # Degenerate test case. Null singly linked list.

    # def test_2(self):
    #     self.assertEqual(None, SinglyLinkedListNode.generate(2)) # Degenerate test case. Null singly linked list.
    #
    # def test_3(self):
    #     self.assertEqual(None, SinglyLinkedListNode.generate(3)) # Degenerate test case. Null singly linked list.

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
