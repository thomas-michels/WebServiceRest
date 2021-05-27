from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from app.domain.models.actors_models import Actor
from app.domain.models.films_models import Film
from database import Base


class Acting(Base):
    __tablename__ = 'acting'
    id = Column(Integer, primary_key=True, index=True)
    actor_id = Column(Integer, ForeignKey('actors.id'))
    film_id = Column(Integer, ForeignKey('films.id'))

    actor = relationship(Actor, backref=backref('acting', cascade='all, delete-orphan'))
    film = relationship(Film, backref=backref('acting', cascade='all, delete-orphan'))
