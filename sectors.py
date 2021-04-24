from peewee import *
from connection import db_connection


class Sector(db_connection.BaseModel):
    name = CharField()
    root_sector_id = IntegerField()

    class Meta:
        db_table = 'sector'


class Sectors:
    def __init__(self):
        self.sectors_data = {}

    def get_sectors(self):
        for sector in Sector.select():
            self.sectors_data[sector.id] = {}
            self.sectors_data[sector.id]["name"] = sector.name
            self.sectors_data[sector.id]["root_sector_id"] = sector.root_sector_id
        return self.sectors_data


if __name__ == '__main__':
    # Sector.insert(name="test").execute()
    # Sector.delete().where(Sector.id == 3).execute()
    x = Sectors()
    print(x.get_sectors())
