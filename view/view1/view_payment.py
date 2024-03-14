from tkinter import *
from controller.controller1.controll import Controller



class View_payment:
    def __init__(self, q1, q2, q3, q4, list_product, username, password):
        self.username = username
        self.password = password
        self.list_product = list_product
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.winp = Tk()
        self.winp.geometry("500x300")
        Label(self.winp, text="PRODUCT1 :", font=("BankGothic Md BT", 15)).place(x=20, y=20)
        Label(self.winp, text="PRODUCT2 :", font=("BankGothic Md BT", 15)).place(x=20, y=70)
        Label(self.winp, text="PRODUCT3 :", font=("BankGothic Md BT", 15)).place(x=20, y=120)
        Label(self.winp, text="PRODUCT4 :", font=("BankGothic Md BT", 15)).place(x=20, y=170)

        self.ce1 = IntVar()
        self.en1 = Entry(self.winp, textvariable=self.ce1, state="readonly", font=("BankGothic Md BT", 15))
        self.en1.place(x=180, y=20, height=30, width=40)
        self.ce1.set(q1)

        self.ce2 = IntVar()
        self.en2 = Entry(self.winp, textvariable=self.ce2, state="readonly", font=("BankGothic Md BT", 15))
        self.en2.place(x=180, y=70, height=30, width=40)
        self.ce2.set(q2)

        self.ce3 = IntVar()
        self.en3 = Entry(self.winp, textvariable=self.ce3, state="readonly", font=("BankGothic Md BT", 15))
        self.en3.place(x=180, y=120, height=30, width=40)
        self.ce3.set(q3)

        self.ce4 = IntVar()
        self.en4 = Entry(self.winp, textvariable=self.ce4, state="readonly", font=("BankGothic Md BT", 15))
        self.en4.place(x=180, y=170, height=30, width=40)
        self.ce4.set(q4)

        Label(self.winp, text="TOTAL PRICE", font=("BankGothic Md BT", 15)).place(x=280, y=20)
        self.pet = IntVar()
        self.ent = Entry(self.winp, textvariable=self.pet, font=("BankGothic Md BT", 15), state="readonly")
        self.ent.place(x=312, y=50, height=30, width=100)
        self.pet.set(q1 * 100 + q2 * 200 + q3 * 300 + q4 * 400)

        Label(self.winp, text="YOUR PAY", font=("BankGothic Md BT", 15)).place(x=300, y=140)
        self.pety = IntVar()
        self.ent = Entry(self.winp, textvariable=self.pety, font=("BankGothic Md BT", 15))
        self.ent.place(x=312, y=170, height=30, width=100)

        self.btp = Button(self.winp, text="PAYMENT", font=("BankGothic Md BT", 15), command=self.btn_pay)
        self.btp.place(x=100, y=230, width=300)

        self.winp.mainloop()

    def btn_pay(self):
        from view.view1 import View_log
        list_product = self.list_product
        self.cntp = Controller()
        self.cntp.final_pay(self.pet.get(), self.pety.get(), list_product, self.q1, self.q2, self.q3, self.q4,
                            self.username, self.password)
        self.winp.destroy()
        bklog = View_log()
