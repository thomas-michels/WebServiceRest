
from utils.token import decode


def check_authorization(token: str):
    data = decode(token)
    print(data.get('id'))
