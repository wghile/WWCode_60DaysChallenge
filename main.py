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
# def fibonacci(n):
#     sequence = [0, 1]
#     if n == 0:
#         return []
#     elif n == 1:
#         return sequence[:1]
#     elif n == 2:
#         return sequence[:2]
#     else:
#         i = 0
#         while len(sequence) < n:
#             sum = sequence[i] + sequence[i+1]
#             sequence.append(sum)
#             i += 1
#         return sequence
# print(fibonacci(10))

# Day 15 - Create a program that checks if a year is a leap year.
# def leap_year_check(year):
#     if year > 0 and year % 4 == 0:
#         print(f'{year} is a leap year')
#     elif year > 0 and year % 4 != 0:
#         print(f'{year} is NOT a leap year')
#     else:
#         print('Error: Please enter a valid year')
# leap_year_check(2024)

# Day 16 - Write a program that counts the frequency of each word in a sentence.
# sentence = input('Enter a sentence: ')
# sentence_list = sentence.split(' ')
# words_dict = dict()
# for word in sentence_list:
#     words_dict[word] = sentence_list.count(word)
# print(words_dict)

# Day 17 - Write a program that capitalizes the first letter of each word in a sentence.
# sentence = input('Enter a sentence: ')
# sentence_list = sentence.split(' ')
# new_sentence = ''
# for i in range(len(sentence_list)):
#     capitalized_word = sentence_list[i].replace(sentence_list[i], sentence_list[i].title())
#     new_sentence += capitalized_word + ' '
# print(new_sentence)

# Day 18 - Create a program to find the largest among three numbers.
# def largest_num(num1, num2, num3):
#     numbers = [num1, num2, num3]
#     numbers.sort()
#     return numbers[2]
# print(largest_num(99, 500, 120))

# Day 19 - Write a function to calculate the factorial of a number.
# def factorial(n):
#     product = 1
#     for i in range(1, n+1):
#         product = product * i
#     return product
# print(factorial(6))

# Day 20 - Write a function that takes a list of numbers and returns a new list containing only the even numbers.
# import random
# random_list = []
# for i in range(10):
#     random_num = random.randint(1, 100)
#     random_list.append(random_num)
# print(random_list)
# even_list = []
# for num in random_list:
#     if num % 2 == 0:
#         even_list.append(num)
# print(f'Even Numbers: {even_list}')

# Day 21 - Create a program to remove a specific element from a set.
# shopping_list = ['blanket', 'towel', 'trash can', 'sofa', 'blender']
# remove_item = input('Enter an item to remove from shopping list: ').lower()
# if remove_item in shopping_list:
#     shopping_list.remove(remove_item)
#     print(shopping_list)
# else:
#     print('Item not found in shopping list')

# Day 22 - Create a program to find the second-largest element in a list.
# import random
# random_list = []
# for i in range(8):
#     random_num = random.randint(1, 25)
#     random_list.append(random_num)
# random_list.sort()
# print(f'The second-largest element of {random_list} is {random_list[-2]}')

# Day 23 - Write a program that checks if a key exists in a dictionary.
# def key_check(dictionary, key):
#     if key in dictionary:
#         return True
#     else:
#         return False
# print(key_check({'hi': 'bye', 'there': 'their'}, 'hi'))

# Day 24 - Write a program to remove vowels from a given string.
# def remove_vowels(string):
#     vowels = 'aeiou'
#     new_string = ''
#     i = 0
#     while i < len(string):
#         if string[i] in vowels:
#             i += 1
#         else:
#             new_string += string[i]
#             i += 1
#     return new_string
# print(remove_vowels('walrus'))

# Day 25 - Create a program to concatenate two lists.
# def concat_lists(list1, list2):
#     return list1 + list2
# print(concat_lists(['there goes my'], ['baby']))

# Day 26 - Create a program that uses a lambda function to square each element of a list.
    # lambda function is an anonymous function
    # syntax: lambda argument(s) : expression
        # invoke function using parenthesis followed by value in parentheses
    # filter(function, iterable) and map(function, iterable)
        # both methods will return an object
# list(map(lambda element : print(element ** 2), [2, 4, 6, 8]))

# Day 27 - Create a program that sorts a list of strings alphabetically.
# list_of_strings = []
# for i in range(3):
#     string = input('Enter a string: ')
#     list_of_strings.append(string)
# list_of_strings.sort()
# print(list_of_strings)

# Day 28 - Create a program that removes the nth element from a list.
# def remove_from_list(n, list):
#     if n < 0 or n >= len(list):
#         return 'Error: please enter valid index'
#     else:
#         list.pop(n)
#         return list
# print(remove_from_list(3, ['chocolate', 'strawberry', 'coconut', 'vanilla bean']))

# Day 29 - Create a function that generates a random number between a given range.
# def random_number(min, max):
#     import random
#     return random.randint(min, max)
# print(random_number(10, 20))

# Day 30 - Create a function that finds the second smallest element in a list.
# def second_smallest(lst):
#     lst.sort()
#     return lst[1]
# print(second_smallest([0, 89, 100, 33, 9, 3, 899]))

