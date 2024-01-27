# WWCode 60 Days of Code Challenge

# Day 1 - Create a program that swaps the values of two variables.
# def swap(var1, var2):
#     print('Before Swap')
#     print('-----------')
#     print(f'Var1: {var1}')
#     print(f'Var2: {var2}')
#     print('\nAfter Swap')
#     print('-----------')
#     storeVar1 = var1
#     var1 = var2
#     var2 = storeVar1
#     print(f'Var1: {var1}')
#     print(f'Var2: {var2}')
# swap('Toast', 'French')

# Day 2 - Create a program to calculate the area of a circle given its radius.
# import math
# def area_of_circle(radius):
#     area = math.pi * radius ** 2
#     return f'{area:.2f}'
# print(area_of_circle(5))

# Day3 - Write a function to count the number of vowels in a given string
# string = input('Enter a word: ').lower()
# vowels = ['a', 'e', 'i', 'o', 'u']
# vowel_count = 0
# for vowel in vowels:
#     for letter in string:
#         if letter == vowel:
#             vowel_count += 1
# print(f'{string} has {vowel_count} vowels')

# Day 4 - Write a program to find the sum of all elements in a list.
# import random
# nums_list = []
# for i in range(5):      # created list of random integers
#     random_num = random.randint(0, 50)
#     nums_list.append(random_num)
# sum = 0
# for num in nums_list:
#     sum += num
# print(f'The sum of {nums_list} is {sum}')

# Day 5 - Write a program to find the maximum and minimum values in a list
# import random
# random_list = []
# for i in range(10):
#     random_num = random.randint(0, 12)
#     random_list.append(random_num)
# max = 0
# min = random_list[0]
# for num in random_list:
#     if num >= max:
#         max = num
#     if num <= min:
#         min = num
# print(f'The min and max of {random_list} is {min} and {max}, respectively')

# Day 6 - Write a program to count the occurrences of a specific character in a string.
# char = input('Enter character: ')
# string = 'magnificient'
# count = string.count(char)
# print(f'There are {count} {char}(s) in {string}')

# Day 7 - Write a program to check if a number is positive, negative, or zero
# number = int(input('Enter a number: '))
# if number == 0:
#     print(f'Your number is zero')
# elif number > 0:
#     print(f'Your number is positive')
# else:
#     print('Your number is negative')

# Day 8 - Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it.
# def upper_or_lower(string):
#     lower_case = 'abcdefghijklmnopqrstuvwxyz'
#     lower_case_count = 0
#     upper_case_count = 0
#     for letter in string:
#         for char in lower_case:
#             if letter == char:
#                 lower_case_count += 1
#             elif letter == char.upper():
#                 upper_case_count += 1
#     print(f'{string} has {upper_case_count} uppercase letters and {lower_case_count} lowercase latters')
# upper_or_lower('MONGOLIa')

# Day 9 - Write a program to check if a number is even or odd.
# def even_or_odd(num):
#     if num == 0:
#         print('Neither')
#     elif num % 2 == 0:
#         print('Even')
#     else:
#         print('Odd')
# even_or_odd(0)
# even_or_odd(100)
# even_or_odd(25)

# Day 10 - Write a program to remove duplicates from a list.
# duplicates_list = [35, 99, 2, 53, 14, 10, 128, 14, 2]
# # print(dir(duplicates_list))
# duplicates_list.sort()
# print(duplicates_list)
# i = 0
# while i < len(duplicates_list) - 1:
#     if duplicates_list[i] == duplicates_list[i+1]:
#         duplicates_list.pop(i+1)
#     i+= 1
# print(duplicates_list)

# Day 11 - Write a program to print the multiplication table of a given number.
# number = int(input('Enter a number: '))
# for i in range(11):
#     print(f'{number} x {i} = {number * i}')

# Day 12 - Write a program to reverse a given string.
# string = input('Enter a string: ')
# reverse_string = ''
# # print(dir(str))
# for i in range(len(string) - 1, -1, -1):
#     reverse_string += string[i]
# print(reverse_string)

# Day 13 - Write a program to shuffle the elements of a list randomly.
import random
# list = ['hi', 'bye', 'there', 'where', 'dare']
# shuffled_list = []
# while len(list) > 0:
#     random_element = random.choice(list)
#     shuffled_list.append(random_element)
#     list.remove(random_element)
# print(shuffled_list)

# Day 14 - Write a program to print the first n numbers of a Fibonacci sequence.
def fibonacci(n):
    sequence = [0, 1]
    i = 0
    while len(sequence) < n:
        sum = sequence[i] + sequence[i+1]
        sequence.append(sum)
        i += 1
    return sequence
print(fibonacci(10))
