from functools import wraps


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