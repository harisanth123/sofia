import requests
import os

from selenium import webdriver


def jokes():
    url="https://official-joke-api.appspot.com/random_joke"

    json_data = requests.get(url).json()
    arr = [" "," "]
    arr[0] = json_data["setup"]
    arr[1] = json_data["punchline"]
    return arr

class yt_data():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")  
        self.driver.maximize_window()
    
    def get_vedio(self,query):
        self.query = query
        self.driver.get(url=" https://www.youtube.com/results?search_query= " + query)
        vedio = self.driver.find_element_by_xpath(' //*[@id="video-title"]/yt-formatted-string')  
        vedio.click() 
        
        while(True):
          pass
    

def get_news():
    key = os.environ.get('news_key')
    api_address= ('https://newsapi.org/v2/top-headlines?country=us&apiKey=' + key )
    json_data = requests.get(api_address).json()
    ar=[]
    for i in range(3):
      ar.append("Number "+str(i+1) +", "+ json_data["articles"][i]["title"]+".")
    return ar
    

class wiki_acess():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")  
        self.driver.maximize_window()
    
    def get_info(self,query):
        self.query = query
        self.driver.get(url=" https://www.wikipedia.org/ ")
        search = self.driver.find_element_by_xpath(' //*[@id="searchInput"] ')  
        search.click() 
        search.send_keys(query)

        enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button ') 
        enter.click()
        while(True):
            pass
        


        


