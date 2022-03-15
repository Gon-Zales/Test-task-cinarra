import werkzeug
from flask import Flask, g

from blueprints.driver import driver_api
from blueprints.client import client_api
from blueprints.order import order_api
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


@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    print(e)
    return 'bad request!', 400


app.register_blueprint(driver_api, url_prefix='/api/v1/drivers')
app.register_blueprint(client_api, url_prefix='/api/v1/clients')
app.register_blueprint(order_api, url_prefix='/api/v1/orders')

if __name__ == '__main__':
    app.run(debug=True)
