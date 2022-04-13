from flask_restx import Namespace, Resource

from implemented import director_service

director_ns = Namespace("directors")


@director_ns.route("/")
class DirectorsView(Resource):
    @director_ns.response(200, description="Возвращает список всех режиссеров")
    def get(self):
        result = director_service.get_director_all()
        return result, 200


@director_ns.route("/<int:uid>")
class DirectorView(Resource):
    @director_ns.param("uid", "ID Режиссера")
    @director_ns.response(200, description="Возвращает данные режиссера по ID")
    def get(self, uid):
        result = director_service.get_director(uid)
        return result, 200
