from peewee import CharField, BooleanField, TimestampField, ForeignKeyField

from models.base_model import BaseModel
from models.client_model import Client
from models.driver_model import Driver


class Order(BaseModel):
    address_from = CharField()
    address_to = CharField()
    client_id = ForeignKeyField(Client, backref='orders')
    driver_id = ForeignKeyField(Driver, backref='orders')
    date_created = TimestampField()
    status = CharField()
