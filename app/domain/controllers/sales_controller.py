from sqlalchemy.orm import Session
from app.domain.models.sales import Sale
from utils.date_converter import date_converter
from app.domain.controllers.base_controller import get as base_get, \
                                                    get_by_id as base_get_by_id,\
                                                    delete as base_delete


def create(db: Session) -> Sale:
    sale = Sale()
    db.add(sale)
    db.commit()
    return sale


def get(db: Session):
    return base_get(db, Sale)


def get_by_id(db: Session, id: str):
    return base_get_by_id(db, Sale, id)


def get_by_day(db: Session, day) -> Sale:
    return db.query(Sale).filter_by(date=day).first()


def update(db: Session, id: str, data: dict):
    date = data.get('date')
    if date:
        date = date_converter(date)

    sale = get_by_id(db, id)
    sale.date = date if date else sale.date
    db.commit()
    return sale


def delete(db: Session, id: str):
    return base_delete(db, Sale, id)
