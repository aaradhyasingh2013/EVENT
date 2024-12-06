from tkinter import *
Window= Tk()
Window.title("event handler")
Window.geometry("100x100")
def handle(event):
    print(event.char)
Window.bind("<Key>",handle)
def click(event):
    print("\n the button was clicked")
button= Button(text= "click me")
button.pack()
button.bind("<Button-1>",click)
Window.mainloop()