from statistics import variance
from tkinter import *
import tkinter.font as Tkfont
import tkinter as tk
def hideLabel():
    mylabel.grid_forget() # if you use .place() then use .place_forget()


def submitEntry():
    print(myentry.get())
    print(myentry1.get())
    print(selected.get())
    print(dropdown_select.get())

def myvalidate():
    #valdiation functions
    print("In validate")
    lent=len(myentry1.get())
    if(lent>1):
        print("In true ")
        return True
    else:
        print("In False")
        return False

    
window=Tk()
window.title("Demo")
window["bg"]="green"
mylabel=Label(
    text="Input name", 
    background="white",borderwidth=2,relief="solid",font=Tkfont.Font(family="Ariel",size=12)) 
#print(Tkfont.families())
mylabel.grid(row=1,column=4) #you can place label using .place(x=,y=) also
#mylabel.place(x=0,y=10)  placing label
#mylabel1=Label(text="HELLO2")
#mylabel1.grid(row=0,column=2)

myentry=Entry()
myentry.grid(row=2,column=4)

mylabel1=Label(
    text="Password", 
    background="white",borderwidth=2,relief="solid",font=Tkfont.Font(size=12)) 
#print(Tkfont.families())
mylabel1.grid(row=3,column=4)
#mylabel1=Label(text="HELLO2")
#mylabel1.grid(row=0,column=2)

myentry1=Entry(validate="focusout",validatecommand=lambda:myvalidate())
myentry1.grid(row=4,column=4)

selected=tk.StringVar()
radio1=tk.Radiobutton(window,text="Male",value="Male",variable=selected)
radio2=tk.Radiobutton(window,text="Female",value="Female",variable=selected)
mybutton=Button(text="Submit",command=lambda: submitEntry())
radio1.grid(row=5,column=4)
radio2.grid(row=5,column=5)

options=["Monday","Tuesday","Wednesday"]
dropdown_select=tk.StringVar()
drop=OptionMenu(window,dropdown_select,*options)
drop.grid(row=7,column=4)

mybutton.grid(row=8,column=4)
window.geometry("500x500")
window.mainloop()