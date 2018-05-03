def f_m_l(long_list):
    print(long_list[0])
    long_list.reverse()
    print(long_list[0])
    x = int(len(long_list)/2)
    return long_list[x]

def reverse_str(literal):
    length = len(literal)
    literal = literal[::-1]
    return literal.replace("", " ")[1: -1]

def roman_numeral(number):
    numerals = {1: "I",
                2: "II",
                3: "III",
                4: "IV",
                5: "V",
                6: "VI",
                7: "VII",
                8: "VIII",
                9: "IX",
                10: "X",
                20: "XX",
                30: "XXX",
                40: "XL",
                50: "L",
                60: "LX",
                70: "LXX",
                80: "LXXX",
                90: "XC",
                100: "C"}
    tens = number - (number % 10)
    print(tens)
    numerals[tens]
    ones = number % 10
    print(ones)
    numerals[ones]
    return numerals[tens] + numerals[ones]

def main():
    beginning = input("Input starting time in HH:MM format: ")
    time_length = input("Input length of time in HH:MM format: ")
    ending_time(beginning, time_length)
    
    
def ending_time(start, length):
    start = start.split(":")
    length = length.split(":")
    hours = int(start[0]) + int(length[0])
    minutes = int(start[1]) + int(length[1])
    hours = hours % 24
    minutes = minutes % 60
    if minutes % 10 > 0:
        minutes = "0" + str(minutes)
    else:
        minutes = minutes
    print(str(hours) + ":" + str(minutes))

print(main())
