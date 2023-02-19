# Dice Simulator v1.1

from dice_art import dice_art_dict
import PySimpleGUI as sg
import random

layout = [
    [sg.Text("DICE SIMULATOR, PRESS ROLL TO PLAY",justification="centre")],
    [sg.Text(dice_art_dict[1],
             font="Courier 20",
             justification="centre",
             pad=(80, 0),
             key="-OUTPUT-")],
    [sg.Button("ROLL", key="-ROLL-", expand_x=True)],
    [sg.Text("ROLLED NUMBERS:")],
    [sg.Text("", key="-ROLLED-")],
    [sg.Text("AVERAGE:")],
    [sg.Text("", key="-AVG-")]
]  # rows

# sg.Window(title,layout)
window = sg.Window(f"Dice Simulator v 1.1", layout)

dice_list = []
dice_list_int = []
output_msg = ""
number_of_rolls = 0

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "-ROLL-":
        number_of_rolls += 1
        dice = random.randint(1, 6)
        output_msg = dice_art_dict[dice]
        dice_list.append(str(dice))
        dice_list_int.append(dice)
        sum_of_rolls = sum(dice_list_int)
        rolled_numbers = ", ".join(dice_list)

        window["-OUTPUT-"].update(output_msg)
        window["-ROLLED-"].update(rolled_numbers)
        window["-AVG-"].update(round(sum_of_rolls / number_of_rolls, 3))

window.close()
