#Import necessary libraries
from tkinter import *

#Setting Up a main window
root = Tk()
root.geometry("400x300")
root.title("Denomination Calculator")

#Function to open new (Top Level) window
def topwin():
    #Setting up top window
    top = Toplevel()
    top.geometry("180x100")
    top.title("Top Level")
    #Adding a label widget to the top window
    l2 = Label(top, text="This is a top level window")
    l2.pack()

    top.mainloop()

#Adding a label and button  widget to Root (main) window
l = Label(root, text="This is root window")
btn = Button(root, text="Click here to open another window", command=topwin)

#Arranging widgets
l.pack()
btn.pack()

root.mainloop()