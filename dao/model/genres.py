from marshmallow import Schema, fields

from setup_db import db


class Genre(db.Model):
    """
    Описывает модель таблицы жанров
   """

    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class GenreSchema(Schema):
    """
   Схема для сериализация
   """

    id = fields.Int(dump_only=True)
    name = fields.Str()
