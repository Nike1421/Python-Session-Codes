# Import Libraries
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk, messagebox
from TreeviewDatabase import Database

# Define Root Window of App
root = Tk()
root.title('Database App')
root.geometry('750x500')

# Define Main frame of App
main_frame = ttk.Frame(root, width=750, height=500)
main_frame.pack(padx=5, pady= 5)
main_frame.pack_propagate(False)

# Connect with Database

# Define Commands for Button Click
def populateTreeview():
    pass

def insert():
    pass

def select(event):
    pass

def delete():
    pass

def update():
    pass

def clear():
    pass

# Define Style for TreeView

# Define Frame for TreeView
tree_frame = ttk.Frame(main_frame)
tree_frame.pack(pady=10)

# Create Treeview

# Create and configure scrollbar for Treeview

# Define Columns for Treeview

# Format Columns

# Create Headings

# Design our Treeview

# Define frame for our entry boxes
data_frame = ttk.LabelFrame(main_frame, text="Record")
data_frame.pack(fill="x", expand="yes", padx=20)

# Define Entry Boxes and Labels
fn_label = ttk.Label(data_frame, text="First Name")
fn_label.grid(row=0, column=0, padx=10, pady=10)
fn_entry = ttk.Entry(data_frame)
fn_entry.grid(row=0, column=1, padx=10, pady=10)

ln_label = ttk.Label(data_frame, text="Last Name")
ln_label.grid(row=0, column=2, padx=10, pady=10)
ln_entry = ttk.Entry(data_frame)
ln_entry.grid(row=0, column=3, padx=10, pady=10)

age_label = ttk.Label(data_frame, text="Age")
age_label.grid(row=1, column=0, padx=10, pady=10)
age_entry = ttk.Entry(data_frame)
age_entry.grid(row=1, column=1, padx=10, pady=10)

email_label = Label(data_frame, text="Email")
email_label.grid(row=1, column=2, padx=10, pady=10)
email_entry = ttk.Entry(data_frame)
email_entry.grid(row=1, column=3, padx=10, pady=10)

id_label = ttk.Label(data_frame, text="ID")
id_label.grid(row=1, column=4, padx=10, pady=10)
id_entry = ttk.Entry(data_frame)
id_entry.grid(row=1, column=5, padx=10, pady=10)

# Define Frame for Buttons
button_frame = ttk.LabelFrame(main_frame, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

# Define buttons
add_button = ttk.Button(button_frame, text="Add Record", command=insert)
add_button.grid(row=0, column=0, padx=10, pady=10)

update_button = ttk.Button(button_frame, text="Update Record", command=update)
update_button.grid(row=0, column=1, padx=10, pady=10)

delete_button = ttk.Button(button_frame, text="Delete", command=delete)
delete_button.grid(row=0, column=2, padx=10, pady=10)

clear_button = ttk.Button(button_frame, text="Clear", command=clear)
clear_button.grid(row=0, column=3, padx=10, pady=10)

populate_button = ttk.Button(button_frame, text="Refresh", command=populateTreeview)
populate_button.grid(row=0, column=4, padx=10, pady=10)

# Bind to Treeview

# Populate Treeview at the beginning

# Main Loop of App
root.mainloop()
