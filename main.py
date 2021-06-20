#libraries
import pyttsx3 as p
import speech_recognition as sr
from wiki import wiki_data
from yt import yt_data

engine = p.init()


rate = engine.getProperty('rate')
engine.setProperty('rate',175)

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

speak("hello i am sofia")



with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening.")
    audio = r.listen(source) 

    text = r.recognize_google(audio)
    

if " what " and "about" and "you" in text:
    speak("i am also having a good day sir.")
    print("i am also having a good day sir.")
speak("what can i do for you??")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening..")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)
    print(text2)

if "information" in text2:
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
    speak("which vedio do you need to watch?")
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening...")
        audio = r.listen(source)
        vedio = r.recognize_google(audio)
    speak("searching {} in youtube".format(vedio))
    assist = yt_data()
    assist.get_vedio(vedio) 