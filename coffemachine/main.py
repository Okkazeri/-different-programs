from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

if __name__ == "__main__":
    coffee_choice = Menu()
    coffee_machine = CoffeeMaker()
    money_operations = MoneyMachine()

    coffee_made = True
    while coffee_made:
        choice = input(f"What would you like? {coffee_choice.get_items()}: ")
        if choice == 'off':
            coffee_made = False
        coffee_choiced = coffee_choice.find_drink(choice)
        if choice == 'report':
            coffee_machine.report()
            money_operations.report()
        if coffee_choiced:
            if coffee_machine.is_resource_sufficient(coffee_choiced):
                if money_operations.make_payment(coffee_choiced.cost):
                    coffee_machine.make_coffee(coffee_choiced)
