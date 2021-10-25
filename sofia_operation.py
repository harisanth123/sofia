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
    url="https://newsapi.org/v2/top-headlines?country=in&apiKey="+key
    news = requests.get(url).json()

    articles = news["articles"]

    my_articles = []
    my_news = ""

    for article in articles:
        my_articles.append(article["title"])
    for i in range(10):
        my_news = my_news + str(i+1) +". " + my_articles[i]+"\n"
    print(my_news)
        

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
        


        


