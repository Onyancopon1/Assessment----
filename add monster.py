import easygui

monsters = [
    {'name': 'Stoneling', 'Strength': 7, 'Speed': 1, 'Stealth': 25,
     'Cunning': 15},
    {'name': 'Vexscream', 'Strength': 1, 'Speed': 6, 'Stealth': 21,
     'Cunning': 19},
    {'name': 'Dawnmirage', 'Strength': 5, 'Speed': 15, 'Stealth': 18,
     'Cunning': 22},
    {'name': 'Blazegolem', 'Strength': 15, 'Speed': 20, 'Stealth': 23,
     'Cunning': 6},
    {'name': 'Websnake', 'Strength': 7, 'Speed': 15, 'Stealth': 10,
     'Cunning': 5},
    {'name': 'Moldvine', 'Strength': 21, 'Speed': 18, 'Stealth': 14,
     'Cunning': 5},
    {'name': 'Vortexwing', 'Strength': 19, 'Speed': 13, 'Stealth': 19,
     'Cunning': 2},
    {'name': 'Rotthing', 'Strength': 16, 'Speed': 7, 'Stealth': 4,
     'Cunning': 12},
    {'name': 'Froststep', 'Strength': 14, 'Speed': 14, 'Stealth': 17,
     'Cunning': 4},
    {'name': 'Wispghoul', 'Strength': 17, 'Speed': 19, 'Stealth': 3,
     'Cunning': 2}
]

# Construct the message to be displayed
def get_monster_message(monsters):
    message = "List of Monsters:\n\n"
    for monster in monsters:
        message += f"Name: {monster['name']}\n\t"
        message += f"Strength: {monster['Strength']}\n\t"
        message += f"Speed: {monster['Speed']}\n\t"
        message += f"Stealth: {monster['Stealth']}\n\t"
        message += f"Cunning: {monster['Cunning']}\n\t\n"
    return message

# Display the message using easygui
def display_monsters(monsters):
    message = get_monster_message(monsters)
    easygui.msgbox(message)

# Display the dictionary before user input
display_monsters(monsters)

while True:
    if len(monsters) == 0:
        easygui.msgbox("No more monsters in the dictionary.", "Monster Manager")
        break

    choice = easygui.buttonbox('What do you want to do?', 'Monster Manager',
                               ('Add Monster', 'Remove Monster', 'Dictionary',
                                'Exit'))

    if choice == 'Add Monster':
        name = easygui.enterbox('Enter monster name:')
        if name is None:
            break

        strength = easygui.enterbox(
            'Enter monster strength number between 1-25:')
        if strength is None or not strength.isdigit() or not (
                1 <= int(strength) <= 25):
            easygui.msgbox('Strength must be a number between 1 and 25')
            continue

        speed = easygui.enterbox('Enter monster speed number between 1-25:')
        if speed is None or not speed.isdigit() or not (1 <= int(speed) <= 25):
            easygui.msgbox('Speed must be a number between 1 and 25')
            continue

        stealth = easygui.enterbox(
            'Enter monster stealth number between 1-25:')
        if stealth is None or not stealth.isdigit() or not (
                1 <= int(stealth) <= 25):
            easygui.msgbox('Stealth must be a number between 1 and 25')
            continue

        cunning = easygui.enterbox(
            'Enter monster cunning number between 1-25:')
        if cunning is None or not cunning.isdigit() or not (
                1 <= int(cunning) <= 25):
            easygui.msgbox('Cunning must be a number between 1 and 25')
            continue

        new_monster = {'name': name, 'Strength': int(strength),
                       'Speed': int(speed),
                       'Stealth': int(stealth), 'Cunning': int(cunning)}
        monsters.append(new_monster)
        easygui.msgbox(f'{name} has been added successfully!',
                       'Monster Manager')