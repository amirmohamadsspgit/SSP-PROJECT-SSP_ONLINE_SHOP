from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import tkinter.messagebox as msg
from model.entity import *


class Databasemanager:
    def __init__(self):
        self.engine = None
        self.session = None

    def make_engine(self):
        if not database_exists("mysql+pymysql://root:root123@localhost:3306/mft"):
            create_database("mysql+pymysql://root:root123@localhost:3306/mft")

        self.engine = create_engine("mysql+pymysql://root:root123@localhost:3306/mft")

        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def save(self, entity):
        self.make_engine()
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        self.session.close()
        # msg.showinfo("SAVED", "SAVED ")
        return entity

    def remove(self, entity):
        self.make_engine()
        self.session.delete(entity)
        self.session.commit()
        self.session.refresh()
        self.session.close()
        return entity

    def edite(self, entity):
        self.make_engine()
        self.session.merge(entity)
        self.session.commit()
        self.session.refresh()
        self.session.close()
        return entity

    def find_all(self, class_name):
        self.make_engine()
        entity_list = self.session.query(class_name).all()
        self.session.close()
        return entity_list

    def find_by_id(self, class_name, id):
        self.make_engine()
        entity = self.session.get(class_name, id)
        self.session.close()
        return entity

    def find_by_username_and_password(self, username1, password1):
        self.make_engine()
        entity = self.session.query(User).filter(User.username == username1 and User.password == password1).all()
        self.session.close()
        return entity

    def update(self, id, q):
        self.make_engine()
        entity = self.session.query(Storage).filter(Storage.id == id)
        entity.update({"quantity": q})
        self.session.commit()
        self.session.close()


