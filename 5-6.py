#CS 126 5-6

def second_highest(num1,num2,num3):
    numbers = [num1, num2, num3]
    numbers.sort()
    return numbers[1]

first_n = int(input("Enter first number: "))
second_n = int(input("Enter second number: "))
third_n = int(input("Enter third number: "))

print("The seond highest number is " + str(second_highest(first_n,second_n,third_n)))
