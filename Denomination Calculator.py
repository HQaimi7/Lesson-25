from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Setting up Main Window
root = Tk()
root.title('Denomination Counter')
root.config(bg='light blue')
root.geometry('550x600')

# Adding Image Labels in the Main Window
try:
    upload = Image.open('money.png')

    # Using resize() method
    upload = upload.resize((300, 300))
    image = ImageTk.PhotoImage(upload)

    label = Label(root, image=image, bg='light blue')
    label.place(x=175, y=99)
except FileNotFoundError:
    label = Label(root, text="Image not found", bg='light blue', fg='red', font=('Arial', 12))
    label.place(x=175, y=99)

label1 = Label(root,
               text="Hey User! Welcome to Denomination Counter Application.",
               bg='light blue')
label1.place(relx=0.5, y=340, anchor=CENTER)

# Function to display a messagebox and proceed if OK is clicked
def msg():
    MsgBox = messagebox.showinfo(
        "Alert", "Do you want to calculate the denomination count?")
    if MsgBox == 'ok':
        topwin()

# Adding Buttons to the main window
button1 = Button(root,
                 text="Let's get started!",
                 command=msg,
                 bg='brown',
                 fg='white')
button1.place(x=260, y=360)

# Function for opening new/top window
def topwin():
    top = Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg='light grey')
    top.geometry("600x350+50+50")

    label = Label(top, text="Enter total amount", bg='light grey')
    entry = Entry(top)

    t1_label = Label(top, text="Here are number of notes for each denomination:", bg='light grey')

    l1 = Label(top, text="2000", bg='light grey')
    l2 = Label(top, text="500", bg='light grey')
    l3 = Label(top, text="100", bg='light grey')

    t1_entry = Entry(top)
    t2_entry = Entry(top)
    t3_entry = Entry(top)

    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note2000 = amount // 2000
            note500 = (amount % 2000) // 500
            note100 = ((amount % 2000) % 500) // 100

            # Update the entry fields with calculated values
            t1_entry.delete(0, END)
            t1_entry.insert(0, str(note2000))
            t2_entry.delete(0, END)
            t2_entry.insert(0, str(note500))
            t3_entry.delete(0, END)
            t3_entry.insert(0, str(note100))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")

    #centering the labels and entry fields
    label.place(x=238, y=50)
    entry.place(x=208, y=80)
    btn = Button(top, text="Calculate", command=calculator, bg='blue', fg='white')
    btn.place(x=190, y=120)
    t1_label.place(x=150, y=150)

    l1.place(x=200, y=180)
    l2.place(x=200, y=210)
    l3.place(x=200, y=240)

    t1_entry.place(x=300, y=180)
    t2_entry.place(x=300, y=210)
    t3_entry.place(x=300, y=240)
    
    top.mainloop()

root.mainloop()