import random

from model.da.user_da import User_da
from model.da.stuff_da import Stuff_da
from model.da.transaction_da import Transaction_da
import tkinter.messagebox as msg
from model.entity import *
from model.da.storage_da import Storage_da
from model.entity.payment import Payment
from model.da.payment_da import Payment_da



class Controller:
    def log_in(self, user_name, password):
        try:
            from view.view1 import View_buy
            from view.view1 import View_log
            usda = User_da()
            if usda.find_by_username_and_password(user_name, password):
                self.entity = usda.find_by_username_and_password(user_name, password)
                n = self.entity[0].name
                f = self.entity[0].family
                self.vwb = View_buy(n, f, user_name, password)
            else:
                msg.showerror("WIN", "USER NOT FOUND ; PLEAS REGISTER")
                ss = View_log()
        except Exception as e:
            msg.showerror("LOGIN ERROR", e)

    def register(self, name, family, username2, password2, phone):
        try:
            fa = User_da()
            if fa.find_by_username_and_password(username2, password2):
                msg.showerror("USER ERROR", "THIS USER IS AVAILABLE")
            else:
                uss = User(name, family, username2, password2, phone)
                ussv = User_da()
                ussv.save(uss)
                msg.showinfo("SAVE", "USER SAVED")
        except Exception as e:
            msg.showerror("REGISTER ERROR", e)

    def final_pay(self, total_price, your_payment, list_product, q1, q2, q3, q4, username, password):
        try:
            No1 = random.randrange(1111, 1111111)
            fasg = Stuff_da()
            all_No = fasg.find_all(Storage)

            def random1():
                for n in all_No:
                    if n.No == No1:
                        No1 = random.randrange(1111, 1111111)
                        random1()

            usda2 = User_da()
            ustr = usda2.find_by_username_and_password(username, password)
            est = 0
            if total_price <= your_payment:
                for p in list_product:
                    osg = Storage_da()
                    q12 = osg.check_storage(1)
                    q22 = osg.check_storage(2)
                    q32 = osg.check_storage(3)
                    q42 = osg.check_storage(4)
                    stftr = Stuff_da()
                    id1 = 1
                    match p[0]:
                        case "product1":
                            id1 = 1
                        case "product2":
                            id1 = 2
                        case "product3":
                            id1 = 3
                        case "product4":
                            id1 = 4
                    if q1 <= q12 and q2 <= q22 and q3 <= q32 and q4 <= q42:
                        tt = stftr.find_by_id(Stuff, id1)
                        ttr = Transaction(ustr[0], tt, p[5], total_price, No1)
                        ttda = Transaction_da()
                        ttda.save(ttr)
                        est = 1


                    else:
                        msg.showerror("storage error", "storage is low")
                        break
                stn = Storage_da()
                stn.change_storage(q1, q2, q3, q4, q12, q22, q32, q42)
                if est == 1:
                    po = Payment(ustr[0], total_price, No1)
                    pda = Payment_da()
                    pda.save(po)
                    msg.showinfo("BUY", "THE ORDER WAS SUCCESSFUL")
            else:
                msg.showerror("pay error", "your payment is low")

        except Exception as e:
            msg.showerror("error", e)
            print(e)
