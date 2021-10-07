from db import db


class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)  # we don't have id in item but it is good to have as a primary key
    name = db.Column(db.String(80))

    # Back-referencing
    items = db.relationship('ItemModel', lazy='dynamic')  # this says we have a relationship with item model

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()  # Select * from items where name=name LIMIT 1  --> this
        # returns first row only  --> this will also return item object such as self.name, self.price
        # this functionality comes from cls which is db.Model comes from SQLAlchemy

    def save_to_db(self):
        """
        This function will replace `insert` and `update`. It will both insert or update to db
        SqlAlchemy can directly translate from object to row for a database
        """
        db.session.add(self)  # session is collection of objects that we are going to write into database
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()