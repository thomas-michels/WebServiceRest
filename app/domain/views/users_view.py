from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.domain.models import users
from app.domain.schemas.users_schemas import User
from typing import List
from sqlalchemy.orm import Session

from database import get_db

router = APIRouter()


@router.get("/", response_model=List[User], tags=['users'])
async def get_users(db: Session = Depends(get_db)):
    all_users = db.query(users.User).all()
    return JSONResponse(all_users)


@router.get("/{id}", response_model=User, tags=['users'])
async def get_user(id: str, db: Session = Depends(get_db)):
    user = db.query(users.User).get(id)
    return JSONResponse(user.serialize())


@router.post("/", response_model=User, tags=['users'])
async def create_user(data: dict, db: Session = Depends(get_db)):
    user = users.User()
    user.id = data.get('id')
    user.name = data.get('name')
    user.email = data.get('email')
    user.password = data.get('password')
    db.add(user)
    db.commit()
    return JSONResponse(user.serialize())


@router.put("/{id}", response_model=User, tags=['users'])
async def update_user(id: str, data: dict, db: Session = Depends(get_db)):
    return JSONResponse()