from flask import Flask, g

from blueprints.driver import driver_api
from blueprints.client import client_api
from database import database
from models.client_model import Client
from models.driver_model import Driver
from models.order_model import Order

database.create_tables([Driver, Client, Order])

app = Flask(__name__)


# @app.before_request
# def get_db():
#     if 'db' not in g:
#         g.db = database
#         g.db.connect()


@app.teardown_appcontext
def teardown_db(exception):
    db = g.pop('db', None)

    if db is not None:
        db.close()


app.register_blueprint(driver_api)
app.register_blueprint(client_api)
# print(app.url_map)

if __name__ == '__main__':
    app.run()
