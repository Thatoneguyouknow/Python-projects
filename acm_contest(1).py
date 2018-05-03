__author__='Dr.Vanderberg'
'''
    Program that helps determine who win the ACM contest.
'''

print("ACM programming contest... ")
# ask user to make an assumption
adam_won = input("Enter T if you think Adam won or F \
if you think he did not.")

# use assumption to determine T/F for other statements
# if Adam won, then the other statement Charles made is false
if adam_won=='T':
    joan_was_second = False
    # set adam_won to a True boolean value
    adam_won = True
# else, if Adam did not win, then the other statement Charles made is true
else:
    joan_was_second = True
    # set adam_won to a False boolean value
    adam_won = False

# if joan_was_second, then we know that 
if joan_was_second == True:
    # linus could not have been second
    linus_was_second = False
    # but this would mean Ada's others statement must be true..
    joan_won = True
# if joan was not second, (which we know if Adam won)
else:
    # then Joan did not win because there is only one winner
    joan_won = False
    # which means the other statement made by Ada must be True
    linus_was_second=True

print("You assumed the statment 'Adam won' was: ", adam_won)
print("This assumption would lead to the following: ")
print("\tThe statement Joan got second is:",joan_was_second)
print("\tThe statement Joan won is: ",joan_won)
print("\tThe statement Linus got second is: ", linus_was_second)

# look for contradiction - joan can't hold two positions
if(joan_was_second and joan_won):
    print("That's impossible, Joan cannot win AND get 2nd.")
    print("You must have guessed incorrectly.")

print("Adam won, Linus was second, and Joan was third.")
