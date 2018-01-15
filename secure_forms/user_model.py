from peewee import *
from datetime import datetime

db = SqliteDatabase("C:\\Users\Kevin Kimaru Chege\\Desktop\\db\\my_database3.db")

class User(Model):
    names = CharField()
    email = CharField(unique=True)
    age = IntegerField()
    password = CharField()
    class Meta:
        database = db


class Product(Model):
    names = CharField()
    quantity = IntegerField()
    price = IntegerField()
    owner = IntegerField()
    date_added = DateField(default=datetime.now())
    class Meta:
        database = db

#User.create_table()
#User.create(names="Kev Robert", email="kev@gmail.com", age=18, password="qwerty")
# person = User.get(User.id == 1)
# print(person.names)

# Product.drop_table()
# Product.create_table()
# Product.create(names="Books", quantity=122, price=70, owner=1 )