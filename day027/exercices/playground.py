def add(*args):
    result = 0
    for arg in args:
        result += arg
    return result


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


print(calculate(3, add=3, multiply=5))


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")

    def __str__(self):
        return f"{self.make} {self.model} {self.color} {self.seats}"


my_car = Car(make="Nissan", model="GT-R", color="Black", seats=4)
print(my_car)


from tkinter import *

window = Tk()
window.title("My window")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I'm a label.", font=("Arial", 18, "bold"))
my_label.grid(column=0, row=0)

# Alter label
my_label["text"] = "New text"
my_label.config(text="Another new text")


def button_clicked():
    my_label.config(text="Button got clicked.")


def input_update_label():
    my_label.config(text=input_field.get())


# Button
my_button = Button(text="Click me!", command=button_clicked)
my_button1 = Button(text="Update label!", command=input_update_label)
my_button.grid(column=1, row=1)
my_button1.grid(row=0, column=2)

# Entry
input_field = Entry(width=10)
input_field.grid(column=3, row=2)

window.mainloop()
