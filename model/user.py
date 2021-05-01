from peewee import *
from connection import db_connection


class User(db_connection.BaseModel):
    user_id = IntegerField(primary_key=True, unique=True, constraints=[SQL('AUTO_INCREMENT')])
    name = CharField()
    agreement = BooleanField()

    class Meta:
        db_table = 'user'


if __name__ == '__main__':
    User.create_table()
