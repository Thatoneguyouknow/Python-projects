print("This program will tell you if a number is odd or even")

uNumber = int(input("Enter a whole number: "))

is_even = uNumber % 2

if is_even == 0:
    print ("The number is even!")
else:
    print("The number is odd!")
