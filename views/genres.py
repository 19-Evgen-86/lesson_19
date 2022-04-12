from flask import request
from flask_restx import Namespace, Resource

genre_ns = Namespace("genres")


@genre_ns.route("/")

class GenresView(Resource):
    @genre_ns.param("uid", "ID Жанра")
    @genre_ns.response(200, description="Возвращает данные жанра по ID, либо список всех жанров")
    @genre_ns.response(404, description="Жанр не найден")
    def get(self):
        uid = request.args.get("uid")
        if uid:
            return uid
        else:
            return "all"
