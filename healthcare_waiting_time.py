# This program asks the user to enter a year (2017-2020)
# and calculates the average waiting time (in minutes) at the public healthcare services
# in Oulu area that year.

import json
import urllib.request

url = "https://api.ouka.fi/v1/chc_waiting_times_monthly_stats?order=year.desc,month.desc"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")
queues = json.loads(raw_data)

# Creating a list that will contain the average waiting time and the year
queue_time = []

# Looping through the entries, skipping those with timestamp as null,
# calculating the average waiting time and adding those to the queue_time list
# using an auxiliary variable total_queue
for queue in queues:
    if queue["time"] is None:
        continue
    else:
        if queue["doctor_queue"] is None or queue["nurse_queue"] is None:
            continue
        else:
            average_time = int((queue["doctor_queue"] + queue["nurse_queue"]) / 2)
            total_queue = average_time, queue["year"]
            queue_time.append(total_queue)

# Asking the user to enter a year:

year = 0

while True:
    try:
        year = int(input("Please enter a year (2017-2020): "))
        if year < 2017 or year > 2020:
           print("Please enter a correct year (min. 2017, max. 2020)")
        else:
           break
    except Exception as e:
       print("Please enter the year as a number.")

# Creating an empty list which will only contain the data for the year
# entered by user, and variables for total waiting time and average waiting time.
total_entries_per_year = []
total_waiting_per_year = 0
average_waiting_per_year = 0

# Looping through the queue_time list, finding only the data for the requested year.
# Adding it to the list total_entries_per_year.
# Adding the waiting times to the variable (total_waiting_per_year) and then
# calculating the average.

for element in queue_time:
    if year == element[1]:
        total_entries_per_year.append(element)
        total_waiting_per_year += element[0]
        average_waiting_per_year = int(total_waiting_per_year / len(total_entries_per_year))

# Printing the requested information:

print(f"The average waiting time at the public healthcare services "
      f"in the Oulu region, year {year}: {average_waiting_per_year} minutes.")
