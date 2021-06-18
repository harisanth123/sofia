#libraries
import pyttsx3 as p
import speech_recognition as sr


engine = p.init()#---------------------------------------------------instance to get driver of computer


rate = engine.getProperty('rate')# ----------------------------------speed of voice
engine.setProperty('rate',170)

voices = engine.getProperty('voices')# ------------------------------to check voice avilable
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()# --------------------------------------------to wait till voice complete

r = sr.Recognizer()

speak("hello i am your assistant.")



with sr.Microphone() as source:
    r.energy_threshold=10000#----------------------------------------to get low voice
    r.adjust_for_ambient_noise(source,1.2)#--------------------------cancel noice
    print("listening")
    audio = r.listen(source)#----------------------------------------listen to audio 
    text = r.recognize_google(audio)#--------------------------------connect to google api

if " what " and "you" in text:
    speak("i am having a good day sir")
speak("what can i do for you??")