from tkinter import *
from tkinter.ttk import *
from tkinter import ttk, messagebox
from TreeviewDatabase import Database

root = Tk()
root.title('Database App')
root.geometry('750x500')

main_frame = ttk.Frame(root, width=800, height=500)
main_frame.pack(padx=5, pady= 5)
main_frame.pack_propagate(False)

db = Database('Student.db')

def populateTreeview():
    records = db.queryAll()
    my_tree.delete()
    # Add our data to the screen
    global count
    count = 0
    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4]), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4]), tags=('oddrow',))
		# increment counter
        count += 1

def select(e):
    clear()
    # Grab record Number
    selected = my_tree.focus()
	# Grab record values
    values = my_tree.item(selected, 'values')
    # outpus to entry boxes
    id_entry.insert(0, values[0])
    fn_entry.insert(0, values[1])
    ln_entry.insert(0, values[2])
    age_entry.insert(0, values[3])
    email_entry.insert(0, values[4])

def insert():
    db.insertEntry(
       {
			'first_name': fn_entry.get(),
			'last_name': ln_entry.get(),
			'id': id_entry.get(),
			'age': age_entry.get(),
			'email': email_entry.get(),
		} 
    )
    clear()
    messagebox.showinfo("Insertion Successful!", "Your Record Has Been Inserted!")
    populateTreeview()
    

def update():
    # Grab the record number
    selected = my_tree.focus()
	# Update record
    my_tree.item(selected, text="", values=(id_entry.get(), fn_entry.get(), ln_entry.get(), age_entry.get(), email_entry.get()))
    db.updateEntry(
        {
            'first_name': fn_entry.get(),
            'last_name': ln_entry.get(),
            'age': age_entry.get(),
            'email': email_entry.get(),
            'id': id_entry.get()
        }
    )
    clear()
    messagebox.showinfo("Updation Successful!", "Your Record Has Been Updated!")

def delete():
    x = my_tree.selection()
    

    db.deleteEntry(
        {
            'id': id_entry.get()
        }
    )
	# Clear The Entry Boxes
    clear()
    my_tree.delete(x)

	# Add a little message box for fun
    messagebox.showinfo("Deleted!", "Your Record Has Been Deleted!")

def clear():
    # Clear entry boxes
	fn_entry.delete(0, END)
	ln_entry.delete(0, END)
	id_entry.delete(0, END)
	age_entry.delete(0, END)
	email_entry.delete(0, END)



style = ttk.Style()
style.theme_use('default')

style.configure(
    "Treeview",
    background="#D3D3D3",
	foreground="black",
	rowheight=25,
	fieldbackground="#D3D3D3"
)

style.map(
    'Treeview',
	background=[('selected', "#347083")]
    )

# Treeview Frame
tree_frame = ttk.Frame(main_frame)
tree_frame.pack(pady=10)


# Create a Treeview Scrollbar
tree_scroll = ttk.Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create The Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack(fill="x", expand="yes",)

# Configure the Scrollbar
tree_scroll.config(command=my_tree.yview)

# Define Our Columns
my_tree['columns'] = ("ID", "First Name", "Last Name", "Age", "Email")

# Format our columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("ID", anchor=W, width=140)
my_tree.column("First Name", anchor=W, width=140)
my_tree.column("Last Name", anchor=W, width=140)
my_tree.column("Age", anchor=W, width=140)
my_tree.column("Email", anchor=W, width=140)

# Create headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("ID", text="ID", anchor=W)
my_tree.heading("First Name", text="First Name", anchor=W)
my_tree.heading("Last Name", text="Last Name", anchor=W)
my_tree.heading("Age", text="Age", anchor=W)
my_tree.heading("Email", text="Email", anchor=W)

# Create Striped Row Tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")


# Add Record Entry Boxes
data_frame = ttk.LabelFrame(main_frame, text="Record")
data_frame.pack(fill="x", expand="yes", padx=20)

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

# Add Buttons
button_frame = ttk.LabelFrame(main_frame, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

add_button = ttk.Button(button_frame, text="Add Record", command=insert)
add_button.grid(row=0, column=0, padx=10, pady=10)

update_button = ttk.Button(button_frame, text="Update Record", command=update)
update_button.grid(row=0, column=1, padx=10, pady=10)

delete_button = ttk.Button(button_frame, text="Delete", command=delete)
delete_button.grid(row=0, column=2, padx=10, pady=10)

clear_button = ttk.Button(button_frame, text="Clear", command=clear)
clear_button.grid(row=0, column=3, padx=10, pady=10)

# Bind the treeview
my_tree.bind("<<TreeviewSelect>>", select)

# Run to pull data from database on start
populateTreeview()

root.mainloop()