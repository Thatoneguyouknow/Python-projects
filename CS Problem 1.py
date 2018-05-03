__author__ = 'Benngy Peterson'
__date__ = 'Sep 5 2017'
'''
    Program to determine how long it will take a monkey to climb a tree.
'''

height = int(input("enter the max hieght the monkey must reach: ") )

minutes = height - 2

print ("It will take the monkey" , minutes, "minutes to reach "\
       + str(height) + " feet")
