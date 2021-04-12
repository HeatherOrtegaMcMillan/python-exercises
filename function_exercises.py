# ----------- Function Exercises -------------
# 1. Define a function named is_two. 
# It should accept one input and return True if the passed input is either:
#  the number or the string 2, False otherwise.
# the is_two function takes in a string or a number and returns True if the string or int is = 2
def is_two(x):
    # here we check to see if x is an int and == 2 and return True
    if x == 2:
        return True
    # here we check to see if x is a string and == '2' True
    if x =='2':
        return True
    # anything that does not meet the above conditions means the input was not 2, string or int
    else:
        return False

# print(is_two(2), is_two('2'), is_two(3)) --- Uncomment to Test

# 2. Define a function named is_vowel. 
# It should return True if the passed string is a vowel, False otherwise.

def is_vowel(string):
    """
    takes in a string with a length of 1 (only one letter) outputs True if string is a vowel, False if it's not
    """
    # this is to check the type of the input to make sure it's a string (had None before)
    if type(string) != str:
        return False
    # if the length is more than 1 char long, will return False (had None before)
    if len(string) != 1:
        return False
    # checking the lowercased string to a list of vowels
    if string.lower() in ('a', 'e', 'i', 'o', 'u'):
        return True
    else:
        return False # must put false, otherwise returns 'NONE'

print('------------ is vowel check ---------------')
print('2 is a vowel:', is_vowel(2), '  a is a vowel:', is_vowel('a'), '  t is a vowel:', is_vowel('t'))

# 3. Define a function named is_consonant. 
# It should return True if the passed string is a consonant, False otherwise. 
# Use your is_vowel function to accomplish this.

def is_consonant(string):
    """
    takes in a string with a length of 1 (only one letter), outputs True if it's a consonant, False if it's not
    """
    # this is to check the type of the input to make sure it's a string
    if type(string) != str:
        return None
    # if the length is more than 1 char long, will not work
    if len(string) != 1:
        return None
    # use previous function is_vowel to check reverse
    if is_vowel(string) == False:
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
    """
    Define a function that accepts a string that is a word 
    The function capitalizes the first letter of the word if the word starts with a consonant

    """
    # checks to make sure input is string
    if type(string) != str: 
        return False
    # checks if first letter of string is a consonant then capatlizes word
    if is_consonant(string[0]) == True:
        return string.capitalize()
    # if string doesn't start with consonant, original string is returned
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
    # check to make sure tip_percent is between 0 and 1, if outside of bounds function won't work
    if tip_percent < 0 or tip_percent > 1:
        return None
    # return the calculated tip and round to nearest hundreth 
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
    # check to make sure discount_percent is inbetween 0 and 1, if not function won't do anything for you
    if discount_percent < 0 or discount_percent > 1:
        return None
    # return calculated percentage off added to the original price, rounded to nearest hundreth
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
    # check to make sure input is a string in order to continue
    if type(string) != str: # <---this check is weak it doesnt check to see if the input has numbers in it
        return None
    # remove any commas and cast input as an int
    return int(string.replace(',', ''))

print('--------------- handle_commas check ------------')
print('Input: 12,345\nOutput:', handle_commas('12,345'))

# 8. Define a function named get_letter_grade. 
# It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(grade):
    """
    This function takes a number as input (grade) 
    and returns the letter grade associated with that number (A-F) as a string.
    """
    # below tests are to classify the inputed value (grade). if not in the 0-100 range, returns None
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
    """
    This function takes a string and outputs a string with the vowels removed
    """
    # initalize a new string and set it to = the input string
    new_string = string
    # loop through each letter in the string
    for letter in string:
        # check to see if letter is a vowel (using previously defined function)
        if is_vowel(letter) == True:
            #remove that letter
            new_string = new_string.replace(letter, '')
    #all that should be left are the consonants 
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
    """
    This function takes a string as input, and outputs a new string that is python friendly
    it will remove whitespace and special charachters, lowercase the string, and replace the spaces with _
    """
    # take any whitespaces off of beginning or end
    string = string.strip()
    # change to lowercase
    string = string.lower()
    # replace spaces with _ (must be done before isalnum())
    string = string.replace(" ","_")
    # go through each letter in string
    for letter in string:
        # if letter is an alpha numeric charachter or an _ keep going
        if letter.isalnum() != False or letter == '_':
            continue
        # anything else must be a special charachter so remove it 
        else:
            string = string.replace(letter, '')
    # return 
    return string
print('--------------- normalize_name check ------------')
print('Input:   This is A %$Test  \nOutput:', normalize_name('   This is A %$Test  '))

# 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

    # notes: this is what I wanted my function to do
    # new_list[0] = list_of_numbers[0]
    # new_list[1] = list_of_numbers[1] + new_list[0]
    # new_list[2] = list_of_numbers[2] + new_list[1]
# -------- had the code below in jupyter notebook and it worked. brought it here and didn't work.
# this function is the one I originally had in Jupyter that didn't work because new_list had been defined alread
# and it had been messing me up
 
def cumulative_sum2(list_of_numbers):
    new_list = list_of_numbers # so i fixed it here by setting the new_list equal to the input list so it would have enough indexes
    new_list[0] = list_of_numbers[0]
    for n in range(1, len(list_of_numbers)):
        new_list[n] = list_of_numbers[n] + new_list[n-1]
    return new_list
print('\n--------------- $$$$$ cumulative_sum2 check $$$$$  ------------')
print('Test List: [1, 2, 3]\nOutput:', cumulative_sum2([1, 2, 3]))

def cumulative_sum(list_of_numbers):
    """
    This function takes a list of numbers as input, and outputs a list of numbers 
    where each one is added to the sum of the numbers before
    """
    # create empty list to store new values
    new_list = []
    # add the first value from the inputted list to the new list
    new_list.append(list_of_numbers[0])
    # use n to count from 1 to the length of the list  
    for n in range(1, len(list_of_numbers)):
        #append the new list with the nth index of the list to the n-1th index of the new list
        new_list.append(list_of_numbers[n] + new_list[n-1])
    return new_list

print('--------------- cumulative_sum check ------------')
print('Test List: [1, 2, 3]\nOutput:', cumulative_sum([1, 2, 3]))



# Create a function named twelveto24. 
# It should accept a string in the format 10:45am or 4:30pm 
# and return a string that is the representation of the time in a 24-hour format. 
# Bonus write a function that does the opposite.

# this function checks to see if the time entered is PM 
def pm_check(string):
    """
    function input is a string, checks to see if 'pm' is anywhere in the string
    used in twelveto24() implementation
    """
    if 'pm' in (string):
        return True

# THIS NEEDS WORK TO GET THE PROPER PLACES
def time_to_number(string):
    """
    this function takes string as input and outputs an int
    removes the am/pm/: and converts string to an int
    used in twelveto24() implementation
    """
    # removes am/pm by removing last two elemnts in string, to account for inputs such as 9:40am 10:45am
    string = string[0:-2:]
    # takes out : in the time 
    string = string.replace(':','')
    # converts numbers to int
    return int(string) #<-- leave as string? need to account for 1:00 changing to 0100

def twelveto24(time):
    """
    This function takes time as a string (format: ie HH:MMam or H:MMpm )
    and outputs the same time but in military, as an int
    must use pm_check() and time_to_number() functions
    """
    #check to see if the time is PM
    if pm_check(time) == True:
        #convert the string to a number and add 1200
        return time_to_number(time) + 1200
    elif '12:' in time:
        time = time.replace('12', '00', 1)
        return time_to_number(time)
    else:
        #convert string to number
        return time_to_number(time)
    

