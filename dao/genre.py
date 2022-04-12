from dao.model.genres import Genre


class GenreDao():
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Genre).all()

    def get_one(self, mid):
        return self.session.query(Genre).get(mid)
