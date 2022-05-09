from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
is_on = True


def coffee():
    while is_on:
        chosen_option = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if chosen_option == "report":
            coffee_maker.report()
            money_machine.report()
            coffee()
        elif chosen_option == "off":
            exit()
        else:
            drink = menu.find_drink(chosen_option)
        if drink is None:
            coffee()
        have_resources = coffee_maker.is_resource_sufficient(drink)
        if not have_resources:
            coffee()
        payment_ok = money_machine.make_payment(drink.cost)
        if not payment_ok:
            coffee()
        coffee_maker.make_coffee(drink)
        coffee()


coffee()
