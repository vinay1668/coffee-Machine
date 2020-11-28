import sys
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0,
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
    "cost":0,
}



def check_resources(drink):

    if resources['water'] >= MENU[drink]['ingredients']['water'] and resources['milk'] >= MENU[drink]['ingredients']['milk'] and resources['coffee'] >= MENU[drink]['ingredients']['coffee']:
        resources['water'] -= MENU[drink]['ingredients']['water']
        resources['milk'] -= MENU[drink]['ingredients']['milk']
        resources['coffee'] -= MENU[drink]['ingredients']['coffee']
        return True


def transaction(drink):
    print("please insert coins")
    quarters=int(input("How many quarters?: "))
    dimes=int(input("How many dimes?: "))
    nickles=int(input("How many nickles?: "))
    pennies=int(input("How many pennies?: "))

    total_in_dollars=float((quarters*0.25)+(dimes*0.1)+(nickles*0.05)+(pennies*0.01))
    if MENU[drink]['cost'] > total_in_dollars:

        print("Sorry that's not enough money.Money refunded")
    elif MENU[drink]['cost'] == total_in_dollars:
        resources['cost'] += MENU[drink]['cost']
        print(f"Here is your {drink}  Enjoy")
    elif MENU[drink]['cost'] < total_in_dollars:
        change = round(total_in_dollars - MENU[drink]['cost'], 2)
        resources['cost'] += MENU[drink]['cost']
        print(f"Here is ${change} in change\n")
        print(f"Here is your {drink} Enjoy")





def machine_run():
    choice=input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "espresso":
        if check_resources(choice):
            transaction(choice)
        else:
            print("Sorry,there are not enough resources")

    elif choice == "latte":
        if check_resources(choice):
            transaction(choice)
        else:
            print("sorry,there are not enough resources")

    elif choice == "cappuccino":
        if check_resources(choice):
            transaction(choice)
        else:
            print("sorry,there are not enough resources")

    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"Money: {resources['cost']}$")

    elif choice == "off":
        sys.exit()

    machine_run()


machine_run()