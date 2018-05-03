#Problem 4-9

print("This program will give you the amount of change for any amount of cents")
print("Change Calculator")
print("=================")
initial = int(input("Enter amount (Cents): "))
if initial >= 100:
    d_cents = initial % 100
    dollars = str(int((initial-d_cents)/100))
    print("You have " + dollars + " dollars.")   
else:
    print("You have 0 Dollars")
    
if d_cents < 100 and d_cents >= 25:
    q_cents = d_cents % 25
    quarters = str(int((d_cents-q_cents)/25))
    print("You have " + quarters + " quarters.")   
else:
    print("You have 0 Quarters")
    
if q_cents < 25 and q_cents >= 10:
    dime_cents = q_cents % 10
    dimes = str(int((q_cents-dime_cents)/10))
    print("You have " + dimes + " dimes.")   
else:
    dime_cents = int(0)
    print("You have 0 Dimes")

if dime_cents < 10 and dime_cents >= 5:
    n_cents = dime_cents % 5
    nickles = str(int((dime_cents-n_cents)/5))
    print("You have " + nickles + " nickles.")   
else:
    n_cents = int(0)
    print("You have 0 Nickles")

if n_cents <5 and n_cents > 0:
    p_cents = n_cents % 1
    pennies = str(int((n_cents-p_cents)))
    print("You have " + pennies + " pennies.")
else:
    print("You have 0 Pennies")
    
