#!/usr/bin/env python3
"""Event Module
"""


class Event:
    """Event Model
    """

    def __init__(self, name: str, organizator: str, location: str, time, price: int, description: str):
        """Instantiates a new event instance
        """
        self.name = name
        self.organizator = organizator
        self.location = location
        self.time = time # datetime
        self.ticket_price = price
        self.description = description

    def to_json(self):
        """"""
        return {
            'name': self.name,
            'organizator': self.organizator,
            'location': self.location,
            'time': self.time,
            'ticket_price': self.ticket_price,
            'description': self.description
        }
