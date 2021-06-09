from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from database import get_db

router = APIRouter()


@router.post("/login", tags=['login'])
def login_user(data: dict, db: Session = Depends(get_db)):
    log = login(db, data)
    json = jsonable_encoder(log)
    return JSONResponse(json)
