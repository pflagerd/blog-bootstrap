from __future__ import annotations

import json
import unittest

singlyLinkedListNode_str_1 = '{"next": null, "value": 0}'
singlyLinkedListNode_str_2 = '{"next": {"next": null, "value": 1}, "value": 0}'
singlyLinkedListNode_str_3 = '{"next": {"next": {"next": null, "value": 2}, "value": 1}, "value": 0}'
singlyLinkedListNode_str_4 = '{"next": {"next": {"next": {"next": null, "value": 3}, "value": 2}, "value": 1}, "value": 0}'

print(f"singlyLinkedListNode_str_1 == '{singlyLinkedListNode_str_1}'")
print(f"singlyLinkedListNode_str_2 == '{singlyLinkedListNode_str_2}'")
print(f"singlyLinkedListNode_str_3 == '{singlyLinkedListNode_str_3}'")
print(f"singlyLinkedListNode_str_4 == '{singlyLinkedListNode_str_4}'")

singlyLinkedListNode__repr__1 = 'SinglyLinkedListNode(0)'
singlyLinkedListNode__repr__2 = 'SinglyLinkedListNode(0, SinglyLinkedListNode(1))'
singlyLinkedListNode__repr__3 = 'SinglyLinkedListNode(0, SinglyLinkedListNode(1, SinglyLinkedListNode(2)))'
singlyLinkedListNode__repr__4 = 'SinglyLinkedListNode(0, SinglyLinkedListNode(1, SinglyLinkedListNode(2, SinglyLinkedListNode(3))))'

