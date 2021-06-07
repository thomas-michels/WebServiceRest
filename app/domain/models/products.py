
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Float
from database import Base


class Product(Base):
    __tablename__ = 'products'
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    created_date = Column(DateTime, default=lambda: datetime.now())
    updated_date = Column(DateTime, default=lambda: datetime.now())

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'created_date': self.created_date,
            'updated_date': self.updated_date
        }
