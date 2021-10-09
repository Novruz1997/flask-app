from app2 import app
from db import db

db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()      # this will create 'sqlite:///data.db' which we see in line 12 unless it already exists
