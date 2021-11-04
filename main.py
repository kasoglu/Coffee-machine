from data import MENU, resources

profit = 0


def report():
    """ Print report the current resource values."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Profit: ${profit}")


def is_item_sufficient(order_ingredients):
    """ Returns True when order can be made, False if ingredients are insufficient. """

    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, There is not enough {item} to make a coffee.")
            return False
    return True


machine_on = True


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


def process_payment():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, coffee_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= coffee_cost:
        change = round(money_received - coffee_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += coffee_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

# Process the machine unless manufacturer turns off the machine.


while machine_on:
    customer_choice = input("What would you like to drink? (espresso/latte/cappuccino): ")
    if customer_choice == "espresso" or customer_choice == "latte" or customer_choice == "cappuccino":
        coffee = MENU[customer_choice]
        if is_item_sufficient(coffee["ingredients"]):
            payment = process_payment()
            if is_transaction_successful(payment, coffee["cost"]):
                make_coffee(customer_choice, coffee["ingredients"])
    elif customer_choice == "turnoff":
        machine_on = False
    elif customer_choice == "report":
        report()
    else:
        print("Please, try again later.") 




