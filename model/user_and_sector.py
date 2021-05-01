from peewee import *
from connection import db_connection


class UserAndSector(db_connection.BaseModel):
    user_id = ForeignKeyField('self', null=True)
    sector_id = ForeignKeyField('self', null=True)

    class Meta:
        db_table = 'user_and_sector'


if __name__ == '__main__':
    UserAndSector.create_table()
