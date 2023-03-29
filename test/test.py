import unittest

target = __import__("main.py")

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(target.encrypt("abcde", 1), "bcdef")  # add assertion here


if __name__ == '__main__':
    unittest.main()
