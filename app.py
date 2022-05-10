from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Fun with Bindings")

# mainframe = ttk.Frame(root, padding="3 3 12 12")

def updateText(event):
    feet.set(feet_entry.get())

feet = StringVar()
feet_entry = ttk.Entry(root, width=7)
feet_entry.bind("<Key>", updateText)
feet_entry.pack()

ttk.Label(root, textvariable=feet).pack()


root.mainloop()