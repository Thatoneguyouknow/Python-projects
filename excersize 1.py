'''
Excercises using Collections #1
'''

def delete_lowest (n1, n2, n3):
    number_list = [n1, n2, n3]
    number_list.sort()
    del number_list[0]
    return number_list

def main():
    num1 = input("Input first number: ")
    num2 = input("Input second number: ")
    num3 = input("Input third number: ")
    any_but_lowest = delete_lowest(num1, num2, num3)
    return any_but_lowest

print(main())
