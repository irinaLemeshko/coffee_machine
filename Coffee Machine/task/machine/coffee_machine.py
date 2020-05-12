def print_state(water, milk, coffee, cups, money):
    print("The coffee machine has:")
    print(str(water) + " of water")
    print(str(milk) + " of milk")
    print(str(coffee) + " g of coffee beans")
    print(str(cups) + " of disposable cups")
    print(str(money) + " of money")


water = 400
milk = 540
coffee = 120
cups = 9
money = 550
print_state(water, milk, coffee, cups, money)
action = input("Write action (buy, fill, take):")
if action == "buy":
    coffee_type = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:"))
    cups -= 1
    if coffee_type == 1:
        water -= 250
        coffee -= 16
        money += 4
    elif coffee_type == 2:
        water -= 350
        milk -= 75
        coffee -= 20
        money += 7
    else:
        water -= 200
        milk -= 100
        coffee -= 12
        money += 6
elif action == "fill":
    water += int(input("Write how many ml of water do you want to add:"))
    milk += int(input("Write how many ml of milk do you want to add:"))
    coffee += int(input("Write how many grams of coffee beans do you want to add:"))
    cups += int(input("Write how many disposable cups of coffee do you want to add:"))
else:
    print("I gave you $" + str(money))
    money = 0
print_state(water, milk, coffee, cups, money)
