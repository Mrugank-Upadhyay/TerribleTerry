# Let the Roasting Begin
# Later on, this will be integrated into Dyme where if someone you know is near you, it will automatically send them a roast

import pull
import sys
import pyperclip
import random
# from time import sleep

roasts = {' photograph' : ['Those upskirt and downblouse pictures you snipe at the mall dont make you a photographer, it makes you a 2020 '
                             'presidential candidate',
                             'Ahh photographer, we call that unemployed over here'],
          ' smok' : ['Cigarette: A bit of tobacco with a fire at one end and a fool at the other.',
                         "You know, you don't actually smoke. The cigarette does all the smoking, you are just the sucker!",
                         "Smoking helps in reducing weight, 1 LUNG at a time"],
          ' read' : ['If we were in the maze together, I\'d push you into a Griever!'],
          ' cat ' : ['Cat lover eh? How does it feel to be ignored all day?'],
          ' adventur' : ['You consider a walk to the fridge an adventure',
          'The closest you will ever get to adventure is the rush you get crossing the street'],
          ' fitness ' : ['You\'re version of \'fitness\' consists of chewing and swallowing'],
          ' Netflix ' : ['When you watch Netflix, the site crashes because they know you can\'t \'chill\''],
          ' beach' : ['Last time you went to the beach they thought a whale got beached'],
          ' dog': ['Dogs have more personality than you do'],
          ' coffee ': ['You\'ve drank so much coffee that I don\'t need to roast you.'],
         ' joke': ['Jokes? I got one for you but I don\' have the time, nor the crayons to explain it to you.'],
          ' drink': ['It\'s okay, everyone has a drinking problem at this point. But drinking that... pathetic. My grandmother drinks that to stay '
                     'sober!'],
          'laurier': ['University? You mean Canada\'s largest highschool.'],
          'goose': ['Thank you Mr. Goose!'],
          'geese': ['Thank you Mr. Goose!'],
         'Trump': ['Trump Water? Failed \n Trump Airlines? Failed\n Trump Casinos? Failed \n Trump Magazine? Failed \n Murica? Failed \n Hotel? Trivago'],
          'CSS': ['Html isnt a language or a skills, its a disgrace. CSS doesnt even count as a disgrace.']
         }

def Roast(person):
    #TODO
    roast = []
    for categ in roasts.keys():
        if categ.lower() in person["bio"].lower():
            roast.append(random.choice(roasts[categ]))
    if roast == []:
        roast = ['I would roast you, but not even my code finds you interesting.']
    return ', '.join(roast)

def main(handle):
    pyperclip.copy("Hey @" + handle + ", " + Roast(pull.user(handle)))
main(sys.argv[1])
