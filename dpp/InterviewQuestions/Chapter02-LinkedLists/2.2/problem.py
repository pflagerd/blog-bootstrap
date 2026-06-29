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

    def dumps(self):
        s = ""
        s += "{next: "
        if self.next is None:
            s += "null"
        else:
            s += str(self.next.dumps())
        s += ", \"value\": " + str(self.value)
        s += "}"
        return s


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
    # We decide to think about parameterizing things, and factoring out the common
    # code, reasoning the beginning might look a little different from the middle
    # which will look a little different from the end.
    #
    # <code>i</code> is the most obvious choice, and since <code>i = 0</code> has to happen before we
    # pass <code>i</code> to the <code>head.next... = SinglyLinkedListNode(i)</code> lines, there
    # seems to emerge groups of pairs of lines like:
    #
    # <code>i <i>= something</i></code>
    # <code>head<i>.something </i>= SinglyLinkedListNode(i)</code>
    #
    # So we could group lines of code together arbitrarily to
    # define beginning, middle and end, with the notion that repeated code
    # (in the middle?) would become our looped code.
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
    # If we're going to do something about the <code>head.next...</code> syntactic phenomenon, we're
    # going to need to keep track of <code>head</code> and be able to append new nodes to one another.
    #
    # This sort of sounds like a <code>tail</code> 
    #
    # We learned that compound assignments like:
    #   <code>head = tail = SinglyLinkedListNode(i)</code>
    # are evaluated in Python differently than other programming languages.
    #
    # Our intuition was based on math and on other C-like programming languages.
    #
    # Python evaluates the compound assignment above as something like this:
    #   <code>x = SinglyLinkedListNode(i) # x is an "invisible" temporary variable.</code>
    #   <code>head = x</code>
    #   <code>tail = x</code>
    #
    # Now some differences in the pattern of the groupings made a beginning, middle and end emerge.
    # They are shown as comments in the code below:
    #
    @staticmethod
    def generate_C(n: int):
        # What is this code block and ones like it (intended to inoculate against bad input data) called?
        if n <= 0:
            return None

        # beginning
        i = 0
        head = tail = SinglyLinkedListNode(i)

        # middle
        i += 1
        tail.next = SinglyLinkedListNode(i)
        tail = tail.next

        i += 1
        tail.next = SinglyLinkedListNode(i)
        tail = tail.next

        # end
        i += 1
        tail.next = SinglyLinkedListNode(i)

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
        head = tail = SinglyLinkedListNode(i)

        # middle
        while True:
            if i >= n:
                break
            i += 1
            tail.next = SinglyLinkedListNode(i)
            tail = tail.next

        # end
        ### This will ALSO always be called ###
        i += 1
        tail.next = SinglyLinkedListNode(i)

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
        head = tail = SinglyLinkedListNode(i)

        # middle
        while True:
            if i > n - 1: # CHANGED to make it get called one time less.
                break
            i += 1
            tail.next = SinglyLinkedListNode(i)
            tail = tail.next

        # end
        ### This will ALSO always be called ###
        i += 1
        tail.next = SinglyLinkedListNode(i)

        return head


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
        head = tail = SinglyLinkedListNode(i)

        # middle
        while True:
            i += 1
            if i >= n:
                return head
            tail.next = SinglyLinkedListNode(i)
            tail = tail.next

        # end
        ### This will now NEVER be called ###
        i += 1
        tail.next = SinglyLinkedListNode(i)

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


    # The __dict__ method actually orders the keys in the order they were defined (typically in the __init__)
    # Since we defined next first, the following should fail.
    def test_lang_01(self):
        self.assertIsNot('{"value": 4, "next": null}',  json.dumps(SinglyLinkedListNode(4).__dict__))

    # But this one should pass, because the order matches.
    def test_lang_02(self):
        self.assertEqual('{"next": null, "value": 4}', json.dumps(SinglyLinkedListNode(4).__dict__))

    def test_lang_03(self): # The == operator compares CONTENTS of strings, not references
        self.assertTrue('{"next": null, "value": 4}' == json.dumps(SinglyLinkedListNode(4).__dict__))


    def test_lang_11(self):
        x = SinglyLinkedListNode(4)
        self.assertIs(x, x) # Language test case. Does python compare references?
        self.assertEqual(x, x) # AMBIGUOUS: Language test case. Does python compare references?
        self.assertTrue(x == x) # AMBIGUOUS: Language test case. Does python compare references?
        # Yes, it compares references for objects

    # Except now we defined an __eq__ method so contents rather than references are compared
    def test_lang_12(self):
        self.assertEqual(SinglyLinkedListNode(4), SinglyLinkedListNode(4))


    # Test __dict__.  This works because json.dumps() displays the keys in the order the attributes (.next and .value) were defined (in __init__)
    def test_20(self):
        self.assertEqual('{"next": null, "value": 0}', json.dumps(SinglyLinkedListNode(0).__dict__))

    def test_21(self):
        self.assertNotEqual('{"value": 0, "next": null}', json.dumps(SinglyLinkedListNode(0).__dict__))


    # Notice that the way we've created the dumps() method, the keys appear in alphabetic order, so the following doesn't work
    # even though according to the json standard it should be allowed because json allows keys to appear in any order.
    # Since we're using literal strings, and because self.assertX() compares literal strings literally, we've got this
    # minor conundrum.
    def test_generate_A_00(self):
        self.assertNotEqual('{"value": 0, "next": null}', json.dumps(SinglyLinkedListNode(0).dumps()))

    def test_generate_A_10(self):
        print(SinglyLinkedListNode.generate_A(4).dumps())
        self.assertEqual('{next: {next: {next: {next: null, "value": 3}, "value": 2}, "value": 1}, "value": 0}', SinglyLinkedListNode.generate_A(4).dumps())


    def test_generate_B_00(self):
        self.assertEqual(SinglyLinkedListNode.generate_A(4), SinglyLinkedListNode.generate_B(4))


    def test_generate_C_00(self):
        self.assertEqual(SinglyLinkedListNode.generate_A(4), SinglyLinkedListNode.generate_C(4))


    def test_generate_D_00(self):
        self.assertNotEqual(SinglyLinkedListNode.generate_A(4), SinglyLinkedListNode.generate_D(4))


    def test_generate_E_00(self):
        self.assertEqual(SinglyLinkedListNode.generate_A(4), SinglyLinkedListNode.generate_E(4))


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
