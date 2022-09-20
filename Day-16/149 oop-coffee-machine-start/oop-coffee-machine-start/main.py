from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

flag = True

while flag != False:
    user = input(f"What would you like (espresso/latte/cappuccino): ").lower()
    maker = CoffeeMaker()
    rep = MoneyMachine()
    
    if user == "report":
        maker.report()
        rep.report()
        
    if maker.is_resource_sufficient(user) == True:
    
            