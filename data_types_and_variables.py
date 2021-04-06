data_types_and_variables.py

# You have rented some movies for your kids: 
# The little mermaid (for 3 days), 
# Brother Bear (for 5 days, they love it) 
# Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?

mermaid = 3
bear = 5
hercules = 1
movies = [mermaid, bear, hercules]
cost = 3 
cost_per_movie = [movie * cost for movie in movies]
total_cost = sum(cost_per_movie)
print (total_cost)


