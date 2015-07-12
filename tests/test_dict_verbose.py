# coding: utf-8
import unittest


class SomeThingTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual({'a': 0, 'b': 1, 'c': 2},
                         {'a': 0, 'b': 2, 'd': 0})


if __name__ == '__main__':
    unittest.main()
