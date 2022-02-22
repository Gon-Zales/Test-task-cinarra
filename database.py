from peewee import SqliteDatabase

from settings import DATABASE

database = SqliteDatabase(DATABASE)
