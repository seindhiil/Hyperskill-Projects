# Write your code here
water = 400#int(input("How many cups of water do you have?"))
milk = 540#int(input("How many cups of milk do you have?"))
beans = 120#int(input("How many grams of beans do you have?"))
coffee_cups = 0#int(input("How many cups do you need? "))
cups = 9
extrawater = 0
extramilk = 0
extrabeans = 0
extracups = 0
lesswater = 0
lessmilk = 0
lessbeans = 0
lesscups = 0
wateradd = 0
milkadd = 0
beansadd = 0
cupsadd = 0
money = 550
waterforcups = coffee_cups * 200
milkforcups = coffee_cups * 50
beansforcups = coffee_cups * 15
coffeeechoice = 0
"""
print("The coffee machine has:")
print(water, " ml of water")
print(milk, " ml of milk")
print(beans, " g of beans")
print(cups, " of disposable cups")
print(money, " of money")
"""
while True:
    print("Write action (buy, fill, take, remaining, and exit):")
    option = input()
    if option == "buy":
        coffeechoice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
        if coffeechoice == "1":
            if water >= 250 and beans >= 16:
                water -= 250
                beans -= 16
                money += 4
                cups -= 1
                """
                print("The coffee machine has:")
                print(water, " ml of water")
                print(milk, " ml of milk")
                print(beans, " g of beans")
                print(cups, " of disposable cups")
                print(money, " of money")
                """
            else:
                print("We don't have the materials for that right now")
        elif coffeechoice == "2":
            if water >= 350 and milk >= 75 and beans >= 20:
                water -= 350
                milk -= 75
                beans -= 20
                money += 7
                cups -= 1
                """
                print("The coffee machine has:")
                print(water, " ml of water")
                print(milk, " ml of milk")
                print(beans, " g of beans")
                print(cups, " of disposable cups")
                print(money, " of money")
                """
        elif coffeechoice == "3":
            if water >= 200 and milk >= 100 and beans >= 12:
                water -= 200
                milk -= 100
                beans -= 12
                money += 6
                cups -= 1
                """
                print("The coffee machine has:")
                print(water, " ml of water")
                print(milk, " ml of milk")
                print(beans, " g of beans")
                print(cups, " of disposable cups")
                print(money, " of money")
                """
        else:
            print("That was not an option.")
    elif option == "fill":
        print("Write how many ml of water do you want to add:")
        wateradd = int(input())
        print("Write how many ml of milk do you want to add:")
        milkadd = int(input())
        print("Write how many grams of coffee beans do you want to add:")
        beansadd = int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        cupsadd = int(input())
        water += wateradd
        milk += milkadd
        beans += beansadd
        cups += cupsadd
        """
        print("The coffee machine has:")
        print(water, " ml of water")
        print(milk, " ml of milk")
        print(beans, " g of beans")
        print(cups, " of disposable cups")
        print(money, " of money")
        """
    elif option == "take":
        print("I gave you ", money, "dollars")
        money = 0
        """
        print("The coffee machine has:")
        print(water, " ml of water")
        print(milk, " ml of milk")
        print(beans, " g of beans")
        print(cups, " of disposable cups")
        print(money, " of money")
        """
    elif option == "remaining":
        print("The coffee machine has:")
        print(water, " ml of water")
        print(milk, " ml of milk")
        print(beans, " g of beans")
        print(cups, " of disposable cups")
        print(money, " of money")
    elif option == "exit":
        exit()

"""
print("For " + str(coffee_cups) + " cups of coffee you will need: ")
print(str(waterforcups) + " ml of water")
print(str(milkforcups) + " ml of milk")
print(str(beansforcups) + " g of coffee beans")
"""
'''
if coffee_cups * 200 + 200 < water and coffee_cups * 50 + 50 < milk and coffee_cups * 15 + 15 < beans:
    extrawater = int((water-200*coffee_cups)/200)
    extramilk = int((milk-50*coffee_cups)/50)
    extrabeans = int((beans-15*coffee_cups)/15)
     extracups = min(extrabeans, extramilk, extrawater)
     print('Yes, I can make that amount of coffee and even ' + str(extracups) + ' more than that')
if coffee_cups * 200 <= water and coffee_cups * 50 <= milk and coffee_cups * 15 <= beans and extracups == 0:
    print('Yes, I can make that amount of coffee')
elif coffee_cups * 200 > water or coffee_cups * 50 > milk or coffee_cups * 15 > beans:
    lesswater = int(water/200)
    lessmilk = int(milk/50)
    lessbeans = int(beans/15)
    lesscups = min(lesswater, lessmilk, lessbeans)
    print('No, I can make only ' + str(lesscups) + ' cup(s) of coffee')
    '''
'''
print('Starting to make a coffee')
print('Grinding coffee beans')
print('Boiling water')
print('Mixing boiled water with crushed coffee beans')
print('Pouring coffee into the cup')
print('Pouring some milk into the cup')
print('Coffee is ready!')
'''
