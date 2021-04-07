data_types_variables_exercises.py

type(99.9)
# float

type("False")
# str

type(False)
# bool

type('0')
# str

type(0)
# int

type(True)
# bool

type("True")
# str

type([{}])
# list

type({'a': []})
# dict

# A term or phrase typed into a search box? - string
# If a user is logged in? - bool
# A discount amount to apply to a user's shopping cart? - int
# Whether or not a coupon code is valid? - bool
# An email address typed into a registration form? - string
# The price of a product? - decimal or int
# A Matrix? - list of lists
# The email addresses collected from a registration form? - list
# Information about applicants to Codeup's data science program? - list of lists
#
'1' + 2
# error

6 % 4
# 2
type(6 % 4)
# int
type(type(6 % 4))
# type

'3 + 4 is ' + 3 + 4
#type error because you can't add a string and ints like that

0 < 0
# False

'False' == False
# False
True == 'True'
# False

5 >= -5
# True

True or "42"
# True 
# when using a bool with or, it returns the first True value
# EX: print(list[]) or oopsie if the list is empty, thats false, so it will return the next thing 

6 % 5
# 1

5 < 4 and 1 == 1
# False
'codeup' == 'codeup' and 'codeup' == 'Codeup'
# False

4 >= 0 and 1 !== '1'
#invalid syntax: there's too many equal signs
4 >= 0 and 1 != '1'
# True

6 % 3 == 0
#True

5 % 2 != 0
#True 
[1] + 2
# Type error: can't join list to int
[1] + [2]
# [1, 2]
[1] * 2
#[1, 1] multiplies list by 2
[1] * [2]
# error, can't multiply a list by a list

[] + [] == []
#True

{} + {}
# you can't add dictionaries



