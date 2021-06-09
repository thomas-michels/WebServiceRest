from pydantic import BaseModel


class Order(BaseModel):
    id: str
    sale_id: str
    product_id: str
    quantity: float
    active: bool

    class Config:
        orm_mode = True
