
from sqlalchemy.orm import Session
from datetime import datetime
from werkzeug.security import generate_password_hash
from app.domain.models.users import User
from utils.token import encode
from typing import List
from app.domain.controllers.base_controller import get as base_get, \
                                                    get_by_id as base_get_by_id,\
                                                    delete as base_delete


def create(db: Session, data: dict) -> User:
    user = User()
    user.name = data.get('name')
    user.email = data.get('email')
    user.password = generate_password_hash(data.get('password'))
    db.add(user)
    db.commit()
    return user


def get(db: Session) -> List[User]:
    return base_get(db, User)


def get_by_id(db: Session, id: str) -> User:
    return base_get_by_id(db, User, id)


def get_by_email(db: Session, email: str) -> User:
    return db.query(User).filter_by(email=email).first()


def get_by_name(db: Session, name: str) -> User:
    return db.query(User).filter_by(name=name).first()


def update(db: Session, id: str, data: dict) -> User:
    user = get_by_id(db, id)
    user.name = data.get('name') if data.get('name') else user.name
    user.email = data.get('email') if data.get('email') else user.email
    user.password = generate_password_hash(data.get('password')) if data.get('password') else user.password
    user.updated_date = datetime.now()
    db.commit()
    return user


def delete(db: Session, id: str) -> User:
    user = base_delete(db, User, id)
    user.updated_date = datetime.now()
    db.commit()
    return user


def login(db: Session, data: dict):
    email = data.get('email')
    password = data.get('password')
    user = get_by_email(db, email)
    if user:
        if user.active:
            if user.verify_password(password):
                return encode(user.serialize())
