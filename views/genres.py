from flask import request
from flask_restx import Namespace, Resource

from implemented import genre_service
from utils import auth_required

genre_ns = Namespace("genres")


@genre_ns.route("/")
class GenresView(Resource):
    @genre_ns.response(200, description="Возвращает список всех жанров")
    @auth_required
    def get(self):
        result = genre_service.get_genres_all()
        return result, 200

    @genre_ns.response(200, description="Фильм добавлен")
    def post(self):
        data = request.json
        result = genre_service.add_genre(data)
        return result, 200


@genre_ns.route("/<int:uid>")
class GenresView(Resource):
    @genre_ns.param("uid", "ID Жанра")
    @genre_ns.response(200, description="Возвращает данные жанра по ID")
    @auth_required
    def get(self, uid):
        result = genre_service.get_genre(uid)
        return result, 200

    @genre_ns.doc(params={"uid": "ID Жанра", "data": "Данные для обновления"})
    @genre_ns.response(201, description="Жанр обновлен")
    def put(self, uid):
        data = request.json
        result = genre_service.update_genre(data, uid)
        return result, 201

    @genre_ns.param("gid", "ID Жанра")
    @genre_ns.response(204, description="Жанр удален")
    def delete(self, gid):
        result = genre_service.delete_genre(gid)
        return result, 204
