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
    (NOT_ACCEPTED, IN_PROGRESS),
    (NOT_ACCEPTED, CANCELLED),
    (IN_PROGRESS, CANCELLED),
    (IN_PROGRESS, DONE),
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
            date_created=datetime.fromisoformat(order['date_created']),
            status=order['status']
        )
