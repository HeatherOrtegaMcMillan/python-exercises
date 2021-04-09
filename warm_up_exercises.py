# Python warm up exercise

truck = "toyota tacoma"
sedan = "hyundai sonata"
sports_car = "lambourgini diablo"

# this was my original idea for the program. changed it to meet requirements
# self imposed BONUS go try and take user input
#make dictionary to hold all the car make and models
#take car input from user (seperate part, do this later)
# car_input = input("Please enter the Make and Model of your car (ex: toyota tacoma: ")

#split string 
name_list = truck.split() 

#create dictionary
type_of_car = {} 
print('--------------Exercise 1 ---------------')
type_of_car["Make"] = name_list[0]
type_of_car["Model"] = name_list[1]
print(type_of_car)

print('--------------Exercise 2 ---------------')
type_of_car["Make"] = name_list[0].capitalize()
type_of_car["Model"] = name_list[1].capitalize()
print(type_of_car)

print('--------------Exercise 3 ---------------')
#initalize list for dictionaries holding car info
all_the_cars = [] 

#add type of car (that holds truck) to list #add dictionary to list of dictionaries
all_the_cars.append(type_of_car)

#add sedan to list of dictionaries (all_the_cars)
name_list = sedan.split()
type_of_car = {}
type_of_car ['Make'] = name_list[0]
type_of_car["Model"] = name_list[1]
all_the_cars.append(type_of_car)

# add sports car to list of dictionaries (all_the_cars)
name_list = sports_car.split()
type_of_car = {}
type_of_car ['Make'] = name_list[0]
type_of_car["Model"] = name_list[1]
all_the_cars.append(type_of_car)

#capitalize all the letters in my new list of cars 
for car in all_the_cars:
    car["Make"] = car["Make"].upper()
    car["Model"] = car["Model"].upper()

for car in all_the_cars:
    [print(key, ":", car[key]) for key in car]


    





