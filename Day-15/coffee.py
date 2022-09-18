from data import MENU, resources

money = 0
flag = True

while flag != False:
    decide = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    def report():
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    
    if decide == "report":
        report()
    
    if decide == "off":
        break
         
#For espresso
    water_esp = MENU["espresso"]["ingredients"]["water"]
    coffee_esp = MENU["espresso"]["ingredients"]["coffee"]
    def espresso():
        if resources["water"] > water_esp and resources["coffee"] > coffee_esp:
            return True
        elif resources["water"] < water_esp:
            print("Sorry there is not enough water")
        elif resources["coffee"] < coffee_esp:
            print("Sorry there is not enough coffee")


#For latte
    water_lat = MENU["latte"]["ingredients"]["water"]
    milk_lat = MENU["latte"]["ingredients"]["milk"]
    coffee_lat = MENU["latte"]["ingredients"]["coffee"]

    def latte():
        if resources["water"] > water_lat and resources["milk"] > milk_lat and resources ["coffee"] > coffee_lat:
            return True
        elif resources["water"] < water_lat:
            print("Sorry there is not enough water")
        elif resources["milk"] < milk_lat:
            print("Sorry there is not enough milk")
        elif resources["coffee"] < coffee_lat:
            print("Sorry there is not enough coffee")
    

    #For Cappucino
    water_cap = MENU["cappuccino"]["ingredients"]["water"]
    milk_cap = MENU["cappuccino"]["ingredients"]["milk"]
    coffee_cap = MENU["cappuccino"]["ingredients"]["coffee"]
    def cappuccino():
        if resources["water"] > water_cap and resources["milk"] > milk_cap and resources ["coffee"] > coffee_cap:
            return True
        elif resources["water"] < water_cap:
            print("Sorry there is not enough water")
        elif resources["milk"] < milk_cap:
            print("Sorry there is not enough milk")
        elif resources["coffee"] < coffee_cap:
            print("Sorry there is not enough coffee")
    
    #If resources are sufficient
    if decide == "espresso":
        if espresso() == True:
            print("Please insert coins.")
            quaters = float(input("How many quaters?: "))
            dimes = float(input("How many dimes?: "))
            penny = float(input("How many pennies?: "))
            nickels = float(input("How many nickles?: "))
    
            penny_conv = (penny * 0.01)
            nick_conv = nickels * 0.05
            dime_conv = dimes * 0.10
            quat_conv = quaters * 0.25
    
            cash_sum = penny_conv + nick_conv + dime_conv + quat_conv
            if cash_sum >= 1.5:
                resources["water"] = resources["water"] - water_esp
                resources["coffee"] = resources["coffee"] - coffee_esp
                money += 1.5
                change = cash_sum - 1.5
                print(f"Here's ${change} in change")
                print("Here's your espresso ☕. Enjoy!")
            else:
                print("Sorry that's not enough. Money refunded")
            
    elif decide == "latte":
        if latte() == True:
            print("Please insert coins.")
            quaters = float(input("How many quaters?: "))
            dimes = float(input("How many dimes?: "))
            penny = float(input("How many pennies?: "))
            nickels = float(input("How many nickles?: "))
    
            penny_conv = (penny * 0.01)
            nick_conv = nickels * 0.05
            dime_conv = dimes * 0.10
            quat_conv = quaters * 0.25
    
            cash_sum = penny_conv + nick_conv + dime_conv + quat_conv
            if cash_sum >= 2.5:
                resources["water"] = resources["water"] - water_lat
                resources["coffee"] = resources["coffee"] - coffee_lat
                resources["milk"] = resources["milk"] - milk_lat
                money += 2.5
                change = cash_sum - 2.5
                print(f"Here's ${round(change, 2)} in change")
                print("Here's your latte ☕. Enjoy!")
            else:
                print("Sorry that's not enough. Money refunded")
    
    elif decide == "cappuccino":
        if cappuccino() == True:
            print("Please insert coins.")
            quaters = float(input("How many quaters?: "))
            dimes = float(input("How many dimes?: "))
            penny = float(input("How many pennies?: "))
            nickels = float(input("How many nickles?: "))
    
            penny_conv = penny * 0.01
            nick_conv = nickels * 0.05
            dime_conv = dimes * 0.10
            quat_conv = quaters * 0.25
    
            cash_sum = penny_conv + nick_conv + dime_conv + quat_conv
            if cash_sum >= 3.0:
                resources["water"] = resources["water"] - water_cap
                resources["coffee"] = resources["coffee"] - coffee_cap
                resources["milk"] = resources["milk"] - milk_cap
                money += 3.0
                change = cash_sum - 3.0
                print(f"Here's ${round(change, 2)} in change")
                print("Here's your cappucino ☕. Enjoy!")
            else:
                print("Sorry that's not enough. Money refunded")
