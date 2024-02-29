from controller.controller1 import *
from tkinter import *


class View_register:
    def __init__(self):
        self.winregister = Tk()
        self.winregister.title("SSP SHOP")
        self.winregister.geometry("500x500")

        Label(self.winregister, text="NAME :", font=("BankGothic Md BT", 20)).place(x=96, y=70, height=40, width=195)
        Label(self.winregister, text="FAMILY :", font=("BankGothic Md BT", 20)).place(x=85, y=120, height=40, width=195)
        Label(self.winregister, text="USER NAME :", font=("BankGothic Md BT", 20)).place(x=10, y=170, height=40,
                                                                                         width=270)
        Label(self.winregister, text="PASSWORD :", font=("BankGothic Md BT", 20)).place(x=14, y=220, height=40,
                                                                                        width=270)
        Label(self.winregister, text="PHONE :", font=("BankGothic Md BT", 20)).place(x=47, y=270, height=40, width=270)

        self.rn = StringVar()
        self.regester_neme = Entry(self.winregister, font=("BankGothic Md BT", 15), bg="grey80", textvariable=self.rn)
        self.regester_neme.place(x=250, y=70, height=40, width=195)

        self.rf = StringVar()
        self.regester_family = Entry(self.winregister, font=("BankGothic Md BT", 15), bg="grey80", textvariable=self.rf)
        self.regester_family.place(x=250, y=120, height=40, width=195)

        self.ru = StringVar()
        self.regester_user = Entry(self.winregister, font=("BankGothic Md BT", 15), bg="grey80", textvariable=self.ru)
        self.regester_user.place(x=250, y=170, height=40, width=195)

        self.rp = IntVar()
        self.regester_password = Entry(self.winregister, font=("BankGothic Md BT", 15), bg="grey80",
                                       textvariable=self.rp)
        self.regester_password.place(x=250, y=220, height=40, width=195)
        self.rp.set("")

        self.rph = StringVar()
        self.regester_phone = Entry(self.winregister, font=("BankGothic Md BT", 15), bg="grey80", textvariable=self.rph)
        self.regester_phone.place(x=250, y=270, height=40, width=195)
        self.rph.set("09")

        self.btn_main_register = Button(self.winregister, text="REGISTER NOW", bg="grey80",
                                        font=("BankGothic Md BT", 25), command=self.register_v)
        self.btn_main_register.place(x=95, y=350)
        self.btn_main_register.bind("<Enter>", self.enter)
        self.btn_main_register.bind("<Leave>", self.leave)

        self.winregister.mainloop()

    def register_v(self):
        self.rg = Controller()
        self.rg.register(self.rn.get(), self.rf.get(), self.ru.get(), self.rp.get(), self.rph.get())

    def enter(self, event):
        event.widget.config(bg="dark slate gray")

    def leave(self, event):
        event.widget.config(bg="grey80")
