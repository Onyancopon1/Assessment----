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

#importingeasyguimodule
from easygui import *

# message to be displayed
text = "What would you like to do"

# window title
title = "Option"

# button list
button_list = []

# button for add combo
button1 = "Add Monster"

# button for find combo
button2 = "Remove the Monster"

#button for Output all
button3 = "Output all"

#button for Exit
button4 = "Exit"

# appending button to the button list
button_list.append(button1)
button_list.append(button2)
button_list.append(button3)
button_list.append(button4)

# creating a button box
output = buttonbox(text, title, button_list)

# printing the button pressed by the user
print("User selected option : ", end=" ")
print(output)
