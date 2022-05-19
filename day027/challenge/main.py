from tkinter import *

window = Tk()
window.title("Mile to Km")
window.minsize(width=200, height=120)
window.config(padx=20, pady=20)


def button_clicked():
    kilometers = float(input_field.get()) * 1.609344
    result.config(text="{:.2f}".format(kilometers))


# Labels
miles = Label(text="Miles.", font=("Arial", 8))
miles.grid(column=2, row=0)
is_equal = Label(text="is equal to", font=("Arial", 8))
is_equal.grid(column=0, row=1)
result = Label(text=0, font=("Arial", 8))
result.grid(column=1, row=1)
km = Label(text="Km", font=("Arial", 8))
km.grid(column=2, row=1)

# Entry
input_field = Entry(width=10)
input_field.grid(column=1, row=0)
input_field.insert(END, string="0")

# Button
my_button = Button(text="Calculate", command=button_clicked)
my_button.grid(column=1, row=2)

window.mainloop()
