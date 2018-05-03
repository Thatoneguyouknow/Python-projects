# 9-3 
class Locks:
    def __init__(self, value):
        if value in range(0, 10):
            self.digit = value
        else:
            print("Please enter a value between 0 and 9")
            value = int(input("Enter value here: "))
        self.open_lock = False
        self.digit = value

    def open(self, value):
        if value == self.digit:
            self.open_lock = True
        else:
            self.open_lock = False
        return self.open_lock

    def change_val(self, value):
        if value in range(0, 10):
            self.digit = value
        else:
            print("Please enter a value between 0 and 9")
            value = int(input("Enter value here: "))
            self.digit = value

# 9-4
class Dig_Lock:
    def __init__(self, val1, val2, val3):
        value = []
        if val1 in range(0, 10):
            value.append(val1)
        else:
            val1 = int(input("Enter value between 0 and 9: "))
            value.append(val1)
        if val2 in range(0, 10):
            value.append(val2)
        else:
            val2 = int(input("Enter value between 0 and 9: "))
            value.append(val2)
        if val3 in range(0, 10):
            value.append(val3)
        else:
            val3 = int(input("Enter value between 0 and 9: "))
            value.append(val3)
        self.open_lock = False
        self.digit = int(str(value[0]) + str(value[1]) + str(value[2]))

    def open(self, value):
        if value == self.digit:
            self.open_lock = True
        else:
            self.open_lock = False
        return self.open_lock

    def change_val(self, val1, val2, val3):
        value = []
        if val1 in range(0, 10):
            value.append(val1)
        else:
            val1 = int(input("Enter value between 0 and 9: "))
            value.append(val1)
        if val2 in range(0, 10):
            value.append(val2)
        else:
            val2 = int(input("Enter value between 0 and 9: "))
            value.append(val2)
        if val3 in range(0, 10):
            value.append(val3)
        else:
            val3 = int(input("Enter value between 0 and 9: "))
            value.append(val3)
        self.open_lock = False
        self.digit = int(str(value[0]) + str(value[1]) + str(value[2]))
