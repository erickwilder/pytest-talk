# coding: utf-8


class Address(object):
    def __init__(self, street, city, state, country):
        self.street = street
        self.city = city
        self.stete = state
        self.country = country


class Place(object):
    def __init__(self, name, address):
        self.name = name
        self.address = address
