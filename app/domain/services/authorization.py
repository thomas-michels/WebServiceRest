from typing import List
from utils.token import decode
from app.exceptions import UnauthorizedException


def check_authorization(token: str, access_required: List[str]) -> bool:
    data = decode(token)
    user_type = data.get('user_type')['type']
    for type_access in access_required:
        if type_access == user_type:
            return True

    raise UnauthorizedException(f"{user_type} não tem autorização para acessar essa rota")
