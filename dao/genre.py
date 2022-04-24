from dao.model.genres import Genre


class GenreDao():
    """
     Класс для взаимодействия c таблицей жанров в БД
     """

    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Genre).all()

    def get_one(self, mid):
        return self.session.query(Genre).get(mid)

    def create(self, data):
        with self.session.begin():
            self.session.add(data)

    def update(self, data, mid):
        with self.session.begin():
            self.session.query(Genre).filter(Genre.id == mid).update(data)

    def delete(self, mid):
        with self.session.begin():
            self.session.query(Genre).filter(Genre.id == mid).delete()
