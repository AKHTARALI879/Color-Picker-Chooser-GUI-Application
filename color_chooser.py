from tkinter import *
from tkinter import colorchooser


def clickme():
    color = colorchooser.askcolor()
    print(color)
    color_hex_value = color[1]
    print(color_hex_value)
    csa.config(bg=color_hex_value)


csa = Tk()
csa.geometry("500x500")
csa.title("Color Chooser App")

button = Button(csa, text="Click Me", fg="#2142AB", bg="#0080FF",
                font=("Cooper Black", 20, "bold"), relief=RAISED, command=clickme)
button.place(x=85, y=400, height=50, width=330)
csa.mainloop()
