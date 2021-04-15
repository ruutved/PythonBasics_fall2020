import json
import urllib.request
from collections import Counter

# This is a program to that checks the current weather information and
# tells the user where in Finland it's the most and least windy right now.

url = "https://edu.frostbit.fi/api/weather/"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")
weather = json.loads(raw_data)

# Creating an empty list where the cities and wind speeds (m/s) will be added:
wind = []

# Extracting the cities and wind speeds from the list,
# using an auxiliary variable windy_city which will contain this information,
# appending them to the previously created list (wind):
for entry in weather:
    windy_city = entry["location"], entry["wind"]
    wind.append(windy_city)


# The list "wind" consists of tuples.
# Making sure the list is ordered by the wind speed:
def getKey(item):
    return item[1]


# Saving the sorted list in a new variable:
sorted_wind = sorted(wind, key=getKey)

# Printing the requested information:
print(f"Today the windiest city is {sorted_wind[-1][0]} - wind speed is {sorted_wind[-1][1]} m/s")
print(f"Today the least windy city is {sorted_wind[0][0]} - wind speed is {sorted_wind[0][1]} m/s")

# Adding information about the average wind speed in each area measured.
# Creating an empty list where the areas and their wind speeds will be added:
area_wind = []

# Adding the areas and wind speeds to the list:
for entry in weather:
    windy_area = entry["area"], entry["wind"]
    area_wind.append(windy_area)

# Creating empty variables for the regional wind speeds:
lapland_wind = 0
middle_wind = 0
south_wind = 0

# Creating variables and counting how many times each area appears on the list, in
# order to calculate the average. (Right now each area appears 3 times but this is to
# prepare for a different scenario):
lapland_counts = Counter(x[0] for x in area_wind)
middle_counts = Counter(x[0] for x in area_wind)
south_counts = Counter(x[0] for x in area_wind)

# With the below we could check if the above works - (not needed now
# so it's commented out)

# print(lapland_counts["lapland"])
# print(middle_counts["middle"])
# print(south_counts["south"])

# Adding up the wind speeds by area:

for item in area_wind:
    if item[0] == "lapland":
        lapland_wind += item[1]
    elif item[0] == "middle":
        middle_wind += item[1]
    else:
        south_wind += item[1]

# Emptying the list "area_wind" to include only the averages in it:

area_wind = []

# Calculating the averages, rounding them up to 1 decimal and saving them
# in variables together with the area name.
# Saving the variables in the list area_wind.
# Using the above created variables (lapland_counts etc.) to calculate the averages.

lapland_wind = round((lapland_wind / lapland_counts["lapland"]), 1), "lapland"
area_wind.append(lapland_wind)
middle_wind = round((middle_wind / middle_counts["middle"]), 1), "middle"
area_wind.append(middle_wind)
south_wind = round((south_wind / south_counts["south"]), 1), "south"
area_wind.append(south_wind)

# Printing the average wind speed for each area:

for wind in area_wind:
    if wind[1] == "lapland":
        print(f"Average wind speed, Lapland: {wind[0]} m/s")
    elif wind[1] == "middle":
        print(f"Average wind speed, Central Finland : {wind[0]} m/s")
    else:
        print(f"Average wind speed, Southern Finland: {wind[0]} m/s")
