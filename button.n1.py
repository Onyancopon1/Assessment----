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
