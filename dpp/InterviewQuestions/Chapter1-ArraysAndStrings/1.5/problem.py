
import unittest

def oneAway(string):
    pass
    
class OneAway(unittest.TestCase):
    def test_1(self):
       self.assertEqual(oneAway("pale, ple"), "True")

    def test_2(self):
       self.assertEqual(oneAway("pales, pale"), "True")

    def test_3(self):
       self.assertEqual(oneAway("pale, bale"), "True")

    def test_4(self):
       self.assertEqual(oneAway("pale, bake"), "False")


if __name__ == "__main__":
    unittest.main()
