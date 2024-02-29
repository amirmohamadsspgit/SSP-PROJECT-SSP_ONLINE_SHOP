from tkinter import *
import tkinter.messagebox as msg
from controller.controller1 import *
from model.da.databasemanager import Databasemanager
from model.entity import Stuff
from view.view1.view_register import View_register


class View_log:
    def __init__(self):
        find_stuf = Databasemanager()
        if not find_stuf.find_all(Stuff):
            s1 = Stuff("product1", "ssp", "ssp1", 100, "********")
            s2 = Stuff("product2", "ssp", "ssp2", 200, "********")
            s3 = Stuff("product3", "ssp", "ssp3", 300, "********")
            s4 = Stuff("product4", "ssp", "ssp4", 400, "********")
            find_stuf.save(s1)
            find_stuf.save(s2)
            find_stuf.save(s3)
            find_stuf.save(s4)
        self.winlog = Tk()
        self.winlog.title("SSP SHOP")
        self.winlog.geometry("500x500")

        Label(self.winlog, text="SSP SHOP", font=("BankGothic Md BT", 25), height=3).pack()
        Label(self.winlog, text="-----------------------", font=("BankGothic Md BT", 25)).place(x=120, y=65)

        Label(self.winlog, text="USER NAME", font=("BankGothic Md BT", 20)).place(x=150, y=140)
        self.ten = StringVar()
        self.entry_username = Entry(self.winlog, font=("BankGothic Md BT", 15), bg="grey80", textvariable=self.ten)
        self.entry_username.place(x=150, y=170, height=50, width=195)

        Label(self.winlog, text="PSSWORD", font=("BankGothic Md BT", 20)).place(x=165, y=240)
        self.tep = IntVar()
        self.entry_password = Entry(self.winlog, font=("BankGothic Md BT", 15), bg="grey80", textvariable=self.tep)
        self.entry_password.place(x=150, y=270, height=50, width=195)
        self.tep.set("")

        self.button_login = Button(self.winlog, text="LOG IN", font=("BankGothic Md BT", 15), bg="grey80",
                                   command=self.log)
        self.button_login.place(x=194, y=350)
        self.button_login.bind("<Enter>", self.enter)
        self.button_login.bind("<Leave>", self.leave)

        self.button_register = Button(self.winlog, text="REGISTER", font=("BankGothic Md BT", 15), bg="grey80",
                                      command=self.register_log)
        self.button_register.place(x=177, y=400)
        self.button_register.bind("<Enter>", self.enter)
        self.button_register.bind("<Leave>", self.leave)

        self.winlog.mainloop()

    def log(self):
        try:
            self.winlog.destroy()
            self.cl = Controller()
            self.cl.log_in(self.ten.get(), self.tep.get())
        except Exception as e:
            msg.showerror("LOG ERROR", e)

    def register_log(self):
        try:
            self.winlog.destroy()
            self.vr = View_register()
        except Exception as e:
            msg.showerror("REGISTER LOG ERROR", e)

    def enter(self, event):
        event.widget.config(bg="dark slate gray")

    def leave(self, event):
        event.widget.config(bg="grey80")
