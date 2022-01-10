from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
my_menu = Menu()

def run_machine():
    machine_on = True

    while machine_on:
        prompt = input("What would you like (espresso/latte/cappuccino)? ").lower()
        if prompt == "off":
            machine_on = False
            return
        elif prompt == "report":
            my_coffee_maker.report()
            my_money_machine.report()
        else:
            drink = Menu.find_drink(my_menu, prompt)
            if my_coffee_maker.is_resource_sufficient(drink):
                if my_money_machine.make_payment(drink.cost):
                    my_coffee_maker.make_coffee(drink)
            else:
                machine_on = False


run_machine()