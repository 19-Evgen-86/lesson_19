from dao.model.user import User


class AuthDao:
    def __init__(self, session):
        self.session = session

    def get_user(self, username, password):
        return self.session.query(User).filter(User.username == username, User.password == password).first()

    def check_username(self, username):
        return self.session.query(User.username).filter(User.username == username).first()
