# coding: utf-8

from example.models import Address, Place
import pytest


@pytest.fixture(params=['Brazil', 'Germany'])
def country(request):
    return request.param


@pytest.fixture
def address(country):
    return Address('Av. Paulista', 'São Paulo', 'SP', country)


@pytest.fixture
def place(address):
    return Place(name='MASP', address=address)


def test_place_country(place):
    assert place.address.country != 'United States'
