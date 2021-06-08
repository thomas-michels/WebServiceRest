
from sqlalchemy.orm import Session
from app.domain.models.users import User
from typing import List


def create(db: Session, data: dict) -> User:
    user = User()
    user.name = data.get('name')
    user.email = data.get('email')
    user.password = data.get('password')
    db.add(user)
    db.commit()
    return user


def get(db: Session) -> List[User]:
    return db.query(User).all()


def get_by_id(db: Session, id: str) -> User:
    return db.query(User).get(id)


def update(db: Session, id: str, data: dict) -> User:
    user = get_by_id(db, id)
    user.name = data.get('name') if data.get('name') else user.name
    user.email = data.get('email') if data.get('email') else user.email
    user.password = data.get('password') if data.get('password') else user.password
    db.commit()
    return user


def delete(db: Session, id: str) -> User:
    user = get_by_id(db, id)
    user.active = False
    db.commit()
    return user
