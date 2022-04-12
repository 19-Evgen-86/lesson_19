from flask import request
from flask_restx import Namespace, Resource

from dao.model.movies import MovieSchema
from implemented import movie_service

movie_ns = Namespace("movies")
movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()


@movie_ns.route("/")
class MoviesView(Resource):
    @movie_ns.doc(params={"director_id": "ID Режиссера", "genre_id": "ID :Жанра"})
    @movie_ns.response(200, description="Возвращает список фильмов")
    @movie_ns.response(404, description="Фильм не найден")
    def get(self):
        result = movie_service.get_movies(request.args)
        return movies_schema.dump(result), 200

    @movie_ns.response(200, description="Фильм добавлен")
    def post(self):
        data = movie_schema.load(request.json)
        movie_service.add_movie(data)
        return {}, 200


@movie_ns.route("/<int:uid>")
class MovieView(Resource):
    @movie_ns.doc(params={"uid": "ID Фильма"})
    @movie_ns.response(200, description="Возвращает фильм по ID")
    def get(self, uid):
        result = movie_service.get_movie(uid)
        return movie_schema.dump(result), 200

    @movie_ns.doc(params={"uid": "ID Фильма", "data": "Данные для обновления"})
    @movie_ns.response(201, description="Фильм обновлен")
    @movie_ns.response(404, description="Фильм не найден")
    def put(self, uid):
        data = movie_schema.load(request.json)
        movie_service.update_movie(data, uid)
        return {}, 201

    @movie_ns.param("uid", "ID Фильма")
    @movie_ns.response(204, description="Фильм удален")
    def delete(self, uid):
        movie_service.delete_movie(uid)
        return {}, 204
