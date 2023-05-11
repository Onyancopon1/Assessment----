import easygui

# Create an empty list to hold the monsters
monsters = [
    {'name': 'Stoneling', 'Strength': 7, 'Speed': 1, 'Stealth': 25, 'Cunning': 15},
    {'name': 'Vexscream', 'Strength': 1, 'Speed': 6, 'Stealth': 21, 'Cunning': 19},
    {'name': 'Dawnmirage', 'Strength': 5, 'Speed': 15, 'Stealth': 18, 'Cunning': 22},
    {'name': 'Blazegolem', 'Strength': 15, 'Speed': 20, 'Stealth': 23, 'Cunning': 6},
    {'name': 'Websnake', 'Strength': 7, 'Speed': 15, 'Stealth': 10, 'Cunning': 5},
    {'name': 'Moldvine', 'Strength': 21, 'Speed': 18, 'Stealth': 14, 'Cunning': 5},
    {'name': 'Vortexwing', 'Strength': 19, 'Speed': 13, 'Stealth': 19, 'Cunning': 2},
    {'name': 'Rotthing', 'Strength': 16, 'Speed': 7, 'Stealth': 4, 'Cunning': 12},
    {'name': 'Froststep', 'Strength': 14, 'Speed': 14, 'Stealth': 17, 'Cunning': 4},
    {'name': 'Wispghoul', 'Strength': 17, 'Speed': 19, 'Stealth': 3, 'Cunning': 2}
]

# Construct the message to be displayed
message = "List of Monsters:\n\n"
for monster in monsters:
    message += f"Name: {monster['name']}\n\t"
    message += f"Strength: {monster['Strength']}\n\t"
    message += f"Speed: {monster['Speed']}\n\t"
    message += f"Stealth: {monster['Stealth']}\n\t"
    message += f"Cunning: {monster['Cunning']}\n\t\n"

# Display the message using easygui
easygui.msgbox(message)

# Define the function to add a new monster
def add_monster():
    # Ask the user for the name of the new monster
    new_name = easygui.enterbox("Enter the name of the new monster:")


    # Create a dictionary for the new monster with default values
    new_monster = {'name': new_name, 'Strength': 0, 'Speed': 0, 'Stealth': 0, 'Cunning': 0}

    # Add the new monster to the list of monsters
    monsters.append(new_monster)

    # Show a message box to confirm that the new monster was added
    easygui.msgbox(f"{new_name} has been added to the list of monsters.")


# Define the function to remove a monster
def remove_monster():
    # Ask the user for the name of the monster to remove
    remove_name = easygui.enterbox("Enter the name of the monster to remove:")

    # Search for the monster in the list of monsters
    for monster in monsters:
        if monster['name'] == remove_name:
            # Remove the monster from the list of monsters
            monsters.remove(monster)
            # Show a message box to confirm that the monster was removed
            easygui.msgbox(f"{remove_name} has been removed from the list of monsters.")
            return

    # If the monster was not found, show an error message
    easygui.msgbox(f"Error: {remove_name} was not found in the list of monsters.")


# Define the function to output all monsters
def output_monsters():
    # Show a message box with the list of monsters
    easygui.msgbox(str(monsters))



# Show the main menu and get the user's choice
while True:
    choice = easygui.buttonbox("Select an action:", choices=["Add Monster", "Remove Monster", "Output All", "Exit"])

    # Take action based on the user's choice
    if choice == "Add Monster":
        add_monster()
    elif choice == "Remove Monster":
        remove_monster()
    elif choice == "Output All":
        output_monsters()
    elif choice == "Exit":
        break
