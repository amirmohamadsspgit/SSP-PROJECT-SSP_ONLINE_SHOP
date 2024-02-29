from sqlalchemy import Integer, String, Column
from model.entity.base import Base



class Stuff(Base):
    __tablename__ = "stuff_tbl"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    brand = Column(String(30))
    model = Column(String(30))
    price = Column(Integer)
    descreption = Column(String(100))

    def __init__(self, name, brand, model, price, descreaption):
        self.name = name
        self.brand = brand
        self.model = model
        self.price = price
        self.descreption = descreaption





    # @property
    # def price(self):
    #     return self._price
    #
    # @price.setter
    # def price(self, price):
    #     if isinstance(price, int):
    #         self._price = price
    #     else:
    #         msg.showerror("valdator", "INVALID PRICE")