print(f"singlyLinkedListNode__repr__1 == '{singlyLinkedListNode__repr__1}'")
print(f"singlyLinkedListNode__repr__2 == '{singlyLinkedListNode__repr__2}'")
print(f"singlyLinkedListNode__repr__3 == '{singlyLinkedListNode__repr__3}'")
print(f"singlyLinkedListNode__repr__4 == '{singlyLinkedListNode__repr__4}'")

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


    #
    # David proposed unrolling the loop
    # We conjectured that there is always a beginning, middle and end to a loop
    # We therefore thought it wise to have at least 3 iterations in the unrolled loop of our example code: one for beginning, one for middle and one for end.
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
    # Let's call the grouped lines of code "code groupings".
    #
    # so for example the following two lines are called a "code grouping":
    #
    #  <code>i += 1</code>
    #  <code>head.next = SinglyLinkedListNode(i)</code>
    #
    # Therefore, in the following function, each code grouping has a comment in front of it.
    #
    # Code groupings can contain any number of contiguous lines of code.
    #
    @staticmethod
    def generate_B(n: int):
        # this is a code grouping
        if n != 4: # this is here to make it clear that this produces exactly 4 <code>SinglyLinkedListNode</code>s
            return None

        # this is a code grouping
        i = 0
        head = SinglyLinkedListNode(i)

        # this is a code grouping
        i += 1
        head.next = SinglyLinkedListNode(i)

        # this is a code grouping
        i += 1
        head.next.next = SinglyLinkedListNode(i)

        # this is a code grouping
        i += 1
        head.next.next.next = SinglyLinkedListNode(i)

        # this is a code grouping
        return head

    #
    # If we're going to do something about the <code>head.next...</code> syntactic phenomenon, we're
    # going to need to keep track of <code>head</code> and be able to append new nodes to one another.
    #
    # This sort of sounds like a <code>tail</code>
    #
    # IMPORTANT: We are beginning to realize that, since we are using Python, it may be useful for us to use terminology
    # from the official Python grammar to help us communicate what we're doing and thinking with greater clarity.
    #
    # This can be found here: <a href="https://docs.python.org/3/reference/grammar.html">Official Python Grammar</a>
    #
    # But other popular tutorial, reference and discusion sites can be useful when a particular grammar construction isn't explicitly named by the Official Python Grammar.
    #
    # For example, the following statement in Python has NO particular name in the grammar:
    #   <code>head = tail = SinglyLinkedListNode(i)</code>
    #
    # <a href="https://docs.python.org/3/reference/simple_stmts.html#assignment-statements">Python Official Grammar</a> shows us that
    # this construct exists as an <a href="https://docs.python.org/3/reference/simple_stmts.html#assignment-statements:~:text=assignment_stmt%3A%20(target_list%20%22%3D%22)%2B%20(starred_expression%20%7C%20yield_expression)">assignment_stmt</a>
    # but it is more usefully called a <a href="https://realpython.com/cheatsheets/python/#:~:text=Parallel%20%26-,Chained%20Assignments,-x%2C%20y">chained assignment</a> in the realpython.com site.
    #
    # In any case we learned that Python's <i>chained assignments</i> like:
    #   <code>head = tail = SinglyLinkedListNode(i)</code>
    # are evaluated differently than other programming languages.
    #
    # Our intuition was based on math and on other C-like programming languages, and Python's implementation seemed counter-intuitive.
    #
    # Python evaluates the <i>chained assignement</> above as something like this:
    #   <code>x = SinglyLinkedListNode(i) # x is an "invisible" temporary variable.</code>
    #   <code>head = x</code>
    #   <code>tail = x</code>
    #
    # Now some differences in the pattern of the groupings made a beginning, middle and end emerge.
    #
    # EXCEPT the designation of the last section being the "end" is purely arbitrary because it's identical
    # to the "middle", except for the <code>tail = tail.next which is not needed - but also not harmful</code>
    #
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
        # tail = tail.next

        return head

    #
    # Having identified the beginning, middle and end, we focus on the middle to craft our loop.
    # Proceeding woodenly as if an automaton, I find the repeated block of code in the middle,
    # eliminate repetition and indent it under a <code>while True:</code>. This is as if there were a <code>Loop:</code> statement or something.
    #
    # Next decision is where and how to exit the loop.
    # We could put an exit condition (<code>if</code>) before or after any of the lines of code of the repeated middle, so why not start at the beginning?
    #
    # David observes that we could put the exit condition at the beginning of the <i>block</i> or the end of the <i>block</i>. We could call that "pre" and "post".
    # This is typical constructs in other languages such as Pascal's <code>repeat <i>block<i> until <i>condition</i> </code> or <code>while <i>condition</i>...</code>.
    #
    # We decide to place the <i>condition</i> (<code>if [expression]:</code>) and a <code>break</code> at the beginning.
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
        # tail = tail.next

        return head

    #
    # So we realized that because the end block was always getting called, we were getting one more element in the list
    # than we wanted (i.e. 5 instead of 4).
    #
    # So we figured we could make the middle's <code>if <i>condition</i></code> execute its code block
    # one time less frequently (add one fewer nodes to the list)
    #
    # Of course, we also realized that we were still always going to get at least two nodes, since the
    # beginning and the end were always getting executed.
    #
    # So we needed a more complete set of tests. Hence <code>test_generate_E_10()</code>
    #
    # But <code>test_generate_E_10()</code> kept failing in unexpected places.
    #
    # In fact, we were always getting one more element than we wanted!
    #
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
            if i >= n - 1: # CHANGED to make it get called one time less.
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
    # Having added tests for SinglyLinkedListNode.generate_E(1), SinglyLinkedListNode.generate_E(2),
    # SinglyLinkedListNode.generate_E(3), and SinglyLinkedListNode.generate_E(4) we observed that
    # the tests for SinglyLinkedListNode.generate_E(1) and SinglyLinkedListNode.generate_E(2) were failing, because they
    # were generating one more node than expected.
    #
    # So we figured we could add an <code>if <i>condition</i></code> to the "end".
    #
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
            if i >= n - 1: # CHANGED to make it get called one time less.
                break
            i += 1
            tail.next = SinglyLinkedListNode(i)
            tail = tail.next

        # end
        ### This will ALSO always be called ###
        if n >= 9999999:
            i += 1
            tail.next = SinglyLinkedListNode(i)

        return head

    #
    # Yes, it has become clear that the "end" section is deletable.
    #
    # So really, we have now a beginning and a middle and and empty end
    #
    @staticmethod
    def generate_G(n: int):
        # What is this code block and ones like it (intended to inoculate against bad input data) called?
        if n <= 0:
            return None

        # beginning
        ### This will always be called ###
        i = 0
        head = tail = SinglyLinkedListNode(i)

        # middle
        while True:
            if i >= n - 1: # CHANGED to make it get called one time less.
                break
            i += 1
            tail.next = SinglyLinkedListNode(i)
            tail = tail.next

        # end

        return head

    #
    # Is the if condition better if we pre-increment i?
    #
    # It has the advantage of eliminating the <code>-1</code>, but it makes our
    # heads go to a <code>for</code> loop.
    #
    @staticmethod
    def generate_H(n: int):
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
            if i >= n: # CHANGED to make it get called one time less.
                break
            tail.next = SinglyLinkedListNode(i)
            tail = tail.next

        # end

        return head


    #
    # So here's a for loop
    #
    # We tried torturing a <code>head = tail = SinglyLinkedListNode(0) into the
    # <code>for</code> loop, but that ended up with all kinds of <code>global</code>
    # hacks with looked uglier than just separating the beginning again
    #
    @staticmethod
    def generate_I(n: int):
        # What is this code block and ones like it (intended to inoculate against bad input data) called?
        if n <= 0:
            return None

        # beginning
        head = tail = SinglyLinkedListNode(0)
        # middle
        for i in range(1, n):
            tail.next = SinglyLinkedListNode(i)
            tail = tail.next

        # end

        return head


    #
    # And in the same general nature, we could just use the while loop
    # as a kind of for loop as before,
    #
    @staticmethod
    def generate_J(n: int):
        # What is this code block and ones like it (intended to inoculate against bad input data) called?
        if n <= 0:
            return None

        # beginning
        ### This will always be called ###
        i = 0
        head = tail = SinglyLinkedListNode(0)

        # middle
        while i < n - 1:
            i += 1
            tail.next = SinglyLinkedListNode(i)
            tail = tail.next

        # end

        return head


    #
    # Or this slight variant where the i += 1 is further down in the <code>while</code>'s body.
    #
    # It's vaguely nicer because of <code>while i < n:</code> being nicer than <code>while i < n - 1</code>
    #
    @staticmethod
    def generate_K(n: int):
        # What is this code block and ones like it (intended to inoculate against bad input data) called?
        if n <= 0:
            return None

        # beginning
        ### This will always be called ###
        head = tail = SinglyLinkedListNode(0)

        # middle
        i = 1
        while i < n:
            tail.next = SinglyLinkedListNode(i)
            tail = tail.next
            i += 1

        # end

        return head




    #
    # Or this slight variant where the i += 1 is further down in the <code>while</code>'s body.
    #
    # It's vaguely nicer because of <code>while i < n:</code> being nicer than <code>while i < n - 1</code>
    #
    @staticmethod
    def generate_AA(n: int):
        # What is this code block and ones like it (intended to inoculate against bad input data) called?
        if n <= 0:
            return None

        head = current = SinglyLinkedListNode(0)
        for i in range(1, n):
            current.next = SinglyLinkedListNode(i)
            current = current.next

        return head


    #
    # Recursive
    #
    @staticmethod
    def generate_BB(n: int):
        # What is this code block and ones like it (intended to inoculate against bad input data) called?
        if n <= 0:
            return None

        def generate_BBx(head: SinglyLinkedListNode | None, n: int) -> SinglyLinkedListNode:
            new_head = SinglyLinkedListNode(n - 1)
            new_head.next = head
            if n == 1:
                return new_head
            return generate_BBx(new_head, n - 1)


        return generate_BBx(None, n)





    #
    # Added some tests for __init__() args to check out the new __init__() form, which looks kind of
    # more natural in the self.assertEqual() tests.
    #

    #
    # Added a __repr__() and some tests for it.
    #


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
        print(f"SinglyLinkedListNode.generate_A(4).dumps() == '{SinglyLinkedListNode.generate_A(4).dumps()}'")
        self.assertEqual('{"next": {"next": {"next": {"next": null, "value": 3}, "value": 2}, "value": 1}, "value": 0}', SinglyLinkedListNode.generate_A(4).dumps())


    def test_generate_B_00(self):
        self.assertEqual(SinglyLinkedListNode.generate_A(4), SinglyLinkedListNode.generate_B(4))


    def test_generate_C_00(self):
        self.assertEqual(SinglyLinkedListNode.generate_A(4), SinglyLinkedListNode.generate_C(4))


    def test_generate_D_00(self):
        # This is what we were hoping would work, but didn't (hence <code>assert<b>NOT</b>Equal</code>)
        self.assertNotEqual('{"next": null, "value": 1}', SinglyLinkedListNode.generate_D(1).dumps())
        # In fact we got 2 nodes instead of 1.
        print(f"SinglyLinkedListNode.generate_D(1).dumps() == '{SinglyLinkedListNode.generate_D(1).dumps()}'")
        self.assertEqual('{"next": {"next": {"next": null, "value": 2}, "value": 1}, "value": 0}', SinglyLinkedListNode.generate_D(1).dumps())
        # Try for 2, 3 and 4
        # YIKES: 2 gets 4 nodes
        self.assertEqual('{"next": {"next": {"next": {"next": null, "value": 3}, "value": 2}, "value": 1}, "value": 0}', SinglyLinkedListNode.generate_D(2).dumps())
        # YIKES: 3 gets 5 nodes
        self.assertEqual('{"next": {"next": {"next": {"next": {"next": null, "value": 4}, "value": 3}, "value": 2}, "value": 1}, "value": 0}', SinglyLinkedListNode.generate_D(3).dumps())
        # YIKES: 4 gets 6 nodes
        self.assertNotEqual(SinglyLinkedListNode.generate_A(4), SinglyLinkedListNode.generate_D(4))


    def test_generate_E_00(self):
        self.assertNotEqual(SinglyLinkedListNode.generate_A(4), SinglyLinkedListNode.generate_E(4))

    def test_generate_E_10(self):
        print(f"SinglyLinkedListNode.generate_E(1).dumps() == '{SinglyLinkedListNode.generate_E(1).dumps()}'")
        self.assertEqual('{"next": {"next": null, "value": 1}, "value": 0}', SinglyLinkedListNode.generate_E(1).dumps())
        print(f"SinglyLinkedListNode.generate_E(2).dumps() == '{SinglyLinkedListNode.generate_E(2).dumps()}'")
        self.assertEqual('{"next": {"next": {"next": null, "value": 2}, "value": 1}, "value": 0}', SinglyLinkedListNode.generate_E(2).dumps())
        print(f"SinglyLinkedListNode.generate_E(3).dumps() == '{SinglyLinkedListNode.generate_E(3).dumps()}'")
        self.assertEqual('{"next": {"next": {"next": {"next": null, "value": 3}, "value": 2}, "value": 1}, "value": 0}', SinglyLinkedListNode.generate_E(3).dumps())
        print(f"SinglyLinkedListNode.generate_E(4).dumps() == '{SinglyLinkedListNode.generate_E(4).dumps()}'")
        self.assertEqual('{"next": {"next": {"next": {"next": {"next": null, "value": 4}, "value": 3}, "value": 2}, "value": 1}, "value": 0}', SinglyLinkedListNode.generate_E(4).dumps())


    def test_generate_F_10(self):
        print(f"SinglyLinkedListNode.generate_F(1).dumps() == '{SinglyLinkedListNode.generate_F(1).dumps()}'")
        self.assertEqual('{"next": null, "value": 0}', SinglyLinkedListNode.generate_F(1).dumps())
        print(f"SinglyLinkedListNode.generate_F(2).dumps() == '{SinglyLinkedListNode.generate_F(2).dumps()}'")
        self.assertEqual('{"next": {"next": null, "value": 1}, "value": 0}', SinglyLinkedListNode.generate_F(2).dumps())
        print(f"SinglyLinkedListNode.generate_F(3).dumps() == '{SinglyLinkedListNode.generate_F(3).dumps()}'")
        self.assertEqual('{"next": {"next": {"next": null, "value": 2}, "value": 1}, "value": 0}', SinglyLinkedListNode.generate_F(3).dumps())
        print(f"SinglyLinkedListNode.generate_F(4).dumps() == '{SinglyLinkedListNode.generate_F(4).dumps()}'")
        self.assertEqual('{"next": {"next": {"next": {"next": null, "value": 3}, "value": 2}, "value": 1}, "value": 0}', SinglyLinkedListNode.generate_F(4).dumps())


    def test_generate_G_10(self):
        print(f"SinglyLinkedListNode.generate_G(1).dumps() == '{SinglyLinkedListNode.generate_G(1).dumps()}'")
        self.assertEqual('{"next": null, "value": 0}', SinglyLinkedListNode.generate_G(1).dumps())
        print(f"SinglyLinkedListNode.generate_G(2).dumps() == '{SinglyLinkedListNode.generate_G(2).dumps()}'")
        self.assertEqual('{"next": {"next": null, "value": 1}, "value": 0}', SinglyLinkedListNode.generate_G(2).dumps())
        print(f"SinglyLinkedListNode.generate_G(3).dumps() == '{SinglyLinkedListNode.generate_G(3).dumps()}'")
        self.assertEqual('{"next": {"next": {"next": null, "value": 2}, "value": 1}, "value": 0}', SinglyLinkedListNode.generate_G(3).dumps())
        print(f"SinglyLinkedListNode.generate_G(4).dumps() == '{SinglyLinkedListNode.generate_G(4).dumps()}'")
        self.assertEqual('{"next": {"next": {"next": {"next": null, "value": 3}, "value": 2}, "value": 1}, "value": 0}', SinglyLinkedListNode.generate_F(4).dumps())


    def test_generate_H_10(self):
        print(f"SinglyLinkedListNode.generate_H(1).dumps() == '{SinglyLinkedListNode.generate_H(1).dumps()}'")
        self.assertEqual('{"next": null, "value": 0}', SinglyLinkedListNode.generate_H(1).dumps())
        print(f"SinglyLinkedListNode.generate_H(2).dumps() == '{SinglyLinkedListNode.generate_H(2).dumps()}'")
        self.assertEqual('{"next": {"next": null, "value": 1}, "value": 0}', SinglyLinkedListNode.generate_H(2).dumps())
        print(f"SinglyLinkedListNode.generate_H(3).dumps() == '{SinglyLinkedListNode.generate_H(3).dumps()}'")
        self.assertEqual('{"next": {"next": {"next": null, "value": 2}, "value": 1}, "value": 0}', SinglyLinkedListNode.generate_H(3).dumps())
        print(f"SinglyLinkedListNode.generate_H(4).dumps() == '{SinglyLinkedListNode.generate_H(4).dumps()}'")
        self.assertEqual('{"next": {"next": {"next": {"next": null, "value": 3}, "value": 2}, "value": 1}, "value": 0}', SinglyLinkedListNode.generate_F(4).dumps())


    def test_generate_I_10(self):
        print(f"SinglyLinkedListNode.generate_I(1).dumps() == '{SinglyLinkedListNode.generate_I(1).dumps()}'")
        self.assertEqual('{"next": null, "value": 0}', SinglyLinkedListNode.generate_I(1).dumps())
        print(f"SinglyLinkedListNode.generate_I(2).dumps() == '{SinglyLinkedListNode.generate_I(2).dumps()}'")
        self.assertEqual('{"next": {"next": null, "value": 1}, "value": 0}', SinglyLinkedListNode.generate_I(2).dumps())
        print(f"SinglyLinkedListNode.generate_I(3).dumps() == '{SinglyLinkedListNode.generate_I(3).dumps()}'")
        self.assertEqual('{"next": {"next": {"next": null, "value": 2}, "value": 1}, "value": 0}', SinglyLinkedListNode.generate_I(3).dumps())
        print(f"SinglyLinkedListNode.generate_I(4).dumps() == '{SinglyLinkedListNode.generate_I(4).dumps()}'")
        self.assertEqual('{"next": {"next": {"next": {"next": null, "value": 3}, "value": 2}, "value": 1}, "value": 0}', SinglyLinkedListNode.generate_F(4).dumps())


    def test_generate_J_10(self):
        print(f"SinglyLinkedListNode.generate_J(1).dumps() == '{SinglyLinkedListNode.generate_J(1).dumps()}'")
        self.assertEqual('{"next": null, "value": 0}', SinglyLinkedListNode.generate_J(1).dumps())
        print(f"SinglyLinkedListNode.generate_J(2).dumps() == '{SinglyLinkedListNode.generate_J(2).dumps()}'")
        self.assertEqual('{"next": {"next": null, "value": 1}, "value": 0}', SinglyLinkedListNode.generate_J(2).dumps())
        print(f"SinglyLinkedListNode.generate_J(3).dumps() == '{SinglyLinkedListNode.generate_J(3).dumps()}'")
        self.assertEqual('{"next": {"next": {"next": null, "value": 2}, "value": 1}, "value": 0}', SinglyLinkedListNode.generate_J(3).dumps())
        print(f"SinglyLinkedListNode.generate_J(4).dumps() == '{SinglyLinkedListNode.generate_J(4).dumps()}'")
        self.assertEqual('{"next": {"next": {"next": {"next": null, "value": 3}, "value": 2}, "value": 1}, "value": 0}', SinglyLinkedListNode.generate_F(4).dumps())


    def test_generate_K_10(self):
        print(f"SinglyLinkedListNode.generate_K(1).dumps() == '{SinglyLinkedListNode.generate_K(1).dumps()}'")
        self.assertEqual('{"next": null, "value": 0}', SinglyLinkedListNode.generate_K(1).dumps())
        print(f"SinglyLinkedListNode.generate_K(2).dumps() == '{SinglyLinkedListNode.generate_K(2).dumps()}'")
        self.assertEqual('{"next": {"next": null, "value": 1}, "value": 0}', SinglyLinkedListNode.generate_K(2).dumps())
        print(f"SinglyLinkedListNode.generate_K(3).dumps() == '{SinglyLinkedListNode.generate_K(3).dumps()}'")
        self.assertEqual('{"next": {"next": {"next": null, "value": 2}, "value": 1}, "value": 0}', SinglyLinkedListNode.generate_K(3).dumps())
        print(f"SinglyLinkedListNode.generate_K(4).dumps() == '{SinglyLinkedListNode.generate_K(4).dumps()}'")
        self.assertEqual('{"next": {"next": {"next": {"next": null, "value": 3}, "value": 2}, "value": 1}, "value": 0}', SinglyLinkedListNode.generate_F(4).dumps())


    def test_generate_AA_10(self):
        print(f"SinglyLinkedListNode.generate_AA(1).dumps() == '{SinglyLinkedListNode.generate_AA(1).dumps()}'")
        self.assertEqual('{"next": null, "value": 0}', SinglyLinkedListNode.generate_AA(1).dumps())
        print(f"SinglyLinkedListNode.generate_AA(2).dumps() == '{SinglyLinkedListNode.generate_AA(2).dumps()}'")
        self.assertEqual('{"next": {"next": null, "value": 1}, "value": 0}', SinglyLinkedListNode.generate_AA(2).dumps())
        print(f"SinglyLinkedListNode.generate_AA(3).dumps() == '{SinglyLinkedListNode.generate_AA(3).dumps()}'")
        self.assertEqual('{"next": {"next": {"next": null, "value": 2}, "value": 1}, "value": 0}', SinglyLinkedListNode.generate_AA(3).dumps())
        print(f"SinglyLinkedListNode.generate_AA(4).dumps() == '{SinglyLinkedListNode.generate_AA(4).dumps()}'")
        self.assertEqual('{"next": {"next": {"next": {"next": null, "value": 3}, "value": 2}, "value": 1}, "value": 0}', SinglyLinkedListNode.generate_F(4).dumps())


    def test_generate_BB_10(self):
        print(f"SinglyLinkedListNode.generate_BB(1).dumps() == '{SinglyLinkedListNode.generate_BB(1).dumps()}'")
        self.assertEqual('{"next": null, "value": 0}', SinglyLinkedListNode.generate_BB(1).dumps())
        print(f"SinglyLinkedListNode.generate_BB(2).dumps() == '{SinglyLinkedListNode.generate_BB(2).dumps()}'")
        self.assertEqual('{"next": {"next": null, "value": 1}, "value": 0}', SinglyLinkedListNode.generate_BB(2).dumps())
        print(f"SinglyLinkedListNode.generate_BB(3).dumps() == '{SinglyLinkedListNode.generate_BB(3).dumps()}'")
        self.assertEqual('{"next": {"next": {"next": null, "value": 2}, "value": 1}, "value": 0}', SinglyLinkedListNode.generate_BB(3).dumps())
        print(f"SinglyLinkedListNode.generate_BB(4).dumps() == '{SinglyLinkedListNode.generate_BB(4).dumps()}'")
        self.assertEqual('{"next": {"next": {"next": {"next": null, "value": 3}, "value": 2}, "value": 1}, "value": 0}', SinglyLinkedListNode.generate_F(4).dumps())


    def test__init__(self):
        self.assertEqual(singlyLinkedListNode_str_1, SinglyLinkedListNode(0).dumps())
        self.assertEqual(singlyLinkedListNode_str_2, SinglyLinkedListNode(0, SinglyLinkedListNode(1)).dumps())
        self.assertEqual(singlyLinkedListNode_str_3, SinglyLinkedListNode(0, SinglyLinkedListNode(1, SinglyLinkedListNode(2))).dumps())
        self.assertEqual(singlyLinkedListNode_str_4, SinglyLinkedListNode(0, SinglyLinkedListNode(1, SinglyLinkedListNode(2, SinglyLinkedListNode(3)))).dumps())


    def test__repr__(self):
        self.assertEqual(eval(repr(SinglyLinkedListNode(0))), SinglyLinkedListNode(0))
        self.assertEqual(eval(repr(SinglyLinkedListNode(0, SinglyLinkedListNode(1)))), SinglyLinkedListNode(0, SinglyLinkedListNode(1)))
        self.assertEqual(eval(repr(SinglyLinkedListNode(0, SinglyLinkedListNode(1, SinglyLinkedListNode(2))))), SinglyLinkedListNode(0, SinglyLinkedListNode(1, SinglyLinkedListNode(2))))
        self.assertEqual(eval(repr(SinglyLinkedListNode(0, SinglyLinkedListNode(1, SinglyLinkedListNode(2, SinglyLinkedListNode(3)))))), SinglyLinkedListNode(0, SinglyLinkedListNode(1, SinglyLinkedListNode(2, SinglyLinkedListNode(3)))))


    def tests_end(self):
        self.assertTrue(True)
        print("Tests all done.")

if __name__ == "__main__":
    unittest.main()
