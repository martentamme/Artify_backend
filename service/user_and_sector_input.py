from model.user_and_sector import UserAndSector


class UserAndSectorInput:
    def __init__(self, user_id, list_of_sectors_id):
        self.user_id = user_id
        self.list_of_sectors_id = list_of_sectors_id

    def addUserAndSectorToDB(self):
        for sector_id in self.list_of_sectors_id:
            user_and_sector = UserAndSector.create(user_id=self.user_id, sector_id=sector_id)
            user_and_sector.save()

    def updateSectorChoices(self):
        self.deleteRecordsFromDB()
        self.addUserAndSectorToDB()

    def deleteRecordsFromDB(self):
        query = UserAndSector.delete().where(UserAndSector.user_id == self.user_id)
        query.execute()
