# WWCode 60 Days of Code Challenge

# Day 1 - Create a program that swaps the values of two variables.
def swap(var1, var2):
    print('Before Swap')
    print('-----------')
    print(f'Var1: {var1}')
    print(f'Var2: {var2}')
    print('\nAfter Swap')
    print('-----------')
    storeVar1 = var1
    var1 = var2
    var2 = storeVar1
    print(f'Var1: {var1}')
    print(f'Var2: {var2}')
swap('Toast', 'French')

# Day 2 - Create a program to calculate the area of a circle given its radius.
import math
def area_of_circle(radius):
    area = math.pi * radius ** 2
    return f'{area:.2f}'
print(area_of_circle(5))