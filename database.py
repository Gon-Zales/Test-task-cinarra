from peewee import SqliteDatabase

from settings import DATABASE

# use an in-memory SQLite for tests.
#database = SqliteDatabase(':memory:')
database = SqliteDatabase(DATABASE)
