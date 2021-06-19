#libraries
import pyttsx3 as p
import speech_recognition as sr
from selenium_web import inflow

engine = p.init()#---------------------------------------------------instance to get driver of computer


rate = engine.getProperty('rate')# ----------------------------------speed of voice
engine.setProperty('rate',175)

voices = engine.getProperty('voices')# ------------------------------to check voice avilable
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()# --------------------------------------------to wait till voice complete

r = sr.Recognizer()

speak("hello i am sofia")



with sr.Microphone() as source:
    r.energy_threshold=10000#----------------------------------------to get low voice
    r.adjust_for_ambient_noise(source,1.2)#--------------------------cancel noice
    print("listening.")
    audio = r.listen(source)#----------------------------------------listen to audio 
    text = r.recognize_google(audio)#--------------------------------connect to google api + listen to 1st voice

if " what " and "about" and "you" in text:
    speak("i am also having a good day sir.")
speak("what can i do for you??")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening..")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)#-------------------------------listen to 2nd voice

if "information" in text2:
    speak("what information do you need ?")
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening...")#--------------------------------------listening to element to be searched
        audio = r.listen(source)
        info = r.recognize_google(audio)

    assist = inflow()
    assist.get_info(info)#--------------------------------------->to enter the element to search