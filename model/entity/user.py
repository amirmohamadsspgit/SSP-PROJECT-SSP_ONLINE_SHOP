from sqlalchemy import Integer, String, Column
from model.entity.base import Base


class User(Base):
    __tablename__ = "user_tbl"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    family = Column(String(30))
    username = Column(String(30))
    password = Column(Integer)
    phone = Column(String(12))

    def __init__(self, name, family, username, password, phone):
        self.name = name
        self.family = family
        self.username = username
        self.password = password
        self.phone = phone

    # @property
    # def name(self):
    #     return self._name
    #
    # @name.setter
    # def name(self, name):
    #     try:
    #         if name_validator(name):
    #             self._name = name
    #         else:
    #             msg.showerror("ERROR", "INVALID NAME")
    #     except Exception as e:
    #         msg.showerror("ERROR", e)

    # @property
    # def username(self):
    #     return self.username
    #
    # @username.setter
    # def username(self, value):
    #     if isinstance(value, str):
    #         self.username = value
    #
    # @property
    # def family(self):
    #     return self.family
    #
    # @family.setter
    # def family(self, name2):
    #     try:
    #         if isinstance(name2, str) and re.match(r"^[a-zA-Z/s]{1,30}$", name2):
    #             self.family = name2
    #         else:
    #             msg.showerror("validator", "INVALID FAMILY")
    #     except Exception as e:
    #         msg.showerror("error", e)
    #
    # @property
    # def password(self):
    #     return self.password
    #
    # @password.setter
    # def password(self, password2):
    #     try:
    #         if id_validator(password2):
    #             self.password = password2
    #         else:
    #             msg.showerror("validator", "INVALID PASSWORD")
    #     except Exception as e:
    #         msg.showerror("error", e)
    #
    # @property
    # def phone(self):
    #     return self.phone
    #
    # @phone.setter
    # def phone(self, value):
    #     try:
    #         if phone_validator(value):
    #             self.phone = value
    #         else:
    #             msg.showerror("validator", "INVALID PHONE")
    #     except Exception as e:
    #         msg.showerror("error", e)


