# Part 3
import math

def main():
    initial_cost = input("What was each item priced? (item 1, item2, etc): ")
    tax_rate = float(input("What is the current tax rate (in decimal format)? ").lower())
    if_tip = input("Would you like to tip (enter True or False)? ").lower()
    initial_cost = initial_cost.split(",")
    initial_cost = [float(i) for i in initial_cost]
    initial_cost = sum(initial_cost)
    tax = calc_tax(tax_rate, initial_cost)
    if if_tip == "true":
        service_level = input("Was your service level bad, mediocre, or good? ").lower()
        tip_to_pay = tip(service_level, initial_cost)
        total_cost = tax + initial_cost + tip_to_pay
        total_cost = round(total_cost, 2)
        print("Your tip is $" + str(tip_to_pay))
    else:
        total_cost = tax + initial_cost
        total_cost = round(total_cost, 2)
    print("The tax you owe is $" + str(tax))
    return "Your total is $" + str(total_cost)
    

def calc_tax(rate_of_tax, meal_price):
    tax = float(rate_of_tax * meal_price)
    tax = round(tax, 2)
    if tax%2 == 0:
        return int(tax)
    else:
        return tax

def tip(service, meal_price):
    if service == "bad":
        meal_price *= .10
        meal_price = round(meal_price, 2)
        return meal_price
    elif service == "mediocre":
        meal_price *= .15
        meal_price = round(meal_price, 2)
        return meal_price
    elif service == "good":
        meal_price *= .20
        meal_price = round(meal_price, 2)
        return meal_price
    else:
        return "Invalid service level"

print(main())
