import smtplib
import datetime as dt

my_email = "vsavgft@gmail.com"
password = "Gftadmin#2021"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="vinicius92as@yahoo.com",
        msg="Subject:Hello\n\nThis is the body."
    )

current = dt.datetime.now()

print(current.year)
print(current.month)
print(current.day)
print(current.weekday())

date_of_birth = dt.datetime(year=1992, month=2, day=14)
print(date_of_birth)
