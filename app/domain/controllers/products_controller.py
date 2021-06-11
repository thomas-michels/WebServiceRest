from typing import List
from datetime import datetime
from sqlalchemy.orm import Session
from app.domain.models.products import Product
from app.exceptions import NotFoundException
from app.domain.controllers.base_controller import get as base_get, \
                                                    get_by_id as base_get_by_id,\
                                                    delete as base_delete


def create(db: Session, data: dict) -> Product:
    product = Product()
    product.name = data.get('name')
    product.price = data.get('price')
    db.add(product)
    db.commit()
    return product


def get(db: Session) -> List[Product]:
    return base_get(db, Product)


def get_by_id(db: Session, id: str) -> Product:
    return base_get_by_id(db, Product, id)


def get_by_name(db: Session, name: str) -> Product:
    product = db.query(Product).filter_by(name=name).first()
    if not product:
        raise NotFoundException('Produto não encontrado')

    return product


def get_by_price(db: Session, price: float) -> Product:
    products = db.query(Product).filter_by(price=price).all()
    if not products:
        raise NotFoundException('Produto não encontrado')

    return products


def update(db: Session, id: str, data: dict) -> Product:
    product = get_by_id(db, id)
    product.name = data.get('name') if data.get('name') else product.name
    product.price = data.get('price') if data.get('price') else product.price
    product.updated_date = datetime.now()
    db.commit()
    return product


def delete(db: Session, id: str) -> Product:
    product = base_delete(db, Product, id)
    product.updated_date = datetime.now()
    db.commit()
    return product
