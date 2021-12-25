from tkinter import *

window = Tk()
window.title("miles to km calculator")
# window.minsize(width=500, height=300)
window.config(padx=40, pady=20)

equal_label = Label(text="is equal to")
equal_label.grid(column=0,row=1)

start_label = Label(text="0")
start_label.grid(column=1,row=1)

km_label = Label(text="km")
km_label.grid(column=2,row=1)

input = Entry()
input.grid(column=1,row=0)

miles_label = Label(text="miles")
miles_label.grid(column=2,row=0)

def converter():
    text_ = input.get()
    start_label.config(text=int(text_)*1.61)

button = Button(text="Calculate", command=converter)
button.grid(column=1,row=2)

window.mainloop()