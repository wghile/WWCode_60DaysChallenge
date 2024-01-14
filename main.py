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

# Day3 - Write a function to count the number of vowels in a given string
string = input('Enter a word: ').lower()
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_count = 0
for vowel in vowels:
    for letter in string:
        if letter == vowel:
            vowel_count += 1
print(f'{string} has {vowel_count} vowels')

# Day 4 - Write a program to find the sum of all elements in a list.
import random
nums_list = []
for i in range(5):      # created list of random integers
    random_num = random.randint(0, 50)
    nums_list.append(random_num)
sum = 0
for num in nums_list:
    sum += num
print(f'The sum of {nums_list} is {sum}')
    