from model.entity.base import Base
from sqlalchemy import String, Integer, Column



class Storage(Base):
    __tablename__ = "storage_tbl"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    quantity = Column(Integer)

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
