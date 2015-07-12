# coding: utf-8

import unittest


class SomethingTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual('foobar', 'foobaz')


if __name__ == '__main__':
    unittest.main()
