from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.domain.schemas.users_schemas import User
from typing import List
from sqlalchemy.orm import Session
from database import get_db
from app.domain.controllers.users_controller import get as user_get, \
                                                           create as user_create, \
                                                           get_by_id as user_get_by_id, \
                                                           update as user_update, \
                                                           delete as user_delete

router = APIRouter()


@router.get("/", response_model=List[User], tags=['users'])
async def get_users(db: Session = Depends(get_db)):
    json = jsonable_encoder(user_get(db))
    return JSONResponse(json)


@router.get("/{id}", response_model=User, tags=['users'])
async def get_user(id: str, db: Session = Depends(get_db)):
    return JSONResponse(user_get_by_id(db, id).serialize())


@router.post("/", response_model=User, tags=['users'])
async def create_user(data: dict, db: Session = Depends(get_db)):
    return JSONResponse(user_create(db, data).serialize())


@router.put("/{id}", response_model=User, tags=['users'])
async def update_user(id: str, data: dict, db: Session = Depends(get_db)):
    return JSONResponse(user_update(db, id, data).serialize())


@router.delete("/{id}", response_model=User, tags=['users'])
async def delete_user(id: str, db: Session = Depends(get_db)):
    return JSONResponse(user_delete(db, id).serialize())
