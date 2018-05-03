# Part 1
import math

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

service_level = input("Was your service level bad, mediocre, or good? ").lower()
initial_cost = input("What was each item priced? (item 1, item2, etc): ")
initial_cost = initial_cost.split(",")
initial_cost = [float(i) for i in initial_cost]
initial_cost = sum(initial_cost)

print("Your tip is $" + str(tip(service_level, initial_cost)))

