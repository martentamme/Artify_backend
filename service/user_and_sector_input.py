from model.user_and_sector import UserAndSector


class UserAndSectorInput:
    def __init__(self, user_id, sector_id):
        self.user_id = user_id
        self.sector_id = sector_id

    def addUserAndSectorToDB(self):
        user_and_sector = UserAndSector.create(user_id=self.user_id, sector_id=self.sector_id)
        user_and_sector.save()
        return user_and_sector.user_id
