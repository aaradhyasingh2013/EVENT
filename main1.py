from tkinter import *
from tkinter import messagebox
Window= Tk()
Window.title("message box")
Window.geometry("400x400")
def msg():
    messagebox.showwarning("alert","stop virus found")
b= Button(Window,text="scan for virus",command=msg)
b.place(x=40,y=80)
Window.mainloop()
