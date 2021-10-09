import os
import re
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList  # SQLAlchemy need to see them to create them automartically
# Because it should see the these tables are exists


app = Flask(__name__)
# keep sqlite too if we want to test app locally if database url is not defined


uri = os.getenv("DATABASE_URL")  # or other relevant config var
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
# rest of connection code using the connection string `uri`
if uri:
    app.config['SQLALCHEMY_DATABASE_URI'] = uri
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://data.db'


# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Only False extension behavior not original SQLAlchemy behaviour
app.secret_key = "jose"
api = Api(app)


jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(ItemList, '/item/<string:name>')  # http://127.0.0.1:5000/student/Rolf
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(StoreList, '/stores')

# if __name__ == '__main__':
#     from db import db
#     db.init_app(app)
#     app.run(host='0.0.0.0', port=8000, debug=True)
