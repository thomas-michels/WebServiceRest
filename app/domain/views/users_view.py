from fastapi import APIRouter, Depends, Security, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from app.domain.schemas.users_schemas import User
from fastapi.security import OAuth2PasswordBearer
from app.domain.controllers.types_controller import create_all_types
from typing import List
from sqlalchemy.orm import Session
from database import get_db
from app.domain.services import authorization
from app.domain.controllers.users_controller import get as user_get, \
    create as user_create, \
    get_by_id as user_get_by_id, \
    update as user_update, \
    delete as user_delete, \
    get_by_email as user_get_email, \
    get_by_name as user_get_name
from settings import SALESMAN, ADMIN

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/')


@router.get("/", response_model=List[User], tags=['users'])
async def get_users(db: Session = Depends(get_db), token = Security(oauth2_scheme)):
    authorization.check_authorization(token, [SALESMAN, ADMIN])
    json = jsonable_encoder(user_get(db))
    return JSONResponse(json)


@router.get("/{id}", response_model=User, tags=['users'])
async def get_user(id: str, db: Session = Depends(get_db)):
    return JSONResponse(user_get_by_id(db, id).serialize())


@router.get("/email/", response_model=User, tags=['users'])
async def get_user_by_email(email: str, db: Session = Depends(get_db)):
    return JSONResponse(user_get_email(db, email).serialize())


@router.get("/name/", response_model=User, tags=['users'])
async def get_user_by_name(name: str, db: Session = Depends(get_db)):
    return JSONResponse(user_get_name(db, name).serialize())


@router.post("/", response_model=User, tags=['users'])
async def create_user(data: dict, db: Session = Depends(get_db)):
    create_all_types(db)
    return JSONResponse(user_create(db, data).serialize())


@router.put("/{id}", response_model=User, tags=['users'])
async def update_user(id: str, data: dict, db: Session = Depends(get_db)):
    return JSONResponse(user_update(db, id, data).serialize())


@router.delete("/{id}", response_model=User, tags=['users'])
async def delete_user(id: str, db: Session = Depends(get_db)):
    return JSONResponse(user_delete(db, id).serialize())
