# Dice Simulator v2.1
import random
import json
import requests
import dice_images
import PySimpleGUI as sg


def create_window():

    # Theme
    sg.theme("black")
    # Font
    f = "Young 10"    # https://www.dafont.com/young.font

    # App layout
    layout = [
        [sg.Push(), sg.Image("images/CloseWindow.png", pad=0, enable_events=True, key="-CLOSE-")],
        [sg.Push(), sg.Text("v2.1", font=f)],

        [sg.VPush()],
        [sg.Image(dice_images.dice_art_dict[7], key="-OUTPUT-", size=(200, 200))],
        [sg.VPush()],

        [sg.Text("PRESS ROLL TO PLAY", font=f)],
        [sg.VPush()],
        [sg.Button("ROLL", key="-ROLL-", border_width=0, size=(5, 2),
                   button_color=('white', "red"), font="Young 16")],
        [sg.VPush()],
        [sg.Text("ROLLED NUMBERS:", font=f)],
        [sg.Text("", key="-ROLLED-", font=f)],

        [sg.Text("AVERAGE:", font=f)],
        [sg.Text("", key="-AVG-", font=f)]
    ]  # rows

    return sg.Window(
        "Stopwatch", layout, size=(300, 550),
        no_titlebar=True, element_justification="center")


window = create_window()

dice_list = []
dice_list_int = []
output_msg = ""
number_of_rolls = 0

# Main loop
while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "-CLOSE-"):
        break

    if event == "-ROLL-":
        try:
            # Roll the dice
            url = 'https://api.random.org/json-rpc/1/invoke'
            data = {'jsonrpc': '2.0',
                    'method': 'generateIntegers',
                    'params': {'apiKey': 'YourKey',        # YOUR KEY
                               'n': 1, 'min': 1, 'max': 6,
                               'base': 10}, 'id': 1}

            params = json.dumps(data)
            response = requests.post(url, params)
            json_dict = response.json()
            final = json_dict['result']['random']['data']
            dice = final[0]

        # Error handling
        except requests.ConnectionError:
            dice = random.randint(1, 6)

        except requests.HTTPError:
            dice = random.randint(1, 6)

        except KeyError:
            dice = random.randint(1, 6)

        # Count number of rolls
        number_of_rolls += 1

        # Print dice
        output_msg = dice_images.dice_art_dict[dice]

        # Append result to list of strings and list of integers
        dice_list.append(str(dice))
        dice_list_int.append(dice)

        # Count sum of list with integers
        sum_of_rolls = sum(dice_list_int)

        # Convert list to sequence of numbers
        rolled_numbers = ", ".join(dice_list)

        # Display results
        window["-OUTPUT-"].update(output_msg, size=(200, 200))
        window["-ROLLED-"].update(rolled_numbers, font="Young 12")
        window["-AVG-"].update(round(sum_of_rolls / number_of_rolls, 3), font="Young 12")

window.close()
