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
}

def redirect():
    input("\nPress enter to return to the main menu.")
    return coffee_machine()

def coffee_machine():

    clearConsole()
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
        print("Menu:")
        item_number = 1
        for beverage in MENU:
            cost = "{:.2f}".format(MENU[beverage]["cost"])
            print(f"{item_number}. {beverage.title()} - ${cost}")
            item_number +=1
        beverage_choice = int(input("What would you like to order (1/2/3)? ").lower())
        if beverage_choice == 1:
            beverage_choice = "espresso"
        elif beverage_choice == 2:
            beverage_choice = "latte"
        elif beverage_choice == 3:
            beverage_choice = "cappuccino"
        else:
            print("Sorry, that is not a valid item!")
            redirect()
        # check if machine has enough resources to make drink
        selected_beverage = MENU[beverage_choice]
        beverage_ingredients = selected_beverage["ingredients"]
        sufficient_resources = True
        for ingredient in beverage_ingredients:
            if beverage_ingredients[ingredient] > resources[ingredient]:
                sufficient_resources = False
                print("Sorry, machine does not have sufficient resources to make that beverage.")
        
        # prompt for money

        # update resources 

        # return change
    elif(machine_action == '2'):
        for resource in resources:
            print(f"{resource.title()}: {resources[resource]}")
        redirect()
    elif(machine_action == '3'):
        print("Bye-bye! (^^)b ")
        exit()
    else: 
        print("Not a valid option.\n")
        redirect()
    

coffee_machine()