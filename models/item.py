from db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)  # we don't have id in item but it is good to have as a primary key
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')  # this sees that we have store id and find store in db and matches the store id

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name':self.name, 'price':self.price}

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