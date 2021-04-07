fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())
    
# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
uppercased_fruits = [fruit.upper() for fruit in fruits]
uppercased_fruits
# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
capitalized_fruits
# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.
def is_vowel(string):
    if string.lower() == "a" or string.lower() == "e" or string.lower() == "i" or string.lower() == "o" or string.lower() == "u":
        return True
    else: 
        return False
def count_vowels(string):
    vowel = 0
    for letter in string:
        if is_vowel(letter) == True:
            vowel += 1
    return vowel   

fruits_with_two_or_more_vowels = [fruit for fruit in fruits if count_vowels(fruit) > 2]
fruits_with_two_or_more_vowels
# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']

fruits_with_only_two_vowels = [fruit for fruit in fruits if count_vowels(fruit) == 2]
fruits_with_only_two_vowels

# Exercise 5 - make a list that contains each fruit with more than 5 characters

fruits_w_more_than_five_chars = [fruit for fruit in fruits if len(fruit) > 5]
fruits_w_more_than_five_chars 

# Exercise 6 - make a list that contains each fruit with exactly 5 characters
fruits_w_five_chars = [fruit for fruit in fruits if len(fruit) == 5]
fruits_w_five_chars

# Exercise 7 - Make a list that contains fruits that have less than 5 characters
fruits_w_less_than_five_chars = [fruit for fruit in fruits if len(fruit) < 5]
fruits_w_less_than_five_chars

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
number_of_chars_in_fruit = [len(fruit) for fruit in fruits]
number_of_chars_in_fruit

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
def has_a(string):
    if 'a' in string.lower():
        return True
    
fruit_has_a = [fruit for fruit in fruits if has_a(fruit) == True]
fruit_has_a

    ## 9 but combined into a single list line
fruit_has_a = [fruit for fruit in fruits if 'a' in fruit.lower()]
fruit_has_a

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
even_numbers = [number for number in numbers if number % 2 == 0]
even_numbers

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers = [number for number in numbers if number % 2 != 0]
odd_numbers

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
positive_numbers = [number for number in numbers if number > 0]
positive_numbers

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
negative_numbers = [number for number in numbers if number < 0]
negative_numbers

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
numbers_w_2_or_more_numerals = [number for number in numbers if len(str(abs(number))) >= 2]
numbers_w_2_or_more_numerals

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
## shows up with every element of the list on a new line
numbers_squared = [n ** 2 for n in numbers]
numbers_squared

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
odd_negative_numbers = [n for n in numbers if n < 0 and n % 2 != 0]
odd_negative_numbers

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 
numbers_plus_5 = [n + 5 for n in numbers]
numbers_plus_5

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        else: 
            return True

prime_numbers = [n for n in numbers if is_prime(n)]
prime_numbers
