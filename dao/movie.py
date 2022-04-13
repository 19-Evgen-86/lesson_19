from dao.model.movies import Movie


class MovieDao():
    """
     Класс для взаимодействия c таблицей фильмов в БД
     """
    def __init__(self, session):
        self.session = session

    def get_all_movies(self):
        return self.session.query(Movie).all()

    def get_one_movie(self, mid):
        return self.session.query(Movie).get(mid)

    def get_movie_filter(self, filter: dict):
        return self.session.query(Movie).filter_by(**filter).all()

    def create(self, data):
        with self.session.begin():
            self.session.add(data)

    def update(self, data, mid):
        with self.session.begin():
            self.session.query(Movie).filter(Movie.id == mid).update(data)

    def delete(self, mid):
        with self.session.begin():
            self.session.query(Movie).filter(Movie.id == mid).delete()
