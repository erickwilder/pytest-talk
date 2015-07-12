# coding: utf-8

from example.models import Address, Place
import pytest


@pytest.fixture
def address():
    return Address('Av. Paulista', 'São Paulo', 'SP', 'Brazil')


@pytest.fixture
def place(address):
    return Place(name='MASP', address=address)


def test_place_street(place):
    assert place.address.street == 'Av. Paulista'
