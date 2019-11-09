# Let the Roasting Begin
# Later on, this will be integrated into Dyme where if someone you know is near you, it will automatically send them a roast

import pull
import pyperclip
import random
# from time import sleep

roasts = {' photography ' : ['1'], 
          ' beer ' : ['2'], 
          ' wine ' : ['3'], 
          ' travelling ' : ['4'], 
          ' smoking ' : ['5'], 
          ' reading ' : ['6'], 
          ' cat ' : ['7'], 
          ' mates ' : ['8'], 
          ' friends ' : ['9'], 
          ' adventure ' : ['10'], 
          ' fitness ' : ['11'], 
          ' camping ' : ['12'], 
          ' Netflix ' : ['13'], 
          ' beach ' : ['14'], 
          ' dog ': ['15'], 
          ' adventures ': ['16'], 
          ' snapchat ': ['17'], 
          ' coffee ': ['18'], 
          ' instagram ': ['19'], 
          ' IG ': ['20'], 
          ' boys ': ['21'], 
          ' jokes ': ['22'], 
          ' tattoos ': ['23'], 
          ' drinking ': ['24'], 
          ' party ': ['25']}
def Roast(person):
    #TODO
    roast = []
    for categ in roasts.keys():
        if categ.lower() in person["bio"].lower():
            roast.append(random.choice(roasts[categ]))
    return '\n '.join(roast)


handle = "realDonaldTrump"
roastees = pull.user(handle)
pyperclip.copy("Hey @" + handle + ", " + Roast(pull.user(handle)))
