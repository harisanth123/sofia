import datetime
import random

from sofia_data import *

def time():

    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        return("morning")
    elif hour>=12 and hour<16:
        return("afternoon")
    else:
        return("evening")

def wishing():
    if time()== "morning":
        wishes = random.choice(morning_data)
    elif time()=="afternoon" :
        wishes = random.choice(afternoon_data)
    else:
        wishes = random.choice(evening_data)
    return wishes

        