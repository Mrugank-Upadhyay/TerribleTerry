# Let the Roasting Begin
# Later on, this will be integrated into Dyme where if someone you know is near you, it will automatically send them a roast

import pull
import pyperclip
import random
# from time import sleep

roasts = { 'photography' : [], 'beer' : [], 'wine' : [], 'travelling' : [], 'smoking' : [], 'reading' : [], 'cat' : [], 'mates' : [], 'friends' : [], 'adventure' : [], 'fitness' : [], 'camping' : [], 'Netflix' : [], 'beach' : [], 'dog': [], 'adventures': [], 'snapchat': [], 'coffee': [], 'instagram': [], 'IG': [], 'boys': [], 'jokes': [], 'tattoos': [], 'drinking': [], 'party': []}
def Roast(person):
    #TODO
    roast = []
    for categ in roasts.keys():
        if categ.lower() in person["bio"].lower():
            roast.append(random.choice(roasts[categ]))
    return '\n '.join(roast)


handle = "realDonaldTrump"
roastees = pull.user(handle)
pyperclip.copy("Hey " + handle + ", " + Roast(pull.user(handle))
