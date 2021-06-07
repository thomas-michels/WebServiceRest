
from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.domain.schemas import actors_schemas

router = APIRouter()


@router.get('/', response_model=List[actors_schemas.Actor])
def get_actors():
    return
