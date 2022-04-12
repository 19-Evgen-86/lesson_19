from dao.model.movies import Movie
from dao.movie import MovieDao


class MovieService:

    def __init__(self, movie_dao: MovieDao):
        self.movie_dao = movie_dao

    def get_movie(self, mid):
        return self.movie_dao.get_one_movie(mid)

    def get_movies(self, param: dict):

        if param:
            filters = {}
            for arg in param:
                filters[arg] = param[arg]

            return self.movie_dao.get_movie_filter(filters)
        else:
            return self.movie_dao.get_all_movies()

    def add_movie(self, data):
        movie = Movie(**data)
        self.movie_dao.create(movie)

    def update_movie(self, data, mid):
        self.movie_dao.update(data, mid)

    def delete_movie(self, mid):
        self.movie_dao.delete(mid)
