# Part 2

import math

def calc_tax(rate_of_tax, meal_price):
    tax = float(initial_cost * tax_rate)
    tax = round(tax, 2)
    if tax%2 == 0:
        return int(tax)
    else:
        return tax

tax_rate = float(input("What is the current tax rate (in decimal format)? ").lower())
initial_cost = input("What was each item priced? (item 1, item2, etc): ")
initial_cost = initial_cost.split(",")
initial_cost = [float(i) for i in initial_cost]
initial_cost = sum(initial_cost)

print("The tax you owe is $" + str(calc_tax(tax_rate, initial_cost)))
