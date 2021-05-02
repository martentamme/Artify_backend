from model.user import User


class UserService:
    def __init__(self, name, agreement):
        self.name = name
        self.agreement = agreement

    def addUserToDB(self):
        u = User.create(name=self.name, agreement=self.agreement)
        u.save()
        return u.user_id
