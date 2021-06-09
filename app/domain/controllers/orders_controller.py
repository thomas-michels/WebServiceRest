from sqlalchemy.orm import Session
from app.domain.models.orders import Order
from app.domain.controllers.base_controller import get as base_get, \
                                                    get_by_id as base_get_by_id,\
                                                    delete as base_delete


def create(db: Session, data: dict):
    order = Order()
    order.sale_id = data.get('sale_id')
    order.product_id = data.get('product_id')
    order.quantity = data.get('quantity')
    db.add(order)
    db.commit()
    return order


def get(db: Session):
    return base_get(db, Order)


def get_by_id(db: Session, id: str):
    return base_get_by_id(db, Order, id)


def update(db: Session, id: str, data: dict):
    order = get_by_id(db, id)
    order.sale_id = data.get('sale_id') if data.get('sale_id') else order.sale_id
    order.product_id = data.get('product_id') if data.get('product_id') else order.product_id
    order.quantity = data.get('quantity') if data.get('quantity') else order.quantity
    db.commit()
    return order


def delete(db: Session, id: str):
    return base_delete(db, Order, id)
