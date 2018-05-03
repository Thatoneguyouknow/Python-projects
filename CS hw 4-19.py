#4-19 CS Homework

print("This program will calculate the mph of a marathon runner")
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

miles = int(26.2)

time = float(hours + (minutes/60) + (seconds/3600))

mph = float(miles/time)
mph = round(mph,3)
mph = str(mph)
print("You need to run " + mph + "mph.")
