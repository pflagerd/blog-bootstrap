import unittest


# if s2 is a substring of s1
def isSubstring(s1: str, s2: str) -> bool:
    return s2 in s1


# return integer offset between 0 and len(s1) if s2 is a substring of s1, else return -1
def isRotationA(s1: str, s2: str) -> int:
    # write code here that calls isSubstring() exactly one time
    s = s2 + s2
    return isSubstring(s, s1) and len(s) == 2 * len(s1)


isRotation = isRotationA
    
class StringRotation(unittest.TestCase):
    def test_0(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                           "The quick brown fox jumps over the lazy dog"))

    def test_1(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                           "he quick brown fox jumps over the lazy dogT"))

    def test_2(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                           "e quick brown fox jumps over the lazy dogTh"))

    def test_3(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                           " quick brown fox jumps over the lazy dogThe"))

    def test_4(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                           "quick brown fox jumps over the lazy dogThe "))

    def test_5(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                           "uick brown fox jumps over the lazy dogThe q"))

    def test_6(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                           "ick brown fox jumps over the lazy dogThe qu"))

    def test_7(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                           "ck brown fox jumps over the lazy dogThe qui"))

    def test_8(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                           "k brown fox jumps over the lazy dogThe quic"))

    def test_9(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                           " brown fox jumps over the lazy dogThe quick"))

    def test_10(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                            "brown fox jumps over the lazy dogThe quick "))

    def test_11(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                            "rown fox jumps over the lazy dogThe quick b"))

    def test_12(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                            "own fox jumps over the lazy dogThe quick br"))

    def test_13(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                            "wn fox jumps over the lazy dogThe quick bro"))

    def test_14(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                            "n fox jumps over the lazy dogThe quick brow"))

    def test_15(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                            " fox jumps over the lazy dogThe quick brown"))

    def test_16(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                            "fox jumps over the lazy dogThe quick brown "))

    def test_17(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                            "ox jumps over the lazy dogThe quick brown f"))

    def test_18(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                            "x jumps over the lazy dogThe quick brown fo"))

    def test_19(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                            " jumps over the lazy dogThe quick brown fox"))

    def test_20(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                            "jumps over the lazy dogThe quick brown fox "))

    def test_21(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                            "umps over the lazy dogThe quick brown fox j"))

    def test_22(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                            "mps over the lazy dogThe quick brown fox ju"))

    def test_23(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                            "ps over the lazy dogThe quick brown fox jum"))

    def test_24(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                            "s over the lazy dogThe quick brown fox jump"))

    def test_25(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                            " over the lazy dogThe quick brown fox jumps"))

    def test_26(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                            "over the lazy dogThe quick brown fox jumps "))

    def test_27(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                            "ver the lazy dogThe quick brown fox jumps o"))

    def test_28(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                            "er the lazy dogThe quick brown fox jumps ov"))

    def test_29(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                            "r the lazy dogThe quick brown fox jumps ove"))

    def test_30(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                            " the lazy dogThe quick brown fox jumps over"))

    def test_31(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                            "the lazy dogThe quick brown fox jumps over "))

    def test_32(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                            "he lazy dogThe quick brown fox jumps over t"))

    def test_33(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                            "e lazy dogThe quick brown fox jumps over th"))

    def test_34(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                            " lazy dogThe quick brown fox jumps over the"))

    def test_35(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                            "lazy dogThe quick brown fox jumps over the "))

    def test_36(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                            "azy dogThe quick brown fox jumps over the l"))

    def test_37(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                            "zy dogThe quick brown fox jumps over the la"))

    def test_38(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                            "y dogThe quick brown fox jumps over the laz"))

    def test_39(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                            " dogThe quick brown fox jumps over the lazy"))

    def test_40(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                            "dogThe quick brown fox jumps over the lazy "))

    def test_41(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                            "ogThe quick brown fox jumps over the lazy d"))

    def test_42(self):
        self.assertEqual(True, isRotation("The quick brown fox jumps over the lazy dog",
                                            "gThe quick brown fox jumps over the lazy do"))

if __name__ == "__main__":
    unittest.main()
