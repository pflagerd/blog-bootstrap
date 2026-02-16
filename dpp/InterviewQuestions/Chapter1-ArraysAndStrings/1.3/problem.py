import unittest


def urlify(string, length):
    pass


class Urlify(unittest.TestCase):
    def test_1(self):
        with self.assertRaises(ValueError):
            urlify("Mr John Smith    ", "13")

    def test_2(self):
        with self.assertRaises(ValueError):
            urlify("None", "13")

    def test_3(self):
        with self.assertRaises(ValueError):
            urlify("Mr John Smith    ", "None")

    def test_4(self):
        with self.assertRaises(ValueError):
            urlify("None", "None")

    def test_5(self):
        self.assertEqual(urlify("", "13"), "")

    def test_6(self):
        with self.assertRaises(ValueError):
            urlify("Mr John Smith    ", "")

    def test_7(self):
        with self.assertRaises(ValueError):
            urlify("Mr John Smith    ", "-1")

    def test_8(self):
        with self.assertRaises(ValueError):
            urlify("Mr John Smith    ", "3")

    def test_9(self):
        with self.assertRaises(ValueError):
            urlify("Mr John Smith    ", "12")

    def test_10(self):
        with self.assertRaises(ValueError):
            urlify("Mr John Smith    ", "14")


if __name__ == "__main__":
    unittest.main()
