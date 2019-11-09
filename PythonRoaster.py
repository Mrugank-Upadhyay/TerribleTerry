# Let the Roasting Begin
# Later on, this will be integrated into Dyme where if someone you know is near you, it will automatically send them a roast

import pull
import sys
import pyperclip
import random
# from time import sleep

roasts = {' photograph ' : ['Those upskirt and downblouse pictures you snipe at the mall dont make you a photographer, it makes you a 2020 '
                             'presidential candidate',
                             'Ahh photographer, we call that unemployed over here'],
          ' smoking ' : ['Cigarette: A bit of tobacco with a fire at one end and a fool at the other.',
                         "You know, you don't actually smoke. The cigarette does all the smoking, you are just the sucker!",
                         "Smoking helps in reducing weight, 1 LUNG at a time"],
          ' read' : ['If we were in the maze together, I\'d push you into a Griever!'],
          ' cat ' : ['Cat lover eh? How does it feel to be ignored all day?',
                     'Lol, pussy!'],
          ' mates ' : ['8'],
          ' friends ' : ['9'],
          ' adventure ' : ['10'],
          ' fitness ' : ['11'],
          ' Netflix ' : ['13'],
          ' beach ' : ['14'],
          ' dog ': ['15'],
          ' adventures ': ['16'],
          ' coffee ': ['18'],
          ' boys ': ['21'],
          ' jokes ': ['22'],
          ' tattoo': ['23'],
          ' drink': ['24'],
          ' party ': ['25']}

def Roast(person):
    #TODO
    roast = []
    for categ in roasts.keys():
        if categ.lower() in person["bio"].lower():
            roast.append(random.choice(roasts[categ]))
    return ', also '.join(roast)

def main(handle):
    pyperclip.copy("Hey @" + handle + ", " + Roast(pull.user(handle)))
main(sys.argv[1])
