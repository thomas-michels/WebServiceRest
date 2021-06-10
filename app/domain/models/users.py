
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from uuid import uuid4
from werkzeug.security import check_password_hash


class User(Base):
    __tablename__ = 'users'
    id = Column(String, default=lambda: str(uuid4()), primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_date = Column(DateTime, default=lambda: datetime.now())
    updated_date = Column(DateTime, default=lambda: datetime.now())
    active = Column(Boolean, default=True)

    user_type_id = Column(Integer, ForeignKey('types.id'), default=3)
    user_type = relationship('Type', uselist=False)

    def verify_password(self, passwd) -> bool:
        return check_password_hash(self.password, passwd)

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'user_type': self.user_type.serialize(),
            'active': self.active
        }

    def serialize_token(self) -> dict:
        return {
            'id': self.id,
            'email': self.email,
            'user_type': self.user_type.name,
            'active': self.active
        }
