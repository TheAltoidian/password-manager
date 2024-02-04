from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]
    password_list = password_numbers + password_symbols + password_letters

    shuffle(password_list)

    password = "".join(password_list)

    # print(f"Your password is: {password}")
    password_textbox.delete(0,END)
    password_textbox.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_entries():
    website = website_textbox.get()
    login = login_textbox.get()
    password = password_textbox.get()

    filled_fields = True
    if website == "" or login == "" or password == "":
        filled_fields = False
        messagebox.showinfo(title="Empty fields", message="Do not leave any empty fields")

    if filled_fields:
        is_ok = messagebox.askokcancel(title=website, message=f"Email: {login}\nPassword: {password}\nSave?")
        if is_ok:
            line = f"{website} | {login} | {password}\n"
            file = open("data.txt", "a")
            file.write(line)

            website_textbox.delete(0, END)
            website_textbox.focus()
            login_textbox.delete(0, END)
            login_textbox.insert(END, "@gmail.com")
            password_textbox.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_textbox = Entry(width=45)
website_textbox.grid(column=1, row=1, columnspan=2, sticky="EW")
website_textbox.focus()

login_label = Label(text="Email/Username:")
login_label.grid(column=0, row=2)
login_textbox = Entry(width=45)
login_textbox.grid(column=1, row=2, columnspan=2, sticky="EW")
login_textbox.insert(END, "@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_textbox = Entry(width=27)
password_textbox.grid(column=1, row=3, sticky="EW")

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=38, command=save_entries)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
