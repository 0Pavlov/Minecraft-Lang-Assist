# Import the json module to be able to work with the lang file
import json

# Open the en_us.json file in read mode
with open('en_us.json', 'r') as file:

    # Store the file content as Python dictionary
    data = json.load(file)

    # Iterate trough data dictionary with enumerate() func that allows to display which object we're at (variable "c")
    # Add 1 to "c" variable to start counting from 1 instead of 0
    for c, i in enumerate(data):

        # Show to user current object id, its name and ask for a new name
        # At the beginning of printed string, display current object number relatively to how many is left
        new_name: str = str(input(f"({c+1}/{len(data)}) What's gonna be new name for ({i}) {data[i]}? : "))

        # Update the data dictionary with the new value for the current key
        data[i] = new_name

# Store updated data back into the file
with open('en_us.json', 'w') as file:
    json.dump(data, file, indent=4)

# Ask user to input something to avoid instant closing of command line
exit_input = input("Translation complete. Press any key to exit.")