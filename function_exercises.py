# ----- Function Exercises --------
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
        return False
    if string.lower() in ['aeiou']: #<-- have to use a list with IN
        return True
    else:
        return False # must put false, otherwise returns 'NONE'

# print(is_vowel(2), is_vowel('a'))

# Define a function named is_consonant. 
# It should return True if the passed string is a consonant, False otherwise. 
# Use your is_vowel function to accomplish this.

def is_consonant(thing):
    if type(thing) != str:
        return False
    if is_vowel(thing) == True:
        return False

print(is_consonant('a'))