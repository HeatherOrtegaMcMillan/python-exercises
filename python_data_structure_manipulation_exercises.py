#The following questions reference the students data structure below. Write the python code to answer the following questions:
from statistics import mean
from collections import Counter

students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]
#----------------------------------------------
# How many students are there?
print('How many students are there?')
how_many_students = len(students)
print('There are ', how_many_students, 'students')

#----------------------------------------------
# How many students prefer light coffee? 
# For each type of coffee roast? ----------- come back to this one!! 

#students[0]["coffee_preference"] -- how to access each element of a dictionary in this list
#[student for student in students if student["coffee_preference"] == 'light'] -- creates list of people (dicts) who 
print('\nHow many students prefer light coffee?')
num_of_light_coffee_drinkers = len([student for student in students if student["coffee_preference"] == 'light'])
print('There are ', num_of_light_coffee_drinkers, ' light coffee drinkers')

#----------------------------------------------
# How many types of each pet are there?

#iterate over list of students (dict), iterate over list of pets (dict or list of dict)
#create new list of the different types of pets
    #maybe create a list of all pets, then count the distinct ones
print('\nHow many types of each pet are there?')
pets_ppl_have = [] #initalize list of types of pets
for p in students:   #loop through students
    #print(p['pets'])
    for kind in p['pets']: # loop through pets key 
        # print(kind['species']) # print all pets in the species dicts
        if kind['species'] not in pets_ppl_have: # check to see if pet name is unique
            pets_ppl_have.append(kind['species']) #add it to list of pets
print(pets_ppl_have)
print("There are ", len(pets_ppl_have), " different types of pets")

#----------------------------------------------       
# How many grades does each student have? 
    # 4
# Do they all have the same number of grades?
    # yes they do
print('\nHow many grades does each student have?')
x = 0 # initalize counter for student number for print chekc
for grade in students: #iterate over list and find grades key
    print("student", x , " has ", len(grade['grades']))  #count number of elements in that list
    x += 1
print('Each student has 4 grades')

#----------------------------------------------
# What is each student's grade average?
print('\nWhat is each student\'s grade average?')
for grade in students:
    print(grade['student'],' : ', mean(grade["grades"]))
#----------------------------------------------
# How many pets does each student have?
print('\nHow many pets does each student have?')
for p in students:
    print(p['student'], 'has', end = ' ')
    number_pets = 0        #set counter to 0 for each person
    for kind in p['pets']: #loop through pets dictionaries
        # print(kind['species']) # print out the types of pets they have
        number_pets += 1   #count up how many pets
    print(number_pets, 'pet(s)') # print out the count of pets

#----------------------------------------------
# How many students are in web development? data science?
    # 7 students in web development and 7 in data science

print('\nHow many students are in web development? Data Science?')
# find list of all types of courses
types_of_courses = [c['course'] for c in students] 
# count distinct types in list 
print(Counter(types_of_courses)) # <---- figure out better way to do this!! 

#----------------------------------------------
# What is the average number of pets for students in web development?

#find number of pets for each web development student
# put values in list
# average list
print('\nWhat is the avg number of pets for students in web development?')
web_dev_pets = []
for p in students:
    if p['course'] != 'web development': #if student isn't in web dev, go to next student
        continue
    number_pets = 0        #set counter to 0 for each person
    for kind in p['pets']: #loop through pets dictionaries
        number_pets += 1   #count up how many pets
    web_dev_pets.append(number_pets)
print('the web development students have an average of ',
      round(mean(web_dev_pets), 2), 'pets per student' #print satement and round the mean of list
     )

#----------------------------------------------
# What is the average pet age for students in data science?
# find pets age for all data science students, make list
# use mean to average that list together

print('\nWhat is the average pet age for students in data science?')
pet_ages = [] # initalize list to store ages
for p in students:
    if p['course'] != 'data science':
        continue
    for a in p['pets']:
        pet_ages.append(a['age'])
print("Average pet age for data science students is ", 
      round(mean(pet_ages), 2))

#----------------------------------------------
# What is most frequent coffee preference for data science students?
# find list of coffee preferences of ds students
# do the counter thing again
# there's probably a better way to do this

# What is the least frequent coffee preference for web development students?
print('\nWhat is most frequent coffee preference for data science students?')
coffee_prefs = [] # create list to store prefs
for c in students:
    if c['course'] != 'data science':
        continue
    else:
        coffee_prefs.append(c['coffee_preference'])
# print(coffee_prefs)
#this outputs a list of tuples, ordered most to least
pref_counts = (Counter(coffee_prefs)) 
#this unpacks the first tuple in the list aka the most common element
most_common_roast_type, count = pref_counts.most_common(1)[0] 
print('most frequent coffee preference for data science students is\n', 
      most_common_roast_type, " with ", count, " people prefering that."
     )
# note about .most_common it returns list a list of the items ordered from most common to least.

#----------------------------------------------
# What is the least frequent coffee preference for web development students?
print('\nWhat is the least frequent coffee preference for web development students?')
coffee_prefs_wd = [] # set empty list for coffe preferences for web dev students
for c in students:
    if c['course'] != 'web development':
        continue
    else:
        coffee_prefs_wd.append(c['coffee_preference'])
