from dao.model.movies import Movie, MovieSchema
from dao.movie import MovieDao
from except_decorator import handling_exceptions

movie_schemas = MovieSchema(many=True)
movie_schema = MovieSchema()


class MovieService:

    def __init__(self, movie_dao: MovieDao):
        self.movie_dao = movie_dao

    @handling_exceptions
    def get_movie_one(self, mid):
        result = self.movie_dao.get_one_movie(mid)
        if result is None:
            return {"message": f"Movie with ID: '{mid}' not found"}
        else:
            return movie_schema.dump(result)

    @handling_exceptions
    def get_movie_all(self, params: dict):
        if params:
            filters = {}
            for arg in params:
                filters[arg] = params[arg]
            result = self.movie_dao.get_movie_filter(filters)
        else:
            result = self.movie_dao.get_all_movies()

        if result:
            return movie_schemas.dump(result)
        else:
            return {"message": "Movies into database not found"}

    @handling_exceptions
    def add_movie(self, data):
        movie_dict = movie_schema.load(data)
        movie = Movie(**movie_dict)
        self.movie_dao.create(movie)

        return {"message": f"Movie {Movie.title} added into database"}

    @handling_exceptions
    def update_movie(self, data, mid):

        movie_dict = movie_schema.load(data)
        self.movie_dao.update(movie_dict, mid)
        return {"message": f"Movie with ID: '{mid}' is updated"}

    @handling_exceptions
    def delete_movie(self, mid):
        self.movie_dao.delete(mid)
        return {"message": f"Movie with ID: '{mid}' is deleted"}
