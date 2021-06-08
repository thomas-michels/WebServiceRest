from sqlalchemy.orm import Session

from app.domain import models


def get(db: Session, model: models):
    return db.query(model).all()


def get_by_id(db: Session, model: models, id: str):
    return db.query(model).get(id)


def delete(db: Session, model: models, id: str):
    entity = get_by_id(db, model, id)
    entity.active = False
    db.commit()
    return entity
