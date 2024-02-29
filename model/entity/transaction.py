from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship
from model.entity.base import Base


class Transaction(Base):
    __tablename__ = "transaction_tbl"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user_tbl.id"))
    stuff_id = Column(Integer, ForeignKey("stuff_tbl.id"))
    quantity = Column(Integer)
    total_price = Column(Integer)
    No = Column(Integer)

    user = relationship("User")
    stuff = relationship("Stuff")

    def __init__(self, user, stuff, quantity, total_price, No):
        self.user = user
        self.stuff = stuff
        self.quantity = quantity
        self.total_price = total_price
        self.No = No

    # @property
    # def quantity(self):
    #     return self._quantity
    #
    # @quantity.setter
    # def quantity(self, quantity):
    #     if isinstance(quantity, int):
    #         self._quantity = quantity
    #     else:
    #         msg.showerror("valdator", "INVALID QUANTITY")
    #
    # @property
    # def total_price(self):
    #     return self._total_price
    #
    # @total_price.setter
    # def total_price(self, total_price):
    #     if isinstance(total_price , int):
    #         self._total_price = total_price
    #     else:
    #         msg.showerror("valdator", "INVALID TOTAL_PRICE")
