# Making a collection of restaurants and then asking the user
# various questions to find out which restaurants to recommend them.

restaurant_0 = {
    "name": "North Delish",
    "rating": 4.5,
    "reservations": True,
    "services": ["lunch", "dinner"],
    "price_level": 5,
    "location": "Rovaniemi"
}

restaurant_1 = {
    "name": "Food Galore",
    "rating": 3.8,
    "reservations": False,
    "services": ["breakfast", "lunch"],
    "price_level": 3,
    "location": "Tornio"
}

restaurant_2 = {
    "name": "Snacksy Oy",
    "rating": 3.2,
    "reservations": False,
    "services": ["lunch", "dinner", "night"],
    "price_level": 2,
    "location": "Oulu"
}

restaurant_3 = {
    "name": "McDonalds",
    "rating": 3.5,
    "reservations": False,
    "services": ["breakfast", "lunch", "dinner", "night"],
    "price_level": 2,
    "location": "Kuopio"
}

restaurant_4 = {
    "name": "2SmallPortions",
    "rating": 5,
    "reservations": True,
    "services": ["breakfast", "lunch", "dinner"],
    "price_level": 5,
    "location": "Kouvola"
}

# Adding the restaurants to one list:
restaurants = [restaurant_0, restaurant_1, restaurant_2, restaurant_3, restaurant_4]

print("Welcome to the restaurant search!")

# The questions are asked so that the program won't stop working if
# the answer is wrong/in wrong format.

# Asking the questions one by one:

while True:
    try:
        stars = int(input("How many stars should the restaurant have at least? (1-5)"))
        if stars < 1 or stars > 5:
            print("Please enter a number between 1 and 5.")
        else:
            break
    except Exception as e:
        print("Please enter the answer as a number.")

while True:
    try:
        price_level = int(input("What should be price level be at the highest? (1-5)"))
        if price_level < 1 or price_level > 5:
            print("Please enter the price level between 1 and 5.")
        else:
            break
    except Exception as e:
        print("Please enter the answer as a number.")

while True:
    try:
        book = str(input("Would you like to make a reservation? (y/n)"))
        if book != "y" and book != "n":
            print("If you want to make a reservation, enter 'y', if not, enter 'n'.")
        elif book == "y":
            book = True
            break
        else:
            book = False
            break
    except TypeError:
        print("Please enter the answer as a letter (y/n)")

while True:
    try:
        time = int(input("At what time would you like to visit the restaurant? (0-23 hrs)\n"))
        if time < 0 or time > 23:
            print("Please enter an hour between 0 and 23.")
        else:
            break
    except Exception as e:
        print("Please enter the hour as a number.")

# Creating an empty list where to add the recommendations found at the next step
suggestions = []

# Finding a suitable restaurant.
# If at least one (the first) condition isn't filled, then there is no suitable restaurant found:

for restaurant in restaurants:
    if restaurant["rating"] >= stars:
        if restaurant["price_level"] <= price_level:
            if restaurant["reservations"] == book:
                if 6 <= time <= 10:
                    if "breakfast" in restaurant["services"]:
                        suggestions.append(restaurant["name"])
                elif 11 <= time <= 16:
                    if "lunch" in restaurant["services"]:
                        suggestions.append(restaurant["name"])
                elif 17 <= time <= 24:
                    if "dinner" in restaurant["services"]:
                        suggestions.append(restaurant["name"])
                else:
                    if "night" in restaurant["services"]:
                        suggestions.append(restaurant["name"])

# Showing a list of suitable suggestions.
# If the list contains at least one restaurant, it's printed out
# and if there are no restaurants on the list, the program informs the
# user that no suitable restaurants were found:

if len(suggestions) > 0:
    print("Based on your answers, we suggest the following restaurants: \n")
    for suggestion in suggestions:
        print("- " + suggestion)
else:
    print("Based on your answers, no suitable restaurants were found!")
