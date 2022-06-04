import requests

HEADER = {"Authorization": "Basic dmluaWNpdXM6dmluaWNpdXM="}
SHEETY = "https://api.sheety.co/6a545d96b4a5f718b409011d51cc2c35/flightDeals/users"


def get_user_data():
    print("Welcome to Vinicius' Flight Club.")
    print("We find the best flight deals and email to you.")
    print("What is your first name?")
    first_name = input()
    print("What is your last name?")
    last_name = input()
    print("What is your email?")
    email = input()
    print("Type your email again.")
    email_validation = input()
    if email == email_validation:
        print("You're in the club!")
        create_user_in_database(first_name, last_name, email)
    else:
        print("Let's start over, emails mismatch.")
        get_user_data()


def create_user_in_database(first_name, last_name, email):
    user = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email
        }
    }
    response = requests.post(SHEETY, headers=HEADER, json=user)
    response.raise_for_status()


get_user_data()
