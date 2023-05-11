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

while True:
    choice = easygui.buttonbox(
        msg="What do you want to do?",
        title="Monster Manager",
        choices=["Add Monster", "Remove Monster", "Output All", "Exit"]
    )

    if choice == "Add Monster":
        monster_name = easygui.enterbox("Enter the name of the new monster:")
        monster_strength = int(easygui.enterbox("Enter the strength of the new monster:"))
        monster_speed = int(easygui.enterbox("Enter the speed of the new monster:"))
        monster_stealth = int(easygui.enterbox("Enter the stealth of the new monster:"))
        monster_cunning = int(easygui.enterbox("Enter the cunning of the new monster:"))
        new_monster = {'name': monster_name, 'Strength': monster_strength, 'Speed': monster_speed,
                       'Stealth': monster_stealth, 'Cunning': monster_cunning}
        monsters.append(new_monster)
        easygui.msgbox(f"{monster_name} has been added to the dictionary.")

    elif choice == "Remove Monster":
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

    elif choice == "Output All":
        output_text = ""
        for monster in monsters:
            output_text += f"{monster['name']} - Strength: {monster['Strength']}, Speed: {monster['Speed']},Stealth: " \
                           f"{monster['Stealth']},Cunning: {monster['Cunning']}\
