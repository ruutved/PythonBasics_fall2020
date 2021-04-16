import json
import datetime

# A simple program to register service notes in a file (service.json, which has to be in the same folder as this .py file)

# First, showing the last entry, if the file exists

try:
    if "service.json":
        file = open("service.json", "r", encoding="utf=8")
        content = file.read()
        file.close()
        service_entries = json.loads(content)

        entries_sorted = sorted(service_entries, key=lambda x: (x["time"]))

        print(f"Latest entry:")

        print("Date:", entries_sorted[-1]['time'])
        print("Name:", entries_sorted[-1]['name'])
        print("Service code:", entries_sorted[-1]['code'])
        print("Message:", entries_sorted[-1]['comment'], "\n")

except:
    print("No entries yet.\n")

# Now, user can choose to read, write or quit:

while True:

    action = input("Do you want to add a new note (w) or read all the existing ones (r)? "
                   "Entering q stops the program.")

    if action == "r":
        try:

            file_handle = open("service.json", "r", encoding="utf-8")
            content = file_handle.read()
            file_handle.close()
            entries = json.loads(content)

            print("All the service notes:")

            for entry in entries_sorted:
                print(f"Pvm: {entry['time']}")
                print(f"Hlö: {entry['name']}")
                print(f"Tilannekoodi: {entry['code']}")
                print(f"Viesti: {entry['comment']}\n")

        except FileNotFoundError:
            print("File not found. Program stopped.")
            break

    elif action == "w":

        try:
            file_handle = open("service.json", "r", encoding="utf-8")
            content = file_handle.read()
            file_handle.close()
            service_entries = json.loads(content)

            print("New entry:\n")

            name = input("Name: ")
            code = int(input("Service code: "))
            comment = input("Comment: ")
            time = datetime.datetime.now().strftime("%d.%m.%Y klo %H.%M.")

        #  Saving the message as a new entry:
            new_entry = {
                "name": name,
                "code": code,
                "comment": comment,
                "time": time
                }

            # Adding the above entry to the collection:
            service_entries.append(new_entry)

            # Converting service_entries to json format:
            json_data = json.dumps(service_entries, indent=2)

            # Adding it to service.json file:
            file = open("service.json", "w")
            file.write(json_data)
            file.close()

            # Finishing the action:
            print("Your note has been saved.")

        except FileNotFoundError or NameError:
            print("File not found. Program stopped.")
            break

    elif action == "q":
        print("Program stopped.")
        break

    else:
        print("Please read the instructions to proceed: \n")
