
import unittest

def urlify(string, length):
    pass
    
class Urlify(unittest.TestCase):
    def test_1(self):
       self.assertEqual(urlify("Mr John Smith    ", "13"), "Raise <code>ValueError</code>")

    def test_2(self):
       self.assertEqual(urlify("None", "13"), "Raise <code>ValueError</code>")

    def test_3(self):
       self.assertEqual(urlify("Mr John Smith    ", "None"), "Raise <code>ValueError</code>")

    def test_4(self):
       self.assertEqual(urlify("None", "None"), "Raise <code>ValueError</code>")

    def test_5(self):
       self.assertEqual(urlify("", "13"), "")

    def test_6(self):
       self.assertEqual(urlify("Mr John Smith    ", ""), "Raise <code>ValueError</code>")

    def test_7(self):
       self.assertEqual(urlify("Mr John Smith    ", "-1"), "Raise <code>ValueError</code>")

    def test_8(self):
       self.assertEqual(urlify("Mr John Smith    ", "3"), "Raise <code>ValueError</code>")

    def test_9(self):
       self.assertEqual(urlify("Mr John Smith    ", "12"), "Raise <code>ValueError</code>")

    def test_10(self):
       self.assertEqual(urlify("Mr John Smith    ", "14"), "Raise <code>ValueError</code>")


if __name__ == "__main__":
    unittest.main()
