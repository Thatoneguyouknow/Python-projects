#Problem 4-3

print("This program will calculate the slope of a line")

x_input = int(input("Enter x coordinate: "))
y_input = int(input("Enter y coordinate: "))
y_int = int(input("Enter y intercept: "))

slope = str((y_int-y_input)/(0-x_input))

print("The slope is " + slope)
