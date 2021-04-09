print("-------- 1. Conditional Basics --------")


today = input('What day is it today? ') # a. prompt the user for a day of the week
if today.lower() == 'monday': # print out whether the day is Monday or not
    print('it\'s Monday!') 
elif today.lower() == 'saturday' or today.lower() == 'sunday': #print out whether the day is a weekday or a weekend
    print('it\'s the freakin weekend baby!')
else: 
    print('it\'s not Monday :(')

print("-------- 1c. Hours worked exercise --------")
# c. create variables and make up values for
    # the number of hours worked in one week
    # the hourly rate
    # how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. 
# You get paid time and a half if you work more than 40 hours

# formula without overtime condition
hrs_worked_week = input(
                  "How many hours did you work this week? (answer with digits): ")   
hourly_rate = input(
                "How much do you get paid per hour? (answer in whole dollars only): $")
paycheck_amt = int(hourly_rate) * int(hrs_worked_week)
print(f"Your paycheck will be ${paycheck_amt} this week")

print("-------- 1.c Hours worked with overtime --------")
# forumla with overtime condition. All hours (not just the hours over 40) 
# will be charged at time and a half
hrs_worked_week = input(
                  "How many hours did you work this week? (answer with digits): ")
hourly_rate = input(
              "How much do you get paid per hour? (answer in whole dollars only): $")
if int(hrs_worked_week) > 40:
    paycheck_amt = (int(hourly_rate) * 1.5) * int(hrs_worked_week)
else:
    paycheck_amt = int(hourly_rate) * int(hrs_worked_week)
print(f"Your paycheck will be ${paycheck_amt} this week")

print("-------- 2. Loop Basics --------")
print("-------- While Loops --------")
print("-------- Count by 2, to 100 --------")
# Create a while loop that will count by 2's starting with 0 and ending at 100. 
# Follow each number with a new line.
i = 0
while i <= 100:
    print(i)
    i += 2
print("-------- Count backwards by 5 --------")
# Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i >= -10:
    print(i)
    i -= 5
print("-------- Squares starting from 2 --------")
# Create a while loop that starts at 2
# displays the number squared on each line 
# while the number is less than 1,000,000
i = 2
while i <= 1000000:
    print(i)
    i = i ** 2
print("-------- Counts down by 5s from 100 to 5 --------")
# Write a loop that uses print to create the output shown below 
# (counts down by 5s from 100 to 5)
i = 100
while i >= 5:
    print(i)
    i -= 5

print("-------- For loops --------")
# Write some code that prompts the user for a number, 
# then shows a multiplication table up through 10 for that number.
n = input("enter a number: ")
x = int(n)
for i in range(1,11):
    print(x, 'x', i, '=', x*i)
print("-------- Number Pyramid --------")
#ii. Create a for loop that uses print to create the output shown below. 
# (number pyramid)
for n in range (1,10):
    for i in range (n):
        print (n, end="")
    print ()   

print("-------- Skipping number exercise --------")
# i. Prompt the user for an odd number between 1 and 50. 
# Use a loop and a break statement to continue prompting the user if they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
skipdigit = int(input("Type in an odd number between 1 and 50: "))
while skipdigit % 2 == 0 or 0 < skipdigit > 51:
    skipdigit = int(input("invalid input. Please type in an odd number between 1 and 50: "))
for i in range(1, 50, 2):
    if i == skipdigit:
        print("Yikes! Skipping number: ", skipdigit)
        continue
    else:
        print("Here is an odd number: ", i)

print("-------- Counting up to your number exercise --------")
# d. The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)
number = int(input("enter a positive number: "))
while number < 0:
    int(input("I said POSITIVE number: "))
for i in range(number + 1):
    print(i)
print("-------- Counting down from your number exercise --------")
# Write a program that prompts the user for a positive integer. 
# Next write a loop that prints out the numbers from the number the user entered down to 1.
number = int(input("enter a positive number: "))
while number < 0:
    number = int(input("I said POSITIVE number: "))
    if number > 0:
        break
for i in range(number, 0, -1):
    print (i)

print("-------- 3. Fizz buzz --------")
# One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
# Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

#Write a program that prints the numbers from 1 to 100.

# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
        continue
    elif n % 3 == 0:
        print("Fizz")
        continue
    elif n % 5 == 0:
        print("Buzz")
        continue
    else:
        print(n)

print("-------- 4. Display table of powers --------")
n = int(input("Please enter an integer: "))
for i in range(1, n + 1):
    print(i, i ** 2, i ** 3) 
cont = (input("would you like to continue? y/n: "))
while cont.lower().startswith('y'):
    n += 1
    print(n, n ** 2, n **3)
    cont = (input("would you like to continue? y/n: "))

print("-------- 5 Convert given number grades into letter grades --------")
grade = int(input("Enter your grade (number from 0 - 100): "))
if 88 <=  grade <= 100:
    print('A')
elif 80 <= grade <= 87:
    print('B')
elif 67 <= grade <= 79:
    print('C')
elif 60 <= grade <= 66:
    print('D')
elif 0 <= grade <= 59:
    print('F')

print("-------- Bonus: add +/- --------")
# Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+)
grade = int(input("Enter your grade (number from 0 - 100): "))
if 88 <=  grade <= 100:
    print('A', end = '')
    if grade in range(99, 101):
        print('+')
    if grade in range (88, 90):
        print('-')
elif 80 <= grade <= 87:
    print('B', end = '')
    if grade in range (86, 88):
        print('+')
    if grade in range (80, 81):
        print ('-')
elif 67 <= grade <= 79:
    print('C', end = '')
    if grade in range(78, 80):
        print('+')
    if grade in range(67, 69):
        print('-')
elif 60 <= grade <= 66:
    print('D', end = '')
    if grade in range(65, 67):
        print('+')
    if grade in range(60, 62):
        print('-')
elif 0 <= grade <= 59:
    print('F', end = '')

print("-------- 6. Book exercise --------")
# 6. Create a list of dictionaries where each dictionary represents 
# a book that you have read
# Dictionary
books_ive_read = [
    {
        'title': 'Harry Potter and the Sorcerer\'s Stone',
        'author': 'J. K. Rowling',
        'genre': ['fantasy', 'mystery', 'young adult']
    },
    {
        'title': 'Lord of the Rings: Fellowship of the Ring',
        'author': 'J. R. R. Tolkein',
        'genre': ['fantasy', 'adventure']
    },
    {
        'title': 'A Darker Shade of Magic',
        'author': 'V. E. Schwab',
        'genre': ['adult fantasy', 'magic']
    },
    {
        'title': 'Percy Jackson and the Lightning Thief',
        'author': 'Rick Riordan',
        'genre': ['young adult', 'adventure', 'greek mythology']
    },
    {
        'title': 'Twilight',
        'author': 'Stephanie Meyer',
        'genre': ['romance', 'vampire']
    },
    {
        'title': 'The Hunger Games',
        'author': 'Suzanne Collins',
        'genre': ['dystopian fiction', 'young adult', 'adventure']
    }   

]

#Each dictionary in the list should have the keys title, author, and genre 
# Loop through the list and print out information about each book

for book in books_ive_read:
    [print(key, ': ', book[key]) for key in book]
    print('---------')

#Prompt the user to enter a genre, 
# then loop through your books list and print out the titles 
# of all the books in that genre.
genre_search = input("What genre are you looking for: ")
genre_search = genre_search.lower()
count = 0
for book in books_ive_read:
    if genre_search in (book['genre']):
        print(book['title'])
        count += 1 
        continue
if count == 0:
    print(f"no books matching {genre_search} genre in database")
    
