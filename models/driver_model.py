from peewee import CharField

from models.base_model import BaseModel


class Driver(BaseModel):
    name = CharField()
    car = CharField()

    @staticmethod
    def create_from_json(driver):
        return Driver.create(
            name=driver['name'],
            car=driver['car']
        )
