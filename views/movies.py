from flask import request
from flask_restx import Namespace, Resource

from implemented import movie_service
from utils import auth_required

movie_ns = Namespace("movies")


@movie_ns.route("/")
class MoviesView(Resource):
    @movie_ns.doc(params={"director_id": "ID Режиссера", "genre_id": "ID :Жанра"})
    @movie_ns.response(200, description="Возвращает список фильмов")
    @auth_required
    def get(self):
        result = movie_service.get_movie_all(request.args)
        return result, 200

    @movie_ns.response(200, description="Фильм добавлен")
    def post(self):
        data = request.json
        result = movie_service.add_movie(data)
        return result, 200


@movie_ns.route("/<int:uid>")
class MovieView(Resource):
    @movie_ns.doc(params={"uid": "ID Фильма"})
    @movie_ns.response(200, description="Возвращает фильм по ID")
    @auth_required
    def get(self, uid):
        result = movie_service.get_movie_one(uid)
        return result, 200

    @movie_ns.doc(params={"uid": "ID Фильма", "data": "Данные для обновления"})
    @movie_ns.response(201, description="Фильм обновлен")
    def put(self, uid):
        data = request.json
        result = movie_service.update_movie(data, uid)
        return result, 201

    @movie_ns.param("uid", "ID Фильма")
    @movie_ns.response(204, description="Фильм удален")
    def delete(self, uid):
        result = movie_service.delete_movie(uid)
        return result, 204
