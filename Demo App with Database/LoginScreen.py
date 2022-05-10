import tkinter
from tkinter import ttk
from PIL import Image, ImageTk

# Declare the main root frame of the application
root = tkinter.Tk()

# Define properties of the root
root.title("Student Portal App")
root.geometry("600x350")
root.resizable(False, False)

# Define other things

collegeLogo = ImageTk.PhotoImage(Image.open("CollegeLogo.jpg").resize((256, 256)))

# Define the Left and Right Frames and define the style for each frame

appStyle = ttk.Style()
appStyle.configure('new.TFrame', background = "blue")
appStyle.configure('new.TButton', font = ('Helvetica', 10))

logoFrame = ttk.Frame(root, style='new.TFrame', width= 280, height=300)
logoFrame.grid(row = 0, column = 0, padx= 10, pady = 25)
logoFrame.pack_propagate(False)

logoLabel = ttk.Label(logoFrame, image=collegeLogo)
logoLabel.pack(padx= 10, pady=20)

buttonFrame = ttk.Frame(root, style='new.TFrame', width= 280, height=300)
buttonFrame.grid(row=0, column= 1, padx= 10, pady= 25)
buttonFrame.pack_propagate(False)

titleLabel = ttk.Label(buttonFrame, text="DJSCE Student Portal", font=('Helvetica', 15))
titleLabel.pack(pady=10)


openButton = ttk.Button(buttonFrame, text="Open App", width= 90, style='new.TButton')
openButton.pack(padx=10, pady=(100, 10))

# Rum the application main loop
root.mainloop()