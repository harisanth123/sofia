from datetime import MAXYEAR
from sofia_voice_recognizeing import *
from sofia_utils import *
from sofia_operation import *
from sofia_data import *
import wikipedia
def sofia_intro():
    voices = voice()
    if " sofia" in voices:
        print("i am also having a good day sir.")
        speak("i am also having a good day sir.")

    elif "good" in voices:
        wish = wishing()
        print(wish)
        speak(wish)

    else:
        intro = random.choice(intro_list)
        print(intro)
        speak(intro)    

def sofia_process():
    voices = voice()
    if "information" in voices:
        print("what information do you need ?")
        speak("what information do you need ?")
        info = voice()
        print("do you wish to open wikipedia in browser")
        speak("do you wish to open wikipedia in browser")
        wiki = voice()
        if wiki == "yes":
            print("searching {} in wikipedia".format(info))
            speak("searching {} in wikipedia".format(info))
            assist=wiki_acess()
            assist.get_info(info)
            
        else:
            print("geting information about {} from wikipedia".format(info))
            speak("geting information about {} from wikipedia".format(info))
            try:
                wiki_data=wikipedia.summary(info, sentences=5)
                print(wiki_data)
                speak(wiki_data)
            
            except  wikipedia.exceptions.DisambiguationError as e:
                print("multiple items founded. please select one")
                speak("multiple items founded. please select one")
                print(e.options)
                opp_wiki = voice()
                wiki_data=wikipedia.summary(opp_wiki, sentences=5)
                print(wiki_data)
                speak(wiki_data)
            
            except wikipedia.exceptions.PageError as e:
                print(e)
                speak(e)
            
            except wikipedia.exceptions.Timeout:
                print("Timeout occurred")
                speak("Timeout occurred")
            
                 
    
    elif "YouTube" and "video" in voices:
        print("which vedio do you need to watch?")
        speak("which vedio do you need to watch?")
        vedio = voice() 
        print("searching {} in youtube".format(vedio))
        speak("searching {} in youtube".format(vedio))
        assist = yt_data()
        assist.get_vedio(vedio) 

    elif "news" in voices:
        print("sure sir, i will get for you ")
        speak("sure sir, i will get for you ")
        news=get_news()
    
        
        
        

    elif "joke" or "jokes" in voices:
        print("ok sir let me find a joke for you...")
        speak("ok sir let me find a joke for you...")
        arr=jokes()
        print(arr[0])
        speak(arr[0])
        print(arr[1])
        speak(arr[1])
    else:
        unable=random.choice(voice_NO)
        print(unable)
        speak(unable)
