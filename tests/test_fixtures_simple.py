# coding: utf-8

from example.models import Address
import pytest


@pytest.fixture
def address():
    return Address('Av. Paulista', 'São Paulo', 'SP', 'Brazil')


def test_address(address):
    assert address.country == 'Brazil'
