from peewee import *

db = MySQLDatabase("python", user = "root", host ="localhost", passwd="")

class User(Model):
    names = CharField()
    email = CharField(unique=True)
    age = IntegerField()
    class Meta:
        database = db
        db_table = "users"

