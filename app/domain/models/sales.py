
from datetime import date
from sqlalchemy import Column, String, Date, Boolean
from database import Base
from uuid import uuid4


class Sale(Base):
    __tablename__ = 'sales'
    id = Column(String, default=lambda: str(uuid4()), primary_key=True)
    date = Column(Date, default=lambda: date.today())
    active = Column(Boolean, default=True)

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'date': self.date.ctime(),
            'active': self.active
        }
