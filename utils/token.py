
import jwt


def encode(data: dict):
    return jwt.encode(data, key='', algorithm='HS256')


def decode(token: str):
    return jwt.decode(token, key='', algorithms='HS256')
