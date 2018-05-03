print("This program will tell you the complemetary color")
print("of whichever color you ask it")
user_color = input("enter a color: ")
user_color = user_color.upper()
if user_color == "RED":
    print("Green")
elif user_color == "GREEN":
    print("Red")
elif user_color == "YELLOW":
    print("Violet")
elif user_color == "VIOLET":
    print("Yellow")
elif user_color == "BLUE":
    print("Orange")
elif user_color == "ORANGE":
    print("Blue")
else:
    print("Please recheck your spelling. If you have spelled")
    print("your color correctly, then we do not have the complementary color")
    print("for that yet. Our sincerest apologies")
        
