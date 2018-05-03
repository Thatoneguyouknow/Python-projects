#CS 126 5-10

def seconds_since12(time):
    time = time.split(":")
    #splits into list format
    hours = int(time[0])
    minutes = int(time[1])
    sec = int(time[2])
    hours *= 3600
    minutes *= 60
    midnight_sec = hours+minutes+sec
    return midnight_sec

time = input("Enter time in hh:mm:ss format: ")
print(seconds_since12(time))

