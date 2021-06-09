
from sqlalchemy import Column, String, Integer
from database import Base


class Type(Base):
    __tablename__ = 'types'
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String)

    def serialize(self):
        return {
            'id': self.id,
            'type': self.type
        }
