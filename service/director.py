from dao.director import DirectorDao
from dao.model.directors import DirectorSchema, Director
from except_decorator import handling_exceptions

director_schemas = DirectorSchema(many=True)
director_schema = DirectorSchema()


class DirectorService:
    def __init__(self, director_dao: DirectorDao):
        self.director_dao = director_dao

    @handling_exceptions
    def get_director_all(self):
        result = self.director_dao.get_all()
        if result:
            return director_schemas.dump(result)
        else:
            return {"message": "Genres into database not found"}

    @handling_exceptions
    def get_director(self, did):
        result = self.director_dao.get_one(did)
        if result:
            return director_schema.dump(result)
        else:
            return {"message": f"Genre with ID: '{did}' not found"}

    @handling_exceptions
    def add_director(self, data):
        director_dict = director_schema.load(data)
        director = Director(**director_dict)
        self.director_dao.create(director)

        return {"message": f"director {Director.name} added into database"}

    @handling_exceptions
    def update_movie(self, data, did):

        director_dict = director_schema.load(data)
        self.director_dao.update(director_dict, did)
        return {"message": f"Director with ID: '{did}' is updated"}

    @handling_exceptions
    def delete_movie(self, did):
        self.director_dao.delete(did)
        return {"message": f"Director with ID: '{did}' is deleted"}
