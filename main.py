from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
coffee_machine_on = True

while coffee_machine_on:
    options = my_menu.get_items()
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "off":
        coffee_machine_on = False
        print("Coffee machine shutting down.")

    elif user_choice == "report":
        my_coffee_maker.report()
        my_money_machine.report()

    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        drink = my_menu.find_drink(user_choice)
        if my_coffee_maker.is_resource_sufficient(drink):
            if my_money_machine.make_payment(drink.cost):
                my_coffee_maker.make_coffee(drink)

    else:
        print("Invalid choice.")
