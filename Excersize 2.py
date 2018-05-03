'''
Exercise part 2
'''

def same_list (l1, l2):
     return l1 in l2

list1 = list(input("Input list 1: "))
list2 = list(input("Input list 2: "))

print(same_list(list1, list2))
