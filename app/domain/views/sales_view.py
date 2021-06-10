from fastapi import APIRouter, Depends, Security
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.domain.schemas.sales_schemas import Sale
from typing import List
from sqlalchemy.orm import Session

from app.domain.services import authorization
from app.domain.services.security import OAUTH2
from database import get_db
from app.domain.controllers.sales_controller import get as sale_get, \
                                                   create as sale_create, \
                                                   get_by_id as sale_get_by_id, \
                                                   update as sale_update, \
                                                   delete as sale_delete

router = APIRouter()


@router.get("/", response_model=List[Sale], tags=['sales'])
async def get_sales(db: Session = Depends(get_db)):
    json = jsonable_encoder(sale_get(db))
    return JSONResponse(json)


@router.get("/{id}", response_model=Sale, tags=['sales'])
async def get_sale(id: str, db: Session = Depends(get_db)):
    return JSONResponse(sale_get_by_id(db, id).serialize())


@router.post("/", response_model=Sale, tags=['sales'])
async def create_sale(db: Session = Depends(get_db)):
    return JSONResponse(sale_create(db).serialize())


@router.put("/{id}", response_model=Sale, tags=['sales'])
async def update_sale(id: str, data: dict, db: Session = Depends(get_db)):
    return JSONResponse(sale_update(db, id, data).serialize())


@router.delete("/{id}", response_model=Sale, tags=['sales'])
async def delete_sale(id: str, db: Session = Depends(get_db), token: str = Security(OAUTH2)):
    authorization.check_authorization(token, [ADMIN])
    return JSONResponse(sale_delete(db, id).serialize())
