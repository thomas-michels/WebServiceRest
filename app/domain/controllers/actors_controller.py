from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash
from app.domain.schemas.actors_schemas import ActorCreate
from app.domain.schemas.films_schemas import FilmCreate
from app.domain.models.actors_models import Actor


def get_actor(db: Session, actor_id: int):
    return db.query(Actor).filter(Actor.id == actor_id).first()


def get_actors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Actor).offset(skip).limit(limit).all()


def create_actor(db: Session, actor: ActorCreate):
    hashed_password = generate_password_hash(actor.password)
    db_actor = Actor(name=actor.name, password=hashed_password, age=actor.age)
    db.add(db_actor)
    db.commit()
    db.refresh(db_actor)
    return db_actor


def get_films(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Actor.Film).offset(skip).limit(limit).all()


def create_user_item(db: Session, film: FilmCreate, actor_id: int):
    db_item = Actor.Film(**film.dict(), actor=actor_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
