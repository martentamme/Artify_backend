from peewee import *

db = MySQLDatabase('artify',
                   host='localhost',
                   port=3306,
                   user='root',
                   password="root")


class BaseModel(Model):
    class Meta:
        database = db
