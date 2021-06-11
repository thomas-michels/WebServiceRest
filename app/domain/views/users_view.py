
from fastapi import APIRouter, Depends, Security
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import IntegrityError

from app.domain.schemas.users_schemas import User
from app.domain.controllers.types_controller import create_all_types
from typing import List
from sqlalchemy.orm import Session
from app.domain.services.security import OAUTH2
from database import get_db
from app.domain.services import authorization
from app.exceptions import UnprocessableEntityException
from utils.contants import ROUTE_UPDATE, ROUTE_DELETE, ROUTE_CREATE, ROUTE_GET, USERS_VIEW
from app.domain.controllers.users_controller import get as user_get, \
    create as user_create, \
    get_by_id as user_get_by_id, \
    update as user_update, \
    delete as user_delete, \
    get_by_email as user_get_email, \
    get_by_name as user_get_name, \
    create_salesman

router = APIRouter()


@router.get("/", response_model=List[User], tags=['users'])
async def get_users(db: Session = Depends(get_db), token: str = Security(OAUTH2)):
    authorization.check_authorization(db, token, route_type=ROUTE_GET, view=USERS_VIEW)
    json = jsonable_encoder(user_get(db))
    return JSONResponse(json)


@router.get("/{id}", response_model=User, tags=['users'])
async def get_user(id: str, db: Session = Depends(get_db), token: str = Security(OAUTH2)):
    authorization.check_authorization(db, token, route_type=ROUTE_GET, view=USERS_VIEW)
    return JSONResponse(user_get_by_id(db, id).serialize())


@router.get("/email/{email}", response_model=User, tags=['users'])
async def get_user_by_email(email: str, db: Session = Depends(get_db), token: str = Security(OAUTH2)):
    authorization.check_authorization(db, token, route_type=ROUTE_GET, view=USERS_VIEW)
    return JSONResponse(user_get_email(db, email).serialize())


@router.get("/name/{name}", response_model=User, tags=['users'])
async def get_user_by_name(name: str, db: Session = Depends(get_db), token: str = Security(OAUTH2)):
    authorization.check_authorization(db, token, name=name, route_type=ROUTE_GET, view=USERS_VIEW)
    return JSONResponse(user_get_name(db, name).serialize())


@router.post("/", response_model=User, tags=['users'])
async def create_user(data: dict, db: Session = Depends(get_db)):
    create_all_types(db)
    try:
        return JSONResponse(user_create(db, data).serialize())

    except IntegrityError as e:
        raise UnprocessableEntityException(e.args[0])


@router.post("/salesman/", response_model=User, tags=['users'])
async def create_salesman(data: dict, db: Session = Depends(get_db), token: str = Security(OAUTH2)):
    authorization.check_authorization(db, token, route_type=ROUTE_CREATE, view=USERS_VIEW)
    try:
        return JSONResponse(create_salesman(db, data))

    except IntegrityError as e:
        raise UnprocessableEntityException(e.args[0])


@router.put("/{id}", response_model=User, tags=['users'])
async def update_user(id: str, data: dict, db: Session = Depends(get_db), token: str = Security(OAUTH2)):
    authorization.check_authorization(db, token, route_type=ROUTE_UPDATE, view=USERS_VIEW)
    return JSONResponse(user_update(db, id, data).serialize())


@router.delete("/{id}", response_model=User, tags=['users'])
async def delete_user(id: str, db: Session = Depends(get_db), token: str = Security(OAUTH2)):
    authorization.check_authorization(db, token, route_type=ROUTE_DELETE, view=USERS_VIEW)
    return JSONResponse(user_delete(db, id).serialize())
