from jwt import DecodeError
from sqlalchemy.orm import Session

from utils.contants import ADMIN, SALESMAN, CLIENT, ROUTE_CREATE, ROUTE_DELETE, ROUTE_UPDATE, ROUTE_GET
from utils.token import decode
from app.exceptions import UnauthorizedException, InvalidToken
from app.domain.controllers.users_controller import get_by_id


def check_authorization(db: Session, token: str, **kwargs) -> bool:

    try:
        data = decode(token)

    except DecodeError:
        raise InvalidToken("Token invalido")

    user = get_by_id(db, data.get('id'))

    if user.user_type.type == ADMIN:
        return True

    if kwargs.get('route_type') != ROUTE_DELETE:
        if user.user_type.type == CLIENT:
            if kwargs.get('name') == user.name:
                return True

        elif user.user_type.type == SALESMAN:
            if kwargs.get('route_type') == ROUTE_UPDATE:
                return True

    raise UnauthorizedException(f"{user.user_type.type} não tem autorização para acessar essa rota")
