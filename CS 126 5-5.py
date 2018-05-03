#CS 126 5-5, last digit equalizer


def same_last_digit(number1, number2, number3):
    number1 %= 10
    number2 %= 10
    number3 %= 10
    if number1 == number2 and number2 == number3:
        return True
    else:
        return False

first_number = abs(int(input("Please enter your first number: ")))
second_number = abs(int(input("Please enter your second number: ")))
third_number= abs(int(input("Please enter your third number: ")))

print(same_last_digit(first_number, second_number, third_number))


    
    
    
