
import unittest

def stringCompression(string):
    pass
    
class StringCompression(unittest.TestCase):
    def test_1(self):
       self.assertEqual(stringCompression("aabcccccaaa"), "a2blc5a3")

    def test_2(self):
       self.assertEqual(stringCompression("aabcdef"), "aabcdef")


if __name__ == "__main__":
    unittest.main()
