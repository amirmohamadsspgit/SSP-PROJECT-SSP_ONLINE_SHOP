from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import tkinter.messagebox as msg
from view.view1.view_payment import View_payment


class View_buy:
    def __init__(self, name, family, username, password):
        self.username = username
        self.password = password
        self.winbuy = Tk()
        self.winbuy.title("SSP SHOP")
        self.winbuy.geometry("1200x650")

        Label(self.winbuy, text=("Dear", name, family), font=("BankGothic Md BT", 25), height=1).place(x=10, y=10)
        Label(self.winbuy, text="WELCOME TO SSP SHOP", font=("BankGothic Md BT", 25), height=1).place(x=10, y=55)
        Label(self.winbuy, text="-------------------------"
                                "------------------", font=("BankGothic Md BT", 25), height=1).place(x=10, y=85)

        self.img = Image.open("spd1.jpg")
        self.img = ImageTk.PhotoImage(self.img)
        # **********************************************  PRODUCT1
        self.p1 = Button(self.winbuy, image=self.img, height=150, width=150, command=self.count_up1)
        self.p1.place(x=20, y=120)
        self.p1.bind("<Enter>", self.enter)
        self.p1.bind("<Leave>", self.leave)
        self.p1 = Label(self.winbuy, font=("BankGothic Md BT", 15), height=1, text="PRODUCT 1")
        self.p1.place(x=30, y=280)
        self.ce1 = IntVar()
        self.etc = Entry(self.winbuy, textvariable=self.ce1)
        self.etc.place(x=85, y=310, height=40, width=30)
        # **********************************************  PRODUCT2
        self.p2 = Button(self.winbuy, image=self.img, height=150, width=150, command=self.count_up2)
        self.p2.place(x=20, y=370)
        self.p2.bind("<Enter>", self.enter)
        self.p2.bind("<Leave>", self.leave)
        self.p2 = Label(self.winbuy, font=("BankGothic Md BT", 15), height=1, text="PRODUCT 2")
        self.p2.place(x=30, y=530)
        self.ce2 = IntVar()
        self.etc = Entry(self.winbuy, textvariable=self.ce2)
        self.etc.place(x=85, y=560, height=40, width=30)

        # **********************************************  PRODUCT3
        self.p3 = Button(self.winbuy, image=self.img, height=150, width=150, command=self.count_up3)
        self.p3.place(x=220, y=370)
        self.p3.bind("<Enter>", self.enter)
        self.p3.bind("<Leave>", self.leave)
        self.p3 = Label(self.winbuy, font=("BankGothic Md BT", 15), height=1, text="PRODUCT 3")
        self.p3.place(x=230, y=530)
        self.ce3 = IntVar()
        self.etc = Entry(self.winbuy, textvariable=self.ce3)
        self.etc.place(x=285, y=560, height=40, width=30)
        # **********************************************  PRODUCT4
        self.p4 = Button(self.winbuy, image=self.img, height=150, width=150, command=self.count_up4)
        self.p4.place(x=220, y=120)
        self.p4.bind("<Enter>", self.enter)
        self.p4.bind("<Leave>", self.leave)
        self.p4 = Label(self.winbuy, font=("BankGothic Md BT", 15), height=1, text="PRODUCT 4")
        self.p4.place(x=230, y=280)
        self.ce4 = IntVar()
        self.etc = Entry(self.winbuy, textvariable=self.ce4)
        self.etc.place(x=285, y=310, height=40, width=30)

        # **********************************************  TABALE
        self.tree = ttk.Treeview(self.winbuy, columns=["1", "2", "3", "4", "5", "6"], height=17, show="headings")
        self.tree.place(x=500, y=110)
        self.tree.column("1", width=120)
        self.tree.column("2", width=100)
        self.tree.column("3", width=100)
        self.tree.column("4", width=100)
        self.tree.column("5", width=150)
        self.tree.column("6", width=120)

        self.tree.heading("1", text="NAME")
        self.tree.heading("2", text="BRAND")
        self.tree.heading("3", text="MODEL")
        self.tree.heading("4", text="PRICE")
        self.tree.heading("5", text="DESCRIPTION")
        self.tree.heading("6", text="QUANTITY")

        # ******************************************************BOTTUN
        self.btni = Button(self.winbuy, text="insert to tabale", font=("BankGothic Md BT", 15),
                           command=self.insert_to_tabale)
        self.btni.place(x=550, y=500, height=40, width=600)

        self.btnt = Button(self.winbuy, text="payment", font=("BankGothic Md BT", 15), command=self.v_pay)
        self.btnt.place(x=550, y=550, height=40, width=600)

        self.winbuy.mainloop()

    def enter(self, event):
        event.widget.config(bg="dark slate gray")

    def leave(self, event):
        event.widget.config(bg="grey80")

    def v_pay(self):
        q1 = self.ce1.get()
        q2 = self.ce2.get()
        q3 = self.ce3.get()
        q4 = self.ce4.get()

        self.winbuy.destroy()
        self.vp = View_payment(q1, q2, q3, q4, self.list_buy, self.username, self.password)

    def insert_to_tabale(self):
        self.list_buy = []
        for i in self.list_buy:
            self.list_buy.remove(i)
        self.list_buy.append(["product1", "ssp", "ssp1", 100, "********", self.ce1.get()])
        self.list_buy.append(["product2", "ssp", "ssp2", 200, "********", self.ce2.get()])
        self.list_buy.append(["product3", "ssp", "ssp3", 300, "********", self.ce3.get()])
        self.list_buy.append(["product4", "ssp", "ssp4", 400, "********", self.ce4.get()])
        for pd in self.list_buy:
            if pd[5] == 0:
                self.list_buy.remove(pd)
        for pr in self.tree.get_children():
            self.tree.delete(pr)
        self.tree.insert("", END, values=("product1", "ssp", "ssp1", 100, "********", self.ce1.get()))
        self.tree.insert("", END, values=("product2", "ssp", "ssp2", 200, "********", self.ce2.get()))
        self.tree.insert("", END, values=("product3", "ssp", "ssp3", 300, "********", self.ce3.get()))
        self.tree.insert("", END, values=("product4", "ssp", "ssp4", 400, "********", self.ce4.get()))

    def count_up1(self):
        try:
            self.c1 = self.ce1.get()
            self.ce1.set(self.c1 + 1)
        except Exception as e:
            msg.showerror("error", e)

    def count_up2(self):
        try:
            self.c2 = self.ce2.get()
            self.ce2.set(self.c2 + 1)
        except Exception as e:
            msg.showerror("error", e)

    def count_up3(self):
        try:
            self.c3 = self.ce3.get()
            self.ce3.set(self.c3 + 1)
        except Exception as e:
            msg.showerror("error", e)

    def count_up4(self):
        try:
            self.c4 = self.ce4.get()
            self.ce4.set(self.c4 + 1)
        except Exception as e:
            msg.showerror("error", e)