# Day 31 - Create a program that checks if a given string is a valid email address.
# email_domains = ['@gmail.com', '@yahoo.com', '@aol.com']
# email = input('What is your email? ')
# def email_check(email=email):
#     domain_start_index = email.find('@')
#     email_domain = email[domain_start_index:]
#     if email_domain in email_domains:
#         print('Valid Email')
#     else:
#         print('Not a Valid Email')
# email_check()

# Day 32 - Create a function that calculates the average of a list of numbers.
# def average(lst):
#     sum = 0
#     for item in lst:
#         sum += item
#     print(sum / len(lst))
# average([1,2,3,6,8])

# Day 33 - Write a test case for a function that checks if a number is prime.
# num = int(input('Enter a number: '))
# def is_prime(num=num):
#     if num == 0 or num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 or num % 9 == 0:
#         return False
#     else:
#         return True

# import unittest
# class TestPrime(unittest.TestCase):
#     def test_is_prime(self):
#         self.assertTrue(is_prime(), f'{num} is NOT prime')
#         self.assertFalse(is_prime(), f'{num} IS prime')
# if __name__ == '__main__':
#     unittest.main()
   
# Day 34 - Write a Python program to merge two dictionaries.
# def merge(dict1, dict2):
#     if type(dict1) != dict or type(dict2) != dict:
#         raise TypeError('Incorrect argument type(s)')
#     else:
#         for key in dict2.keys():
#             dict1[key] = dict2[key]
#         return dict1
# print(merge({1: 2, 2: 3}, {4: 5, 6: 8}))

# Day 35 - Write a simple unit test for a function that adds two numbers.
# def add_nums(num1, num2):
#     return num1 + num2
# import unittest
# class TestSum(unittest.TestCase):
#     def test_sum(self):
#         num1 = int(input('Enter a number: '))
#         num2 = int(input('Enter a number: '))
#         self.assertEqual(add_nums(num1=num1, num2=num2), num1 - num2, msg='Not Equal')
# if __name__ == '__main__':
#     unittest.main()

# Day 36 - Write a Python program to check if two strings are anagrams.
    # anagram = word that can be made from rearranging another word (i.e. cinema and iceman)
# def is_anagram(str1, str2):
#     i = 0
#     while (i < len(str1)):
#         if str1.count(str1[i]) != str2.count(str1[i]):
#             result = f'{str1} and {str2} are NOT anagrams'
#             break
#         else:
#             i += 1
#             result = f'{str1} and {str2} are anagrams'
#     print(result)
# is_anagram('icemun', 'cinema')

# Day 37 - Write a program to iterate through a dictionary and print its keys and values.
# def keys_values(dict1):
#     if type(dict1) != dict:
#         raise TypeError('Input must be a dictionary')
#     else:
#         for key in dict1.keys():
#             print(f'{key}: {dict1[key]}')
# keys_values({'chocolate': 5, 'strawberry': 10, 'mango': 2})

# Day 38 - Write a program to flatten a nested list.
# def flatten_nested_list(lst):
#     flat = []
#     for el in lst:
#         if type(el) == int:
#             flat.append(el)
#         else:
#             for sub_el in el:
#                 flat.append(sub_el)
#     print(flat)
# flatten_nested_list([1, [2, 3], [4, 5, 6]])

# Day 39 - Write a program to find the most common words in a text file.
# with open('Python60_2024/words.txt') as text_file:
#     contents = text_file.read()     # returns a string
# words = contents.split('\n')
# words_dict = {}
# for word in words:
#     words_dict[word] = words.count(word)     # counting the occurrence of each unique word in the text file
# max_value = max(list(words_dict.values()))      # finding the max occurrence = most common word(s)
# common_words = []
# for key in words_dict.keys():
#     if words_dict[key] == max_value:            # finding the word from the max value in dict
#         common_words.append(key)
# print('The most common word(s) in the text file:')
# for word in common_words:
#     print(f' {word}')

# Day 40 - Write a function to find the largest common divisor of two numbers using a function.
# def largest_divisor(num1, num2):
#     i = 1
#     while i <= num1:
#         if num1 % i == 0 and num2 % i == 0:
#             max_divisor = i
#         i += 1
#     print(f'The largest common divisor of {num1} and {num2} is {max_divisor}')
# largest_divisor(25, 35)

# Day 41 - Write a program that uses recursion to generate all permutations of a list.
# import random
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# permutations_list = []
# def permutations(lst):
#     while len(permutations_list) < factorial(len(lst)):
#         if lst not in permutations_list:
#             permutations_list.append(lst)
#         else:
#             permutations(random.sample(lst, k=len(lst)))
# permutations([1,2,3,4])
# for i in range(len(permutations_list)):
#     print(f'{i + 1}) {permutations_list[i]}')

# Day 42 - Write a program that uses a try-except block to handle division by zero.
# def division(num1, num2):
#     try:
#         return num1 / num2
#     except:
#         return 'Can\'t divide by 0'
# print(division(9,0))

# Day 43 - Write a program that removes all whitespaces from a given string.
# def trim_string(string):
#     new_string = ''
#     for el in string:
#         if el != ' ':
#             new_string += el
#     return new_string
# print(trim_string('  Hi there'))

# Day 44 - Write a program that reads an integer from the user and handles invalid inputs
def integer_check(num):
    if type(num) == int:
        return num
    else:
        raise TypeError('Invalid input')
print(integer_check(5))