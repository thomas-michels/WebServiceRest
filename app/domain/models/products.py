
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Float, Boolean
from database import Base
from uuid import uuid4


class Product(Base):
    __tablename__ = 'products'
    id = Column(String, default=lambda: str(uuid4()), primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    created_date = Column(DateTime, default=lambda: datetime.now())
    updated_date = Column(DateTime, default=lambda: datetime.now())
    active = Column(Boolean, default=True)

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'created_date': self.created_date.ctime(),
            'updated_date': self.updated_date.ctime(),
            'active': self.active
        }
