# A guestbook program

# Defining the functions first, before asking the user if they want to read/write

import json
import datetime

def guestbook(action):

    # If the user chooses to read the guestbook:
    if action == "r":

        file_handle = open("guestbook.json", "r", encoding="utf-8")
        content = file_handle.read()
        file_handle.close()
        entries = json.loads(content)

        # Checking first if the guestbook is empty.
        # If not, the messages are printed. If it's empty,
        # the user is informed.
        for entry in entries:
            result = bool(entry)
            if result:
                message = entry["message"]
                time = entry["time"]

                print(f"{time}: {message}")

            else:
                print("No messages.")

    # If the user has chosen to write in the guestbook:
    else:
        file_handle = open("guestbook.json", "r", encoding="utf-8")
        content = file_handle.read()
        file_handle.close()
        entries = json.loads(content)

        # Requesting to enter a new message
        entry_message = input("Write a new message: \n")

        # Adding a timestamp:
        entry_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")

        # Saving the message as a new entry in a dictionary:
        new_entry = {
            "message": entry_message,
            "time": entry_time
        }

        # Adding the new entry to entries:
        entries.append(new_entry)

        # Converting entries to json:
        json_data = json.dumps(entries, indent=2)

        # Adding that to guestbook.json:
        file = open("guestbook.json", "w")
        file.write(json_data)
        file.close()

        # Informing the user that the message has been saved:
        print("Viesti tallennettu vieraskirjaan.")
        
action = input("Would you like to read the guestbook or write in it? (r/w)? \n")

guestbook(action)
