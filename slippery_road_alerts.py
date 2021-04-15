# This is a program to find out which city in Finland
# has statistically had the most slippery road alerts.

import json
import urllib.request
from collections import Counter
from datetime import datetime

url = "https://liukastumisvaroitus-api.beze.io/api/v1/warnings"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")
warnings = json.loads(raw_data)

# Creating an empty list for the cities:
cities = []

# Extracting the cities from the data (warnings) and adding them to the list:
for entry in warnings:
    cities.append(entry["city"])

# Finding out how many cities there are on the list,
# creating a short list to see a list without duplicates:
cities_without_duplicates = list(set(cities))

# print(cities_without_duplicates) - this is just for checking purposes

# After checking with the above print function and noticing that Kuopio
# is found on the list in four different versions (with different additions to the name).
# So we need to get rid of three of those - to only have Kuopio on the list as "Kuopio".
# This is done by looping through the list and changing Kuopio with any extra part to the
# pure form "Kuopio". Creating a list cities_parsed for the final form of the cities list

cities_parsed = []

for city in cities:
    if "Kuopio" in city:
        final_city = city.replace(city, "Kuopio")
        cities_parsed.append(final_city)
    else:
        final_city = city
        cities_parsed.append(final_city)

# Double checking the list for no duplicate forms
cities_final_check = list(set(cities_parsed))
# print(cities_final_check)

# Having a list that contains six cities, we want to find out the one with
# the most slippery road alerts:

cities_final = Counter(cities_parsed)
highest = cities_final.most_common(1)

# Now printing this information:
print(f"The city with the most slippery road alerts: \n{highest[0][0]}, {highest[0][1]} alerts.\n")

# Additionally the program prints the 5 last slippery road alerts based on the time stamp.
# Sorting them now from the oldest to the newest:

warnings_sorted = sorted(warnings, key=lambda x: datetime.strptime(x["created_at"], "%Y-%m-%d %H:%M:%S"))

# Printing the 5 newest ones, modifying the date and time to a more easily readable form (Finnish format):

print("Five latest slippery road alerts:")
for warning in warnings_sorted[-5:]:
    warning["created_at"] = datetime.strptime(warning["created_at"], "%Y-%m-%d %H:%M:%S")
    warning["created_at"] = warning["created_at"].strftime('%d.%m.%Y at %H:%M:%S')
    print(warning["city"], warning["created_at"])
