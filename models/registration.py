#!/usr/bin/env python3
"""Registration Module
"""


class Registration:
    """Registration Model
    """

    def __init__(self, event_id: str, quantity: int, email: str, phone: str):
        """Instantiates a new registration instance
        """
        self.event_id = event_id
        self.quantity = quantity
        self.email = email
        self.phone = phone

    def to_json(self):
        """"""
        return {
            'event_id': self.event_id,
            'quantity': self.quantity,
            'email': self.email,
            'phone': self.phone
        }
