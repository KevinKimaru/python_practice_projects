from peewee import *

db = MySQLDatabase("cars_db",user="root", host="localhost", passwd="")
class Car(Model):
    make = CharField()
    model = CharField()
    color = CharField()
    price = IntegerField()
    class Meta:
        database = db
        db_table = "cars"