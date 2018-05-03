print("This program will tell you if a grade is an A, B, C, D, or F")

grade = int(input("Enter a number between 0 and 100 inclusive: "))

if grade >= 90 and grade <= 100:
    print("It's an A!")
elif grade >= 80 and grade < 90:
    print("It's a B!")
elif grade >= 70 and grade < 80:
    print("It's a C!")
elif grade >= 60 and grade < 70:
    print("It's a D!")
elif grade >= 0 and grade < 60:
    print("It's an F!")
else:
    print("You have not put in a valid grade between 0 and 100")
