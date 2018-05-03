'''
Chapter 8 worksheet
'''

# Problem 1
# fh = open("cs_desc.txt", "r")
# x = fh.read()
# print(x)

# Problem 2
# fh = open("cs_desc.txt", "r")
# lines = fh.readlines()
# x = lines[2]
# fh.close()

#Problem 3 and 4
#fh = open("cs_desc.txt", "a")
#fh.write("\nCheck out NAU.")
#fh.close()

#fh = open("cs_desc.txt", "r")
#lines = fh.readline()
#x = lines[6]
#fh.close()

#Problem 5
#fh = open("cs_desc.txt", "a")
#x = fh.readline()
#fh.close()

#Problem 6
#fh = open("cs_desc.txt", "w")
#for i in range(3):
#    fh.write(i)
#x = i
#fh.close()

#Problem 7
#fh = open("cs_desc.txt", "r")
#x = fh.readline()
#x = len(x)
#fh.close()

#Problem 9
#fh = open("cs_desc.txt", "r+")
#lines = fh.readlines()
#for i in lines:
#    x = i
#    fh.write(i)
#fh.close()

#Problem 10
fh = open("cs_desc.txt", "r+")
lines = fh.readlines()
for i in range(len(lines)):
    fh.write(str(i))
    print(lines)
x = fh.readline()
fh.close()
