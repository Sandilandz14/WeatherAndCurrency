from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("logins")
root.geometry("400x230")
root.config(background='red')






#Functions of buttons
def login():
    usp = {"Sandile":"Tukani", "Amahle":"Ngcombo", "Tsedza":"Sadzadza", "Madzikane":"Phedlha"}
    usr = us_entry.get()
    psw = p_entry.get()
    if (usr,psw)in usp.items():
        messagebox.showinfo("Info","Correct!!! You are now logged in!")
        root.withdraw()
        import qualifications
        qualifications.verify()
    else:
        messagebox.showinfo("Info","Oops!,unmatching details, please try again")
        us_entry.delete(0,END)
        p_entry.delete(0,END)

#labels
instr_l1 = Label(root, text = 'Please enter your login details', font = 40)
usr_l2 = Label(root, text = 'Username: ', background = "yellow")
psswrd_l3 = Label(root, text = 'Password: ',background = "orange")

#entry boxes
us_entry = Entry(root, textvariable = "username")
p_entry = Entry(root,textvariable = "password", show = '*')

#buttons
login_btn = Button(root, text = 'Login', command=login)

#Placements
instr_l1.place(x=90, y=5)
usr_l2.place(x=100, y=55)
psswrd_l3.place(x=100, y=105)
us_entry.place(x=100, y=75)
p_entry.place(x=100, y=125)
login_btn.place(x=150, y=160)



root.mainloop()
