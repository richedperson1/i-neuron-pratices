from tkinter import *


root = Tk()
value = Entry(root)
value.pack()


def click_here():
    val = value.get()
    label = Label(root, text=f'Thank you for {val}')
    label.pack()


rj_button = Button(root, text="Enter your age ", command=click_here)
rj_button.pack()

root.mainloop()
