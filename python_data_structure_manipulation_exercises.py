#The following questions reference the students data structure below. Write the python code to answer the following questions:
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
# How many students are there?
how_many_students = len(students)
how_many_students

# How many students prefer light coffee? For each type of coffee roast?

#students[0]["coffee_preference"] -- how to access each element of a dictionary in this list
#[student for student in students if student["coffee_preference"] == 'light'] -- creates list of people (dicts) who 

num_of_light_coffee_drinkers = len([student for student in students if student["coffee_preference"] == 'light'])
num_of_light_coffee_drinkers

# How many types of each pet are there?

#iterate over list of students (dict), iterate over list of pets (dict or list of dict)
#create new list of the different types of pets
    #maybe create a list of all pets, then count the distinct ones


pets_ppl_have = [] #initalize list of types of pets
for p in students:   #loop through students
    #print(p['pets'])
    for kind in p['pets']: # loop through pets key 
        # print(kind['species']) # print all pets in the species dicts
        if kind['species'] not in pets_ppl_have: # check to see if pet name is unique
            pets_ppl_have.append(kind['species']) #add it to list of pets
print(pets_ppl_have)
print("There are ", len(pets_ppl_have), " different types of pets")
        
# How many grades does each student have? 
    # 4
# Do they all have the same number of grades?
    # yes they do

x = 0 # initalize counter for student number for print chekc
for grade in students: #iterate over list and find grades key
    print("student", x , " has ", len(grade['grades']))  #count number of elements in that list
    x += 1


# What is each student's grade average?
from statistics import mean

for grade in students:
    print(grade['student'], mean(grade["grades"]))

# How many pets does each student have?

for p in students:
    print(p['student'], 'has', end = ' ')
    number_pets = 0        #set counter to 0 for each person
    for kind in p['pets']: #loop through pets dictionaries
        # print(kind['species']) # print out the types of pets they have
        number_pets += 1   #count up how many pets
    print(number_pets, 'pet(s)') # print out the count of pets

# How many students are in web development? data science?
    # 7 students in web development and 7 in data science

from collections import Counter
# find list of all types of courses
types_of_courses = [c['course'] for c in students] 
# count distinct types in list 
print(Counter(types_of_courses)) 

# What is the average number of pets for students in web development?

#find number of pets for each web development student
# put values in list
# average list
from statistics import mean
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

# What is the average pet age for students in data science?
# find pets age for all data science students, make list
# use mean to average that list together

pet_ages = [] # initalize list to store ages
for p in students:
    if p['course'] != 'data science':
        continue
    for a in p['pets']:
        pet_ages.append(a['age'])
print("average pet age for data science students is ", 
      round(mean(pet_ages), 2))

# What is most frequent coffee preference for data science students?
# find list of coffee preferences of ds students
# do the counter thing again
# there's probably a better way to do this

coffee_prefs = [] # create list to store prefs
for c in students:
    if c['course'] != 'data science':
        continue
    else:
        coffee_prefs.append(c['coffee_preference'])
pref_counts = (Counter(coffee_prefs))
print('most frequent coffee preference for data science students is\n', 
      pref_counts.most_common(1)[0])


# What is the least frequent coffee preference for web development students?

# What is the average grade for students with at least 2 pets?

# How many students have 3 pets?

# What is the average grade for students with 0 pets?

# What is the average grade for web development students? data science students?

# What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?

# What is the average number of pets for medium coffee drinkers?

# What is the most common type of pet for web development students?

# What is the average name length?

# What is the highest pet age for light coffee drinkers?