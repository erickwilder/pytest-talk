# coding: utf-8


class Address(object):

    def __init__(self, street, city, state, country):
        self.street = street
        self.city = city
        self.state = state
        self.country = country

    def where(self):
        return 'Street: {}, City: {}, State: {}, Country: {}'.format(
            self.street, self.city, self.state, self.country)


class Place(object):

    def __init__(self, name, address):
        self.name = name
        self.address = address
