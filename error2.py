from tkinter import *
from tkinter import messagebox

Window = Tk()
Window.geometry('400x200')
Window.title('Netflix & Chill')
Window.config(background='peach')

labelling = Label()

def verify():
    messagebox.showinfo("Y'all insane")

mycheck = Button(Window, text="check status", command=verify)
mycheck.pack()


def check():
    try:
        entry_get = int(chck_entry.get())
    if entry_get > 3000:
        messagebox.showinfo("Qualify", 'You won a Netflix & Chill with me. Congratulations.')
        chck_entry.delete(0, END)

    else:
        messagebox.showinfo("Qualify", 'Insufficient funds')
        chck_entry.delete(0, END)

    except ValueError:
    messagebox.showinfo("Quality", 'Top up your account ')


chck_l1 = Label(Window, text="Please enter amount in your account", bg='brown')
chck_l1.pack()

chck_entry = Entry(Window, textvariable="")
chck_entry.pack()

btn = Button(Window, text="Check qualfication ", bg="magenta", command=check).pack()
