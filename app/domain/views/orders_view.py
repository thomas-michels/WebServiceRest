from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.domain.schemas.orders_schema import Order
from typing import List
from sqlalchemy.orm import Session
from database import get_db
from app.domain.controllers.orders_controller import get as order_get, \
                                                           create as order_create, \
                                                           get_by_id as order_get_by_id, \
                                                           update as order_update, \
                                                           delete as order_delete

router = APIRouter()


@router.get("/", response_model=List[Order], tags=['orders'])
async def get_orders(db: Session = Depends(get_db)):
    json = jsonable_encoder(order_get(db))
    return JSONResponse(json)


@router.get("/{id}", response_model=Order, tags=['orders'])
async def get_order(id: str, db: Session = Depends(get_db)):
    return JSONResponse(order_get_by_id(db, id).serialize())


@router.post("/", response_model=Order, tags=['orders'])
async def create_order(data: dict, db: Session = Depends(get_db)):
    return JSONResponse(order_create(db, data).serialize())


@router.put("/{id}", response_model=Order, tags=['orders'])
async def update_order(id: str, data: dict, db: Session = Depends(get_db)):
    return JSONResponse(order_update(db, id, data).serialize())


@router.delete("/{id}", response_model=Order, tags=['orders'])
async def delete_order(id: str, db: Session = Depends(get_db)):
    return JSONResponse(order_delete(db, id).serialize())
