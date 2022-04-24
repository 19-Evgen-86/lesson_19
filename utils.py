import base64
import hashlib
from datetime import datetime, timedelta
from functools import wraps

import jwt
from flask import request
from flask_restx import abort

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS, PWD_HASH_NAME, SECRET_KEY, ALGO
from implemented import auth_service


def get_hash(password):
    """
    саздает Хэш пароля
    :param password:
    :return:
    """
    hash: bytes = hashlib.pbkdf2_hmac(
        PWD_HASH_NAME,
        password.encode('utf-8'),  # Convert the password to bytes
        PWD_HASH_SALT,
        PWD_HASH_ITERATIONS
    )

    return base64.b64encode(hash).decode("utf-8")


def create_tokens(data: dict) -> dict:
    """
    создает токен для пользователя data['username']
    :param data:
    :return:
    """
    data["exp"] = datetime.utcnow() + timedelta(minutes=30)
    data["refresh_token"] = False
    access_token: str = jwt.encode(data, SECRET_KEY, algorithm=ALGO)

    data["exp"] = datetime.utcnow() + timedelta(days=30)
    data["refresh_token"] = True
    refresh_token: str = jwt.encode(data, SECRET_KEY, algorithm=ALGO)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }


def get_token_from_headers(headers: dict):
    """
    получаем токен из заголовка
    :param headers:
    :return:
    """
    if "Authorization" not in headers:
        abort(401, message="Неправильный заголовок")
    return headers['Authorization'].split(' ')[-1]


def decode_token(token: str, refresh_token: bool = False):
    """
    декодирует токен
    :param token:
    :param refresh_token:
    :return:
    """
    decoded_token: dict = {}
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, ALGO)
    except jwt.PyJWTError as exc:
        abort(401)
    if decoded_token["refresh_token"] != refresh_token:
        abort(401)

    return decoded_token


def auth_required(func):
    """
    проверяем авторизован ли пользователя
    :param func:
    :return:
    """

    def inner(*args, **kwargs):
        token = get_token_from_headers(request.headers)
        decoded_token = decode_token(token)

        if not auth_service.check_username(decoded_token["username"]):
            abort(401, message="Необходима авторизация")

        return func(*args, **kwargs)

    return inner


def auth_admin_required(func):
    def inner(*args, **kwargs):
        token = get_token_from_headers(request.headers)
        decoded_token = decode_token(token)

        if decoded_token['role'] != 'admin':
            abort(403, message="Только для аdmin`ов")

        if not auth_service.check_username(decoded_token["username"]):
            abort(401, message="Необходима авторизация")

        return func(*args, **kwargs)

    return inner
