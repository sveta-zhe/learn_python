from data import MENU, resources

profit = 0
is_on = True


def resources_enough(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please deposit money")
    total = int(input("How many quarters?: ")) * 0.25
    return total


def successful_result(money_received, drink_cost):
    if money_received >= drink_cost:
        change_money = round(money_received - drink_cost, 2)
        print(f"Here is ${change_money} in change money")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_drink(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is you {drink_name}. Please enjoy!")


while True:
    choice = input("“What would you like? Type espresso, latte or cappuccino?")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffe: {resources['coffe']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if resources_enough(drink["ingredients"]):
            payment = process_coins()
            if successful_result(payment, drink["cost"]):
                make_drink(choice, drink["ingredients"])