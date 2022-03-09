from peewee import CharField, BooleanField

from models.base_model import BaseModel


class Client(BaseModel):
    name = CharField()
    is_vip = BooleanField()

    @staticmethod
    def create_from_json(client):
        return Client.create(
            name=client['name'],
            is_vip=client['is_vip']
        )
