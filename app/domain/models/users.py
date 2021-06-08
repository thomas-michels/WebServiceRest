
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Boolean
from database import Base
from uuid import uuid4


class User(Base):
    __tablename__ = 'users'
    id = Column(String, default=lambda: str(uuid4()),primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_date = Column(DateTime, default=lambda: datetime.now())
    updated_date = Column(DateTime, default=lambda: datetime.now())
    active = Column(Boolean, default=True)

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'active': self.active
        }