# print(coffee_prefs_wd)
pref_counts_wd = Counter(coffee_prefs_wd)
# print(pref_counts_wd)
#there are two least common preferences so add those tuples to a list
#use the .most_common()[:-2-1:-1]] to get least. see documentation for clarification
least_common_list = pref_counts_wd.most_common()[:-2-1:-1]
    # print(least_common_list[0])
#unpack each tuple from the least common list
leastcommonwd1, lcwdcounter1 = least_common_list[0]
leastcommonwd2, lcwdcounter2 = least_common_list[1]
print('The least common preferences for the web development students are ',
      leastcommonwd1, ' and ', leastcommonwd2,
      '\nwith ', lcwdcounter1, ' students and ', lcwdcounter2,
      ' students liking those roasts respectively.'
     )   #this is a little redunant but I was practicing 

#----------------------------------------------
# What is the average grade for students with at least 2 pets?
    # find students that have 2 pets
    # find the avg grade for each student with 2 pets
    # find the avg of those avgs (can you just do an average of all of their grades togeher?)
print('\nWhat is the average grade for students with at least 2 pets?')
list_of_grades = [] #create list to hold all the grades 
for s in students:
    if len(s['pets']) >= 2: # at least 2 pet check
        list_of_grades.extend(s['grades']) #had to use extend instead of append to make one big list
print(mean(list_of_grades)) #print average of all grades

#----------------------------------------------
# How many students have 3 pets?
three_pet_ppl = [] #create list to hold names of ppl who have 3 pets
for s in students:
    if len(s['pets']) == 3: # 3 pet check
        three_pet_ppl.append(s['student']) # fill in the list with the names
print("There is ", len(three_pet_ppl), ' person who has 3 pets.',
      '\n And it is: ', three_pet_ppl[0]
     )

#----------------------------------------------
# What is the average grade for students with 0 pets?
    # find people with 0 pets 
    # get their grades in a list
    # average that list 
print('\nWhat is the average grade for students with 0 pets?')
grades_zero_pet_ppl = []
for s in students:
    if len(s['pets']) == 0:
        grades_zero_pet_ppl.extend(s['grades'])
print(round(mean(grades_zero_pet_ppl), 2 ))

#----------------------------------------------
# What is the average grade for web development students? data science students?
print('\nWhat is the average grade for web development students?')
grades_webdev = []
grades_datasci = []
for s in students:
    if s['course'] == 'web development':
        grades_webdev.extend(s['grades'])
    elif s['course'] == 'data science':
        grades_datasci.extend(s['grades'])
    else:
        print('something weird happened')
print(round(mean(grades_webdev), 2), ' is the average grade for web dev students')
print(round(mean(grades_datasci), 2), ' is the average grade for data science students')

#----------------------------------------------
# What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
    #find all grades for dark coffee drinkers
    #find range -- use max() and min()
print('\nWhat is the average grade range for dark coffee drinkers?')
dark_coffee_grades = []
for s in students:
    if s['coffee_preference'] == 'dark':
        dark_coffee_grades.extend(s['grades'])
    else:
        continue
print('The highest grade of dark coffee drinkers is ', max(dark_coffee_grades),
      '\nThe lowest grade of dark coffee drinkers is ', min(dark_coffee_grades)
     )

#----------------------------------------------
# What is the average number of pets for medium coffee drinkers?
print('\nWhat is the average number of pets for medium coffee drinkers?')
    # make list for pet numbers
    # find medium coffee drinkers and add their pet count to the list
    # average that list
med_coffee_pets = []
for s in students:
    if s['coffee_preference'] == 'medium':
        med_coffee_pets.append(len(s['pets']))
print('The average number of pets for medium coffee drinkers is: ', 
       round(mean(med_coffee_pets), 2)
     )


#----------------------------------------------
# What is the most common type of pet for web development students?
    # find web dev students
    # find pet types
common_pets = []
for s in students:
    if s['course'] == 'web development':
        for kind in s['pets']:
            common_pets.append(kind['species'])
pet_totals = Counter(common_pets)
most_common_pet, countp = pet_totals.most_common(1)[0]
print('The most common type of pet among web development students is a ',
       most_common_pet, '. \nThere are ', countp, '.'
     )

#----------------------------------------------
# What is the average name length?
 #I'm gonna use a function for funzies. 
 # create function that counts name chars minus any whitespaces
 # loop through dictionary of names
 # add length to list 
 # averge that list
def len_of_name(full_name):
    letter_count = len(full_name) - full_name.count(' ')
    return letter_count

print('\nWhat is the average name length?')
name_lengths = []
for s in students:
    name_lengths.append(len_of_name(s['student']))
print('The average length of students\' names is: ',
       round(mean(name_lengths), 2))

#----------------------------------------------
# What is the highest pet age for light coffee drinkers?
    # find all pet ages from light coffee drinkers
    # put values in a list
    # use max() to find highest

print('\nWhat is the highest pet age for light coffee drinkers?')

pet_ages =[]
for s in students:
    if s['coffee_preference'] == 'light':
        for pet in s['pets']:
            pet_ages.append(pet['age'])
            
print('The highest pet age for light coffee drinkers is: ', 
       max(pet_ages), 'years old.'
     )