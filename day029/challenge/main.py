from tkinter import *
from tkinter import messagebox
import password_generator
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def get_password():
    generated_pass = password_generator.generate_password()
    password_entry.insert(0, generated_pass)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    site_input = site_entry.get()
    email_input = email_user_entry.get()
    password_input = password_entry.get()
    if len(site_input) < 1 or len(email_input) < 1 or len(password_input) < 1:
        messagebox.showinfo(title="Oops!", message="Please don't let fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=site_input,
                                       message=f"These are the details entered: \nEmail: {email_input} "
                                               f"\nPassword: {password_input} \nIs it ok to save?")
        if is_ok:
            with open("passwords.txt", "a") as file:
                file.write(f"{site_input},{email_input},{password_input}\n")
            site_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# Labels
website = Label(text="Website")
website.grid(column=0, row=1)
email_username = Label(text="Email/Username")
email_username.grid(column=0, row=2)
password = Label(text="Password")
password.grid(column=0, row=3)
# Image
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)
# Entries
site_entry = Entry(width=40)
site_entry.grid(column=1, row=1, columnspan=2)
site_entry.focus()
email_user_entry = Entry(width=40)
email_user_entry.grid(column=1, row=2, columnspan=2)
email_user_entry.insert(0, "vinicius92as@gmail.com")
password_entry = Entry(width=24)
password_entry.grid(column=1, row=3)
# Buttons
generate = Button(text="Generate", width=12, command=get_password)
generate.grid(column=2, row=3)
add_password = Button(text="Add", width=36, height=1, command=save)
add_password.grid(column=1, row=4, columnspan=2)

window.mainloop()
