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
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def redirect():
    input("Press enter to return to the main menu.")
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

    if(machine_action == '1'):
        print("Here's the menu")
    elif(machine_action == '2'):
        print(resources)
        redirect()
    elif(machine_action == '3'):
        print("Bye-bye! (^^)b ")
        exit()
    else: 
        print("Not a valid option.\n")
        redirect()
    

coffee_machine()