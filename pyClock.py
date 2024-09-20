from tkinter import *
from tkinter.ttk import *
from time import strftime

# Initialize Tk widget
root = Tk()

# Add Tk widget title
root.title("Clock")

# Define time function  
def time():
    # Convert time tuple to string
    string = strftime("%I:%M:%S %p")
    label.config(text=string)

    # Call function every second
    label.after(1000, time)

# Add label
label = Label(root, font=("ds-digital", 80), background="black", foreground="cyan")

# Pack label
label.pack(anchor="center")

# Call time function
time()

# Call Tk mainloop
root.mainloop()