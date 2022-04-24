from dao.genre import GenreDao
from dao.model.genres import GenreSchema, Genre
from except_decorator import handling_exceptions

genre_schemas = GenreSchema(many=True)
genre_schema = GenreSchema()


class GenreService:
    def __init__(self, genre_dao: GenreDao):
        self.genre_dao = genre_dao

    @handling_exceptions
    def get_genres_all(self):
        result = self.genre_dao.get_all()
        if result:
            return genre_schemas.dump(result)
        else:
            return {"message": "Genres into database not found"}

    @handling_exceptions
    def get_genre(self, gid):
        result = self.genre_dao.get_one(gid)
        if result:
            return genre_schema.dump(result)
        else:
            return {"message": f"Genre with ID: '{gid}' not found"}

    @handling_exceptions
    def add_genre(self, data):
        genre_dict = genre_schema.load(data)
        genre = Genre(**genre_dict)
        self.genre_dao.create(genre)

        return {"message": f"Genre {Genre.title} added into database"}

    @handling_exceptions
    def update_genre(self, data, gid):

        genre_dict = genre_schema.load(data)
        self.genre_dao.update(genre_dict, gid)
        return {"message": f"Genre with ID: '{gid}' is updated"}

    @handling_exceptions
    def delete_genre(self, gid):
        self.genre_dao.delete(gid)
        return {"message": f"Genre with ID: '{gid}' is deleted"}
