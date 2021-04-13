##### Import Exercises #####


# 1. Import and test 3 of the functions from your functions exercise file. 
# Import each function in a different way:
    # a. Run an interactive python session and import the module. 
    #   Call the is_vowel function using the . syntax.
    # b. Create a file named import_exericses.py. 
    #   Within this file, use from to import the calculate_tip function directly. 
    #   Call this function with values you choose and print the result.
from function_exercises import calculate_tip 
print('------------------------------------------------------------')
print(' ~~ Exercise 1 ~~ ')
print(calculate_tip(.15, 100))

    # c. Create a jupyter notebook named import_exercises.ipynb. 
    #   Use from to import the get_letter_grade function and give it an alias. 
    #   Test this function in your notebook.

# Make sure your code that tests the function imports is run from the same directory that your functions exercise file is in.

# Read about and use the itertools module from the python standard library to help you solve the following problems:
import itertools as it
    # How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
print('------------------------------------------------------------')
print(' ~~ Exercise 2 ~~ ')
countlist = (list(it.product('abc123')))
print(f'there are {len(countlist)} ways to combine abc and 123')

    # How many different combinations are there of 2 letters from "abcd"?
abcdlist = list(it.combinations('abcd', 2))
print(f'there are {len(abcdlist)} different ways to combine 2 letters from ABCD')   

    # How many different permutations are there of 2 letters from "abcd"?
abcdlist = list(it.permutations('abcd', 2))
print(f'there are {len(abcdlist)} different ways to combine 2 letters from ABCD')

# Save this file as profiles.json inside of your exercises directory 
# (right click -> save file as...).

import function_exercises as funx
import function_file as ff
import statistics
from collections import Counter

print('------------------------------------------------------------')
print(' ~~ Exercise 3 ~~ ')

# Use the load function from the json module to open this file.

import json

dict_file = json.load(open('profiles.json'))
# madelines way ---- with open('filepath', 'r')
# as f:
    #profiles (name you want to give your file) = file_ext.load(f)

# 1. Total number of users
total_num_users = len(dict_file)
print(f'The total number of users is {total_num_users}')

# 2. Number of active users
# Find names of keys are in the first dictionary entry
keylist = dict_file[0].keys()
# this is a test to see what the isActive type is (bool), and how it works
dict_file[0].get('isActive')

active_user = [user for user in dict_file if user['isActive'] == True]
active_user_count = len(active_user)
print(f'There are {active_user_count} active users in the database')

# 3. Number of inactive users
inactive_user = [user for user in dict_file if user['isActive'] == False]
inactive_user_count = len(inactive_user)
print(f'There are {inactive_user_count} inactive users in the database')

# 4. Grand total of balances for all users
    # the comments below were my method for testing how to transform string to float
    # ended up creating a function
        # testsubject = dict_file[0].get('balance')
        # testsubject = testsubject.replace('$', '')
        # testsubject = testsubject.replace(',', '')
        # testsubject = float(testsubject)
        # type(testsubject)

all_the_balances = []
for user in dict_file:
    all_the_balances.append(ff.string_money_to_float(user['balance']))
print(f'The grand total of the balances from all users is ${sum(all_the_balances)}')

# 5. Average balance per user
avg_balance_per_user = round(statistics.mean(all_the_balances),2)

print(f'The average balance per user is ${avg_balance_per_user}')

# 6. User with the lowest balance
lowest_balance = min(all_the_balances)
lowest_balance

poor_people = []  # this is in case there's more than 1 poorest person
for user in dict_file:
    temp_balance = ff.string_money_to_float(user['balance'])
    if temp_balance == lowest_balance:
        poor_people.append(user)


print('The person with the lowest balance is ', poor_people[0]['name'])

# 7. User with the highest balance
highest_balance = max(all_the_balances)
highest_balance

richie_rich = []
for user in dict_file:
    if highest_balance == ff.string_money_to_float(user['balance']):
        richie_rich.append(user)
print('The person with the highest balance is', richie_rich[0]['name'])

# 8. Most common favorite fruit
fruit_prefs = [user['favoriteFruit'] for user in dict_file]

fav_fruits_list = Counter(fruit_prefs)

popular_fruit, mpcount = (fav_fruits_list.most_common(1))[0]

print(f'The most common favorite fruit is {popular_fruit}, with {mpcount}, people liking it')

# 9. Least most common favorite fruit
least_popular_fruit, lpcount = (fav_fruits_list.most_common()[:-1-1:-1])[0]

print(f'The least common favorite fruit is {least_popular_fruit}, with {lpcount}, people liking it')

# 10. Total number of unread messages for all users
test_message = dict_file[0]['greeting']

def find_message_number(string):
    for char in string:
        if char.isdigit() == True:
            return int(char)

all_messages = [find_message_number(user['greeting']) for user in dict_file]

print(f'The total nubmer of messages for all users is {sum(all_messages)}')







