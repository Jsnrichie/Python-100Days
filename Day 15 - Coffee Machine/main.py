# Make 3 hot flavors - espresso, latte, cappuccino
from menu import MENU, resources


def get_info(coffee):
    item_info = []

    ingredients = MENU[f"{coffee}"]["ingredients"]
    for item in ingredients:
        item_info.append(ingredients[item])
    if len(item_info) == 2:
        item_info.insert(1, 0)

    money_req = MENU[f"{coffee}"]["cost"]
    item_info.append(money_req)

    needed_resources = {}
    index = 0
    for item in resources:
        needed_resources[item] = item_info[index]
        index += 1

    return needed_resources


def get_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def check_resources(item_info):
    for key in resources:
        if key != "money":
            if resources[key] < item_info[key]:
                print(f"Sorry there is not enough {key}.")
                return False

    return True


def process_coins():
    total = 0
    print("Insert coins:")
    quarter_amt = int(input("Quarters: "))
    total += quarter_amt * 0.25
    dime_amt = int(input("Dimes: "))
    total += dime_amt * 0.1

    print(f"You inserted a total of {total}")

    return total


def process_transaction(money_in, money_req):
    if money_in >= money_req:
        if money_in != money_req:
            change = money_in - money_req
            print(f"Here's your change: ${change}")

        resources["money"] += money_req

    else:
        print(f"You don't have enough money, Here's your refund: ${money_in}")


def make_coffee(item_info):
    for key in resources:
        if key != "money":
            resources[key] -= item_info[key]

    print("Here is your latte. Enjoy!")


def coffee_machine():
    prompt = input("What would you like (espresso/latte/cappuccino)? ").lower()
    if prompt == "off":
        return
    elif prompt == "report":
        get_report()
    else:
        item_info = get_info(prompt)
        money_req = item_info["money"]
        print(f"A {prompt} costs a total of ${money_req}")
        # item_info["milk"] = 1000
        # print(item_info)

        if check_resources(item_info):
            money_in = process_coins()
            process_transaction(money_in, money_req)

            # get_report()
            make_coffee(item_info)
            get_report()


coffee_machine()
