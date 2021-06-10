from jwt import DecodeError
from sqlalchemy.orm import Session

from utils.contants import ADMIN, SALESMAN, CLIENT, ROUTE_CREATE, ROUTE_DELETE, ROUTE_UPDATE, ROUTE_GET, SALES_VIEW, USERS_VIEW, ORDERS_VIEW, PRODUCTS_VIEW
from utils.token import decode
from app.exceptions import UnauthorizedException, InvalidToken
from app.domain.controllers.users_controller import get_by_id


def check_authorization(db: Session, token: str, **kwargs) -> bool:

    try:
        data = decode(token)

    except DecodeError:
        raise InvalidToken("Token invalido")

    user = get_by_id(db, data.get('id'))

    if ROUTE_CREATE == kwargs.get('route_type'):
        if user.user_type.type == ADMIN:
            return True

        if kwargs.get('view') == PRODUCTS_VIEW or kwargs.get('view') == ORDERS_VIEW:
            if user.user_type.type == SALESMAN:
                return True

    elif ROUTE_GET == kwargs.get('route_type'):
        if user.user_type.type == ADMIN:
            return True

        if kwargs.get('view') == PRODUCTS_VIEW or kwargs.get('view') == ORDERS_VIEW or kwargs.get('view') == USERS_VIEW:
            if user.user_type.type == SALESMAN:
                return True

            if user.user_type.type == CLIENT:
                if user.name == kwargs.get('name'):
                    return True

    elif ROUTE_UPDATE == kwargs.get('route_type'):
        if user.user_type.type == ADMIN:
            return True

        if kwargs.get('view') == PRODUCTS_VIEW or kwargs.get('view') == ORDERS_VIEW:
            if user.user_type.type == SALESMAN:
                return True

    elif ROUTE_DELETE == kwargs.get('route_type'):
        if user.user_type.type == ADMIN:
            return True

        if kwargs.get('view') == PRODUCTS_VIEW:
            if user.user_type.type == SALESMAN:
                return True

    raise UnauthorizedException(f"{user.user_type.type} não tem autorização para acessar essa rota")
