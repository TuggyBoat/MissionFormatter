import re
import PySimpleGUI as sg

def space_check(string: str):
    if ' ' in string:
        return f'"{string}"'
    return string


sg.theme('Reddit')

layout = [
    [sg.Text('Mission Command Formatter')],
    [sg.Text('Mission Type', size=(15, 1)), sg.Combo(values=['Load', 'Unload', 'Load w/ Message', 'Unload w/ Message'],
                                                     size=(15, 6), default_value='Load', key='-TYPE-')],
    [sg.Text('Carrier Name', size=(15, 1)), sg.In(size=(15, 1), key='-CARRIER-')],
    [sg.Text('Commodity Name', size=(15, 1)), sg.In(size=(20, 1), key='-COMMODITY-')],
    [sg.Text('System Name', size=(15, 1)), sg.In(size=(20, 1), key='-SYSTEM-')],
    [sg.Text('Station Name', size=(15, 1)), sg.In(size=(15, 1), key='-STATION-')],
    [sg.Text('Profit per Ton', size=(15, 1)), sg.In(size=(5, 1), key='-PROFIT-')],
    [sg.Text('Pad Size', size=(15, 1)), sg.Radio('S', 'RADI01', default=True, key='-SMALL-'), sg.Radio('M', 'RADI01',
                                                                                                       key='-MEDIUM-'),
     sg.Radio('L', 'RADI01', key='-LARGE-')],
    [sg.Text('Supply', size=(15, 1)), sg.In(size=(5, 1), key='-SUPPLY-')],
    [sg.Text('ETA', size=(15, 1)), sg.In(size=(5, 1), key='-ETA-')],
    [sg.Submit('Format', key='-FORMAT-'), sg.Button('Clear', key='-CLEAR-')],
    [sg.Text('Output', size=(15, 1)), sg.Output(size=(50, 2), key='-OUTPUT-')]
]

window = sg.Window('Mission Command Formatter', layout)

while True:

    event, values = window.read()
    print(event, values)
    values_list = []
    if event == sg.WIN_CLOSED:
        break

    if event == '-FORMAT-':
        mission_type = values['-TYPE-']

        # Mission Type
        if mission_type.lower() == 'load':
            values_list.append('m.load')
        elif mission_type.lower() == 'unload':
            values_list.append('m.unload')
        elif mission_type.lower() == 'load w/ message':
            values_list.append('m.loadrp')
        else:
            values_list.append('m.unloadrp')

        # Carrier Name
        carrier_name = values['-CARRIER-'].lower()
        carrier_name = space_check(carrier_name)
        values_list.append(carrier_name)

        # Commodity Name
        commodity = values['-COMMODITY-'].lower()
        commodity = space_check(commodity)
        values_list.append(commodity)

        # System Name
        system = values['-SYSTEM-'].lower()
        system = space_check(system)
        values_list.append(system)

        # Station Name
        station = values['-STATION-'].lower()
        station = space_check(station)
        values_list.append(station)

        # Profit
        profit = values['-PROFIT-']
        if len(profit) < 3:
            values_list.append(profit)

        # Pad Size
        if values['-SMALL-']:
            values_list.append('S')
        elif values['-MEDIUM-']:
            values_list.append('M')
        else:
            values_list.append('L')

        # Supply
        supply = values['-SUPPLY-']
        if len(supply) > 2:
            values_list.append(supply)
        else:
            values_list.append(supply+'k')

        # ETA
        eta = values['-ETA-']
        if eta != '':
            values_list.append(eta)

        # Build String
        command = ' '.join(values_list)

        # Output
        print(command)
        window['-OUTPUT-'].update(command)

    if event == '-CLEAR-':
        clear_list = ['-CARRIER-', '-COMMODITY-', '-SYSTEM-', '-STATION-', '-PROFIT-', '-SUPPLY-', '-ETA-', '-OUTPUT-']

        for key in clear_list:
            window[key].update('')


window.close()
