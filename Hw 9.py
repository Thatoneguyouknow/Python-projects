""" Messing Around"""

import time
#import tkinter

class soda:

    def __init__(self):
        self.fizzy = True
#        self.with_ice = False
        self.cold = False
        self.fizz = 2
        self.time = 0
        self.parent = ""
        self.name = ""

    def leave_out(self):
        name = self.name
        print("You left the " + name + " out")
        print("The " + name + "'s fizz is gone")
        self.fizz = 0
        self.fizzy = False
        self.cold = False
        return self.fizz

    def refridgerate(self):
        name = self.name
        self.cold = True
        #self.fizzy = True
        print("You put the " + name + " in the fridge\
 it is now cold")
        return self.cold

    def open_soda(self):
        if self.fizz > 0:
            self.fizz -= 1
            self.time += 1
            name = self.name
            print("You opened the " + name)
            print("The " + name + ' is still fizzy')
            self.fizzy = True
        else:
            print("This soda was already open")
        return self.time

    def set_soda_name(self, n):
        self.name = n

    def get_soda_name(self):
        return self.name

    def set_parent(self, p):
        self.parent = p

    def get_parent(self):
        return self.parent
    
    def __eq__(self, other):
        if isinstance(other, soda):
            return ((self.parent == other.parent) and (self.time == other.time))
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
        
def main():
    Coke = soda()
    Coke.set_parent("Coca Cola")
    Coke.set_soda_name("Coke")
    Coke.open_soda()
    Coke.leave_out()
    print()
    Dr_Pepper = soda()
    Dr_Pepper.set_parent("7up")
    Dr_Pepper.set_soda_name("Dr Pepper")
    Dr_Pepper.refridgerate()
    print()
    Sprite = soda()
    Sprite.set_parent("Coca Cola")
    Sprite.set_soda_name("Sprite")
    Sprite.open_soda()
    Sprite.leave_out()
    print()
    print("Are Coke and Sprite equal?")
    print(Coke == Sprite)
    print("Are Coke and Dr Pepper equal?")
    print(Coke == Dr_Pepper)

main()

    #def add_ice(self):
#        self.cold = True
#        self.with_ice = True
#        return self.with_ice

    #root = tkinter.Tk()
    #tkinter.Button(root, text='Open Soda', command=opened).pack()
    #tkinter.Button(root, text='Refridgerate', command=refridgerated).pack()
    #tkinter.Button(root, text='Add Ice', command=add_ice).pack()
    #tkinter.Button(root, text='Leave Out', command=left_out_for_days).pack()
    #root.mainloop()
    
        
