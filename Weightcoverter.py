from tkinter import *

window = Tk()

def from_kg():

    gram = float(a2.get()) * 1000

    pound = float(a2.get()) * 2.20462


    t1.delete("1.0", END)
    t1.insert(END, gram)

    t2.delete("1.0", END)
    t2.insert(END, pound)


a1 = Label(window, text="Enter the weight in Kg")
a2 = Entry(window, textvariable=StringVar)
a3 = Label(window, text='Gram')
a4 = Label(window, text='Pounds')



t1 = Text(window, height=1, width=20)
t2 = Text(window, height=1, width=20)


b1 = Button(window, text="Convert", command=from_kg)

a1.grid(row=0, column=0)
a2.grid(row=0, column=1)
a3.grid(row=1, column=0)
a4.grid(row=1, column=1)
t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
b1.grid(row=0, column=2)

window.mainloop()
