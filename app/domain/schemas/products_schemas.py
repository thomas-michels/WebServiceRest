from datetime import datetime
from pydantic import BaseModel


class Product(BaseModel):
    id: str
    name: str
    price: float
    created_date: datetime
    updated_date: datetime
    active: bool

    class Config:
        orm_mode = True
