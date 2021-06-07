
from sqlalchemy import Column, String, Integer, ForeignKey
from database import Base


class Order(Base):
    __tablename__ = 'orders'
    id = Column(String, primary_key=True)
    sale_id = Column(String, ForeignKey('sales.id'))
    product_id = Column(String, ForeignKey('products.id'))
    quantity = Column(Integer, nullable=False)

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'sale_id': self.sale_id,
            'product_id': self.product_id,
            'quantity': self.quantity
        }
