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
print ("total cost is:", total_cost)


# Suppose you're working as a contractor for 3 companies: 
# Google, Amazon and Facebook, they pay you a different rate per hour 
# Google pays 400 dollars per hour 
# Amazon 380, and Facebook 350 
# How much will you receive in payment for this week? 
# You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

google = 400
amazon = 380
facebook = 350

paycheck = 10 * facebook + 6 * google + 4 * amazon
print("my paycheck will be ", paycheck, " dollars") 

# A student can be enrolled to a class only if: 
# the class is not full 
# and the class schedule does not conflict with her current schedule

class_full = False
conflicts_with_schedule = False

can_be_enrolled = not class_full and not conflicts_with_schedule
print(can_be_enrolled)

# A product offer can be applied only if people buys more than 2 items 
# and the offer has not expired 
# Premium members do not need to buy a specific amount of products

number_of_items_bought = 3
offer_expired = True
is_premium_member = True

eligible_for_product_offer =  not offer_expired and number_of_items_bought > 2 or is_premium_member 
print(eligible_for_product_offer)


