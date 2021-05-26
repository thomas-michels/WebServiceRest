from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Film(Base):
    __tablename__ = "films"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    year = Column(Integer)
    characters_id = Column(Integer, ForeignKey('actors.id'), use_list=True)
    is_active = Column(Boolean, default=True)

    character = relationship('Actor', back_populates="films")
