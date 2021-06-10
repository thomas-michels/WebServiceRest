
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base
from uuid import uuid4


class Order(Base):
    __tablename__ = 'orders'
    id = Column(String, default=lambda: str(uuid4()), primary_key=True)
    user_id = Column(String, ForeignKey('users.id'))
    sale_id = Column(String, ForeignKey('sales.id'))
    product_id = Column(String, ForeignKey('products.id'))
    quantity = Column(Integer, nullable=False)
    active = Column(Boolean, default=True)

    product = relationship('Product', uselist=False)
    sale = relationship('Sale', uselist=False)
    user = relationship('User', uselist=False)

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'sale': self.sale.serialize(),
            'product': self.product.serialize(),
            'user': self.user.serialize(),
            'quantity': self.quantity,
            'active': self.active
        }
