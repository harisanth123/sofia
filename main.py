#libraries
import pyttsx3 as p
import speech_recognition as sr
import random
import datetime

from random import choice
from wiki import *
from yt import *
from news import *
from data import *
from joke import *
from speed import *

engine = p.init()

rate = engine.getProperty('rate')
engine.setProperty('rate',175)

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def time():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        return("morning")
    elif hour>=12 and hour<16:
        return("afternoon")
    else:
        return("evening")

r = sr.Recognizer()

print("hello sir, good " + time() +" ,i am  sofia. your personal assistent")
speak("hello sir, good " + time() +" , iam sofia.  your personal assistent")


with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening.")
    audio = r.listen(source) 
    text = r.recognize_google(audio)
    text = text.lower()
    
if " what " and "about" and "you" in text:
    print("i am also having a good day sir.")
    speak("i am also having a good day sir.")

elif "good" in text:
    if time()== "morning":
        morning = random.choice(morning_data)
        print(morning)
        speak(morning)
    elif time()=="afternoon" :
        afternoon = random.choice(afternoon_data)
        print(afternoon)
        speak(afternoon)
    else:
        evening = random.choice(evening_data)
        print(evening)
        speak(evening)

else:
    intro = random.choice(intro_list)
    print(intro)
    speak(intro)    


print("what can i do for you??")
speak("what can i do for you??")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening..")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)
    text2 = text2.lower()
    

if "information" in text2:
    print("what information do you need ?")
    speak("what information do you need ?")
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening...")
        audio = r.listen(source)
        info = r.recognize_google(audio)
    print("searching {} in wikipedia".format(info))
    speak("searching {} in wikipedia".format(info))
    assist = wiki_data()
    assist.get_info(info)
     
elif "YouTube" and "video" in text2:
    print("which vedio do you need to watch?")
    speak("which vedio do you need to watch?")
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening...")
        audio = r.listen(source)
        vedio = r.recognize_google(audio)
    print("searching {} in youtube".format(vedio))
    speak("searching {} in youtube".format(vedio))
    assist = yt_data()
    assist.get_vedio(vedio) 

elif "news" in text2:
    print("sure sir, i will get for you ")
    speak("sure sir, i will get for you ")
    arr=get_news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])

elif "joke" or "jokes" in text2:
    print("ok sir let me find a joke for you")
    speak("ok sir let me find a joke for you")
    arr=joke()
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])

#elif "internet" and "speed" in text2:
    print("please wait. let me check your network speed")
    speak("please wait. let me check your network speed")
    print("loading server list")
    speak("loading server list")
    #print(f"Found:{best['host']} located in{best['country']}")
    #speak(f"Found:{best['host']} located in{best['country']}")