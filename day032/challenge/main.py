import pandas
import random
import smtplib
import datetime as dt

MY_EMAIL = "vsavgft@gmail.com"
PASSWORD = "Gftadmin#2021"
# Preparing files and data
data = pandas.read_csv("birthdays.csv").to_records(index=False)
data_list = []
for record in data:
    data_list.append({"name": record["name"],
                      "email": record["email"],
                      "year": record["year"],
                      "month": record["month"],
                      "day": record["day"]})
letters = []
with open("letter_templates/letter_1.txt") as file:
    letters.append(file.read())
with open("letter_templates/letter_2.txt") as file:
    letters.append(file.read())
with open("letter_templates/letter_3.txt") as file:
    letters.append(file.read())


# Functions
def sendmail(person, email):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=person.get("email"),
            msg=f"Subject:Happy Birthday!\n\n{email}."
        )


def create_letter(name):
    letter = random.choice(letters)
    return letter.replace("[NAME]", birthday_person.get("name"))


def check_birthdays(list_of_data):
    today = dt.datetime.now()
    for item in list_of_data:
        if today.day == item.get("day") and today.month == item.get("month"):
            return item


birthday_person = check_birthdays(data_list)
if birthday_person is not None:
    finished_letter = create_letter(birthday_person.get("name"))
    sendmail(birthday_person, finished_letter)
