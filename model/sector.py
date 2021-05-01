import csv

from peewee import *
from connection import db_connection


class Sector(db_connection.BaseModel):
    sector_id = IntegerField(primary_key=True, unique=True, constraints=[SQL('AUTO_INCREMENT')])
    name = CharField()
    root_sector_id = ForeignKeyField('self', null=True)

    class Meta:
        db_table = 'sector'


if __name__ == '__main__':
    Sector.create_table()
    with open("../sectors_data.csv", encoding="utf-8") as f:
        rd = csv.reader(f)
        for sector_id, name, root_id in rd:
            if root_id != "null":
                s = Sector.create(name=name, root_sector_id=root_id)
            else:
                s = Sector.create(name=name)
            s.save()
