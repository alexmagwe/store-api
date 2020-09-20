from . import db
import csv

class Products(db.Model):
    __tablename__='products'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(100),nullable=False)
    price=db.Column(db.String(10),nullable=False)
    def __repr__(self):
        return [f'name:{self.name},price:{self.email}']
    def getQuantity(self):
        total=len(Products.query.filter_by(name=self.name).all())
        return total
    def generatefake(count=100):
        with open('MOCK_DATA.csv') as file:
            reader=csv.DictReader(file)
            for line in reader[:count]:
                p=Products(name=line['name'],price=line['price'])
                db.session.add(p)
                try:
                    db.session.commit()
                except:
                    db.session.rollback()   