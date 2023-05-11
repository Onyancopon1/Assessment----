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
    choice = easygui.buttonbox(msg='What would you like to do?', title='Monster Manager',
                               choices=['Add Monster', 'Remove Monster', 'Output All Monsters', 'Exit'])

    if choice == 'Add Monster':
        if choice == 'Add Monster':
            name = easygui.enterbox(msg='Enter the name of the new monster:', title='Add Monster')
            if name:
                monsters.append({'name': name})
            Strength = easygui.enterbox(msg='Enter the Strength of the new monster:', title='Strength of Monster')
            if Strength:
                monsters.append({'Strength': Strength})
            Speed = easygui.enterbox(msg='Enter the speed of the new monster:', title='Speed of Monster')
            if Speed:
                monsters.append({'Speed': Speed})
            Stealth = easygui.enterbox(msg='Enter the Stealth of the new monster:', title='Stealth of Monster')
            if Stealth:
                monsters.append({'Stealth': Stealth})
            Cunning = easygui.enterbox(msg='Enter the Cunning of the new monster:', title='Cunning of Monster')
            if Stealth:
                monsters.append({'Cunning': Cunning})



        pass

    elif choice == 'Remove Monster':
        # Remove a monster
        # code to remove a monster from the list goes here
        pass

    elif choice == 'Output All Monsters':
        # Output all monsters
        output = 'All Monsters:\n'
        for monster in monsters:
            output += f"{monster['name']}\t\t: Strength {monster['Strength']}\t\t, Speed {monster['Speed']}\t\t," \
                      f" Stealth {monster['Stealth']}\t\t, Cunning {monster['Cunning']}\t\t\n"
        easygui.msgbox(msg=output, title='Monster Manager')

    elif choice == 'Exit':
        # Exit the program
        break
