# Dice Simulator v2.0

import json
import requests
import dice_art
import PySimpleGUI as sg

# Application layout as list
layout = [
    [sg.Text("DICE SIMULATOR, PRESS ROLL TO PLAY", justification="centre")],
    [sg.Text(dice_art.dice_art_dict[1],
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

window = sg.Window(f"Dice Simulator v 2.0", layout)  # sg.Window(title,layout)

dice_list = []
dice_list_int = []
output_msg = ""
number_of_rolls = 0


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "-ROLL-":

        # Roll the dice
        url = 'https://api.random.org/json-rpc/1/invoke'
        data = {'jsonrpc': '2.0',
                'method': 'generateIntegers',
                'params': {'apiKey': 'yourKey',
                           'n': 1, 'min': 1, 'max': 6,
                           'base': 10}, 'id': 1}
        params = json.dumps(data)
        response = requests.post(url, params)
        dice = int(response.text[45])

        # Count number of rolls
        number_of_rolls += 1

        # Print dice
        output_msg = dice_art.dice_art_dict[dice]

        # Append result to list of strings and list of integers
        dice_list.append(str(dice))
        dice_list_int.append(dice)

        # Count sum of list with integers
        sum_of_rolls = sum(dice_list_int)

        # Convert list to sequence of numbers
        rolled_numbers = ", ".join(dice_list)

        # Display results
        window["-OUTPUT-"].update(output_msg)
        window["-ROLLED-"].update(rolled_numbers)
        window["-AVG-"].update(round(sum_of_rolls / number_of_rolls, 3))

window.close()
