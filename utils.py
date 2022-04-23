import hashlib
from functools import wraps

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS

def handling_exceptions(func):
    """
    отлавливает возможные ошибки
    используется в качестве декоратора
    :param func:
    :return:
    """

    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as ex:
            return {"error ": ex.__repr__()}, 404

    return inner


def get_hash(password):
    return hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),  # Convert the password to bytes
        PWD_HASH_SALT,
        PWD_HASH_ITERATIONS
    ).decode("utf-8", "ignore")
