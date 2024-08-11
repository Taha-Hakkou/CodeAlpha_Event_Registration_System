#!/usr/bin/env python3
"""DB Module
"""
from pymongo import MongoClient
from bson import ObjectId
from models.event import Event
from models.registration import Registration


class DB():
    """MongoDB class
    """

    def __init__(self):
        """Instantiates
        """
        self.__client = MongoClient('localhost', 27017)
        self.db = self.__client.event_registration_system_db

    def create_event(self, event: Event) -> None:
        """Inserts a new Event instance in database
        """
        self.db.events.insert_one(event.to_json())
        return event

    def create_registration(self, reg: Registration) -> None:
        """Inserts a new Registration instance in database
        """
        self.db.registrations.insert_one(reg.to_json())
        return reg

    def get_events(self, page):
        """Returns list of all events
        """
        events = self.db.events.aggregate([
            {'$skip': page * 8},
            {'$limit': 8}
        ])
        return events

    def get_event(self, id: str):
        """Returns an event corresponding to ID
        """
        event = self.db.events.find_one({'_id': ObjectId(id)})
        return event

    def get_registrations(self, page):
        """Returns list of all registered events
        """
        registrations = self.db.registrations.aggregate([
            {'$skip': page * 8},
            {'$limit': 8}
        ])
        if registrations != []:
            ids = [r.get('event_id') for r in registrations]
            registered_events = [self.get_event(id) for id in ids]
        else:
            registered_events = []
        return registered_events

    def get_registration(self, event_id: str):
        """"""
        return self.db.registrations.find_one({'event_id': ObjectId(event_id)})


if __name__ == '__main__':
    db = DB()
    events_data = [
        ["Community Picnic", "Green Park Association", "Green Park", "12:00 PM", 20, "Join us for a fun-filled day with food, games, and activities for the whole family!"],
        ["Tech Talk: AI in Action", "Silicon Valley Insiders", "Tech Hub Auditorium", "7:00 PM", 0, "Learn about the latest advancements in Artificial Intelligence from industry experts."],
        ["Movie Night Under the Stars", "Stargazers Club", "Galaxy Park Observatory", "8:30 PM", 15, "Enjoy a classic movie under the night sky with breathtaking views of the stars."],
        ["Yoga in the Park", "Wellness Collective", "Central Park Meadow", "10:00 AM", 10, "Start your day with a relaxing yoga session in the beautiful park setting."],
        ["Book Club Meeting", "Lit Lovers Society", "Cozy Bookstore Cafe", "6:30 PM", 0, "Discuss your favorite book with fellow bookworms over coffee and treats."],
        ["event1", "org1", "place1", "time1", 1, "desc1"],
        ["event2", "org2", "place2", "time2", 2, "desc2"],
        ["event3", "org3", "place3", "time3", 3, "desc3"],
        ["event4", "org4", "place4", "time4", 4, "desc4"]
]
    for event_data in events_data:
        event = Event(*event_data)
        db.create_event(event)
