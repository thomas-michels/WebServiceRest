
from sqlalchemy.orm import Session
from app.domain.models.type import Type
from app.domain.controllers.base_controller import get as base_get, \
                                                    get_by_id as base_get_by_id,\
                                                    delete as base_delete


def create(db: Session, data: dict):
    type = Type()
    type.id = data.get('id')
    type.type = data.get('type')
    db.add(type)
    db.commit()
    return type


def get_by_id(db: Session, id):
    return base_get_by_id(db, Type, id)


def create_all_types(db: Session):
    if not get_by_id(db, 1):
        create(db, data={"id": "1", "type": "admin"})
    if not get_by_id(db, 2):
        create(db, data={"id": "2", "type": "salesman"})
    if not get_by_id(db, 3):
        create(db, data={"id": "3", "type": "client"})
