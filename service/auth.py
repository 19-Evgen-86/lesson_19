from dao.auth import AuthDao
from except_decorator import handling_exceptions
from utils import  get_hash, create_tokens, decode_token


class AuthService:
    def __init__(self, dao: AuthDao):
        self.dao = dao

    @handling_exceptions
    def login(self, data):
        user = self.dao.get_user(data["username"], get_hash(data['password']))
        if user is not None:
            tokens = create_tokens({
                "username": user.username,
                "role": user.role
            })
            return tokens

        else:
            return {"message": "Неверный имя пользователя или пароль"}

    def get_new_tokens(self, refresh_token: str):

        decoded_token = decode_token(refresh_token, refresh_token=True)

        tokens = create_tokens({
            "username": decoded_token["username"],
            "role": decoded_token["role"]
        })

        return tokens

    def check_username(self, username):
        return self.dao.check_username(username)
