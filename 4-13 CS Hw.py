#4-13 Cs Homework

print("This program will format your date correctly")
date = int(input("Enter a date (yyyymmdd): "))
month_dictionary = {"1": "January",
                    "2": "February",
                    "3": "March",
                    "4": "April",
                    "5": "May",
                    "6": "June",
                    "7": "July",
                    "8": "August",
                    "9": "September",
                    "10": "October",
                    "11": "November",
                    "12": "December"}
year = str(int((date - date % 10000)/10000))
day = int(date % 100)
month = str(int((((date % 10000) - day)/100)))
month = month_dictionary[month]
day = str(day)
print("The date is:\n\
" + month + " " + day + ", " + year)
