# coding: utf-8

import unittest
import pytest


@pytest.fixture
def foobar(request):
    if request.cls:
        request.cls.foo = 'bar'


@pytest.fixture
def barbaz():
    return 'foo'


@pytest.mark.usefixtures('foobar')
class ClassicWithFixtureTestCase(unittest.TestCase):

    def test_something(self, barbaz):
        assert self.foo == 'baz'
        assert barbaz == 'lorem ipsum'
