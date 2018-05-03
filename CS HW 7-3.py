'''
Problem 7-3
'''

num = int(input("input a number: "))

def sum_cubes(n):
    cube = []
    for i in range(1, n+1):
        cube_i = i * i * i
        cube.append(cube_i)
        cube_sum = sum(cube)
        print(cube)
    print(cube_sum)
    
sum_cubes(num)

def cube_sum(n):
    cube = [n * n * n]
    while n > 0:
        n = n -1
        cube.append(n * n * n)
        print(cube)
    cube_sum = sum(cube)
    print(cube_sum)
    
cube_sum(num)
        
        
            
        
