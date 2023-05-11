import easygui

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

while True:
    choice = easygui.buttonbox('What do you want to do?', 'Monster Manager', ('Add Monster', 'Remove Monster', 'Output All', 'Exit'))

    if choice == 'Add Monster':
        name = easygui.enterbox('Enter monster name:')
        if not name:
            break
        strength = easygui.enterbox('Enter monster strength number between 1-25:')
        if not (1 <= int(strength) <= 25):
            easygui.msgbox('Strength must be between 1 and 25')
            break
        speed = easygui.enterbox('Enter monster speed number between 1-25:')
        if not (1 <= int(speed) <= 25):
            easygui.msgbox('Speed must be between 1 to 25')
            break
        stealth = easygui.enterbox('Enter monster stealth number between 1-25:')
        if not (1 <= int(stealth) <= 25):
            easygui.msgbox('Stealth must be between 1 to 25')
            break
        cunning = easygui.enterbox('Enter monster cunning number between 1-25:')
        if not (1 <= int(cunning) <= 25):
            easygui.msgbox('Stealth must be between 1 to 25')
            break
        new_monster = {'name': name, 'Strength': strength, 'Speed': speed, 'Stealth': stealth, 'Cunning': cunning}
        monsters.append(new_monster)
        easygui.msgbox(f'{name} has added successfully!', 'Monster Manager')

    elif choice == 'Remove Monster':
        monster_names = [monster['name'] for monster in monsters]
        monster_to_remove = easygui.choicebox("Which monster do you want to remove?", "Remove Monster", monster_names)
        if monster_to_remove:
            for monster in monsters:
                if monster['name'] == monster_to_remove:
                    monsters.remove(monster)
                    easygui.msgbox(f"{monster_to_remove} has been removed from the dictionary.")
                    break
            else:
                easygui.msgbox(f"{monster_to_remove} not found in the dictionary.")

                pass

    elif choice == 'Output All':
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

    else:
        # Exit the program
        break
