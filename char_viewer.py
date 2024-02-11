import PySimpleGUI as sg
import os.path
import random

char_list = [
    'Asuka R#',
    'Baiken',
    'Bridget',
    'Elphelt',
    'Giovanna',
    'Happy Chaos',
    'I-No',
    'Jack-O',
    'May',
    'Millia',
    'Nagoriyuki',
    'Ramlethal',
    'Testament',
    'Variety',
    ]

char_dict = {
    'Asuka R#': 'asuka_r#',
    'Baiken': 'baiken',
    'Bridget' : 'bridget',
    'Elphelt' : 'elphelt',
    'Giovanna' : 'giovanna',
    'Happy Chaos' : 'happy_chaos',
    'I-No' : 'i-no',
    'Jack-O' : 'jack-o',
    'May' : 'may',
    'Millia' : 'millia',
    'Nagoriyuki' : 'nagoriyuki',
    'Ramlethal' : 'ramlethal',
    'Testament' : 'testament',
    'Variety' : 'variety',
    }

file_list = os.listdir('char_imgs')

def choose():
    return random.choice(char_list)

char_viewer_column = [
    [sg.Text(key='-NAME-')],
    [sg.Image(key='-IMAGE-')],
    [sg.Button('New')],
    [sg.Button('Close')],
]

layout = [
    [sg.Column(char_viewer_column)]
]

window = sg.Window("Today's Character", layout)

while True:
    event, values = window.read()

    if event == 'Close' or event == sg.WIN_CLOSED:
        break
    
    if event == 'New':
        char = choose()
        filename = os.path.join('char_imgs', char_dict[char] + '.png')

        try:
            window['-NAME-'].update(char)
            window['-IMAGE-'].update(filename=filename)

        except:
            pass

window.close()