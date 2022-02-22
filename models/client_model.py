from peewee import CharField, BooleanField

from models.base_model import BaseModel


class Client(BaseModel):
    name = CharField()
    is_vip = BooleanField()
