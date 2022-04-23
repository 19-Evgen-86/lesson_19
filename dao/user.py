from flask_sqlalchemy import SQLAlchemy

from dao.model.user import User


class UserDao:
    def __init__(self, session: SQLAlchemy):
        self.session = session

    def create(self, data: User):
        with self.session.begin():
            self.session.add(data)

    def update(self, data: dict, uid: int):
        with self.session.begin():
            self.session.query(User).filter(User.id == uid).update(data)

    def get_all(self):
        return self.session.query(User).all()
