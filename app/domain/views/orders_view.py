from fastapi import APIRouter, Depends, Security
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.domain.schemas.orders_schema import Order
from typing import List
from sqlalchemy.orm import Session

from app.domain.services import authorization
from app.domain.services.security import OAUTH2
from database import get_db
from app.domain.controllers.orders_controller import get as order_get, \
                                                           create as order_create, \
                                                           get_by_id as order_get_by_id, \
                                                           update as order_update, \
                                                           delete as order_delete
from utils.contants import ROUTE_DELETE, ROUTE_UPDATE, ROUTE_CREATE, ROUTE_GET

router = APIRouter()


@router.get("/", response_model=List[Order], tags=['orders'])
async def get_orders(db: Session = Depends(get_db), token: str = Security(OAUTH2)):
    authorization.check_authorization(db, token, route_type=ROUTE_GET)
    json = jsonable_encoder(order_get(db))
    return JSONResponse(json)


@router.get("/{id}", response_model=Order, tags=['orders'])
async def get_order(id: str, db: Session = Depends(get_db), token: str = Security(OAUTH2)):
    authorization.check_authorization(db, token, route_type=ROUTE_GET)
    return JSONResponse(order_get_by_id(db, id).serialize())


@router.post("/", response_model=Order, tags=['orders'])
async def create_order(data: dict, db: Session = Depends(get_db), token: str = Security(OAUTH2)):
    authorization.check_authorization(db, token, route_type=ROUTE_CREATE)
    return JSONResponse(order_create(db, data).serialize())


@router.put("/{id}", response_model=Order, tags=['orders'])
async def update_order(id: str, data: dict, db: Session = Depends(get_db), token: str = Security(OAUTH2)):
    authorization.check_authorization(db, token, route_type=ROUTE_UPDATE)
    return JSONResponse(order_update(db, id, data).serialize())


@router.delete("/{id}", response_model=Order, tags=['orders'])
async def delete_order(id: str, db: Session = Depends(get_db), token: str = Security(OAUTH2)):
    authorization.check_authorization(db, token, route_type=ROUTE_DELETE)
    return JSONResponse(order_delete(db, id).serialize())
