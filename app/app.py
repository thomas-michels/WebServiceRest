from fastapi import FastAPI, Depends, HTTPException
from settings import PROJECT_NAME, BACKEND_CORS_ORIGINS
from starlette.middleware.cors import CORSMiddleware
from app.domain import api_router
from app.domain.models import users
from database import engine, SessionLocal
from starlette.responses import RedirectResponse
from app.domain.schemas.users_schemas import User
from typing import List
from sqlalchemy.orm import Session

users.Base.metadata.create_all(bind=engine)

app = FastAPI(title=PROJECT_NAME)

if BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")
# app.include_router(api_router)


@app.get("/users/", response_model=List[User])
def show_records(db: Session = Depends(get_db)):
    records = db.query(users.User).all()
    return records


@app.post("/users/", response_model=List[User])
def create(db: Session = Depends(get_db)):
    user = users.User()
    user.id = '9'
    user.name = 'asdasdas'
    user.email = ''
    user.password = 'asdasd'
    records = db.add(user)
    db.commit()
    return records