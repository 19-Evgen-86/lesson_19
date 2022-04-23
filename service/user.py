
from dao.model.user import UserSchema, User
from dao.user import UserDao




class UserService:

    def __init__(self, dao: UserDao):
        self.dao = dao

    def get(self):
        result = self.dao.get_all()
        return UserSchema(many=True).dump(result)

    def create(self, data):
        user = UserSchema.dump(User(**data))
        self.dao.create(user)


    def update(self, data, uid):
        self.dao.update(data, uid)
