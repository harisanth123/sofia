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

engine = p.init()
currentTime = datetime.datetime.now()
currentTime.hour

rate = engine.getProperty('rate')
engine.setProperty('rate',175)

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

print("i am is sofia. your personal assistent")
speak("i am sofia. your personal assistent")


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
    if currentTime.hour < 12:
        morning = random.choice(morning_data)
        print(morning)
        speak(morning)
    elif 12 <= currentTime.hour < 18:
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
    speak("searching {} in wikipedia".format(info))
    print("searching {} in wikipedia".format(info))
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
