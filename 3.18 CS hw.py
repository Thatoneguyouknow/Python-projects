print("This program is a tip calculator")

meal_cost = float(input("Enter the price of your meal: "))
service = input("Was your service poor, good, or excellent: ")
service = service.lower()

if service == "excellent":
    meal_cost *= 1.25
    meal_cost = round(meal_cost,2)
    print("Your total price is \n" + str(meal_cost))
elif service == "good":
    meal_cost *= 1.2
    meal_cost = round(meal_cost,2)
    print("your total price is \n" + str(meal_cost))
elif service == "poor":
    meal_cost *= 1.15
    meal_cost = round(meal_cost,2)
    print("your total price is \n" + str(meal_cost))
else:
    print("Please enter a number")
