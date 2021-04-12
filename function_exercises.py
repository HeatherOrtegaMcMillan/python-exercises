# ----------- Function Exercises -------------
# 1. Define a function named is_two. 
# It should accept one input and return True if the passed input is either:
#  the number or the string 2, False otherwise.

def is_two(x):
    if x == 2:
        return True
    if x =='2':
        return True
    else:
        return False

# print(is_two(2), is_two('2'), is_two(3)) --- Uncomment to Test

# 2. Define a function named is_vowel. 
# It should return True if the passed string is a vowel, False otherwise.

def is_vowel(string):
    if type(string) != str:
        return None
    if string.lower() in ('a', 'e', 'i', 'o', 'u'):
        return True
    else:
        return False # must put false, otherwise returns 'NONE'

print('------------ is vowel check ---------------')
print('2 is a vowel:', is_vowel(2), '  a is a vowel:', is_vowel('a'), '  t is a vowel:', is_vowel('t'))

# 3. Define a function named is_consonant. 
# It should return True if the passed string is a consonant, False otherwise. 
# Use your is_vowel function to accomplish this.

def is_consonant(thing):
    if type(thing) != str:
        return None
    if is_vowel(thing) == False:
        return True
    else:
        return False

print('------------ is_consonant check -------------')
print('2 is a consonant:', is_consonant(2), '  t is a consonant:', is_consonant('t'))


# 3.  Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the word if the word starts with a consonant.
    # define input
    # check if string
    # RETURN value is the string but capitalized 

def capitalize_consonant(string):
    if type(string) != str: 
        return 'Type error: enter one word string'
    if is_consonant(string[0]) == True:
        return string.capitalize()
    else:
        return string

print('--------- capitalize consonant check -----------')
print('Testinput : word', '   output:', capitalize_consonant('word'))


# 5. Define a function named calculate_tip. 
# It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(tip_percent, bill_total):
    """
    This function takes in the tip percentage (number between 0 and 1), and the total of the bill
    And returns the amount you should tip, rounded to two decimal places. 
    """
    if tip_percent < 0 or tip_percent > 1:
        return None
    else:
        return round((bill_total * tip_percent), 2)

print('------------- calculate_tip check --------------')
print ('Input: .15 tip and 10.50 total. Tip is: ', calculate_tip(.15, 10.50))

# 6. Define a function named apply_discount. 
# It should accept a original price, and a discount percentage, and return the price after the discount is applied.

def apply_discount(orig_price, discount_percent):
    """
    This function takes in the original price, and the discount percentage (number between 0 and 1)
    And returns the price after the discount is applied.
    """
    if discount_percent < 0 or discount_percent > 1:
        return None
    else:
        return round(((discount_percent * orig_price) + orig_price), 2)

print('------------- apply_discount check ---------------')
print('Original Price: 19.99\nDiscount Percent: .20\nPrice after discount is: ', 
        apply_discount(19.99, .20))


# 7. Define a function named handle_commas. 
#  It should accept a string that is a number that contains commas in it as input, 
#  and return a number as output.

def handle_commas(string):
    """
    This function takes a string that is a number that contains commas in it as input 
    and return a number as output.
    """
    if type(string) != str: # <---this check is weak it doesnt check to see if the input will actually work.
        return None
    return int(string.replace(',', ''))

print('--------------- handle_commas check ------------')
print('Input: 12,345\nOutput:', handle_commas('12,345'))

# 8. Define a function named get_letter_grade. 
# It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(grade):
    if 88 <=  grade <= 100:
        return('A')
    elif 80 <= grade <= 87:
        return('B')
    elif 67 <= grade <= 79:
        return('C')
    elif 60 <= grade <= 66:
        return('D')
    elif 0 <= grade <= 59:
        return('F')
print('--------------- get_letter_grade ------------')
print(f'If your grade was 87, your letter grade is {get_letter_grade(87)}')
print(f'If your grade was 100, your letter grade is {get_letter_grade(100)}')

# 9. Define a function named remove_vowels that accepts a string and 
# returns a string with all the vowels removed

def remove_vowels(string):
    new_string = string
    for letter in string:
        if is_vowel(letter) == True:
            new_string = new_string.replace(letter, '')
    return new_string

print('--------------- remove_vowels ------------')
print('Input: this is a test\n Output:', remove_vowels('this is a test'))

# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
    # anything that is not a valid python identifier should be removed
    # leading and trailing whitespace should be removed
    # everything should be lowercase
    # spaces should be replaced with underscores
    # for example:
        # Name will become name
        # First Name will become first_name
        # % Completed will become completed

def normalize_name(string):
    string = string.strip()
    string = string.lower()
    string = string.replace(" ","_")
    for letter in string:
        if letter.isalnum() != False or letter == '_':
            continue
        else:
            string = string.replace(letter, '')
    return string

print('Input:   This is A %$Test  \nOutput:', normalize_name('   This is A %$Test  '))

# 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

    # notes: this is what I wanted my function to do
    # new_list[0] = list_of_numbers[0]
    # new_list[1] = list_of_numbers[1] + new_list[0]
    # new_list[2] = list_of_numbers[2] + new_list[1]
# -------- had the code below in jupyter notebook and it worked. brought it here and didn't work.
# ?????? Why ??????? 
# list_of_numbers = [1, 2, 3]
# new_list[0] = list_of_numbers[0]
# for n in range(1, len(list_of_numbers)):
#   new_list[n] = list_of_numbers[n] + new_list[n-1]
# new_list

def cumulative_sum(list_of_numbers):
    new_list = []
    new_list.append(list_of_numbers[0])
    for n in range(1, len(list_of_numbers)):
        new_list.append(list_of_numbers[n] + new_list[n-1])
    return new_list

print('--------------- cumulative_sum ------------')
print('Test List: [1, 2, 3]\nOutput:', cumulative_sum([1, 2, 3]))


