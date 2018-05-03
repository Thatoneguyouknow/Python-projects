# 7-1 CS HW

def pig_translator(string):
    string = string.lower()
    vowels = ["a", "e", "i", "o", "u"]
    pig_list = string.split(" ")
    for i in range(len(pig_list)):
        if pig_list[i][0] in vowels:
            pig_list[i] += "yay"
        else:
            pig_list[i] = pig_list[i][1:] + pig_list[i][0]
            pig_list[i] += "ay"
        pig_list = " ".join(pig_list)
        pig_list = pig_list.split(" ")
    pig_list = " ".join(pig_list)
    print(pig_list)
pig_translator("Today is a nice day")
pig_translator("I can not wait until lunch")
pig_translator("It is about time")
