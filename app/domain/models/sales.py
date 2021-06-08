
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Boolean
from database import Base


class Sale(Base):
    __tablename__ = 'sales'
    id = Column(String, primary_key=True)
    date = Column(DateTime, default=lambda: datetime.now())
    active = Column(Boolean, default=True)

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'date': self.date.ctime(),
            'active': self.active
        }
