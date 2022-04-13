from dao.model.directors import Director


class DirectorDao():
    """
    Класс для взаимодействия c таблицей режиссеров в БД
    """

    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Director).all()

    def get_one(self, mid):
        return self.session.query(Director).get(mid)
