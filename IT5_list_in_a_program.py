# IT5 - List in a Program


pets = ["Storm", "Diesel", "Alfie", "JD", "Bailey", "Darcey"]

def count_pets(pets):
    how_many_pets = 0 
    for pet in pets:
        how_many_pets += 1 
    return how_many_pets

total_pets = count_pets(pets)

print(total_pets)


# What are lists? 
# Lists are a ordered data type used to host a collection of data, these can be strings, integers, float or boolean. 

# How can they be used in programming? 
# Lists can be used to store multiples items in a single variable. 

# What is this code doing?
# This code is counting how many pets there are in the list, using the function "count_pets". This function is using
# a for loop to iterate through the list and counting the pets as it goes. Returning the final number. It is then storing
# the result of the function in a variable called "total_pets" which is then printed. 



