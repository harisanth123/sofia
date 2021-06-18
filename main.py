#libraries
import pyttsx3 as p

#instance to get driver of computer
engine = p.init()

#speed of speeking
rate = engine.getProperty('rate')
engine.setProperty('rate',180)
print(rate)

#checking voice
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
print(voices)

engine.say(" my name is sofia. your voice assistant")

#wait till output is finish
engine.runAndWait()#c