from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

flag = True

while flag != False:
    user = input(f"What would you like (espresso/latte/cappuccino): ").lower()
    
    if user == "report":
        maker = CoffeeMaker()
        maker.report()
        rep = MoneyMachine()
        rep.report()
    
            