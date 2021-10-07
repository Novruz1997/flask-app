from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList  # SQLAlchemy need to see them to create them automartically
# Because it should see the these tables are exists
from db import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  # database will live at the root folder of our project
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Only False extension behavior not original SQLAlchemy behaviour
app.secret_key = "jose"
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()      # this will create 'sqlite:///data.db' which we see in line 12 unless it already exists


jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')  # http://127.0.0.1:5000/student/Rolf
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':
    db.init_app(app)
    app.run(host='0.0.0.0', port=8000, debug=True)
