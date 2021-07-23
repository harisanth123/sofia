import pyttsx3 as p
import speech_recognition as sr
import random

from sofia_data import *

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',175)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening.")
        audio = r.listen(source) 
        text=""
        try:
            text = r.recognize_google(audio)
            text = text.lower()
            return text
        except sr.UnknownValueError:
            v_error = random.choice(voice_error)
            print(v_error)
            speak(v_error)
            return voice()

