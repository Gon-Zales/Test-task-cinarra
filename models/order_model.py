from datetime import datetime

from peewee import CharField, ForeignKeyField, TimestampField

from models.base_model import BaseModel
from models.client_model import Client
from models.driver_model import Driver

NOT_ACCEPTED = "not_accepted"
IN_PROGRESS = "in_progress"
DONE = "done"
CANCELLED = "cancelled"
ORDER_STATUS = ("not_accepted", "in_progress", "done", "cancelled")
STATUS_CHANGE = [
    (NOT_ACCEPTED, NOT_ACCEPTED, True),
    (NOT_ACCEPTED, IN_PROGRESS, True),
    (NOT_ACCEPTED, CANCELLED, True),
    (NOT_ACCEPTED, DONE, False),
    (IN_PROGRESS, NOT_ACCEPTED, False),
    (IN_PROGRESS, IN_PROGRESS, True),
    (IN_PROGRESS, CANCELLED, True),
    (IN_PROGRESS, DONE, True),
    (CANCELLED, NOT_ACCEPTED, False),
    (CANCELLED, IN_PROGRESS, False),
    (CANCELLED, CANCELLED, True),
    (CANCELLED, DONE, False),
    (DONE, NOT_ACCEPTED, False),
    (DONE, IN_PROGRESS, False),
    (DONE, CANCELLED, False),
    (DONE, DONE, True)
]


class Order(BaseModel):
    address_from = CharField()
    address_to = CharField()
    client_id = ForeignKeyField(Client, backref='orders')
    driver_id = ForeignKeyField(Driver, backref='orders')
    date_created = TimestampField()
    status = CharField()  # TODO create custom field

    @staticmethod
    def create_from_json(order):
        return Order.create(
            address_from=order['address_from'],
            address_to=order['address_to'],
            client_id=order['client_id'],
            driver_id=order['driver_id'],
            date_created=datetime.strptime(order['date_created'], '%Y-%m-%d %H:%M:%S'),
            status=order['status']
        )
