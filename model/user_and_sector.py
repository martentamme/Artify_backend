from peewee import *
from connection import db_connection
from model.sector import Sector
from model.user import User


class UserAndSector(db_connection.BaseModel):
    user_sector_id = IntegerField(primary_key=True, unique=True, constraints=[SQL('AUTO_INCREMENT')])
    user_id = ForeignKeyField(User)
    sector_id = ForeignKeyField(Sector)

    class Meta:
        db_table = 'user_and_sector'


if __name__ == '__main__':
    UserAndSector.create_table()
