import Product
import art
print(art.ascii_logo)
# print(Product.Flavour)
#variable
quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01
#global
profit = 0
is_on = True

def Check_resources_sufficient(order_ingredient):
    for item in order_ingredient:
        if(order_ingredient[item] >= Product.resource["ingredient"][item]):
            print(f"there is not enough {item}!")
            return False
    return True

def process_coin():
    """caculate the coin"""
    print("enter the coin you have")
    total = int(input("Number of quaters ")) * quarters
    total += int(input("Number of diimes ")) * dimes
    total += int(input("Number of nickles ")) * nickles
    total += int(input("Number of pennies ")) * pennies
    return total

def is_transaction_successful(money_receive, drink_cost):
    if(money_receive >= drink_cost):
        change = round(money_receive - drink_cost,2)
        print(f"money in change = {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("there is not enough money!")
        return False

def make_coffee(drink, resource):
    """make coffee and deduct the ingredient"""
    print("here is your coffe ☕")
    for item in drink:
        resource["ingredient"][item] -= drink[item]

while is_on:
    order = input("What would you like? (epressor/latte/cappuccino)? ")
    if(order == "off"):
        print("shutting down machine...")
        is_on = False
    elif order == "report":
        print(f"Water: {Product.resource["ingredient"]["water"]} ml")
        print(f"Milk: {Product.resource["ingredient"]["milk"]} ml")
        print(f"Coffee: {Product.resource["ingredient"]["coffee"]} g")
        print(f"Money: {profit} $")
    else:
        drink = Product.Menu[order]
        if Check_resources_sufficient(drink["ingredient"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink["price"]):
                make_coffee(drink=drink["ingredient"], resource=Product.resource)

