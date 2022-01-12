import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def redirect(menu):
    input(f"\nPress enter to return to the {menu}.")
    clearConsole()
    print("")
    if menu == "main menu":
        return main_menu()
    elif menu == "beverage menu":
        return order_beverage()

def main_menu():

    
    print(
"""
Available Options: 
1. Order a drink
2. See resources
3. Turn off machine
"""
    )

    machine_action = input("What would you like to do (1/2/3)? ")
    print("")
    
    if(machine_action == '1'):
        return order_beverage()
    elif(machine_action == '2'):
        clearConsole()
        for resource in resources:
            if resource == "water" or resource == "milk":
                print(f"{resource.title()}: {resources[resource]}ml")
            elif resource == "coffee":
                print(f"{resource.title()}: {resources[resource]}g")
            else:
                print(f"{resource.title()}: ${resources[resource]}")

        redirect("main menu")
    elif(machine_action == '3'):
        print("Bye-bye! (^^)b ")
        exit()
    else: 
        print("Not a valid option.\n")
        redirect("main menu")
    

def order_beverage():
    clearConsole()
    print("Menu:")
    item_number = 1
    for beverage in MENU:
        cost = "{:.2f}".format(MENU[beverage]["cost"])
        print(f"{item_number}. {beverage.title()} - ${cost}")
        item_number +=1
    beverage_choice = int(input("\nWhat would you like to order (1/2/3)? ").lower())
    if beverage_choice == 1:
        beverage_choice = "espresso"
    elif beverage_choice == 2:
        beverage_choice = "latte"
    elif beverage_choice == 3:
        beverage_choice = "cappuccino"
    else:
        print("Sorry, that is not a valid item!")
        redirect("beverage menu")
    # check if machine has enough resources to make drink
    selected_beverage = MENU[beverage_choice]
    beverage_ingredients = selected_beverage["ingredients"]
    sufficient_resources = True
    for ingredient in beverage_ingredients:
        if beverage_ingredients[ingredient] > resources[ingredient]:
            sufficient_resources = False
            print("Sorry, machine does not have sufficient resources to make that beverage.")
            redirect("main menu")
    
    # prompt for money
    remaining_cost = selected_beverage["cost"]*100
    while remaining_cost > 0:
        remaining_cost_formatted = "{:.2f}".format(remaining_cost/100)
        print(f"\nPlease pay ${remaining_cost_formatted} to receive your {beverage_choice}.\n")
        remaining_cost -= convert_change()
    #update resources
    for ingredient in beverage_ingredients:
        resources[ingredient] -= beverage_ingredients[ingredient]
    resources["money"] += selected_beverage["cost"]
    print(f"\nHere is your {beverage_choice}. Please enjoy it while its hot! (^^)b")
     # return change
    if remaining_cost < 0:
        remaining_cost = "{:.2f}".format(remaining_cost / 100 * -1)
        print(f"Please do not forget to take your change of ${remaining_cost}.")
    redirect("main menu")

def convert_change():
    print("Enter your change as requested below.\n")
    coins = {
        "quarters": {"amount": 0, "value": 25},
        "dimes": {"amount": 0, "value": 10},
        "nickels": {"amount": 0, "value": 5},
        "pennies":{"amount": 0, "value": 1}
    }
    amount_payed = 0
    for coin in coins:
        try:
            coins[coin]["amount"] = int(input(f"Enter number of {coin}: "))
        except ValueError:
            coins[coin]["amount"] = 0
        amount_payed += coins[coin]["amount"] * coins[coin]["value"]
    return amount_payed


clearConsole()
main_menu()

