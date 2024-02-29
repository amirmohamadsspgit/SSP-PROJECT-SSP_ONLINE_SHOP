import re
import tkinter.messagebox as msg


def name_validator(name):
    if isinstance(name, str) and re.match(r"^[a-zA-Z/s]{1,30}$", name):
        return name
    # else:
    #     msg.showerror("validator1", "INVALID NAME")


def id_validator(id):
    if isinstance(id, int):
        return id
    # else:
    #     msg.showerror("validator", "INVALID ID")


def phone_validator(phone):
    if re.match(r"^09[0-9]{9}$", phone):
        return phone


