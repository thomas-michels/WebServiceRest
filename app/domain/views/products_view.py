from fastapi import APIRouter, Depends, Security
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.domain.schemas.products_schemas import Product
from typing import List
from sqlalchemy.orm import Session

from app.domain.services import authorization
from app.domain.services.security import OAUTH2
from database import get_db
from app.domain.controllers.products_controller import get as product_get, \
                                                           create as product_create, \
                                                           get_by_id as product_get_by_id, \
                                                           update as product_update, \
                                                           delete as product_delete

router = APIRouter()


@router.get("/", response_model=List[Product], tags=['products'])
async def get_products(db: Session = Depends(get_db)):
    json = jsonable_encoder(product_get(db))
    return JSONResponse(json)


@router.get("/{id}", response_model=Product, tags=['products'])
async def get_product(id: str, db: Session = Depends(get_db)):
    return JSONResponse(product_get_by_id(db, id).serialize())


@router.post("/", response_model=Product, tags=['products'])
async def create_product(data: dict, db: Session = Depends(get_db)):
    return JSONResponse(product_create(db, data).serialize())


@router.put("/{id}", response_model=Product, tags=['products'])
async def update_product(id: str, data: dict, db: Session = Depends(get_db)):
    return JSONResponse(product_update(db, id, data).serialize())


@router.delete("/{id}", response_model=Product, tags=['products'])
async def delete_product(id: str, db: Session = Depends(get_db), token: str = Security(OAUTH2)):
    authorization.check_authorization(token, [ADMIN])
    return JSONResponse(product_delete(db, id).serialize())
