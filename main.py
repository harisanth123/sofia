#libraries
import pyttsx3 as p

#instance to get driver of computer
engine = p.init()

engine.say(" my name is sofia.")

#wait till output is finish
engine.runAndWait()#c