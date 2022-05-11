from tkinter import *
from tkinter.ttk import *
from tkinter import ttk, messagebox

root = Tk()
root.title('Naviagtion App')
root.geometry('500x500')

def goToPageTwo():
    root.destroy()
    import PageTwo


main_frame = ttk.Frame(root, width=500, height=500)
main_frame.pack(padx=5, pady= 5)
main_frame.pack_propagate(False)


navButton = ttk.Button(main_frame, text="Page Two", command = goToPageTwo)
navButton.pack()

root.mainloop()