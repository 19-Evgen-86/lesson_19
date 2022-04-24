from dao.model.user import UserSchema, User
from dao.user import UserDao
from except_decorator import handling_exceptions
from utils import get_hash


class UserService:

    def __init__(self, dao: UserDao):
        self.dao = dao

    @handling_exceptions
    def get(self):
        result = self.dao.get_all()
        return UserSchema(many=True).dump(result)

    @handling_exceptions
    def create(self, data):
        valid_user = UserSchema().load(data=data)
        valid_user["password"] = get_hash(valid_user["password"])
        user = User(**valid_user)

        self.dao.create(user)

    @handling_exceptions
    def update(self, data, uid):
        valid_user = UserSchema().load(data)
        if valid_user.get("password", False):
            valid_user["password"] = get_hash(valid_user["password"])
        self.dao.update(data, uid)
