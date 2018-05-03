'''
Excercise 3
'''

def class_credits(level):
    level = level.lower()
    year = {'freshman' : '0',
            'sophomore' : '30',
            'junior' : '60',
            'senior' : '90'}
    return year[level]

def main():
    class_level = input("What year are you? ")
    credit_min = class_credits(class_level)
    return credit_min

print("You need a minimun of " + main() + " credits.")

    
