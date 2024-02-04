from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_entries():
    line = f"{website_textbox.get()} | {login_textbox.get()} | {password_textbox.get()}\n"
    print(f"line is {line} test")
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

password_button = Button(text="Generate Password", )
password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=38, command=save_entries)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
