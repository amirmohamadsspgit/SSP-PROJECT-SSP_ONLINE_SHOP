from model.da.databasemanager import Databasemanager
from model.entity.storage import Storage


class Storage_da:
    def __init__(self):
        self.gs = Databasemanager()
        if not self.gs.find_all(Storage):
            self.s1 = Storage("product1", 20)
            self.s2 = Storage("product2", 20)
            self.s3 = Storage("product3", 20)
            self.s4 = Storage("product4", 20)
            self.gs.save(self.s1)
            self.gs.save(self.s2)
            self.gs.save(self.s3)
            self.gs.save(self.s4)

    def check_storage(self, id):
        self.st_da = Databasemanager()
        self.stg = self.st_da.find_by_id(Storage, id)
        self.qs = self.stg.quantity
        return self.qs

    def change_storage(self, q1, q2, q3, q4, qd1, qd2, qd3, qd4):
        self.stc_da = Databasemanager()
        if q1 >= 0:
            qna = qd1 - q1
            self.stc_da.update(1, qna)
        if q2 >= 0:
            qnb = qd2 - q2
            self.stc_da.update(2, qnb)
        if q3 >= 0:
            qnc = qd3 - q3
            self.stc_da.update(3, qnc)
        if q4 >= 0:
            qnd = qd4 - q4
            self.stc_da.update(4, qnd)

# ss = Storage_da()
# ss.change_storage(1, 1, 1, 1, 10, 10, 10, 10)
