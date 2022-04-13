from flask_restx import Namespace, Resource

from implemented import genre_service

genre_ns = Namespace("genres")


@genre_ns.route("/")
class GenresView(Resource):
    @genre_ns.response(200, description="Возвращает список всех жанров")
    def get(self):
        result = genre_service.get_genres_all()
        return result, 200

    @genre_ns.route("/<int:uid>")
    class GenresView(Resource):
        @genre_ns.param("uid", "ID Жанра")
        @genre_ns.response(200, description="Возвращает данные жанра по ID")
        def get(self, uid):
            result = genre_service.get_genre(uid)
            return result, 200
