#!/usr/bin/python3
import os
import random
import multiprocessing
import time
import PySimpleGUI as sg
#Import playsound module
from playsound import playsound
sg.theme('Topanga')      #DarkAmber,Kayak,Reds.DarkGreen,DarkGreen2,LightBrown1,Topanga,DarkTeal12,DarkBlue17,DarkBlue13,DarkBlack1,
#sg.ChangeLookAndFeel('Kayak')

# ------ Menu Definition ------ #
menu_def = [['File', ['Open', 'Save',]],
            ['Edit', ['Paste', ['Special', 'Normal',], 'Undo'],],
            ['Help', 'About...'],]
# ------ GUI Defintion ------ #
def reset():
        keylist= ['low_end','high_end','collect','sets_v','ball','textbox']
        for key in keylist:
            form[key]('')
            #print(values)
# ------ Loop & Process button menu choices ------ #
    # ------ Process menu choices ------ #
column1 = [[sg.Text('Column 1', background_color='#F7F3EC', justification='center', size=(10, 1))]]
layout = [
        [sg.Menu(menu_def)],
        [sg.Text('Lucky Number Generator', size=(30, 1), font=("Helvetica", 25))],
        [sg.Text('Enter low value'),sg.Input(key='low_end',size=(5, 3)), sg.Text('Enter high value'),sg.Input(key='high_end',size=(5, 3))],
              [sg.Text('How Many Numbers'), sg.Input(key='collect',size=(5, 3)), sg.Text('How many sets:'), sg.Input(key='sets_v',size=(5, 3))], 
    [sg.Text('Do you want a seperate Powerball'), sg.Checkbox('Yes',key='ball'),sg.Text('(A seperate random draw.)',text_color='white')],
    [sg.Button('Submit'), sg.Button('Reset'), sg.Button('Exit')],
    [sg.Text('Your Lucky Numbers:',size=(30, 1), font=("Helvetica", 14)),sg.Text('', size=(13,5)),sg.Text('Would you like some music',size=(30, 1), font=("Helvetica", 14))],
    [sg.Listbox(values=[''],size=(20, 5), key='textbox', font=("Helvetica", 12),select_mode='browse',enable_events=True),sg.Text('', size=(30,5)),sg.Listbox(values= ['ChristmasTree.mp3', 'PrettyWoman.wav', 'TakeitEasy.wav', 'ComeTogether.wav', '50Ways.wav', 'LovesMe.wav', 'MotherandChild.wav'], default_values='PrettyWoman.wav',size=(20, 5), key='choice',select_mode='single',font=("Helvetica", 12),enable_events=True)],

    [sg.Text('',size=(65,5)),sg.Button('Play'),sg.Button('Stop')]
   ]
form = sg.FlexForm('Lucky Number Generator', layout,default_element_size=(60, 1),grab_anywhere=False).Finalize() # as form:

while True:
    event,values = form.Read()
    #event, values = form.Layout(layout).Read()
    if event == 'Reset':
        reset()
        form.read()
    if event == 'Play':
        folder = 'Music'
        select = folder + '/' + values['choice'][0]
        p = multiprocessing.Process(target=playsound, args=(select,))
        p.start()
        time.sleep(2)
    if event == 'Stop':
        #p.terminate()
        p.kill()
        while 1:
            os.system('./win10.py')
            #print('Restarting...')
            exit()
    if event in (None, 'Exit'):
        break           # exit button clicked
    if event == 'About...':
        sg.Popup('Luck Number Generator, a simple diversion of time. We like playing the lottery, so first we enter a range. Low value, (usually 1,) to a high value,(35, 72, etc...,) depends on values used in lottery. Number of numbers depends on game your playing, pick 3,5,12, Powerball, Mega millions. A set is a group of your numbers,from 1 to.... Selecting powerball will give a seperate draw of one ball added to your numbers. Good Luck,and its all luck!!',font=("Helvetica", 12))
        #form()
        #event, values = form.Read()
    if event == 'Open':
        filename = sg.PopupGetFile('file to open', no_window=True)
        print(filename)
    if event == 'Submit':
        keylist= ['low_end','high_end','collect','sets_v','ball','textbox']
        for key in keylist:
            if form[key] == (''):
                form.read()
        else:
            low_end = int(values['low_end'])
            high_end = int(values['high_end'])
            collect = int(values['collect'])
            sets_v = int(values['sets_v'])
        if values['ball'] == True:
            combo = []
            for i in range(0,sets_v):
                combo.append(random.sample(range(low_end, high_end), collect) + random.sample(range(low_end, high_end), 1))
                form['textbox'].update(combo)
                #form.close()
        else:
            if values['ball'] == False:
                combo = []
                for i in range(0,sets_v):
                    combo.append(random.sample(range(low_end, high_end), collect))
                    form['textbox'].update(combo)
#form.close()
