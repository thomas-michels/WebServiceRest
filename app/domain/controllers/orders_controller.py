from sqlalchemy.orm import Session
from app.domain.models.orders import Order
from app.domain.controllers.users_controller import get_by_name as user_get_by_name
from app.domain.controllers.products_controller import get_by_name as product_get_by_name
from app.domain.controllers.base_controller import get as base_get, \
                                                    get_by_id as base_get_by_id,\
                                                    delete as base_delete


def create(db: Session, data: dict):
    order = Order()
    order.user_id = data.get('user_id')
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


def get_by_product(db: Session, name):
    product = product_get_by_name(db, name)
    return db.query(Order).filter_by(product_id=product.id).all()


def get_by_user(db: Session, name):
    user = user_get_by_name(db, name)
    return db.query(Order).filter_by(user_id=user.id).all()


def update(db: Session, id: str, data: dict):
    order = get_by_id(db, id)
    order.user_id = data.get('user_id') if data.get('user_id') else order.user_id
    order.sale_id = data.get('sale_id') if data.get('sale_id') else order.sale_id
    order.product_id = data.get('product_id') if data.get('product_id') else order.product_id
    order.quantity = data.get('quantity') if data.get('quantity') else order.quantity
    db.commit()
    return order


def delete(db: Session, id: str):
    return base_delete(db, Order, id)
