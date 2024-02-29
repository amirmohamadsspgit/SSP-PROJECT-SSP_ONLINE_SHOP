from sqlalchemy.orm import relationship

from model.entity.base import Base

from sqlalchemy import  Integer, ForeignKey, Column


class Payment(Base):
    __tablename__ = "payment_tbl"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user_tbl.id"))
    pay = Column(Integer)
    No = Column(Integer)

    user = relationship("User")

    def __init__(self, user, pay, NO_P):
        self.user = user
        self.pay = pay
        self.No = NO_P

    # @property
    # def pay(self):
    #     return self._pay
    #
    # @pay.setter
    # def pay(self, pay):
    #     if isinstance(pay, int):
    #         self._pay = pay
    #     else:
    #         msg.showerror("valdator", "INVALID PAY")
