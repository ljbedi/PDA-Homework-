# IT6 - Dictionary in a Program

top_5_places = {
    "Iceland": 3,
    "South Africa": 4,
    "Taiwan": 1,
    "Japan": 2,
    "Phillipines" : 5
}

def where_is_iceland_on_list(top_5_places):
    for place in top_5_places:
        where_is_iceland = min(top_5_places.items())
    print(where_is_iceland)

where_is_iceland_on_list(top_5_places)

# What are dictionaries?
# Dictionaries are a data type used to store collections of data. Dictionaries are unique as they store "key:value" pairs,
# where a key is used rather than an index. 

# How can they be used in programming?
# They are unordered and can be changed, can be used to store values with definitions. 

# What is this code doing?
# This code is identifying where Iceland stands on the list of top_5_places. The function is looking for the min value in
# dictionary - in this case giving us "I" as it is giving min/max letters of the alphabet. As Iceland is first, it is 
# returned with this function. The "items" is there to store both the key and the value so they are both printed when the
# function is called. 



