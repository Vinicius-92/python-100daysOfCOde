import art
from coffee_machine_db import MENU, resources,  cashier


def verify_resources(coffee_type):
    coffee = MENU[coffee_type]
    if coffee["ingredients"]["water"] > resources["water"]:
        print("Sorry there is no enough water.")
        return False
    elif coffee["ingredients"]["milk"] > resources["milk"]:
        print("Sorry there is no enough milk.")
        return False
    elif coffee["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is no enough coffee.")
        return False
    return True


def debit_resources(coffee_type):
    coffee = MENU[coffee_type]
    resources["water"] -= coffee["ingredients"]["water"]
    resources["milk"] -= coffee["ingredients"]["milk"]
    resources["coffee"] -= coffee["ingredients"]["coffee"]


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Milk: {resources['coffee']}g")
    print(f"Money: ${cashier['money']}")
    wait_restart()


def wait_restart():
    get = input("Press any button to start make make choose again.")
    get_coffee()


def get_money(coffee_type):
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    total = (quarters * 0.25) + (nickles * 0.05) + (dimes * 0.10) + (pennies * 0.01)
    if total < MENU[coffee_type]["cost"]:
        print(total)
        print(MENU[coffee_type]["cost"])
        print("Sorry that's not enough money. Money refunded.")
        wait_restart()
    else:
        print(f"Here is ${'{:.2f}'.format(total - MENU[coffee_type]['cost'])} in change.")
        cashier["money"] += (total - (total - MENU[coffee_type]['cost']))


def get_coffee():
    print(art.logo)
    chosen_type = input("What would you like? (espresso/latte/cappuccino):")
    make_drink = True
    if chosen_type == "report":
        report()
    elif chosen_type == "off":
        exit()
    else:
        make_drink = verify_resources(chosen_type)
    if not make_drink:
        wait_restart()
    get_money(chosen_type)
    debit_resources(chosen_type)
    print(f"Here is your {chosen_type} ☕. Enjoy.")
    get_coffee()


get_coffee()
