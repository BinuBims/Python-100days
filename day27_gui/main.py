from tkinter import *

window = Tk()
window.title("my first GUI program")
window.minsize(width=500, height=300)

my_label = Label(text="im a label", font=("Arial",24,"bold"))
my_label.pack()

def button_clicked():
    my_label.config(text=input.get())

button = Button(text="click me", command=button_clicked)
button.pack()

input = Entry(width=10)
input.pack()
print(input.get())

window.mainloop()