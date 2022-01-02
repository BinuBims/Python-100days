from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    n_letters = random.randint(8,10)
    n_numbers = random.randint(2,4)
    n_symbols = random.randint(2,4)

    password_list = [random.choice(letters) for _ in range(n_letters)] + [random.choice(numbers) for _ in range(n_numbers)] + [random.choice(symbols) for _ in range(n_symbols)]
    random.shuffle(password_list)
    password = "".join(password_list)
    
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def password_save():
    websie = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(websie) == 0 or len(password)==0:
        messagebox.showerror(message="please complete all the requiedfields")
    else:

        is_ok = messagebox.askokcancel(title=websie, message="Please confirm and save!")
        if is_ok:
            with open("data.txt", mode="a") as data_file:
                data_file.writelines(f"{websie} | {email} | {password}\n")
            
        website_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()
        email_entry.insert(0, "binu@gmail.com")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2,column=0)
password_label = Label(text="Password")
password_label.grid(row=3, column=0)


#Entries
website_entry = Entry(width=36)
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=36)

email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "binu@gmail.com")
password_entry = Entry(width=18)
password_entry.grid(row=3, column=1)

#buttons
password_button = Button(text="Generate Password",width=14, command=password_generator)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=25, command = password_save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
