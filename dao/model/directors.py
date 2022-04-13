from marshmallow import fields, Schema

from setup_db import db


class Director(db.Model):
    """
     Описывает модель таблицы режиссеров
    """
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class DirectorSchema(Schema):
    """
    Схема для сериализация
    """
    id = fields.Int(dump_only=True)
    name = fields.Str()
