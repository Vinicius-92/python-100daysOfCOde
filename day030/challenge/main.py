import json
import password_generator
from tkinter import messagebox
from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def get_password():
    generated_pass = password_generator.generate_password()
    password_entry.insert(0, generated_pass)

# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search():
    website_name = site_entry.get()
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
            register = data[website_name.title()]
    except FileNotFoundError:
        messagebox.showinfo(title="Oops!", message="Password file not found.")
    except KeyError:
        messagebox.showinfo(title="Oops!", message="Password does not exists in database.")
    else:
        messagebox.showinfo(title=website_name, message=f"Email: {register['email']}\n "
                                                        f"Password: {register['password']}")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    site_input = site_entry.get().title()
    email_input = email_user_entry.get()
    password_input = password_entry.get()
    if len(site_input) < 1 or len(email_input) < 1 or len(password_input) < 1:
        messagebox.showinfo(title="Oops!", message="Please don't let fields empty!")
    else:
        new_data = {
            site_input: {
                "email": email_input,
                "password": password_input
            }
        }
        try:
            with open("passwords.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("passwords.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("passwords.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
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
site_entry = Entry(width=24)
site_entry.grid(column=1, row=1)
site_entry.focus()
email_user_entry = Entry(width=40)
email_user_entry.grid(column=1, row=2, columnspan=2)
email_user_entry.insert(0, "vinicius92as@gmail.com")
password_entry = Entry(width=24)
password_entry.grid(column=1, row=3)
# Buttons
generate = Button(text="Generate", width=12, command=get_password)
generate.grid(column=2, row=3)
add_password = Button(text="Add", width=38, height=1, command=save)
add_password.grid(column=1, row=4, columnspan=2)
search_btn = Button(text="Search", width=12, height=1, command=search)
search_btn.grid(column=2, row=1)

window.mainloop()
